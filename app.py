import streamlit as st
from streamlit_option_menu import option_menu
import pickle

st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed",
    page_title="Anirek",
    page_icon=":robot_face:",
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

selected = option_menu(
    None, ["Rek", "About","Contact"],
    icons=['robot', 'info-circle','envelope-at'],
    default_index=0, 
    orientation="horizontal"
    )

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

if selected == "About":
    
    st.markdown("""
            Anime :grey[is a form of hand-drawn or computer-generated animation originating from Japan.]
            :grey[In terms of genres, there are more than] **34,211+** :grey[anime listed on] [myanimelist.net](https://myanimelist.net/anime.php).
                
            **The problem is the difficulty in finding anime that aligns with individual viewer preferences due to the vast number of options available.**
            :grey[**This leads to users spending excessive time searching instead of watching content.**]
            <br>
            
            This is web app is designed for anime viewers who
            <!--<p style="text-align: left; color: #808495; font-size: 30px;">This is web app is designed for anime viewers who</p>-->
            
            - Feel overwhelmed by the vast amount of anime available
            -  Want to avoid wasting time on anime they won't enjoy
            -  Appreciate a streamlined and user-friendly experience
            """, unsafe_allow_html=True)
        
if selected == "Rek":
    st.markdown("""
                <h1 style="color: #3DD56D; text-align: center;">I'm 🤖 Rek</h1>
                """, unsafe_allow_html=True)
    st.markdown("""
                <p style="text-align: center;">Anime recommendation companion</p>
                """, unsafe_allow_html=True)
    
    animes = pickle.load(open('anime_list.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    anime_list=animes['title'].values
    
    selectvalue=st.selectbox(" ",anime_list, label_visibility="hidden")
    
    def recommend(anime):
        index = animes[animes['title']==anime].index[0]
        distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
        recommend_anime=[]
        anime_poster=[]
        for i in distance[1:6]:
            recommend_anime.append(animes.iloc[i[0]]['title'])
            anime_poster.append(animes.iloc[i[0]]['img_url'])
        return recommend_anime, anime_poster
    
    if selectvalue:
         anime_name, anime_cover = recommend(selectvalue)
         col1,col2,col3,col4,col5=st.columns(5)
         with col1:
              st.text(anime_name[0])
              st.image(anime_cover[0])
         with col2:
              st.text(anime_name[1])
              st.image(anime_cover[1])
         with col3:
              st.text(anime_name[2])
              st.image(anime_cover[2])
         with col4:
              st.text(anime_name[3])
              st.image(anime_cover[3])
         with col5:
              st.text(anime_name[4])
              st.image(anime_cover[4])
if selected == "Contact":
    
        st.header(":email: GET IN TOUCH")

        contact_form = """
        <form action="https://formsubmit.co/aavesbilal@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <textarea name="message" placeholder="Message"></textarea>
        <br>
        <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

        # CSS for contact form
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
                
                local_css("style.css")