#!/usr/bin/env python3
"""
Test script for Wakeon Voice Assistant
"""

import logging
import sys
import time

from src.wake_word_detector import SimpleWakeWordDetector
from src.speech_recognition import SimpleSpeechRecognizer
from src.ai_processor import SimpleAIProcessor
from src.text_to_speech import SimpleTextToSpeech
from src.audio_manager import SimpleAudioManager
import config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def test_components():
    """Test all components individually."""
    print("🧪 Testing Wakeon Components")
    print("=" * 40)
    
    try:
        # Test Audio Manager
        print("1. Testing Audio Manager...")
        audio_manager = SimpleAudioManager()
        audio_manager.play_activation_sound()
        audio_manager.play_success_sound()
        audio_manager.play_error_sound()
        print("✅ Audio Manager: OK")
        
        # Test Wake Word Detector
        print("2. Testing Wake Word Detector...")
        wake_detector = SimpleWakeWordDetector()
        detected = wake_detector.detect()
        print(f"✅ Wake Word Detector: {detected}")
        
        # Test Speech Recognition
        print("3. Testing Speech Recognition...")
        speech_recognizer = SimpleSpeechRecognizer()
        command = speech_recognizer.listen_for_command()
        print(f"✅ Speech Recognition: '{command}'")
        
        # Test AI Processor
        print("4. Testing AI Processor...")
        ai_processor = SimpleAIProcessor()
        response = ai_processor.process_command(command)
        print(f"✅ AI Processor: '{response}'")
        
        # Test Text-to-Speech
        print("5. Testing Text-to-Speech...")
        tts = SimpleTextToSpeech()
        tts.speak(response)
        print("✅ Text-to-Speech: OK")
        
        # Cleanup
        audio_manager.cleanup()
        wake_detector.cleanup()
        speech_recognizer.cleanup()
        ai_processor.cleanup()
        tts.cleanup()
        
        print("\n🎉 All components tested successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        logger.error(f"Test failed: {e}")
        return False


def test_full_flow():
    """Test the complete voice assistant flow."""
    print("\n🔄 Testing Full Flow")
    print("=" * 40)
    
    try:
        # Initialize components
        audio_manager = SimpleAudioManager()
        wake_detector = SimpleWakeWordDetector()
        speech_recognizer = SimpleSpeechRecognizer()
        ai_processor = SimpleAIProcessor()
        tts = SimpleTextToSpeech()
        
        print("Listening for wake word...")
        
        # Simulate wake word detection
        if wake_detector.detect():
            print("Wake word detected!")
            audio_manager.play_activation_sound()
            
            # Listen for command
            print("Listening for command...")
            command = speech_recognizer.listen_for_command()
            
            if command:
                print(f"Command: {command}")
                
                # Process with AI
                response = ai_processor.process_command(command)
                
                if response:
                    print(f"Response: {response}")
                    tts.speak(response)
                    audio_manager.play_success_sound()
                else:
                    print("No response from AI")
                    tts.speak("I'm sorry, I couldn't process that request.")
                    audio_manager.play_error_sound()
            else:
                print("No command detected")
                tts.speak("I didn't catch that. Could you repeat?")
                audio_manager.play_error_sound()
        
        # Cleanup
        audio_manager.cleanup()
        wake_detector.cleanup()
        speech_recognizer.cleanup()
        ai_processor.cleanup()
        tts.cleanup()
        
        print("✅ Full flow test completed!")
        return True
        
    except Exception as e:
        print(f"❌ Full flow test failed: {e}")
        logger.error(f"Full flow test failed: {e}")
        return False


def main():
    """Main test function."""
    print("🎙️  Wakeon Voice Assistant - Test Suite")
    print("=" * 50)
    
    # Test individual components
    if not test_components():
        print("❌ Component tests failed!")
        sys.exit(1)
    
    # Test full flow
    if not test_full_flow():
        print("❌ Full flow test failed!")
        sys.exit(1)
    
    print("\n🎉 All tests passed! Wakeon is ready to use.")
    print("\nTo run the full assistant:")
    print("1. Set your OpenAI API key in config.py")
    print("2. Run: python wakeon.py")


if __name__ == "__main__":
    main() 