import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar :
    selected = option_menu ('bukanya urut yhh',
    ['p','buka yg inii','abis tu yg ini','nah ini closing wkw'],
    default_index=0)

if (selected == 'p') :
    st.title('Haiii Jilly :wave:')
    st.subheader('Gimana kabarnya? sehat2 kan?')
    st.subheader('semangat ya buat PKL-nyaa')
    st.write('btww, coba buka menu yg di pojok kiri atas jil')

if (selected == 'buka yg inii') : 
    st.write('*ini beneran hari ini kan jil, plis semoga beneran :pensive:') 
    st.write('---')
    st.subheader('to Jilan Hakam aka Jilly')
    st.title('Happy Birthday :tada:')
    st.title('tiup lilin online :partying_face::candle:')
    st.title('Yeayy :tada::tada::tada:')
    st.write('---')
    st.write('ciee dah umur 31 ya')
    st.write('dah jadi sepuh gais :relieved:')
    st.write('*canda')

if (selected == 'abis tu yg ini') :
        st.write('---')
        st.title('Sekali lagi selamat ulang tahun ya jil')
        st.subheader('May your birthday bring boundless joy and all your dreams come true!!!')
        st.subheader('anddd')
        st.subheader("Thank you for everyyy moments we've shared :smile: :pray:")
        st.write('---')
        st.write('truss km kan dah sepuh nih, jan lupa sholat wkwk, makan yg bener jil, istirahat juga jan lupa, semangat pklnya dan kuliah nantii, pejuang 3.3 kan katanya, semoga tercapaii aamiinnnn:palms_up_together:')
        st.write('*maap ya kesannya kek lagi ngomel, tp ini ngga ngomel kokk')

if (selected == 'nah ini closing wkw') :
    with st.container():
        st.write("---")
        st.header("Teruntuk sepuh :bowing_woman: ")
        st.write("terakhirrr")
        st.write('maap ya jil ngerepotin :pensive: :pray:')
        st.write("---")
    contact_form = """
    <form action="https://formsubmit.co/septinafisa1972@gmail.com" method="POST">
    <label for="kado">mau kado apa nii</label>
    <input type="text" id="kado" name="kado" placeholder="plis jawaaaabbb" required>
    <br>
    <button type="submit"> kirimm </button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
