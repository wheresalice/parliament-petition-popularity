import streamlit as st
import matplotlib.pyplot as plt
import requests

st.title('Public opinion of mask usage in shops in England')

data_load_state = st.text('Loading data...')

repeal_shop_masks = requests.get("https://petition.parliament.uk/petitions/331430.json").json()
# print(repeal_shop_masks['data']['attributes']['signature_count'])
require_shop_masks = requests.get("https://petition.parliament.uk/petitions/325327.json").json()
# print(require_shop_masks['data']['attributes']['signature_count'])

data_load_state.text('Loading data...done!')

plt.bar("repeal", repeal_shop_masks['data']['attributes']['signature_count'], label="Repeal law requiring masks in shops", color="g")
plt.bar("require", require_shop_masks['data']['attributes']['signature_count'], label="Make wearing masks in shops mandatory", color="r")
plt.legend()
plt.title("Public opinion on masks in England")
st.pyplot()

st.markdown("Data from [petition.parliament.uk](https://petition.parliament.uk/), specificially - [make mandatory](https://petition.parliament.uk/petitions/325327), [repeal](https://petition.parliament.uk/petitions/331430)")