import streamlit as st
from datetime import datetime

def set_bg():
    bg_url = "https://raw.githubusercontent.com/digitalangel444/self-care-app/98aed4de0d358507ea8ced9fc60240e2a257c509/pic.png"
    bg_style = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background: url("{bg_url}") no-repeat center center fixed;
        background-size: cover;
    }}
    [data-testid="stSidebar"] {{
        background-color: rgba(40, 40, 40, 0.95) !important;
        border-radius: 10px;
        padding: 10px;
        color: white !important;
    }}
    .main-container {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }}
    .main-title {{
        color: #ffffff !important; 
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        text-shadow: 2px 2px 4px #000000;
        margin-bottom: 10px;
    }}
    .sub-header {{
        color: #ffffff !important; 
        text-align: center;
        font-size: 20px;
        text-shadow: 1px 1px 2px #000000;
        margin-bottom: 20px;
    }}
    .task-progress {{
        color: #ffffff !important;
        background-color: rgba(0, 0, 0, 0.6);
        padding: 15px;
        border-radius: 5px;
        margin: 15px 0;
    }}
    .stCheckbox label {{
        color: white !important;
    }}
    .stProgress > div > div > div {{
        background-color: #4CAF50 !important;
    }}
    .status-message {{
        background-color: rgba(0, 0, 0, 0.7) !important;
        color: white !important;
        padding: 10px;
        border-radius: 5px;
    }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

def main():
    set_bg()

    st.markdown("""
    <div class="main-container">
        <h1 class="main-title">🌿 Self-Care Application</h1>
        <h3 class="sub-header">📅 Date: {date}</h3>
    </div>
    """.format(date=datetime.now().strftime("%Y-%m-%d")), unsafe_allow_html=True)

    categories = {
        "💪 Physical Health": ["🏃 Morning Exercise", "💧 Drink Water", "🥗 Eat Healthy", "🚶 Go for a Walk", "😴 Get Enough Sleep"],
        "📚 Learning Skills": ["📖 Read a Book", "💻 Practice Coding", "📝 Learn New Words", "🎥 Watch Educational Video", "🧩 Solve Puzzles"],
        "🎉 Entertainment": ["🎵 Listen to Music", "🎬 Watch a Movie", "🎮 Play a Game", "🎨 Draw or Paint", "👫 Spend Time with Friends"]
    }

    st.sidebar.title("📌 Task Categories")
    completed_tasks = 0
    total_tasks = sum(len(tasks) for tasks in categories.values())

    for category, tasks in categories.items():
        st.sidebar.markdown(f'**{category}**', unsafe_allow_html=True)
        for task in tasks:
            if st.sidebar.checkbox(task):
                completed_tasks += 1

    progress = (completed_tasks / total_tasks) * 100 if total_tasks else 0
    
    st.markdown(f"""
    <div class="task-progress">
        <h3>✅ Tasks Completed: {completed_tasks}/{total_tasks} ({progress:.0f}%)</h3>
    </div>
    """, unsafe_allow_html=True)
    st.progress(progress / 100)

    status_container = st.empty()
    if progress >= 70:
        status_container.markdown("""
        <div class="status-message">
            🎯 Perfect! Keep it up! 💪
        </div>
        """, unsafe_allow_html=True)
    elif progress >= 40:
        status_container.markdown("""
        <div class="status-message">
            👍 Good Job! You're on the right track!
        </div>
        """, unsafe_allow_html=True)
    else:
        status_container.markdown("""
        <div class="status-message">
            🔥 You can do it! Keep pushing!
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    st.markdown("""
    <div style="color: white; background-color: rgba(0, 0, 0, 0.6); padding: 10px; border-radius: 5px;">
        🌱 Made with ❤️ by Noa
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
    st.caption("✨ Noa's Project")
