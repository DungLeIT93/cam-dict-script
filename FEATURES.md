# Oxford Dictionary Script - Features Overview

## 📚 Core Features

### 1. Online Dictionary Search
- Searches Oxford Learner's Dictionary (https://www.oxfordlearnersdictionaries.com/)
- Extracts comprehensive word information
- Handles multiple words in a single query
- Internet connection required

### 2. Data Extraction
The script extracts:
- ✅ Word pronunciation (IPA format)
- ✅ Part of speech (noun, verb, adjective, etc.)
- ✅ Up to 5 definitions per word
- ✅ Up to 3 example sentences per word

### 3. Anki Integration
- Exports to tab-separated CSV format
- HTML formatting for better card appearance
- Ready-to-import format
- 5-field structure optimized for flashcards

### 4. Batch Processing
- Process multiple words from command line
- Read word lists from files
- Combine file input with direct arguments
- Efficient bulk vocabulary processing

### 5. User Interface
- Command-line interface
- Multiple output modes (console display, CSV export)
- Quiet mode for automation
- Detailed error messages
- Progress indicators

## 🛠️ Technical Features

### Code Quality
- **248 lines** of well-structured Python code
- Object-oriented design (OOP)
- Type hints for better code clarity
- Comprehensive error handling
- **7 unit tests** with 100% pass rate

### Documentation
- English documentation (README.md)
- Vietnamese documentation (VIETNAMESE.md)
- Quick start guide (QUICKSTART.md)
- Inline code comments
- Usage examples

### Dependencies
- Minimal dependencies (2 packages)
- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- Python 3.6+ compatible

## 📊 Output Format

### Console Display
```
============================================================
Word: hello
Pronunciation: /həˈləʊ/
Part of Speech: exclamation, noun

Definitions:
  1. used as a greeting when you meet somebody
  2. used to show that you are surprised
  3. used to show that you think somebody has done something stupid

Examples:
  • Hello! How are you today?
  • I just called to say hello.
  • Hello? Is anybody there?
============================================================
```

### CSV Export (Tab-separated)
```
Word    Pronunciation    Part of Speech    Definitions    Examples
hello   /həˈləʊ/        exclamation       1. used as... 2. used to...    • Hello! How...
```

## 🎯 Use Cases

### For Language Learners
- Build custom Anki decks
- Study vocabulary systematically
- Include pronunciation and examples
- Track word meanings and usage

### For Teachers
- Create study materials for students
- Prepare vocabulary lists
- Generate flashcard sets
- Customize content for lessons

### For Developers
- Automate dictionary lookups
- Integrate with other tools
- Batch process word lists
- Export data programmatically

## 🧪 Testing

### Included Tests
- CSV formatting validation
- Display formatting validation
- HTML preservation tests
- Edge case handling
- Multiple definitions/examples

### Example Script
- Demonstrates output format
- Creates sample CSV file
- Shows expected results
- No internet required

## 📦 Package Contents

```
oxford-dict-script/
├── oxford_dict.py      # Main script (248 lines)
├── example.py          # Example/demo (122 lines)
├── test_oxford_dict.py # Unit tests (162 lines)
├── requirements.txt    # Dependencies
├── README.md           # English documentation
├── VIETNAMESE.md       # Vietnamese documentation
├── QUICKSTART.md       # Quick reference
├── LICENSE             # MIT License
├── .gitignore          # Git ignore rules
└── words_sample.txt    # Sample word list
```

## 🚀 Future Enhancement Possibilities

Potential additions (not currently implemented):
- Audio pronunciation download
- Additional dictionary sources
- Word frequency information
- Synonyms and antonyms
- Collocations and phrases
- Offline caching
- GUI interface
- Browser extension

## 📝 License

MIT License - Free to use, modify, and distribute

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Additional dictionary sources
- More export formats
- Enhanced error handling
- Performance optimizations
- Additional language support
