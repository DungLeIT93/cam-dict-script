# Quick Reference - Oxford Dictionary Script

## Installation
```bash
pip install -r requirements.txt
```

## Basic Usage

### Search single word
```bash
python oxford_dict.py hello
```

### Search multiple words
```bash
python oxford_dict.py hello world example
```

### Export to CSV for Anki
```bash
python oxford_dict.py -o output.csv hello world
```

### Batch from file
```bash
python oxford_dict.py -f words.txt -o output.csv
```

### Quiet mode (no console output)
```bash
python oxford_dict.py -q -o output.csv hello world
```

## Anki Import Steps

1. **Create CSV**: `python oxford_dict.py -o vocab.csv word1 word2 word3`
2. **Open Anki**: File → Import
3. **Select file**: vocab.csv
4. **Configure**:
   - Fields separated by: **Tab**
   - Allow HTML in fields: **Yes**
5. **Map fields**: Word, Pronunciation, POS, Definitions, Examples
6. **Import**

## File Format for Batch Processing

Create a text file (e.g., `words.txt`) with one word per line:
```
hello
world
example
beautiful
```

Then run:
```bash
python oxford_dict.py -f words.txt -o output.csv
```

## Output Fields

1. **Word** - The vocabulary word
2. **Pronunciation** - IPA pronunciation (e.g., /həˈləʊ/)
3. **Part of Speech** - noun, verb, adjective, etc.
4. **Definitions** - Numbered list (max 5)
5. **Examples** - Example sentences (max 3)

## Testing

Run unit tests:
```bash
python test_oxford_dict.py
```

Run example:
```bash
python example.py
```

## Common Issues

**No results found?**
- Check spelling
- Use base form (run, not running)
- Check internet connection

**Import error in Anki?**
- Enable "Allow HTML in fields"
- Use Tab separator
- Verify CSV file exists

## See Also

- `README.md` - Full documentation (English)
- `VIETNAMESE.md` - Hướng dẫn tiếng Việt
- `words_sample.txt` - Sample word list
- `example.py` - Example output generator
