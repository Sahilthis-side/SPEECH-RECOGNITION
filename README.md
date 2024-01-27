# Speech Recognition and Text-to-Speech (TTS) Python Script

This Python script utilizes the `speech_recognition` library for speech recognition and the `pyttsx3` library for text-to-speech (TTS) functionality. It continuously listens to the user's speech using the microphone, converts it to text, and then plays back the recognized text using TTS.

## Dependencies

- `speech_recognition`: A library for performing speech recognition with support for various engines, including Google Speech Recognition.
- `pyttsx3`: A text-to-speech conversion library in Python.

## Installation

To install the required dependencies, run the following commands:

```bash
pip install SpeechRecognition
pip install pyttsx3
```
## Usage
1. Run the script in a Python environment.
   ```bash
   python sp1.py
   ```
2. Speak into the microphone, and the script will recognize your speech, convert it to text, and play it back using TTS.
## Configuration
  You can adjust the script's behavior by modifying the following parameters:
  1. `rate`: Controls the speed of the TTS engine.
  2. `volume`: Sets the volume level for TTS.
  3. `voices`: Allows you to choose different voices for TTS.
## Troubleshooting
If the script fails to recognize your speech or encounters an unknown value error, it will display an error message and continue listening. You may need to adjust the microphone settings or speak more clearly.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to use, modify, and distribute this code according to the terms of the license.
