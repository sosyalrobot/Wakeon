"""
Audio Manager for handling audio playback and system sounds
"""

import logging
import os
import config

# Try to import optional dependencies
try:
    import wave
    import numpy as np
    import sounddevice as sd
    AUDIO_AVAILABLE = True
except ImportError:
    AUDIO_AVAILABLE = False

logger = logging.getLogger(__name__)


class AudioManager:
    """Manages audio playback and system sounds."""
    
    def __init__(self):
        """Initialize the audio manager."""
        logger.info("Initializing audio manager...")
        
        if not AUDIO_AVAILABLE:
            logger.warning("Audio libraries not available. Using simple audio manager.")
            raise ImportError("Audio libraries not available. Install with: pip install sounddevice numpy")
        
        try:
            # Create audio output directory if it doesn't exist
            os.makedirs(config.AUDIO_OUTPUT_DIR, exist_ok=True)
            
            # Generate system sounds
            self._generate_system_sounds()
            
            logger.info("Audio manager initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize audio manager: {e}")
            raise
    
    def play_activation_sound(self):
        """Play a sound when wake word is detected."""
        try:
            # Generate a simple beep sound
            sample_rate = 44100
            duration = 0.3  # seconds
            frequency = 800  # Hz
            
            # Generate sine wave
            t = np.linspace(0, duration, int(sample_rate * duration), False)
            audio = np.sin(2 * np.pi * frequency * t) * 0.3
            
            # Play the sound
            sd.play(audio, sample_rate)
            sd.wait()
            
            logger.debug("Activation sound played")
            
        except Exception as e:
            logger.error(f"Error playing activation sound: {e}")
    
    def play_error_sound(self):
        """Play a sound when an error occurs."""
        try:
            # Generate a simple error beep
            sample_rate = 44100
            duration = 0.2  # seconds
            frequency = 400  # Hz
            
            # Generate sine wave
            t = np.linspace(0, duration, int(sample_rate * duration), False)
            audio = np.sin(2 * np.pi * frequency * t) * 0.3
            
            # Play the sound
            sd.play(audio, sample_rate)
            sd.wait()
            
            logger.debug("Error sound played")
            
        except Exception as e:
            logger.error(f"Error playing error sound: {e}")
    
    def play_success_sound(self):
        """Play a sound when a command is successful."""
        try:
            # Generate a simple success chime
            sample_rate = 44100
            duration = 0.2  # seconds
            frequency = 1000  # Hz
            
            # Generate sine wave
            t = np.linspace(0, duration, int(sample_rate * duration), False)
            audio = np.sin(2 * np.pi * frequency * t) * 0.3
            
            # Play the sound
            sd.play(audio, sample_rate)
            sd.wait()
            
            logger.debug("Success sound played")
            
        except Exception as e:
            logger.error(f"Error playing success sound: {e}")
    
    def save_audio(self, audio_data, filename, sample_rate=16000):
        """
        Save audio data to a WAV file.
        
        Args:
            audio_data (numpy.ndarray): Audio data to save
            filename (str): Name of the file to save
            sample_rate (int): Sample rate of the audio
        """
        try:
            filepath = os.path.join(config.AUDIO_OUTPUT_DIR, filename)
            
            with wave.open(filepath, 'wb') as wav_file:
                wav_file.setnchannels(1)  # Mono
                wav_file.setsampwidth(2)  # 16-bit
                wav_file.setframerate(sample_rate)
                wav_file.writeframes(audio_data.tobytes())
            
            logger.debug(f"Audio saved to {filepath}")
            
        except Exception as e:
            logger.error(f"Error saving audio: {e}")
    
    def _generate_system_sounds(self):
        """Generate system sound files."""
        try:
            # This could be expanded to generate and save various system sounds
            logger.debug("System sounds ready")
            
        except Exception as e:
            logger.error(f"Error generating system sounds: {e}")
    
    def get_audio_devices(self):
        """
        Get list of available audio devices.
        
        Returns:
            dict: Dictionary of audio devices
        """
        try:
            devices = sd.query_devices()
            return devices
        except Exception as e:
            logger.error(f"Error getting audio devices: {e}")
            return {}
    
    def set_audio_device(self, device_id):
        """
        Set the audio device for playback.
        
        Args:
            device_id (int): ID of the audio device
        """
        try:
            # This would be implemented based on the audio library being used
            logger.debug(f"Audio device set to {device_id}")
        except Exception as e:
            logger.error(f"Error setting audio device: {e}")
    
    def cleanup(self):
        """Clean up audio resources."""
        try:
            # Stop any playing audio
            sd.stop()
            logger.debug("Audio manager cleaned up")
        except Exception as e:
            logger.error(f"Error cleaning up audio manager: {e}")


class SimpleAudioManager:
    """Simple audio manager for testing."""
    
    def __init__(self):
        """Initialize simple audio manager."""
        logger.info("Initializing simple audio manager (for testing)")
    
    def play_activation_sound(self):
        """Simulate activation sound."""
        print("🔊 *activation beep*")
        logger.info("Simple activation sound played")
    
    def play_error_sound(self):
        """Simulate error sound."""
        print("🔊 *error beep*")
        logger.info("Simple error sound played")
    
    def play_success_sound(self):
        """Simulate success sound."""
        print("🔊 *success chime*")
        logger.info("Simple success sound played")
    
    def cleanup(self):
        """Clean up resources."""
        logger.debug("Simple audio manager cleaned up") 