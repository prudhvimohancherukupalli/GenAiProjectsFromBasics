import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os

from dotenv import load_dotenv
load_dotenv()

# %load 
import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os

from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_API_KEY"] =os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACKING']='true'
os.environ['LANGCHAIN_PROJECT']= "Simple Q&A chaitbot with OPENAI and SteamLit"

prompt= ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful massistant.please respond to the user queries"),
        ("user","Question:{Question}")
    ]
)


def generate_repsond(Question, api_key,engine,template,mex_token):
    openai.api_key=api_key
    llm=ChatOpenAI(model=engine)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'Question':Question})
    return answer

st.title("Enhanced Q&A ChatBot with OpenAI")
st.sidebar.title("Setting")
api_key=st.sidebar.text_input("Enter your Open AI API Key:",type="password")
engine=st.sidebar.selectbox("Select OpenAI model",["gpt-4o","gpt-4-turbo","gpt-4"])

temperature =st.sidebar.slider("Temperature",min_value=0.1,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)


st.write("Go head and ask any question")
user_input=st.text_input("You:")
if user_input and api_key:
    respond=generate_repsond(user_input,api_key,engine,temperature,max_tokens)
    st.write(respond)
elif user_input:
    st.warning("Please enter the Open AI api key in the slider bar")
else:
    st.write("Please provide the user input")