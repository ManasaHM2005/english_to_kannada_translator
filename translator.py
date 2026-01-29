"""
English to Kannada Translator
Uses Google Cloud Translation API or translate library
"""

from typing import Optional


class KannadaTranslator:
    """Translator using translate library (free, no API key needed)"""
    
    def __init__(self):
        """Initialize the translator"""
        try:
            from translate import Translator
            self.translator = Translator(from_lang='en', to_lang='kn')
            self.available = True
        except ImportError:
            self.available = False
            self.translator = None
    
    def translate(self, text: str, target_language: str = "kn") -> dict:
        """
        Translate English text to target language (default: Kannada)
        
        Args:
            text: Text to translate
            target_language: Target language code (default: 'kn' for Kannada)
            
        Returns:
            Dictionary with original text and translated text
        """
        if not text or not text.strip():
            return {
                "original": text,
                "translated": "",
                "source_language": "en",
                "target_language": target_language,
                "error": "Empty text provided"
            }
        
        if not self.available or not self.translator:
            return {
                "original": text,
                "translated": "",
                "source_language": "en",
                "target_language": target_language,
                "error": "Translator not available. Please try again."
            }
        
        try:
            # Use the translator to convert English to Kannada
            translated = self.translator.translate(text)
            return {
                "original": text,
                "translated": translated,
                "source_language": "en",
                "target_language": target_language
            }
        except Exception as e:
            return {
                "original": text,
                "translated": "",
                "source_language": "en",
                "target_language": target_language,
                "error": f"Translation error: {str(e)}"
            }

    def batch_translate(self, texts: list, target_language: str = "kn") -> list:
        """
        Translate multiple texts
        
        Args:
            texts: List of texts to translate
            target_language: Target language code
            
        Returns:
            List of translation results
        """
        results = []
        for text in texts:
            results.append(self.translate(text, target_language))
        return results

    def batch_translate(self, texts: list, target_language: str = "kn") -> list:
        """
        Translate multiple texts
        
        Args:
            texts: List of texts to translate
            target_language: Target language code
            
        Returns:
            List of translation results
        """
        results = []
        for text in texts:
            results.append(self.translate(text, target_language))
        return results


if __name__ == "__main__":
    # Test the translator
    translator = KannadaTranslator()
    
    if translator.available:
        test_texts = [
            "Hello, how are you?",
            "Welcome to Kannada translator",
            "Good morning"
        ]
        
        print("=" * 50)
        print("English to Kannada Translator Test")
        print("=" * 50)
        
        for text in test_texts:
            result = translator.translate(text)
            print(f"\nEnglish: {result['original']}")
            if 'error' not in result:
                print(f"Kannada: {result['translated']}")
            else:
                print(f"Error: {result['error']}")
    else:
        print("Translator library not installed. Run: pip install google-translate-new")
