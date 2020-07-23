import streamlit as st
import matplotlib.pyplot as plt
import requests

st.title('Petition signature counts')

petition_1 = st.text_input("petition id", "331430")
petition_2 = st.text_input("petition id", "325327")


data_load_state = st.text('Loading data...')



petition_1_data = requests.get(f"https://petition.parliament.uk/petitions/{petition_1}.json").json()
petition_2_data = requests.get(f"https://petition.parliament.uk/petitions/{petition_2}.json").json()


plt.bar("petition 1", petition_1_data['data']['attributes']['signature_count'], label=petition_1_data['data']['attributes']['action'], color="g")
plt.bar("petition 2", petition_2_data['data']['attributes']['signature_count'], label=petition_2_data['data']['attributes']['action'], color="r")
plt.legend()
plt.title("Petition Signatures")
st.pyplot()

st.markdown(f"Data from [petition.parliament.uk](https://petition.parliament.uk/), specificially - [1](https://petition.parliament.uk/petitions/{petition_1}), [2](https://petition.parliament.uk/petitions/{petition_2})")
