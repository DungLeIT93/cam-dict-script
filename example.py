#!/usr/bin/env python3
"""
Example usage demonstration for Oxford Dictionary Script
This creates a sample CSV file showing the expected output format
"""

import csv
import sys


def create_sample_data():
    """Create sample dictionary data."""
    return [
        {
            'word': 'hello',
            'pronunciation': '/həˈləʊ/',
            'pos': 'exclamation, noun',
            'definitions': [
                'used as a greeting when you meet somebody, when you answer the telephone or when you want to attract somebody\'s attention',
                'used to show that you are surprised by something',
                'used to show that you think somebody has said or done something stupid'
            ],
            'examples': [
                'Hello! How are you today?',
                'I just called to say hello.',
                'Hello? Is anybody there?'
            ]
        },
        {
            'word': 'world',
            'pronunciation': '/wɜːld/',
            'pos': 'noun',
            'definitions': [
                'the earth, with all its countries, peoples and natural features',
                'a particular part of the earth',
                'a particular period of history and the people of that time'
            ],
            'examples': [
                'to travel around the world',
                'the world\'s largest democracy',
                'the ancient world'
            ]
        },
        {
            'word': 'example',
            'pronunciation': '/ɪɡˈzɑːmpl/',
            'pos': 'noun',
            'definitions': [
                'something such as an object, a fact or a situation that shows, explains or supports what you say',
                'a thing that is typical of or represents a particular group or set',
                'a person or their behaviour that is thought to be a good model for others to copy'
            ],
            'examples': [
                'Can you give me an example of what you mean?',
                'This is a good example of the artist\'s early work.',
                'Her courage is an example to us all.'
            ]
        }
    ]


def format_for_csv(word_data):
    """Format word data as a CSV row."""
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


def main():
    """Generate sample CSV file."""
    output_file = 'sample_output.csv'
    
    # Get sample data
    sample_data = create_sample_data()
    
    # Write to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        # Write header
        writer.writerow(['Word', 'Pronunciation', 'Part of Speech', 'Definitions', 'Examples'])
        # Write data
        for word_data in sample_data:
            writer.writerow(format_for_csv(word_data))
    
    print(f"Sample data created in {output_file}")
    print("\nSample output preview:")
    print("="*70)
    
    for word_data in sample_data:
        print(f"\nWord: {word_data['word']}")
        print(f"Pronunciation: {word_data['pronunciation']}")
        print(f"Part of Speech: {word_data['pos']}")
        print("\nDefinitions:")
        for i, defn in enumerate(word_data['definitions'], 1):
            print(f"  {i}. {defn}")
        print("\nExamples:")
        for ex in word_data['examples']:
            print(f"  • {ex}")
        print("-"*70)
    
    print(f"\nImport '{output_file}' into Anki:")
    print("1. Open Anki → File → Import")
    print("2. Select the CSV file")
    print("3. Set 'Fields separated by' to Tab")
    print("4. Enable 'Allow HTML in fields'")
    print("5. Map the fields and click Import")


if __name__ == '__main__':
    main()
