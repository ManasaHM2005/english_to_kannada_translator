# English to Kannada Translator

A complete English to Kannada translation application with web interface and CLI support.

## Features

- 🌐 **Web Interface**: Beautiful, responsive web UI for easy translation
- 📱 **Mobile Friendly**: Works seamlessly on desktop, tablet, and mobile devices
- 🔄 **Batch Translation**: Translate multiple texts at once via API
- 💾 **Multiple Input Methods**: Web UI, CLI, or API
- 🎨 **Modern Design**: Clean and intuitive user interface
- ⚡ **Fast**: Instant translation powered by Google Cloud Translation API
- 📝 **Character Limit**: Support for up to 5000 characters per translation

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project**:
   ```bash
   cd english_to_kannada_translator
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Google Cloud Setup (Optional but Recommended)

For the best translation quality, set up Google Cloud Translation API:

1. **Create a Google Cloud Project**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable the Cloud Translation API

2. **Create Service Account**:
   - Go to "Service Accounts" in the Google Cloud Console
   - Create a new service account
   - Create a JSON key for the service account
   - Download the JSON file

3. **Set up Environment Variable**:
   - Save the JSON file securely on your machine
   - Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable:
     - On Windows (PowerShell):
       ```powershell
       $env:GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your\service-account-key.json"
       ```
     - On macOS/Linux:
       ```bash
       export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
       ```

## Usage

### Web Interface

1. **Start the Flask application**:
   ```bash
   python app.py
   ```

2. **Open your browser** and go to:
   ```
   http://localhost:5000
   ```

3. **Enter English text** in the left text area

4. **Click "Translate"** to get the Kannada translation

### Command-Line Interface (CLI)

1. **Translate text directly**:
   ```bash
   python cli_translator.py "Hello, how are you?"
   ```

2. **Translate from a file**:
   ```bash
   python cli_translator.py -f input.txt -o output.txt
   ```

3. **Pipe text from stdin**:
   ```bash
   echo "Good morning" | python cli_translator.py
   ```

4. **Get JSON output**:
   ```bash
   python cli_translator.py "Hello" --format json
   ```

### Python API

```python
from translator import KannadaTranslator

# Initialize translator
translator = KannadaTranslator()

# Single translation
result = translator.translate("Hello, how are you?")
print(result['translated'])

# Batch translation
texts = ["Good morning", "Welcome", "Thank you"]
results = translator.batch_translate(texts)
for result in results:
    print(f"{result['original']} → {result['translated']}")
```

### REST API

1. **Start the Flask app**:
   ```bash
   python app.py
   ```

2. **Single Translation**:
   ```bash
   curl -X POST http://localhost:5000/api/translate \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello, world!"}'
   ```

3. **Batch Translation**:
   ```bash
   curl -X POST http://localhost:5000/api/batch-translate \
     -H "Content-Type: application/json" \
     -d '{"texts": ["Hello", "Good morning", "Welcome"]}'
   ```

4. **Health Check**:
   ```bash
   curl http://localhost:5000/health
   ```

## Project Structure

```
english_to_kannada_translator/
├── app.py                    # Flask web application
├── translator.py             # Core translation logic
├── cli_translator.py         # Command-line interface
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── .env.example             # Example environment variables
└── templates/
    └── index.html           # Web interface HTML/CSS/JS
```

## Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

```env
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=False
FLASK_PORT=5000

# Google Cloud Configuration
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service-account-key.json
```

## API Response Format

### Successful Translation

```json
{
  "original": "Hello, how are you?",
  "translated": "ನಿಮಗೆ ಹೇಗೆ ಇದೆ?",
  "source_language": "en",
  "target_language": "kn"
}
```

### Error Response

```json
{
  "original": "text",
  "translated": "",
  "source_language": "en",
  "target_language": "kn",
  "error": "Error message"
}
```

## Supported Languages

While this translator is optimized for English to Kannada (kn), it supports translation to any language supported by Google Cloud Translation API. Common language codes:

- `kn` - Kannada (default)
- `en` - English
- `hi` - Hindi
- `ta` - Tamil
- `te` - Telugu
- `ml` - Malayalam
- `es` - Spanish
- `fr` - French
- `de` - German

## Troubleshooting

### Google Cloud Credentials Error

If you see: `google.auth.exceptions.DefaultCredentialsError`

**Solution**:
- Make sure `GOOGLE_APPLICATION_CREDENTIALS` environment variable is set correctly
- The path should be absolute and the file should exist
- Reload your terminal after setting the environment variable

### Translation Quality

If translations are not accurate or complete:
- Check that your input text is clear and well-formatted
- For long texts, try breaking them into sentences
- Some technical or domain-specific terms may not translate perfectly

### Flask App Won't Start

If you get a "port already in use" error:
```bash
python app.py --port 5001
```

Or kill the process using the port:
- On Windows: `netstat -ano | findstr :5000`
- On macOS/Linux: `lsof -i :5000`

## Requirements

- Flask 2.3.0+
- google-cloud-translate 3.11.1+
- python-dotenv 1.0.0+

See `requirements.txt` for exact versions.

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review Google Cloud Translation API documentation
3. Open an issue in the project repository

---

**Happy Translating! 🌍**