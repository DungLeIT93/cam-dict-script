#!/usr/bin/env python3
"""
Oxford Dictionary Search Script for Anki
This script searches Oxford Learner's Dictionary online and formats the results for Anki import.
"""

import requests
from bs4 import BeautifulSoup
import sys
import csv
import argparse
from typing import Dict, List, Optional


class OxfordDictionary:
    """Class to handle Oxford Learner's Dictionary searches."""
    
    BASE_URL = "https://www.oxfordlearnersdictionaries.com/definition/english/"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def search_word(self, word: str) -> Optional[Dict]:
        """
        Search for a word in Oxford Learner's Dictionary.
        
        Args:
            word: The word to search for
            
        Returns:
            Dictionary containing word information or None if not found
        """
        try:
            # Clean the word for URL
            search_term = word.lower().strip().replace(' ', '-')
            url = f"{self.BASE_URL}{search_term}"
            
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract word information
            result = {
                'word': word,
                'pronunciation': self._get_pronunciation(soup),
                'definitions': self._get_definitions(soup),
                'examples': self._get_examples(soup),
                'pos': self._get_part_of_speech(soup)
            }
            
            return result if result['definitions'] else None
            
        except requests.RequestException as e:
            print(f"Error fetching data for '{word}': {e}", file=sys.stderr)
            return None
    
    def _get_pronunciation(self, soup: BeautifulSoup) -> str:
        """Extract pronunciation from the page."""
        pron_elements = soup.select('.phonetics .phon')
        if pron_elements:
            return pron_elements[0].get_text(strip=True)
        return ''
    
    def _get_part_of_speech(self, soup: BeautifulSoup) -> str:
        """Extract part of speech."""
        pos_element = soup.select_one('.pos')
        if pos_element:
            return pos_element.get_text(strip=True)
        return ''
    
    def _get_definitions(self, soup: BeautifulSoup) -> List[str]:
        """Extract definitions from the page."""
        definitions = []
        def_elements = soup.select('.senses_multiple .def, .sense-body .def')
        
        for def_elem in def_elements[:5]:  # Limit to first 5 definitions
            def_text = def_elem.get_text(strip=True)
            if def_text:
                definitions.append(def_text)
        
        return definitions
    
    def _get_examples(self, soup: BeautifulSoup) -> List[str]:
        """Extract example sentences from the page."""
        examples = []
        example_elements = soup.select('.examples .x, .examples .unx')
        
        for example in example_elements[:3]:  # Limit to first 3 examples
            example_text = example.get_text(strip=True)
            if example_text:
                examples.append(example_text)
        
        return examples


class AnkiFormatter:
    """Format dictionary results for Anki import."""
    
    @staticmethod
    def format_for_csv(word_data: Dict) -> List[str]:
        """
        Format word data as a CSV row for Anki import.
        
        Args:
            word_data: Dictionary containing word information
            
        Returns:
            List of fields for CSV row
        """
        word = word_data['word']
        pronunciation = word_data.get('pronunciation', '')
        pos = word_data.get('pos', '')
        
        # Join definitions with HTML line breaks
        definitions = '<br>'.join(
            f"{i+1}. {defn}" for i, defn in enumerate(word_data.get('definitions', []))
        )
        
        # Join examples with HTML line breaks
        examples = '<br>'.join(
            f"• {ex}" for ex in word_data.get('examples', [])
        )
        
        return [word, pronunciation, pos, definitions, examples]
    
    @staticmethod
    def format_for_display(word_data: Dict) -> str:
        """
        Format word data for console display.
        
        Args:
            word_data: Dictionary containing word information
            
        Returns:
            Formatted string for display
        """
        output = []
        output.append(f"\n{'='*60}")
        output.append(f"Word: {word_data['word']}")
        
        if word_data.get('pronunciation'):
            output.append(f"Pronunciation: {word_data['pronunciation']}")
        
        if word_data.get('pos'):
            output.append(f"Part of Speech: {word_data['pos']}")
        
        if word_data.get('definitions'):
            output.append("\nDefinitions:")
            for i, defn in enumerate(word_data['definitions'], 1):
                output.append(f"  {i}. {defn}")
        
        if word_data.get('examples'):
            output.append("\nExamples:")
            for ex in word_data['examples']:
                output.append(f"  • {ex}")
        
        output.append(f"{'='*60}\n")
        return '\n'.join(output)


def main():
    """Main function to run the dictionary search."""
    parser = argparse.ArgumentParser(
        description='Search Oxford Learner\'s Dictionary and format for Anki'
    )
    parser.add_argument(
        'words',
        nargs='*',
        help='Word(s) to search for'
    )
    parser.add_argument(
        '-f', '--file',
        help='Read words from a file (one word per line)',
        default=None
    )
    parser.add_argument(
        '-o', '--output',
        help='Output CSV file for Anki import',
        default=None
    )
    parser.add_argument(
        '-q', '--quiet',
        action='store_true',
        help='Suppress console output'
    )
    
    args = parser.parse_args()
    
    # Collect words from arguments and/or file
    words_to_search = list(args.words) if args.words else []
    
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                file_words = [line.strip() for line in f if line.strip()]
                words_to_search.extend(file_words)
        except IOError as e:
            print(f"Error reading file {args.file}: {e}", file=sys.stderr)
            sys.exit(1)
    
    if not words_to_search:
        parser.print_help()
        print("\nError: Please provide words to search either as arguments or via -f/--file", file=sys.stderr)
        sys.exit(1)
    
    dictionary = OxfordDictionary()
    formatter = AnkiFormatter()
    results = []
    
    for word in words_to_search:
        if not args.quiet:
            print(f"Searching for '{word}'...", file=sys.stderr)
        
        word_data = dictionary.search_word(word)
        
        if word_data:
            results.append(word_data)
            if not args.quiet:
                print(formatter.format_for_display(word_data))
        else:
            print(f"No results found for '{word}'", file=sys.stderr)
    
    # Export to CSV if output file specified
    if args.output and results:
        try:
            with open(args.output, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, delimiter='\t')
                # Write header
                writer.writerow(['Word', 'Pronunciation', 'Part of Speech', 'Definitions', 'Examples'])
                # Write data
                for word_data in results:
                    writer.writerow(formatter.format_for_csv(word_data))
            
            print(f"\nResults exported to {args.output}", file=sys.stderr)
            print(f"Import this file into Anki with tab-separated fields.", file=sys.stderr)
        except IOError as e:
            print(f"Error writing to file: {e}", file=sys.stderr)
            sys.exit(1)
    
    sys.exit(0 if results else 1)


if __name__ == '__main__':
    main()
