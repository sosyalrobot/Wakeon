# Wakeon Quick Start Guide

Get Wakeon running in 5 minutes!

## 🚀 Quick Setup

### 1. Install Dependencies
```bash
# Unix/Linux/macOS
./install.sh

# Windows
install.bat
```

### 2. Configure (Optional)
Edit `.env` file to add your OpenAI API key:
```bash
OPENAI_API_KEY=your_api_key_here
```

### 3. Test
```bash
python test_wakeon.py
```

### 4. Run
```bash
python wakeon.py
```

## 🎯 Basic Usage

1. Say "computer" (or your wake word)
2. Speak your command
3. Listen to the response

### Example Commands
- "What time is it?"
- "Tell me a joke"
- "Hello"
- "Help"

## 🔧 Troubleshooting

**No audio?** Check your microphone and speaker settings.

**Wake word not working?** Try speaking clearly and at normal volume.

**Need help?** Check `docs/` directory or run with debug:
```bash
DEBUG=True python wakeon.py
```

## 📚 Next Steps

- Read `docs/INSTALLATION.md` for detailed setup
- Read `docs/USAGE.md` for advanced features
- Customize your wake word and voice settings
- Add custom commands and integrations

## 🆘 Support

- GitHub Issues: Report bugs
- Documentation: Check `docs/` folder
- Test first: Run `python test_wakeon.py`

---

**Happy voice assisting! 🎙️** 