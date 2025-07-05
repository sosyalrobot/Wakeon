#!/usr/bin/env python3
"""
Wakeon - A lightweight, customizable voice assistant
"""

import logging
import sys
import time
from pathlib import Path

from src.wake_word_detector import WakeWordDetector
from src.speech_recognition import SpeechRecognizer
from src.ai_processor import AIProcessor
from src.text_to_speech import TextToSpeech
from src.audio_manager import AudioManager
import config

# Configure logging
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f"{config.LOGS_DIR}/wakeon.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class WakeonAssistant:
    """Main voice assistant class that coordinates all components."""
    
    def __init__(self):
        """Initialize the voice assistant with all components."""
        logger.info("Initializing Wakeon Assistant...")
        
        try:
            self.audio_manager = AudioManager()
            self.wake_word_detector = WakeWordDetector()
            self.speech_recognizer = SpeechRecognizer()
            self.ai_processor = AIProcessor()
            self.tts = TextToSpeech()
            
            logger.info("Wakeon Assistant initialized successfully!")
            
        except Exception as e:
            logger.error(f"Failed to initialize Wakeon Assistant: {e}")
            raise
    
    def run(self):
        """Main loop for the voice assistant."""
        logger.info(f"Starting Wakeon Assistant. Say '{config.WAKE_WORD}' to activate!")
        
        try:
            while True:
                # Wait for wake word
                logger.debug("Listening for wake word...")
                if self.wake_word_detector.detect():
                    logger.info("Wake word detected!")
                    
                    # Play activation sound
                    self.audio_manager.play_activation_sound()
                    
                    # Listen for command
                    logger.debug("Listening for command...")
                    command = self.speech_recognizer.listen_for_command()
                    
                    if command:
                        logger.info(f"Command received: {command}")
                        
                        # Process with AI
                        response = self.ai_processor.process_command(command)
                        
                        if response:
                            logger.info(f"AI Response: {response}")
                            
                            # Speak the response
                            self.tts.speak(response)
                        else:
                            logger.warning("No response from AI")
                            self.tts.speak("I'm sorry, I couldn't process that request.")
                    else:
                        logger.warning("No command detected")
                        self.tts.speak("I didn't catch that. Could you repeat?")
                
                time.sleep(0.1)  # Small delay to prevent CPU overuse
                
        except KeyboardInterrupt:
            logger.info("Shutting down Wakeon Assistant...")
            self.cleanup()
        except Exception as e:
            logger.error(f"Error in main loop: {e}")
            self.cleanup()
            raise
    
    def cleanup(self):
        """Clean up resources."""
        try:
            self.audio_manager.cleanup()
            self.wake_word_detector.cleanup()
            logger.info("Cleanup completed")
        except Exception as e:
            logger.error(f"Error during cleanup: {e}")


def main():
    """Main entry point."""
    print("🎙️  Wakeon Voice Assistant")
    print("=" * 40)
    print(f"Wake word: '{config.WAKE_WORD}'")
    print("Press Ctrl+C to exit")
    print("=" * 40)
    
    try:
        assistant = WakeonAssistant()
        assistant.run()
    except Exception as e:
        logger.error(f"Failed to start Wakeon Assistant: {e}")
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 