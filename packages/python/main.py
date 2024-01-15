from dotenv import load_dotenv
import os
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import Clarifai
load_dotenv()
# CLARIFAI_PAT = os.environ["CLARIFAI_PAT"]
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
MODEL_URL = "https://clarifai.com/openai/chat-completion/models/GPT-4"
clarifai_llm = Clarifai(model_url=MODEL_URL)
llm_chain = LLMChain(prompt=prompt, llm=clarifai_llm)
question = "What is a cat?"

panda=llm_chain.invoke(question)
print(panda)