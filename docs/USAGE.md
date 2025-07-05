# Wakeon Usage Guide

Learn how to use Wakeon effectively and customize it for your needs.

## Basic Usage

### Starting Wakeon

1. Activate your virtual environment:
```bash
source venv/bin/activate  # Unix/Linux/macOS
# or
venv\Scripts\activate.bat  # Windows
```

2. Start the assistant:
```bash
python wakeon.py
```

3. Wait for the startup message and say your wake word (default: "computer")

### Using Wakeon

1. **Wake Word**: Say "computer" (or your custom wake word)
2. **Command**: Speak your command or question
3. **Response**: Listen to Wakeon's response

### Example Commands

- "What's the weather today?"
- "What time is it?"
- "Tell me a joke"
- "What's the date?"
- "Hello"
- "Help"

## Configuration

### Environment Variables

Edit your `.env` file to customize Wakeon:

```bash
# Wake Word
WAKE_WORD=jarvis  # Change to your preferred wake word

# Voice Settings
TTS_VOICE_RATE=150    # Speech speed (words per minute)
TTS_VOICE_VOLUME=0.9  # Volume level (0.0 to 1.0)

# AI Settings
OPENAI_MODEL=gpt-3.5-turbo  # AI model to use
OPENAI_MAX_TOKENS=150       # Maximum response length

# Audio Settings
TIMEOUT_SECONDS=30          # How long to listen for commands
```

### Wake Word Customization

To use a custom wake word with Porcupine:

1. Get a Porcupine access key from [Picovoice Console](https://console.picovoice.ai/)
2. Create a custom wake word
3. Download the `.ppn` file
4. Update your `.env`:
```
PORCUPINE_ACCESS_KEY=your_access_key
PORCUPINE_KEYWORD_PATH=path/to/your/wakeword.ppn
```

## Advanced Features

### Custom Commands

You can extend Wakeon with custom commands by modifying the AI processor:

```python
# In src/ai_processor.py, add to _fallback_response method:
elif "custom" in command_lower:
    return "This is a custom response!"
```

### Smart Home Integration

Example integration with smart home devices:

```python
def control_lights(command):
    if "turn on lights" in command.lower():
        # Add your smart home API calls here
        return "Lights turned on"
    elif "turn off lights" in command.lower():
        # Add your smart home API calls here
        return "Lights turned off"
```

### Media Controls

Add media control commands:

```python
def control_media(command):
    if "play music" in command.lower():
        # Add your media player integration here
        return "Playing music"
    elif "pause" in command.lower():
        # Add pause functionality
        return "Media paused"
```

## Troubleshooting

### Common Issues

1. **Wake word not detected**:
   - Speak clearly and at normal volume
   - Check microphone settings
   - Try a different wake word

2. **Commands not recognized**:
   - Speak slowly and clearly
   - Check if Vosk model is properly installed
   - Try the fallback input mode

3. **No AI responses**:
   - Check your OpenAI API key
   - Verify internet connection
   - Check API usage limits

4. **Audio issues**:
   - Test microphone and speakers
   - Check audio device settings
   - Try different audio devices

### Debug Mode

Run Wakeon with debug logging:

```bash
DEBUG=True LOG_LEVEL=DEBUG python wakeon.py
```

### Logs

Check the logs for detailed information:

```bash
tail -f logs/wakeon.log
```

## Tips for Better Performance

1. **Microphone**: Use a good quality microphone in a quiet environment
2. **Wake Word**: Choose a unique wake word that's easy to pronounce
3. **Commands**: Speak naturally but clearly
4. **Responses**: Keep AI responses concise for better voice output
5. **Updates**: Keep dependencies updated for best performance

## Extending Wakeon

### Adding New Components

1. Create a new module in the `src/` directory
2. Implement the required interface
3. Update the main `wakeon.py` file to use your component

### Plugin System

You can create a plugin system for easy extensions:

```python
# Example plugin structure
plugins/
├── weather_plugin.py
├── music_plugin.py
└── smart_home_plugin.py
```

### GUI Interface

Add a graphical interface using PyQt5 or Tkinter:

```python
# Example GUI integration
from PyQt5.QtWidgets import QApplication, QMainWindow

class WakeonGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wakeon Voice Assistant")
        # Add your GUI components here
```

## Support

- **Documentation**: Check the docs/ directory
- **Issues**: Report bugs on GitHub
- **Community**: Join discussions in GitHub Discussions
- **Contributing**: Submit pull requests for improvements 