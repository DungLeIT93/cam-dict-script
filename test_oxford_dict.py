#!/usr/bin/env python3
"""
Unit tests for Oxford Dictionary Script
"""

import unittest
import sys
import os
from io import StringIO

# Add parent directory to path
sys.path.insert(0, os.path.dirname(__file__))

from oxford_dict import AnkiFormatter


class TestAnkiFormatter(unittest.TestCase):
    """Test the AnkiFormatter class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.formatter = AnkiFormatter()
        self.sample_data = {
            'word': 'test',
            'pronunciation': '/test/',
            'pos': 'noun',
            'definitions': [
                'A procedure to check quality',
                'An examination of knowledge'
            ],
            'examples': [
                'This is a test.',
                'The test was difficult.'
            ]
        }
    
    def test_format_for_csv_basic(self):
        """Test basic CSV formatting."""
        result = self.formatter.format_for_csv(self.sample_data)
        
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0], 'test')
        self.assertEqual(result[1], '/test/')
        self.assertEqual(result[2], 'noun')
        self.assertIn('1. A procedure to check quality', result[3])
        self.assertIn('2. An examination of knowledge', result[3])
        self.assertIn('<br>', result[3])
        self.assertIn('• This is a test.', result[4])
        self.assertIn('<br>', result[4])
    
    def test_format_for_csv_empty_data(self):
        """Test CSV formatting with missing data."""
        minimal_data = {
            'word': 'minimal',
            'definitions': ['Single definition']
        }
        
        result = self.formatter.format_for_csv(minimal_data)
        
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0], 'minimal')
        self.assertEqual(result[1], '')  # No pronunciation
        self.assertEqual(result[2], '')  # No POS
        self.assertEqual(result[3], '1. Single definition')
        self.assertEqual(result[4], '')  # No examples
    
    def test_format_for_display(self):
        """Test display formatting."""
        result = self.formatter.format_for_display(self.sample_data)
        
        self.assertIn('Word: test', result)
        self.assertIn('Pronunciation: /test/', result)
        self.assertIn('Part of Speech: noun', result)
        self.assertIn('Definitions:', result)
        self.assertIn('1. A procedure to check quality', result)
        self.assertIn('Examples:', result)
        self.assertIn('• This is a test.', result)
        self.assertIn('='*60, result)
    
    def test_format_for_display_minimal(self):
        """Test display formatting with minimal data."""
        minimal_data = {
            'word': 'test',
            'definitions': ['Single definition']
        }
        
        result = self.formatter.format_for_display(minimal_data)
        
        self.assertIn('Word: test', result)
        self.assertIn('Definitions:', result)
        self.assertIn('1. Single definition', result)
        # Should not crash with missing fields
    
    def test_csv_format_html_escaping(self):
        """Test that HTML tags are preserved in definitions."""
        data_with_special = {
            'word': 'special',
            'definitions': ['A <test> definition'],
            'examples': ['Example with & characters']
        }
        
        result = self.formatter.format_for_csv(data_with_special)
        
        # HTML should be preserved
        self.assertIn('<test>', result[3])
        self.assertIn('&', result[4])


class TestWordProcessing(unittest.TestCase):
    """Test word processing functionality."""
    
    def test_multiple_definitions_formatting(self):
        """Test formatting of multiple definitions."""
        formatter = AnkiFormatter()
        data = {
            'word': 'test',
            'definitions': ['Def 1', 'Def 2', 'Def 3', 'Def 4', 'Def 5']
        }
        
        result = formatter.format_for_csv(data)
        definitions_text = result[3]
        
        # Should have all 5 definitions numbered
        for i in range(1, 6):
            self.assertIn(f'{i}. Def {i}', definitions_text)
    
    def test_multiple_examples_formatting(self):
        """Test formatting of multiple examples."""
        formatter = AnkiFormatter()
        data = {
            'word': 'test',
            'examples': ['Ex 1', 'Ex 2', 'Ex 3']
        }
        
        result = formatter.format_for_csv(data)
        examples_text = result[4]
        
        # Should have all examples with bullets
        for i in range(1, 4):
            self.assertIn(f'• Ex {i}', examples_text)


def run_tests():
    """Run all tests."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTests(loader.loadTestsFromTestCase(TestAnkiFormatter))
    suite.addTests(loader.loadTestsFromTestCase(TestWordProcessing))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(run_tests())
