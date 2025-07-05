"""
Text-to-Speech using pyttsx3
"""

import logging
import config

# Try to import optional dependencies
try:
    import pyttsx3
    PYTTSX3_AVAILABLE = True
except ImportError:
    PYTTSX3_AVAILABLE = False

logger = logging.getLogger(__name__)


class TextToSpeech:
    """Handles text-to-speech conversion using pyttsx3."""
    
    def __init__(self):
        """Initialize the text-to-speech engine."""
        logger.info("Initializing text-to-speech engine...")
        
        if not PYTTSX3_AVAILABLE:
            logger.warning("pyttsx3 not available. Using simple text-to-speech.")
            raise ImportError("pyttsx3 not available. Install with: pip install pyttsx3")
        
        try:
            # Initialize pyttsx3 engine
            self.engine = pyttsx3.init()
            
            # Configure voice properties
            self.engine.setProperty('rate', config.TTS_VOICE_RATE)
            self.engine.setProperty('volume', config.TTS_VOICE_VOLUME)
            
            # Get available voices and set a good one
            voices = self.engine.getProperty('voices')
            if voices:
                # Try to find a female voice, otherwise use the first available
                female_voice = None
                for voice in voices:
                    if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
                        female_voice = voice
                        break
                
                if female_voice:
                    self.engine.setProperty('voice', female_voice.id)
                else:
                    self.engine.setProperty('voice', voices[0].id)
                
                logger.info(f"TTS initialized with voice: {self.engine.getProperty('voice')}")
            else:
                logger.warning("No voices found for TTS")
            
        except Exception as e:
            logger.error(f"Failed to initialize text-to-speech: {e}")
            raise
    
    def speak(self, text):
        """
        Convert text to speech and play it.
        
        Args:
            text (str): Text to speak
        """
        if not text:
            logger.warning("No text provided for speech")
            return
        
        try:
            logger.debug(f"Speaking: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
            logger.debug("Speech completed")
            
        except Exception as e:
            logger.error(f"Error in text-to-speech: {e}")
            # Fallback to print if TTS fails
            print(f"🔊 {text}")
    
    def set_voice_rate(self, rate):
        """
        Set the speech rate.
        
        Args:
            rate (int): Speech rate (words per minute)
        """
        try:
            self.engine.setProperty('rate', rate)
            logger.debug(f"Voice rate set to {rate}")
        except Exception as e:
            logger.error(f"Error setting voice rate: {e}")
    
    def set_voice_volume(self, volume):
        """
        Set the speech volume.
        
        Args:
            volume (float): Volume level (0.0 to 1.0)
        """
        try:
            self.engine.setProperty('volume', volume)
            logger.debug(f"Voice volume set to {volume}")
        except Exception as e:
            logger.error(f"Error setting voice volume: {e}")
    
    def get_available_voices(self):
        """
        Get list of available voices.
        
        Returns:
            list: List of available voice names
        """
        try:
            voices = self.engine.getProperty('voices')
            return [voice.name for voice in voices]
        except Exception as e:
            logger.error(f"Error getting available voices: {e}")
            return []
    
    def cleanup(self):
        """Clean up resources."""
        try:
            if hasattr(self, 'engine'):
                self.engine.stop()
            logger.debug("Text-to-speech engine cleaned up")
        except Exception as e:
            logger.error(f"Error cleaning up text-to-speech: {e}")


class SimpleTextToSpeech:
    """Simple text-to-speech for testing."""
    
    def __init__(self):
        """Initialize simple text-to-speech."""
        logger.info("Initializing simple text-to-speech (for testing)")
    
    def speak(self, text):
        """
        Simulate text-to-speech by printing.
        
        Args:
            text (str): Text to speak
        """
        print(f"🔊 {text}")
        logger.info(f"Simple TTS: {text}")
    
    def cleanup(self):
        """Clean up resources."""
        logger.debug("Simple text-to-speech cleaned up") 