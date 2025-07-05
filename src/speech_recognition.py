"""
Speech Recognition using Vosk
"""

import logging
import config

# Try to import optional dependencies
try:
    import sounddevice as sd
    import numpy as np
    import json
    import vosk
    VOSK_AVAILABLE = True
except ImportError:
    VOSK_AVAILABLE = False

logger = logging.getLogger(__name__)


class SpeechRecognizer:
    """Handles speech-to-text conversion using Vosk."""
    
    def __init__(self):
        """Initialize the speech recognizer."""
        logger.info("Initializing speech recognizer...")
        
        if not VOSK_AVAILABLE:
            logger.warning("Vosk not available. Using fallback speech recognition.")
            self.use_fallback = True
            return
        
        try:
            # Initialize Vosk model
            if not vosk.Model.exists(config.VOSK_MODEL_PATH):
                logger.warning(f"Vosk model not found at {config.VOSK_MODEL_PATH}")
                logger.info("Please download a Vosk model from https://alphacephei.com/vosk/models")
                logger.info("For now, using fallback speech recognition...")
                self.use_fallback = True
            else:
                self.model = vosk.Model(config.VOSK_MODEL_PATH)
                self.rec = vosk.KaldiRecognizer(self.model, config.SAMPLE_RATE)
                self.use_fallback = False
                logger.info("Speech recognizer initialized with Vosk")
                
        except Exception as e:
            logger.error(f"Failed to initialize speech recognizer: {e}")
            self.use_fallback = True
    
    def listen_for_command(self, timeout=config.TIMEOUT_SECONDS):
        """
        Listen for a voice command.
        
        Args:
            timeout (int): Maximum time to listen in seconds
            
        Returns:
            str: Recognized text or None if no speech detected
        """
        logger.debug("Listening for command...")
        
        if self.use_fallback:
            return self._fallback_listen()
        
        try:
            # Record audio
            audio_data = self._record_audio(timeout)
            
            if audio_data is None:
                return None
            
            # Process with Vosk
            if self.rec.AcceptWaveform(audio_data.tobytes()):
                result = json.loads(self.rec.Result())
                text = result.get('text', '').strip()
                
                if text:
                    logger.info(f"Recognized: {text}")
                    return text
                else:
                    logger.debug("No speech detected")
                    return None
            else:
                logger.debug("Speech not fully processed")
                return None
                
        except Exception as e:
            logger.error(f"Error in speech recognition: {e}")
            return None
    
    def _record_audio(self, timeout):
        """
        Record audio from microphone.
        
        Args:
            timeout (int): Recording timeout in seconds
            
        Returns:
            numpy.ndarray: Audio data or None if recording failed
        """
        try:
            logger.debug(f"Recording audio for {timeout} seconds...")
            
            # Record audio
            audio_data = sd.rec(
                int(timeout * config.SAMPLE_RATE),
                samplerate=config.SAMPLE_RATE,
                channels=config.CHANNELS,
                dtype=np.int16
            )
            sd.wait()
            
            return audio_data
            
        except Exception as e:
            logger.error(f"Error recording audio: {e}")
            return None
    
    def _fallback_listen(self):
        """
        Fallback speech recognition using input().
        
        Returns:
            str: User input or None
        """
        try:
            print("🎤 Speak your command (or type it): ", end="", flush=True)
            command = input().strip()
            
            if command:
                logger.info(f"Fallback input: {command}")
                return command
            else:
                return None
                
        except KeyboardInterrupt:
            return None
        except Exception as e:
            logger.error(f"Error in fallback input: {e}")
            return None
    
    def cleanup(self):
        """Clean up resources."""
        logger.debug("Speech recognizer cleaned up")


class SimpleSpeechRecognizer:
    """Simple speech recognizer for testing."""
    
    def __init__(self):
        """Initialize simple speech recognizer."""
        logger.info("Initializing simple speech recognizer (for testing)")
    
    def listen_for_command(self, timeout=5):
        """
        Simulate speech recognition.
        
        Returns:
            str: Simulated command
        """
        import time
        time.sleep(1)
        return "What's the weather today?"
    
    def cleanup(self):
        """Clean up resources."""
        logger.debug("Simple speech recognizer cleaned up") 