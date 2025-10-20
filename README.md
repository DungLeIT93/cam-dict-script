# Oxford Dictionary Script for Anki

Công cụ tìm kiếm từ điển Oxford Learner's Dictionary trực tuyến và xuất kết quả cho Anki flashcards.

A tool to search Oxford Learner's Dictionary online and export results for Anki flashcards.

## Features

- 🔍 Search words in Oxford Learner's Dictionary
- 📝 Extract definitions, pronunciation, and examples
- 📤 Export to CSV/TSV format for Anki import
- 🎯 Support for multiple words in one command
- 💻 Command-line interface

## Installation

1. Clone this repository:
```bash
git clone https://github.com/DungLeIT93/oxford-dict-script.git
cd oxford-dict-script
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Search

Search for a single word and display results:
```bash
python oxford_dict.py hello
```

### Search Multiple Words

Search for multiple words:
```bash
python oxford_dict.py hello world example
```

### Batch Processing from File

Create a text file with one word per line (e.g., `words.txt`):
```
hello
world
example
```

Then search all words from the file:
```bash
python oxford_dict.py -f words.txt -o output.csv
```

You can also combine file input with direct words:
```bash
python oxford_dict.py -f words.txt hello world -o output.csv
```

### Export to Anki

Export search results to a CSV file for Anki import:
```bash
python oxford_dict.py -o output.csv hello world example
```

### Quiet Mode

Suppress console output (useful when only exporting):
```bash
python oxford_dict.py -q -o output.csv hello world
```

### Command-line Options

- `words`: One or more words to search (optional if using -f)
- `-f, --file FILE`: Read words from a file (one word per line)
- `-o, --output FILE`: Export results to CSV file for Anki import
- `-q, --quiet`: Suppress console output
- `-h, --help`: Show help message

## Importing to Anki

1. Run the script with `-o` option to create a CSV file:
   ```bash
   python oxford_dict.py -o vocabulary.csv beautiful amazing wonderful
   ```

2. Open Anki and go to: **File → Import**

3. Select your CSV file (e.g., `vocabulary.csv`)

4. Configure import settings:
   - **Type**: Basic (or create a custom note type)
   - **Deck**: Choose your target deck
   - **Fields separated by**: Tab
   - **Allow HTML in fields**: Yes (recommended)

5. Map the fields:
   - Field 1: Word
   - Field 2: Pronunciation
   - Field 3: Part of Speech
   - Field 4: Definitions
   - Field 5: Examples

6. Click **Import**

## Output Format

The script outputs 5 fields per word:
1. **Word**: The searched word
2. **Pronunciation**: IPA pronunciation
3. **Part of Speech**: e.g., noun, verb, adjective
4. **Definitions**: Numbered list of definitions
5. **Examples**: Example sentences

## Examples

### Example 1: Display in Console
```bash
$ python oxford_dict.py happy

============================================================
Word: happy
Pronunciation: /ˈhæpi/
Part of Speech: adjective

Definitions:
  1. feeling or showing pleasure; pleased
  2. giving or causing pleasure
  3. lucky; fortunate

Examples:
  • I'm happy that everything worked out.
  • We are happy to announce the opening of our new store.
  • By a happy coincidence, we were both in Paris at the same time.
============================================================
```

### Example 2: Export to CSV
```bash
$ python oxford_dict.py -o words.csv happy sad angry
Searching for 'happy'...
Searching for 'sad'...
Searching for 'angry'...

Results exported to words.csv
Import this file into Anki with tab-separated fields.
```

## Requirements

- Python 3.6+
- requests
- beautifulsoup4

## Notes

- The script searches Oxford Learner's Dictionary (https://www.oxfordlearnersdictionaries.com/)
- Internet connection required
- Limited to first 5 definitions and 3 examples per word
- Respects the website's structure as of the implementation date

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Troubleshooting

### Connection Errors
If you encounter connection errors, check your internet connection and ensure the Oxford Learner's Dictionary website is accessible.

### No Results Found
- Verify the spelling of the word
- Try searching with the base form of the word (e.g., "run" instead of "running")
- Some very specialized or rare words may not be in the learner's dictionary

### Import Issues in Anki
- Ensure "Allow HTML in fields" is enabled
- Check that field separator is set to "Tab"
- Verify the CSV file was created successfully