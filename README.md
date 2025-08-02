# OIBSIP_Python_1_Voice_assistant_Internship
As a project for my internship at Oasis Infobyte

# AI Voice Assistant – Oasis Infobyte Internship

## 🎯 Objective
The objective of this project was to build a **voice-controlled AI assistant** using Python that can perform everyday tasks like telling time, searching Wikipedia, playing music, opening system apps, and telling jokes — all through **Hinglish (Hindi+English) voice commands**.

---

## 🛠 Tools & Technologies Used
- **Python 3.9**
- `speech_recognition` – Convert speech to text
- `gTTS` + `pygame` – Text-to-speech conversion
- `wikipedia` – Quick summaries
- `pyjokes` – Generate random jokes
- `subprocess` & `webbrowser` – System and web automation

---

## 📝 Steps Performed
1. **Voice Input Setup** – Used `speech_recognition` to capture user commands via microphone.  
2. **Text-to-Speech Output** – Converted assistant responses into speech using `gTTS` and played using `pygame`.  
3. **Command Handling** – Implemented logic to respond to:
   - Greeting and activation words (*"hello"*, *"theek hai"*)
   - Tell current time
   - Wikipedia search summaries
   - Play jokes, music, or open calculator/notepad/paint
   - Google search queries
4. **Error Handling** – Added fallback for unclear speech, no internet, or unknown commands.  
5. **Testing** – Verified responses and command accuracy on multiple Hinglish commands.

---

## 📊 Outcome
- Successfully created a **working voice assistant** that performs multiple tasks using Hinglish commands.  
- Learned **speech-to-text and text-to-speech integration** and improved understanding of **automation with Python**.  
- The project can be **extended to GUI or more APIs** like weather, news, etc.

---

## ▶️ How to Run
1. Install dependencies:
   ```bash
   pip install speechrecognition gTTS pygame wikipedia pyjokes
