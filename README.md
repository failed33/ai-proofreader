# AI Proofreader for Word Documents

An intelligent proofreading tool that uses OpenAI's GPT models to analyze and improve Word documents paragraph by paragraph, providing detailed feedback and corrections.

## Features

- 📖 **Reads Word documents** (.docx format)
- 🤖 **AI-powered proofreading** using OpenAI's GPT models
- 📝 **Structured output** with original text, corrections, and detailed feedback
- 🔄 **Automatic retry logic** for API rate limits and timeouts
- 📊 **Progress tracking** with visual progress bars
- ⚡ **Token management** to handle large documents efficiently
- 🎯 **Highlighted changes** in the output document

## Files Overview

- `review.py` - Complete standalone script with all functionality
- `review_modular.py` - Modular version that imports from `config.py`
- `config.py` - Configuration module (used by modular version)
- `create_sample_doc.py` - Utility to create test documents with errors
- `test_setup.py` - Validation script to test your setup
- `requirements.txt` - Required Python packages
- `.env.example` - Template for environment variables

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (get one at [platform.openai.com](https://platform.openai.com))
- Word documents in .docx format (not .doc)

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your OpenAI API key**:
   ```bash
   cp .env.example .env
   # Edit .env and add your actual API key
   ```

3. **Test your setup**:
   ```bash
   python test_setup.py
   ```

4. **Create a sample document** (optional):
   ```bash
   python create_sample_doc.py
   ```

5. **Run the proofreader**:
   ```bash
   python review.py
   # OR use the modular version:
   python review_modular.py
   ```

## File Path Configuration - Detailed Guide

### Understanding File Paths

The script needs to know where to find your input document and where to save the output. File paths can be specified in several ways:

#### 1. **Relative Paths** (Recommended for beginners)
Relative paths are specified relative to where you run the script from.

**Examples:**
```python
INPUT_DOCX_PATH = "my_draft.docx"                    # Same folder as script
INPUT_DOCX_PATH = "documents/my_draft.docx"          # In a 'documents' subfolder
INPUT_DOCX_PATH = "../my_draft.docx"                 # One folder up
INPUT_DOCX_PATH = "../../Desktop/my_draft.docx"      # Two folders up, then Desktop
```

#### 2. **Absolute Paths** (Full path from root)
Absolute paths specify the complete path from your system's root directory.

**Windows Examples:**
```python
INPUT_DOCX_PATH = "C:\\Users\\YourName\\Documents\\my_draft.docx"
INPUT_DOCX_PATH = "C:/Users/YourName/Documents/my_draft.docx"     # Also works
OUTPUT_DOCX_PATH = "C:\\Users\\YourName\\Desktop\\proofread_output.docx"
```

**macOS/Linux Examples:**
```python
INPUT_DOCX_PATH = "/Users/YourName/Documents/my_draft.docx"
INPUT_DOCX_PATH = "/home/username/Documents/my_draft.docx"        # Linux
OUTPUT_DOCX_PATH = "/Users/YourName/Desktop/proofread_output.docx"
```

#### 3. **Handling Spaces in File Names**
If your file or folder names contain spaces, the paths will still work correctly:

```python
INPUT_DOCX_PATH = "My Important Document.docx"
INPUT_DOCX_PATH = "Documents/My Project/Draft Document.docx"
INPUT_DOCX_PATH = "/Users/John Smith/My Documents/Research Paper.docx"
```

#### 4. **Different Operating Systems**
- **Windows**: Use either `\\` or `/` as path separators
- **macOS/Linux**: Use `/` as path separators
- **Python handles both formats on most systems**

### How to Configure File Paths

#### **Method 1: Edit the Script Directly** (Simplest)

**For standalone version** (`review.py`):
Edit lines 33-34 in `review.py`:
```python
# File Paths - Edit these lines
INPUT_DOCX_PATH = "your_document.docx"
OUTPUT_DOCX_PATH = "your_output.docx"
```

**For modular version** (`config.py`):
Edit lines 19-20 in `config.py`:
```python
# File Paths - Edit these lines
INPUT_DOCX_PATH = os.getenv("INPUT_DOCX_PATH", "your_document.docx")
OUTPUT_DOCX_PATH = os.getenv("OUTPUT_DOCX_PATH", "your_output.docx")
```

#### **Method 2: Environment Variables** (Advanced)

Create or edit your `.env` file:
```bash
# .env file contents
OPENAI_API_KEY=your_api_key_here
INPUT_DOCX_PATH=path/to/your/document.docx
OUTPUT_DOCX_PATH=path/to/your/output.docx
```

Or set them in your terminal:
```bash
# macOS/Linux
export INPUT_DOCX_PATH="/Users/YourName/Documents/my_draft.docx"
export OUTPUT_DOCX_PATH="/Users/YourName/Desktop/proofread_output.docx"

# Windows Command Prompt
set INPUT_DOCX_PATH=C:\Users\YourName\Documents\my_draft.docx
set OUTPUT_DOCX_PATH=C:\Users\YourName\Desktop\proofread_output.docx

# Windows PowerShell
$env:INPUT_DOCX_PATH="C:\Users\YourName\Documents\my_draft.docx"
$env:OUTPUT_DOCX_PATH="C:\Users\YourName\Desktop\proofread_output.docx"
```

### Common File Path Examples

#### **Scenario 1: Files in same folder as script**
```
review/
├── review.py
├── my_draft.docx          ← Your input file
└── proofread_output.docx  ← Generated output
```
**Configuration:**
```python
INPUT_DOCX_PATH = "my_draft.docx"
OUTPUT_DOCX_PATH = "proofread_output.docx"
```

#### **Scenario 2: Organized folder structure**
```
review/
├── review.py
├── documents/
│   ├── my_draft.docx      ← Your input file
│   └── output/
│       └── proofread_output.docx  ← Generated output
```
**Configuration:**
```python
INPUT_DOCX_PATH = "documents/my_draft.docx"
OUTPUT_DOCX_PATH = "documents/output/proofread_output.docx"
```

#### **Scenario 3: Files on Desktop**
```
Desktop/
├── my_draft.docx          ← Your input file
└── Projects/
    └── review/
        └── review.py      ← Script location
```
**Configuration:**
```python
INPUT_DOCX_PATH = "../../my_draft.docx"
OUTPUT_DOCX_PATH = "../../proofread_output.docx"
```

#### **Scenario 4: Absolute paths (different drives/locations)**
**Configuration:**
```python
# Windows
INPUT_DOCX_PATH = "C:/Users/John/Documents/Important/my_draft.docx"
OUTPUT_DOCX_PATH = "D:/Backup/proofread_output.docx"

# macOS
INPUT_DOCX_PATH = "/Users/john/Documents/my_draft.docx"
OUTPUT_DOCX_PATH = "/Users/john/Desktop/proofread_output.docx"

# Linux
INPUT_DOCX_PATH = "/home/john/documents/my_draft.docx"
OUTPUT_DOCX_PATH = "/home/john/desktop/proofread_output.docx"
```

### Troubleshooting File Paths

#### **Common Issues and Solutions:**

1. **"File not found" error**
   ```bash
   FileNotFoundError: Input file 'my_draft.docx' not found.
   ```
   **Solutions:**
   - Check if the file exists where you think it is
   - Verify the file name and extension (.docx not .doc)
   - Use absolute path to be certain
   - Check your current working directory: `python -c "import os; print(os.getcwd())"`

2. **Permission denied error**
   ```bash
   PermissionError: [Errno 13] Permission denied
   ```
   **Solutions:**
   - Make sure the output folder exists and is writable
   - Close the output file if it's open in Word
   - Run with administrator privileges if needed

3. **Path with backslashes not working**
   **Problem:** `INPUT_DOCX_PATH = "C:\Users\Name\my_draft.docx"`
   **Solutions:**
   ```python
   # Use forward slashes (works on all systems)
   INPUT_DOCX_PATH = "C:/Users/Name/my_draft.docx"
   
   # Or use raw strings (Windows)
   INPUT_DOCX_PATH = r"C:\Users\Name\my_draft.docx"
   
   # Or escape backslashes
   INPUT_DOCX_PATH = "C:\\Users\\Name\\my_draft.docx"
   ```

4. **Spaces in paths causing issues**
   ```python
   # This works fine - no quotes needed in the string
   INPUT_DOCX_PATH = "My Important Document.docx"
   INPUT_DOCX_PATH = "/Users/John Smith/My Documents/file.docx"
   ```

## Installation

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `python-docx` - For reading/writing Word documents
- `tiktoken` - For accurate token counting
- `openai` - OpenAI API client
- `backoff` - Automatic retry with exponential backoff
- `pydantic` - Data validation
- `tqdm` - Progress bars
- `python-dotenv` - Environment variable management

### Step 2: Set Up API Key

Create a `.env` file:
```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your_actual_api_key_here
```

**Getting an API Key:**
1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy and paste it into your `.env` file

### Step 3: Validate Setup

Run the test script to ensure everything is working:
```bash
python test_setup.py
```

## Usage

### Basic Usage

1. **Place your Word document** in the same directory and name it `my_draft.docx`
2. **Run the script**:
   ```bash
   python review.py
   ```
3. **Check the output**: `proofread_output.docx`

### Using Custom File Paths

See the detailed "File Path Configuration" section above for comprehensive examples.

### Creating Test Documents

Generate a sample document with intentional errors:
```bash
python create_sample_doc.py
```

This creates `my_draft.docx` with various types of errors for testing.

## Configuration Options

### Available Models
- `gpt-4o-mini` (default, cost-effective, ~$0.15/1M input tokens)
- `gpt-4o` (highest quality, ~$2.50/1M input tokens)
- `gpt-4` (high quality, ~$10/1M input tokens)
- `gpt-3.5-turbo` (fastest, lower cost, ~$0.50/1M input tokens)

### Environment Variables

You can configure the script using environment variables:

```bash
# API Configuration
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=gpt-4o-mini
TEMPERATURE=0.0

# File Paths
INPUT_DOCX_PATH=my_draft.docx
OUTPUT_DOCX_PATH=proofread_output.docx

# Token Management
MAX_TOKENS_PER_API_REQUEST=4000

# Retry Settings
MAX_RETRY_TIME_SECONDS=60
```

### Editing Script Configuration

**In `review.py` (lines 23-35):**
```python
# OpenAI API Configuration
OPENAI_MODEL = "gpt-4o-mini"  # Change model here
TEMPERATURE = 0.0  # 0.0 = deterministic, 0.7 = more creative

# Token Management
MAX_TOKENS_PER_API_REQUEST = 4000  # Adjust for longer/shorter paragraphs

# File Paths
INPUT_DOCX_PATH = "my_draft.docx"  # Change input file here
OUTPUT_DOCX_PATH = "proofread_output.docx"  # Change output file here
```

## Output Format

The generated Word document contains:

1. **Summary**: Overview of processed and corrected paragraphs
2. **For each paragraph**:
   - **Original**: The original text (in quote style)
   - **Corrected**: The AI-corrected version (highlighted if changes were made)
   - **Feedback**: Bullet-pointed list of issues found and suggestions

### Example Output Structure

```
AI Proofreading Report

Summary: Processed 5 paragraphs. 3 paragraphs had corrections.

==================================================

Paragraph 1: Original
"This is the orginal text with some erors."

Paragraph 1: Corrected
This is the original text with some errors.

Paragraph 1: Feedback
• Fixed spelling: "orginal" → "original"
• Fixed spelling: "erors" → "errors"

------------------------------
```

## Error Handling

The script includes robust error handling for:

- **API rate limits**: Automatic retry with exponential backoff
- **Token limits**: Warnings for overly long paragraphs
- **Network issues**: Retry mechanism for connection problems
- **Invalid responses**: Fallback to original text with error notes
- **File access**: Clear error messages for missing files

## Cost Estimation

Approximate costs using different models:

### gpt-4o-mini (Recommended)
- Small document (5-10 paragraphs): ~$0.01-0.03
- Medium document (20-50 paragraphs): ~$0.05-0.15
- Large document (100+ paragraphs): ~$0.25-0.75

### gpt-4o
- Small document (5-10 paragraphs): ~$0.05-0.15
- Medium document (20-50 paragraphs): ~$0.25-0.75
- Large document (100+ paragraphs): ~$1.00-3.00

### gpt-4
- Small document (5-10 paragraphs): ~$0.20-0.60
- Medium document (20-50 paragraphs): ~$1.00-3.00
- Large document (100+ paragraphs): ~$5.00-15.00

*Costs vary based on text length and complexity. Check current OpenAI pricing.*

## Troubleshooting

### Common Issues

1. **"OPENAI_API_KEY environment variable not set"**
   - Run: `python test_setup.py` to diagnose
   - Ensure your `.env` file exists and contains the API key
   - Check that your API key is valid and has credits

2. **"Input file 'my_draft.docx' not found"**
   - Verify the file exists at the specified path
   - Check file name and extension (.docx not .doc)
   - Try using absolute path: `INPUT_DOCX_PATH = "/full/path/to/your/file.docx"`
   - Try creating a test document: `python create_sample_doc.py`

3. **Import errors**
   - Run: `pip install -r requirements.txt`
   - Verify installation: `python test_setup.py`
   - Check you're using the virtual environment: `source .venv/bin/activate`

4. **Token limit warnings**
   - Very long paragraphs might exceed token limits
   - Consider breaking up extremely long paragraphs manually
   - Increase `MAX_TOKENS_PER_API_REQUEST` if needed

5. **API rate limit errors**
   - The script will automatically retry
   - Check your OpenAI account for rate limits and billing
   - Consider using a slower model if hitting limits frequently

6. **Output file already open**
   - Close the output Word document before running the script
   - The script cannot overwrite files that are open in Word

### Debug Mode

To see more detailed information, you can modify the script to add debug prints or run the test validation:

```bash
python test_setup.py
```

For more debugging, add print statements in the script:
```python
print(f"Current working directory: {os.getcwd()}")
print(f"Looking for file: {INPUT_DOCX_PATH}")
print(f"File exists: {os.path.exists(INPUT_DOCX_PATH)}")
```

## Script Versions

### Standalone Version (`review.py`)
- **Best for**: Simple use cases, one-time usage
- **Pros**: Complete functionality in a single file, easy to share
- **Cons**: Less flexible for customization
- **Configuration**: Edit variables at the top of the file

### Modular Version (`review_modular.py` + `config.py`)
- **Best for**: Development, complex setups, repeated use
- **Pros**: Separated configuration, environment variable support, easier to extend
- **Cons**: Requires multiple files
- **Configuration**: Edit `config.py` or use environment variables

Choose the version that best fits your needs!

## Advanced Features

### Custom Prompts

You can modify the AI prompts to focus on specific types of errors:

**In `config.py` (modular version) or at the top of `review.py`:**

```python
# Academic writing focus
SYSTEM_PROMPT = "You are an expert academic editor. Focus on formal tone, precise terminology, and scholarly writing conventions. Return JSON only."

# Business writing focus  
SYSTEM_PROMPT = "You are a professional business editor. Focus on clarity, conciseness, and professional tone appropriate for business communications. Return JSON only."

# Creative writing focus
SYSTEM_PROMPT = "You are an expert creative writing editor. Focus on narrative flow, character voice, and literary techniques while maintaining the author's style. Return JSON only."
```

### Batch Processing

For multiple documents, create a simple batch script:

```python
# batch_process.py
import os
from your_review_script import main

documents = [
    "document1.docx",
    "document2.docx", 
    "document3.docx"
]

for doc in documents:
    print(f"Processing {doc}...")
    os.environ["INPUT_DOCX_PATH"] = doc
    os.environ["OUTPUT_DOCX_PATH"] = f"proofread_{doc}"
    main()  # Run the proofreading
```

### Processing Different File Types

The script currently supports `.docx` files. For other formats:

- **Convert .doc to .docx**: Use Word's "Save As" feature
- **PDF files**: Convert to .docx using online converters or Word
- **Google Docs**: Download as .docx format
- **Text files**: Create a simple .docx wrapper or modify the script

## Future Improvements

Potential enhancements for production use:

- **Async processing**: Use `asyncio` for faster batch processing
- **Caching**: Avoid re-processing unchanged paragraphs
- **Advanced splitting**: Better handling of very long paragraphs
- **Custom prompts**: Document-type-specific prompting
- **Web interface**: GUI for easier use
- **Batch processing**: Process multiple documents at once
- **Diff visualization**: Show changes more clearly
- **Export formats**: Support for different output formats

## License

This project is open source. Please ensure you comply with OpenAI's usage policies when using their API.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this tool!

## Support

If you encounter issues:
1. Run `python test_setup.py` to diagnose common problems
2. Check the troubleshooting section above
3. Verify your file paths are correct
4. Ensure your OpenAI API key is valid and has credits
5. Check that your input file is a valid .docx document 