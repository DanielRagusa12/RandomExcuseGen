#---PPD---

import streamlit as st
import requests
import re
from streamlit_lottie import st_lottie
import json
from requests.exceptions import HTTPError




#---base_urls---

API_URL = 'https://excuser.herokuapp.com/v1/'
LOTTIE_URL_1 = 'https://assets10.lottiefiles.com/packages/lf20_5eil5ze3.json'
LOTTIE_URL_2 = 'https://assets10.lottiefiles.com/private_files/lf30_rlssnwpv.json'


#---stream_lit_config---

st.set_page_config(page_title = 'Random Excuse Generator', page_icon=':space_invader:', layout ='wide')

#---lottie load function---

def load_lottie_image(LOTTIE_URL):
    r = requests.get(LOTTIE_URL)
    if r.status_code != 200:
        return None
    return r.json()

lottie_return_1 = load_lottie_image(LOTTIE_URL_1)
lottie_return_2 = load_lottie_image(LOTTIE_URL_2)


#---main_container---

with st.container():

    category=''
    excuse=''

    st.write("---")
    
    left_column,right_column = st.columns(2)

    with right_column:
        st_lottie(lottie_return_1,height=600,key = "random_gen",quality="High")

    
    
    with left_column:
        st.header("Random Excuse Generator")
        if st.button('Click for random excuse'):
            try:
                r = requests.get(API_URL+'excuse')
                r.raise_for_status()
                
                my_dict = r.json()
                id = my_dict[0]['id']
                category = my_dict[0]['category']
                excuse = my_dict[0]['excuse']
                st.write(excuse)

            except HTTPError as http_err:
                print("HTTP ERROR OCCURED")


            except Exception as err:
                print("OTHER ERROR OCCURED")



    with left_column:        
        
        st.write("---")
        st.header('Custom Generator')
        cat_selection = st.selectbox('Pick one Category', ['Family', 'Office', 'Children', 'College', 'Party'])
        num_selection = st.number_input('Number of Excuses', 1, 10)
        if st.button('Generate'):
            try:
                st.write("")
                st.write("")
                
                cat_select_lower = cat_selection[0].lower() + cat_selection[1:]
        
                r = requests.get('https://excuser.herokuapp.com/v1/excuse/'+cat_select_lower+'/'+str(num_selection))
                r.raise_for_status()
                
                generated_list = r.json()
                
                for i in range (num_selection):
                    st.write(str(i+1)+': '+generated_list[i]['excuse'])
                    st.write("***")  
            
            except HTTPError as http_err:
                print("HTTP ERROR OCCURED")


            except Exception as err:
                print("OTHER ERROR OCCURED")
