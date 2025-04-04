# 💖 Chat with Sophia - Your Virtual AI Companion!

A Streamlit app built around a fine-tuned conversational AI that simulates a caring, flirty, or supportive virtual girlfriend. Powered by Hugging Face's Microsoft `DialoGPT` model, this app is designed to deliver heartwarming, personalized chat experiences.



## 📦 Installation

**1. Clone the repository**

git clone https://github.com/ErikElcsics/Custom-Virtual-Companion-Chatbot-Using-Microsoft-DialoGPT-medium-Model-Streamlit-Python.git
cd virtual-girlfriend-chat


**2. Create a virtual environment (optional but recommended)**
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


**3. Install dependencies**

The pip install command to install all required dependencies
- pip install streamlit transformers torch

**4. (Recommended) Install CUDA-enabled PyTorch for NVIDIA GPU support**

using an NVIDIA GPU, install the CUDA-enabled version of PyTorch for better performance
Visit the [official PyTorch site](https://pytorch.org/get-started/locally/) and follow instructions specific to your CUDA version:

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118


**5. Run the app**

streamlit run VirtualCompanionApp.py


## 🌟 Features

- 🧠 Conversational AI using `microsoft/DialoGPT-medium`
- 💕 Customizable personality: Sweet, Flirty, Philosophical, Supportive
- 🎀 Themed UI: Romantic Pink, Midnight Blue, Pastel Love, Classic Light
- 📝 Relationship level tracker based on interaction
- 🗨️ Memory of recent chats and user preferences
- 🎨 Customizable companion name
- 📖 Chat history sidebar
- 🔄 Reset relationship option



## 🧠 Model Info

This app uses [DialoGPT-medium](https://huggingface.co/microsoft/DialoGPT-medium), a conversational model developed by Microsoft, fine-tuned on Reddit conversations. It’s been adapted here for personalized, emotionally expressive interactions to simulate a virtual companion.



## 🧩 How It’s Customized for a Virtual Companion

- Affectionate responses and emojis are randomly added to simulate human-like warmth.
- The model adapts to the user’s name and "remembers" favorites.
- Personality types affect the tone and structure of responses.
- Relationship level increases with meaningful interaction.



## 🚀 How to Use the App

1. Launch the app with `streamlit run VirtualCompanionApp.py`.
2. Enter your name or share personal info like "My name is Alex" to personalize.
3. Choose your companion’s name and personality in the sidebar.
4. Start chatting—watch the relationship evolve!
5. Want to reset? Use the 💔 "Reset Relationship" button anytime.



## 🧰 Libraries Used

- [`streamlit`](https://streamlit.io/)
- [`transformers`](https://huggingface.co/docs/transformers/)
- [`torch`](https://pytorch.org/)
- `random`, `re` (Python standard libraries)



## 💡 App Summary

### From a User Perspective
- Launch the app in a browser.
- Customize your virtual companion.
- Chat in real time with a flirty, caring, or supportive AI.
- Experience growing "closeness" and affection over time.
- Use the sidebar to check past conversations and companion personality.

### From a Technical Perspective
- **Model**: The `DialoGPT` model handles context-based dialogue generation.
- **Customization Layer**: Injects emojis, affectionate phrases, and name recognition.
- **State Management**: `streamlit.session_state` keeps track of chat history, personality, name, and relationship level.
- **Frontend**: Built using Streamlit with custom themes and dynamic UI updates.
- **Response Generation**:
  - Uses a temperature sampling strategy (`top_k=50`, `top_p=0.95`) for creative responses.
  - New user input is encoded, appended to past context, and fed to the model for generation.
- **Customization Engine**: Based on user input and personality type, the app tweaks the raw output for emotional realism.



## ❤️ Credits
 
Inspired by AI-human interaction and the future of emotionally intelligent agents.
