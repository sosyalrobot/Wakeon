# Wakeon Installation Guide

This guide will help you install and set up Wakeon on your system.

## Prerequisites

- Python 3.8 or higher
- Microphone and speakers
- OpenAI API key (optional, for advanced features)

## Quick Installation

### Unix/Linux/macOS

1. Clone the repository:
```bash
git clone https://github.com/sosyalrobot/wakeon.git
cd wakeon
```

2. Run the installation script:
```bash
./install.sh
```

### Windows

1. Clone the repository:
```cmd
git clone https://github.com/sosyalrobot/wakeon.git
cd wakeon
```

2. Run the installation script:
```cmd
install.bat
```

## Manual Installation

If you prefer to install manually:

1. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate.bat
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create necessary directories:
```bash
mkdir -p models logs audio_output
```

4. Copy environment template:
```bash
cp env.example .env
```

## Configuration

1. Edit the `.env` file with your settings:
```bash
nano .env  # or use your preferred editor
```

2. Set your OpenAI API key (optional):
```
OPENAI_API_KEY=your_actual_api_key_here
```

3. Customize other settings as needed:
- `WAKE_WORD`: Change the wake word (default: "computer")
- `TTS_VOICE_RATE`: Adjust speech speed
- `TTS_VOICE_VOLUME`: Adjust volume level

## Speech Recognition Setup

For better speech recognition, download a Vosk model:

1. Visit [Vosk Models](https://alphacephei.com/vosk/models)
2. Download a model (recommended: `vosk-model-small-en-us-0.15`)
3. Extract to the `models/` directory
4. Update the path in your `.env` file:
```
VOSK_MODEL_PATH=models/vosk-model-small-en-us-0.15
```

## Testing

Run the test suite to verify everything works:

```bash
python test_wakeon.py
```

## Running Wakeon

Start the voice assistant:

```bash
python wakeon.py
```

Say your wake word (default: "computer") and then speak your command.

## Troubleshooting

### Common Issues

1. **Audio not working**: Check your microphone and speaker settings
2. **Import errors**: Make sure you're in the virtual environment
3. **Permission errors**: Run with appropriate permissions
4. **API errors**: Check your OpenAI API key and internet connection

### Getting Help

- Check the logs in the `logs/` directory
- Run with debug mode: `DEBUG=True python wakeon.py`
- Open an issue on GitHub

## Next Steps

- Customize the wake word
- Add custom commands
- Integrate with smart home devices
- Create a GUI interface 