import streamlit as st
from streamlit_option_menu import option_menu
from app_utils import switch_page
from PIL import Image

im = Image.open("icon.png")
st.set_page_config(page_title="InterPrep AI", layout="centered", page_icon=im)

lan = st.selectbox("#### Language", ["English"])

if lan == "English":
    home_title = "InterPrep AI"
    home_introduction = "Welcome to InterPrep AI, empowering your interview preparation with generative AI."
    with st.sidebar:
        st.markdown(""" 
        #### Let's contact:
        [Mrudul John](https://www.linkedin.com/in/mruduljohnmathews/)
        #### Powered by
    
        [OpenAI](https://openai.com/)
    
        [FAISS](https://github.com/facebookresearch/faiss)
    
        [Langchain](https://github.com/hwchase17/langchain)
    
                    """)
    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True
    )
    st.image(im, width=100)
    st.markdown(f"""# {home_title} """, unsafe_allow_html=True)
    st.markdown("""\n""")
    st.markdown("Welcome to InterPrep AI! 👏 This is your personal interviewer powered by generative AI that conducts mock interviews and gives you suggestions."
                "You can upload your resume and enter job descriptions, and InterPrep AI will ask you customized questions. Additionally, you can configure your own Interviewer!")
    st.markdown("""\n""")
    st.markdown("#### Get started!")
    st.markdown("Select one of the following screens to start your interview!")
    selected = option_menu(
        menu_title=None,
        options=["Professional", "Resume", "Behavioral", "Customize!"],
        icons=["cast", "cloud-upload", "cast"],
        default_index=0,
        orientation="horizontal",
    )
    if selected == 'Professional':
        st.info("""
            📚In this mode, the InterPrep AI will assess your technical skills as they relate to the job description.
            Note: The maximum length of your answer is 4097 tokens!
            - Each Interview will take 10 to 15 mins.
            - To start a new session, just refresh the page.
            - Start introduce yourself and enjoy！ """)
        if st.button("Start Interview!"):
            switch_page("Professional Screen")
    if selected == 'Resume':
        st.info("""
        📚In this session, the InterPrep AI will review your resume and discuss your past experiences.
        Note: The maximum length of your answer is 4097 tokens!
        - Each Interview will take 10 to 15 mins.
        - To start a new session, just refresh the page.
        - Start introduce yourself and enjoy！ """
                )
        if st.button("Start Interview!"):
            switch_page("Resume Screen")
    if selected == 'Behavioral':
        st.info("""
        📚In this session, the InterPrep AI will assess your soft skills as they relate to the job description.
        Note: The maximum length of your answer is 4097 tokens!
        - Each Interview will take 10 to 15 mins.
        - To start a new session, just refresh the page.
        - Start introduce yourself and enjoy！ 
        """)
        if st.button("Start Interview!"):
            switch_page("Behavioral Screen")
    if selected == 'Customize!':
        st.info("""
            📚In this session, you can customize your own InterPrep AI and practice with it!
             - Configure AI Interviewer in different specialties.
             - Configure AI Interviewer in different personalities.""")

# The rest of your code...
