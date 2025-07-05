#!/usr/bin/env python3
"""
Simple test for Wakeon Voice Assistant (no external dependencies)
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test that all modules can be imported."""
    print("🧪 Testing Module Imports")
    print("=" * 30)
    
    try:
        # Test config import
        import config
        print("✅ config.py: OK")
        
        # Test simple components (these don't require external deps)
        from wake_word_detector import SimpleWakeWordDetector
        print("✅ SimpleWakeWordDetector: OK")
        
        from speech_recognition import SimpleSpeechRecognizer
        print("✅ SimpleSpeechRecognizer: OK")
        
        from ai_processor import SimpleAIProcessor
        print("✅ SimpleAIProcessor: OK")
        
        from text_to_speech import SimpleTextToSpeech
        print("✅ SimpleTextToSpeech: OK")
        
        from audio_manager import SimpleAudioManager
        print("✅ SimpleAudioManager: OK")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_simple_flow():
    """Test the simple components without external dependencies."""
    print("\n🔄 Testing Simple Flow")
    print("=" * 30)
    
    try:
        # Initialize simple components
        from wake_word_detector import SimpleWakeWordDetector
        from speech_recognition import SimpleSpeechRecognizer
        from ai_processor import SimpleAIProcessor
        from text_to_speech import SimpleTextToSpeech
        from audio_manager import SimpleAudioManager
        
        wake_detector = SimpleWakeWordDetector()
        speech_recognizer = SimpleSpeechRecognizer()
        ai_processor = SimpleAIProcessor()
        tts = SimpleTextToSpeech()
        audio_manager = SimpleAudioManager()
        
        print("✅ All components initialized")
        
        # Test wake word detection
        print("Testing wake word detection...")
        detected = wake_detector.detect()
        print(f"✅ Wake word detection: {detected}")
        
        # Test speech recognition
        print("Testing speech recognition...")
        command = speech_recognizer.listen_for_command()
        print(f"✅ Speech recognition: '{command}'")
        
        # Test AI processing
        print("Testing AI processing...")
        response = ai_processor.process_command(command)
        print(f"✅ AI processing: '{response}'")
        
        # Test text-to-speech
        print("Testing text-to-speech...")
        tts.speak(response)
        print("✅ Text-to-speech: OK")
        
        # Test audio manager
        print("Testing audio manager...")
        audio_manager.play_activation_sound()
        audio_manager.play_success_sound()
        print("✅ Audio manager: OK")
        
        # Cleanup
        wake_detector.cleanup()
        speech_recognizer.cleanup()
        ai_processor.cleanup()
        tts.cleanup()
        audio_manager.cleanup()
        
        print("\n🎉 Simple flow test completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Simple flow test failed: {e}")
        return False

def test_config():
    """Test configuration loading."""
    print("\n⚙️  Testing Configuration")
    print("=" * 30)
    
    try:
        import config
        
        # Test basic config values
        print(f"Wake word: {config.WAKE_WORD}")
        print(f"Sample rate: {config.SAMPLE_RATE}")
        print(f"TTS engine: {config.TTS_ENGINE}")
        print(f"Debug mode: {config.DEBUG}")
        
        # Test directory creation
        print(f"Audio output dir: {config.AUDIO_OUTPUT_DIR}")
        print(f"Logs dir: {config.LOGS_DIR}")
        print(f"Models dir: {config.MODELS_DIR}")
        
        print("✅ Configuration test passed")
        return True
        
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def main():
    """Main test function."""
    print("🎙️  Wakeon Voice Assistant - Simple Test Suite")
    print("=" * 50)
    
    # Test imports
    if not test_imports():
        print("❌ Import tests failed!")
        sys.exit(1)
    
    # Test configuration
    if not test_config():
        print("❌ Configuration tests failed!")
        sys.exit(1)
    
    # Test simple flow
    if not test_simple_flow():
        print("❌ Simple flow tests failed!")
        sys.exit(1)
    
    print("\n🎉 All simple tests passed!")
    print("\nNext steps:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Run full tests: python test_wakeon.py")
    print("3. Start Wakeon: python wakeon.py")

if __name__ == "__main__":
    main() 