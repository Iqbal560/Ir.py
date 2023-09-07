import streamlit as st
from langchain .llms import OpenAI
st.title('Quickstart App ChatGpt')
openai_api_key=st.sidebar.text_input('OpenAI API Key')
#openai_api_key="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"
def generate_response(text_input):
	llm=OpenAI(temperature=0.7,openai_api_key=openai_api_key)
	st.info(llm(text_input))
with st.form('my_form'):
	text=st.text_area('Enter text:''What are the three key pieces of advice how to learn code')
	submitted=st.form_submit_button('Submit')
	if not openai_api_key.startswith('sk-'):
		st.warning('please enter your openai_api_key!')
	if submitted and openai_api_key.startswith('sk-'):
		generate_response(text)
