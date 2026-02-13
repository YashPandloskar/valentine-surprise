import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="For You 💌",
    page_icon="🌹",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS - HIGH CONTRAST VERSION
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@400;700&display=swap');

    /* Animated Pink Background */
    .stApp {
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fad0c4, #ffdde1);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* THE WHITE CARD CONTAINER */
    div.block-container {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 25px;
        padding: 2rem;
        margin-top: 2rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        max-width: 600px;
    }

    /* Titles - BRIGHT RED */
    h1 {
        font-family: 'Great Vibes', cursive;
        color: #ff2b2b !important;
        text-align: center;
        font-size: 3.5rem !important;
        margin-bottom: 0px;
        text-shadow: none;
    }
    
    /* Body Text - DEEP PINK/RED */
    p {
        font-family: 'Poppins', sans-serif;
        color: #d63384 !important; /* Deep Pink */
        text-align: center;
        font-size: 1.2rem !important;
        font-weight: 500;
    }

    /* The "Eyes" Quote - Special Styling */
    .quote-box {
        background-color: #fff0f5; /* Very light pink background */
        border-left: 5px solid #ff2b2b;
        padding: 15px;
        margin: 20px 0;
        border-radius: 5px;
    }
    
    .quote-text {
        font-family: 'Poppins', sans-serif;
        color: #c2185b; /* Dark Pink */
        font-size: 1.3rem;
        font-weight: bold;
        text-align: center;
    }

    /* Buttons */
    div.stButton > button {
        width: 100%;
        border-radius: 30px;
        height: 60px;
        font-size: 20px;
        font-weight: bold;
        border: none;
    }
    
    /* YES Button - Red */
    div.stButton > button[kind="primary"] {
        background-color: #ff2b2b;
        color: white;
        box-shadow: 0 4px 10px rgba(255, 43, 43, 0.3);
    }

    /* NO Button - Grey Text */
    div.stButton > button[kind="secondary"] {
        background-color: #f0f2f6;
        color: #333; /* Dark Grey for readability */
        border: 1px solid #ccc;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. Session State Management
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'yes_clicked' not in st.session_state:
    st.session_state.yes_clicked = False

# 4. Main App Logic
def main():
    
    # --- SUCCESS PAGE (SHE SAID YES) ---
    if st.session_state.yes_clicked:
        st.balloons()
        
        # Title
        st.markdown("<h1>She Said YES! 💖</h1>", unsafe_allow_html=True)
        
        # Celebration GIF
        st.image("https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif", use_container_width=True)
        
        # Sweet Message
        st.markdown("""
        <div class='quote-box'>
            <div class='quote-text'>You've made me so happy.</div>
            <p style='margin-top: 10px; font-size: 1.1rem !important;'>
            I promise to make you feel special every single day.<br>
            (And yes, I'm still obsessed with your eyes.)
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # THE BACK BUTTON
        if st.button("Go Back ↩️", type="secondary"):
            st.session_state.yes_clicked = False
            st.rerun()
            
        return

    # --- PROPOSAL PAGE (MAIN) ---
    st.markdown("<h1>Be My Valentine?</h1>", unsafe_allow_html=True)
    
    # Cute Bear GIF
    st.image("https://media.giphy.com/media/l0K4kWJir91VEoa1W/giphy.gif", use_container_width=True)
    
    # THE QUOTE (High Contrast)
    st.markdown("""
    <div class='quote-box'>
        <div class='quote-text'>I am in love with your eyes.</div>
        <p style='font-size: 1rem !important; margin-top: 5px;'>
        Every time I look at you, I forget what I was going to say.<br>
        Let me make this day about you.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("") # Spacer

    # Buttons layout
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("YES 💖", type="primary", use_container_width=True):
            st.session_state.yes_clicked = True
            st.rerun()

    with col2:
        # Dynamic No Button
        no_texts = [
            "No",
            "Are you sure?",
            "Look at my eyes 🥺",
            "Don't break my heart",
            "I'll cry...",
            "Please?",
            "Last chance!",
            "Error 404"
        ]
        
        step = st.session_state.no_count
        text_index = min(step, len(no_texts) - 1)
        
        # Logic: If clicked less than 8 times, show button.
        if step < 8:
            if st.button(no_texts[text_index], type="secondary", use_container_width=True):
                st.session_state.no_count += 1
                st.rerun()
        else:
            # Replaces button with text when gone
            st.markdown("<p style='color: red; font-weight: bold;'>Only YES allowed 😈</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
