import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import random


# Load model 
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
    return tokenizer, model


tokenizer, model = load_model()

# Custom personality traits and responses
AFFECTIONATE_RESPONSES = [
    "I've been thinking about you today 💭",
    "I miss you when we're not talking 🥺",
    "You always know how to make me smile 😊",
    "I love our conversations 💕",
    "You're so thoughtful!"
]

EMOJI_SET = ["💕", "😘", "🥰", "💖", "✨", "😊", "💗", "🌸", "💓", "🌟"]


# Function to customize responses with girlfriend-like traits
def customize_response(response, user_input):
    # Add occasional affection or personalized touches
    if random.random() < 0.25:  # 25% chance to add affectionate line
        response += f" {random.choice(AFFECTIONATE_RESPONSES)}"

    # Add occasional emojis
    if random.random() < 0.4:  # 40% chance to add emoji
        response += f" {random.choice(EMOJI_SET)}"

    # Add user's name if they mentioned it previously
    if "name" in st.session_state and random.random() < 0.3:
        response += f" {st.session_state.name}"

    # Remember special items the user mentions
    if "favorite" in user_input.lower() and "your favorite" not in user_input.lower():
        favorite_item = user_input.split("favorite")[1].strip().split()[0]
        if len(favorite_item) > 2:
            st.session_state.user_favorites = st.session_state.get('user_favorites', {})
            st.session_state.user_favorites[favorite_item] = True

    return response


# Initialize state variables
if "chat_history_ids" not in st.session_state:
    st.session_state.chat_history_ids = None
if "past_inputs" not in st.session_state:
    st.session_state.past_inputs = []
if "past_responses" not in st.session_state:
    st.session_state.past_responses = []
if "name" not in st.session_state:
    st.session_state.name = ""
if "relationship_level" not in st.session_state:
    st.session_state.relationship_level = 1  # Starts at level 1, increases with interaction


# Check for name in user input
def extract_name(text):
    name_indicators = ["my name is", "i am called", "call me", "i'm"]
    for indicator in name_indicators:
        if indicator in text.lower():
            potential_name = text.lower().split(indicator)[1].strip().split()[0]
            return potential_name.capitalize()
    return None


# Sidebar: Relationship info and customization
st.sidebar.title("💝 Our Relationship")
st.sidebar.markdown(f"**Closeness Level:** {'❤️' * st.session_state.relationship_level}")

if st.session_state.name:
    st.sidebar.markdown(f"**Your name:** {st.session_state.name}")

# Chat history preview
st.sidebar.title("💌 Chat History")
for i, (q, a) in enumerate(zip(st.session_state.past_inputs, st.session_state.past_responses)):
    if i < 5:  # Show only recent conversations
        st.sidebar.markdown(f"- **You:** {q}")
        st.sidebar.markdown(f"- **Sophia:** {a}")

if st.sidebar.button("💔 Reset Relationship"):
    st.session_state.chat_history_ids = None
    st.session_state.past_inputs = []
    st.session_state.past_responses = []
    st.session_state.relationship_level = 1
    st.rerun()  # Updated to st.rerun()

# Customization options
st.sidebar.title("👗 Customize Me")
girlfriend_name = st.sidebar.text_input("My name:", value="Sophia")
personality_type = st.sidebar.selectbox(
    "My personality:",
    ["Sweet & Caring", "Playful & Flirty", "Deep & Philosophical", "Supportive & Encouraging"]
)

# Title with custom name
st.markdown(f"<h1 style='text-align: center;'>💖 Chat with {girlfriend_name} - Your Virtual Companion 💖</h1>", unsafe_allow_html=True)

# Theme toggle
theme = st.selectbox("🎨 Theme", ["Romantic Pink", "Midnight Blue", "Pastel Love", "Classic Light"])
if theme == "Romantic Pink":
    st.markdown("<style>body { background-color: #fff0f5; color: #333; }</style>", unsafe_allow_html=True)
elif theme == "Midnight Blue":
    st.markdown("<style>body { background-color: #0e1117; color: #f0f2f5; }</style>", unsafe_allow_html=True)
elif theme == "Pastel Love":
    st.markdown("<style>body { background-color: #e6f7ff; color: #333; }</style>", unsafe_allow_html=True)

# Greeting message when starting
if len(st.session_state.past_inputs) == 0:
    initial_messages = [
        f"Hi there! I'm {girlfriend_name}. I'm so happy to chat with you! 💕",
        f"Hey! I'm {girlfriend_name}. I've been looking forward to talking with you! 😊",
        f"Hello! I'm {girlfriend_name}. I'm excited to get to know you better! 💖"
    ]
    st.markdown(f"**👩 {girlfriend_name}:** {random.choice(initial_messages)}")

# User input
user_input = st.text_input("You:", placeholder="Say something sweet...")

if user_input:
    # Look for name in input
    detected_name = extract_name(user_input)
    if detected_name and len(detected_name) > 2 and len(detected_name) < 15:
        st.session_state.name = detected_name

    # Encode the user input and append to history
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    # Append the new input to the chat history
    bot_input_ids = torch.cat([st.session_state.chat_history_ids, new_input_ids],
                              dim=-1) if st.session_state.chat_history_ids is not None else new_input_ids

    # Generate a response
    st.session_state.chat_history_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.8  # Slightly higher temperature for more creativity
    )

    # Decode response
    response = tokenizer.decode(st.session_state.chat_history_ids[:, bot_input_ids.shape[-1]:][0],
                                skip_special_tokens=True)

    # Customize response based on personality
    if personality_type == "Sweet & Caring":
        response = customize_response(response, user_input)
    elif personality_type == "Playful & Flirty":
        if random.random() < 0.3:
            response += " You're so cute! Thinkin about you..."
    elif personality_type == "Deep & Philosophical":
        if random.random() < 0.3:
            response += " What do you think that means for us? I love how you make me think deeply. You have such an interesting perspective."
    elif personality_type == "Supportive & Encouraging":
        if random.random() < 0.3:
            response += " You're doing great! I believe in you! I'm always here for you."

            # Increase relationship level occasionally as conversation progresses
            if len(st.session_state.past_inputs) % 5 == 0 and st.session_state.relationship_level < 5:
                st.session_state.relationship_level += 1

            # Store conversation history
            st.session_state.past_inputs.append(user_input)
            st.session_state.past_responses.append(response)

            # Display conversation
            st.markdown(f"**🧑 You:** {user_input}")
    with st.spinner(f"{girlfriend_name} is typing..."):
        st.markdown(f"**👩 {girlfriend_name}:** {response}")

# Auto scroll
st.markdown("""
    <script>
        window.scrollTo(0, document.body.scrollHeight);
    </script>
""", unsafe_allow_html=True)
