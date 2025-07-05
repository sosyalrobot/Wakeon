# Wakeon

Wakeon is a lightweight, customizable voice assistant you can run on your computer. It listens for your personal wake word and connects to ChatGPT (or any other AI API) to process your commands and respond with speech. No cloud dependency, no corporate restrictions — just your own assistant, your rules.

---

## 🚀 Features

- 🎙 **Custom Wake Word**  
  Use any wake word you like — no more "Hey Google" or "Alexa." Powered by open-source wake word engines like Porcupine or Snowboy.

- 🧠 **ChatGPT Integration**  
  Sends your speech input to OpenAI’s API and returns intelligent responses.

- 🔊 **Text-to-Speech (TTS)**  
  Wakeon speaks the AI’s response out loud using local TTS engines like pyttsx3 or Coqui TTS.

- ⚡ **Runs Locally**  
  No vendor lock-in. Your assistant runs entirely on your machine, respecting your privacy.

- 🛠 **Modular & Hackable**  
  Easily extend with new features (smart home controls, media commands, etc).

---

## 🛠 Tech Stack

- Python 3
- Porcupine / Snowboy (for wake word detection)
- Vosk / SpeechRecognition (for speech-to-text)
- OpenAI API (for AI responses)
- pyttsx3 / Coqui TTS (for text-to-speech)
- Optionally: PyQt5 (for a GUI)

---

## ⚡ Getting Started

### 1️⃣ Clone the repo
```bash
git clone https://github.com/sosyalrobot/wakeon.git
cd wakeon
````

### 2️⃣ Install requirements

```bash
pip install -r requirements.txt
```

### 3️⃣ Set your OpenAI API key

Edit `config.py`:

```python
OPENAI_API_KEY = "your_api_key_here"
```

### 4️⃣ Run it

```bash
python wakeon.py
```

---

## 📂 Example Usage

Say your wake word (e.g., "computer") — Wakeon will listen for your command:
🗣 *"What’s the weather today?"*
Wakeon will respond using ChatGPT and read the reply aloud.

---

## 🤖 Roadmap

* [ ] Add support for multiple wake words
* [ ] Integrate smart home device commands
* [ ] GUI with real-time speech transcript
* [ ] Offline AI model (optional)

---

## 📄 License

MIT License

---

## 🙌 Contributing

Pull requests are welcome. Feel free to open issues for feature requests or bugs!

---

## 🔗 Links

* [Porcupine](https://picovoice.ai/platform/porcupine/)
* [OpenAI API](https://platform.openai.com/)
* [Vosk](https://alphacephei.com/vosk/)
* [pyttsx3](https://pyttsx3.readthedocs.io/)
