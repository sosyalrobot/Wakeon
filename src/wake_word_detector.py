"""
Wake Word Detection using Porcupine
"""

import logging
import config

# Try to import optional dependencies
try:
    import pvporcupine
    import pvrecorder
    import numpy as np
    PORCUPINE_AVAILABLE = True
except ImportError:
    PORCUPINE_AVAILABLE = False

logger = logging.getLogger(__name__)


class WakeWordDetector:
    """Detects wake words using Porcupine."""
    
    def __init__(self):
        """Initialize the wake word detector."""
        logger.info("Initializing wake word detector...")
        
        if not PORCUPINE_AVAILABLE:
            logger.warning("Porcupine not available. Using simple wake word detector.")
            raise ImportError("Porcupine not available. Install with: pip install pvporcupine pvrecorder")
        
        try:
            # Initialize Porcupine
            if config.PORCUPINE_ACCESS_KEY:
                # Use custom wake word if access key is provided
                self.porcupine = pvporcupine.create(
                    access_key=config.PORCUPINE_ACCESS_KEY,
                    keyword_paths=[config.PORCUPINE_KEYWORD_PATH] if config.PORCUPINE_KEYWORD_PATH else None,
                    keywords=[config.WAKE_WORD] if not config.PORCUPINE_KEYWORD_PATH else None
                )
            else:
                # Use built-in wake words
                self.porcupine = pvporcupine.create(
                    keywords=[config.WAKE_WORD]
                )
            
            # Initialize recorder
            self.recorder = pvrecorder.PvRecorder(
                device_index=-1,
                frame_length=self.porcupine.frame_length
            )
            
            logger.info(f"Wake word detector initialized with wake word: '{config.WAKE_WORD}'")
            
        except Exception as e:
            logger.error(f"Failed to initialize wake word detector: {e}")
            raise
    
    def detect(self):
        """
        Detect wake word in audio stream.
        
        Returns:
            bool: True if wake word detected, False otherwise
        """
        try:
            self.recorder.start()
            
            while True:
                pcm = self.recorder.read()
                keyword_index = self.porcupine.process(pcm)
                
                if keyword_index >= 0:
                    self.recorder.stop()
                    return True
                    
        except Exception as e:
            logger.error(f"Error in wake word detection: {e}")
            self.recorder.stop()
            return False
    
    def cleanup(self):
        """Clean up resources."""
        try:
            if hasattr(self, 'recorder'):
                self.recorder.stop()
                self.recorder.delete()
            if hasattr(self, 'porcupine'):
                self.porcupine.delete()
            logger.debug("Wake word detector cleaned up")
        except Exception as e:
            logger.error(f"Error cleaning up wake word detector: {e}")


class SimpleWakeWordDetector:
    """Simple wake word detector for testing without Porcupine."""
    
    def __init__(self):
        """Initialize simple wake word detector."""
        logger.info("Initializing simple wake word detector (for testing)")
        self.detected = False
    
    def detect(self):
        """
        Simulate wake word detection.
        
        Returns:
            bool: True if wake word detected, False otherwise
        """
        # For testing purposes, always return True after a delay
        import time
        time.sleep(2)
        return True
    
    def cleanup(self):
        """Clean up resources."""
        logger.debug("Simple wake word detector cleaned up") 