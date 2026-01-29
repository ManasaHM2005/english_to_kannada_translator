"""
Flask Web Application for English to Kannada Translator
"""

from flask import Flask, render_template, request, jsonify
from translator import KannadaTranslator
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize translator
translator = KannadaTranslator()


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/api/translate', methods=['POST'])
def translate():
    """
    API endpoint for translation
    
    Expected JSON payload:
    {
        "text": "text to translate",
        "target_language": "kn" (optional, default: "kn")
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({
                'error': 'No text provided'
            }), 400
        
        text = data.get('text', '').strip()
        target_language = data.get('target_language', 'kn')
        
        if not text:
            return jsonify({
                'error': 'Empty text provided'
            }), 400
        
        result = translator.translate(text, target_language)
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            'error': f'Translation error: {str(e)}'
        }), 500


@app.route('/api/batch-translate', methods=['POST'])
def batch_translate():
    """
    API endpoint for batch translation
    
    Expected JSON payload:
    {
        "texts": ["text1", "text2", ...],
        "target_language": "kn" (optional)
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'texts' not in data:
            return jsonify({
                'error': 'No texts provided'
            }), 400
        
        texts = data.get('texts', [])
        target_language = data.get('target_language', 'kn')
        
        if not texts or not isinstance(texts, list):
            return jsonify({
                'error': 'Texts must be a non-empty list'
            }), 400
        
        results = translator.batch_translate(texts, target_language)
        
        return jsonify({
            'results': results
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': f'Batch translation error: {str(e)}'
        }), 500


@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'English to Kannada Translator'
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error'
    }), 500


if __name__ == '__main__':
    # Run the Flask app
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.getenv('FLASK_PORT', 5000))
    
    print("=" * 60)
    print("🌐 English to Kannada Translator")
    print("=" * 60)
    print(f"✓ Flask app starting on http://localhost:{port}")
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    
    app.run(debug=debug_mode, port=port, host='0.0.0.0')
