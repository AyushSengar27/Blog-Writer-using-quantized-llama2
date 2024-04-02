import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

#Fuction to get response from Llama2 model
def getLlamaResponse(input_text,no_words,blog_style):
    llm = CTransformers(model='models\llama-2-7b-chat.ggmlv3.q8_0.bin',model_type='llama',
                        config={'temperature':0.5})
    

    template = """Write a blog on {input_text} with the writing style as {blog_style} in {no_words} words."""
    prompt = PromptTemplate(input_variables = ['input_text','no_words','blog_style'],
                   template=template)
    response= llm(prompt.format(input_text=input_text,no_words=no_words,blog_style=blog_style))
    print(response)
    return(response)




st.set_page_config(page_title="Generate Blogs",layout = "centered",initial_sidebar_state='collapsed',page_icon="💬")
st.header("Generate Blogs 💬")
input_text = st.text_input("Enter the blog topic")

col1,col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("Number of words")

with col2:
    blog_style = st.selectbox('Select Writing Style',("Formal","Informal","Educational","Creative"),index=0)

submit = st.button("Write")

if submit:
    st.write(getLlamaResponse(input_text,no_words,blog_style))

