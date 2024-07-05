# JaJathon: GenAI based Virtual banking assistant
A virtual genAI financial assistant 

## ChatVRM

<img src="public/ogp-en.png" width="600">

ChatVRM is a demo application that allows you to easily talk with a 3D character in your browser.

By importing VRM files, you can adjust the voice to match the character, and generate responses that include emotional expressions.

ChatVRM mainly uses the following technologies:

- User speech recognition
    - [Web Speech API (SpeechRecognition)](https://developer.mozilla.org/ja/docs/Web/API/SpeechRecognition)
- Text to speech
    - [ElevenLabs](https://beta.elevenlabs.io/)
- Displaying 3D characters
    - [@pixiv/three-vrm](https://github.com/pixiv/three-vrm)

## Execution
Clone or download this repository to run locally.

```bash
git clone https://github.com/adas598/jajathon-vr-banking-assistant.git
```

Please install the required packages.
```bash
npm install
```

After package installation is complete, start the development web server with the following command.
```bash
npm run dev
```

After execution, access the following URL.

[http://localhost:3000](http://localhost:3000) 

---

## ElevenLabs
ChatVRM uses ElevenLabs API to do text to speech.

- [https://beta.elevenlabs.io/](https://beta.elevenlabs.io/)
