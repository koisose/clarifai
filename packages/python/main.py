from dotenv import load_dotenv
import os
from getpass import getpass
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import Clarifai
load_dotenv()
os.environ["CLARIFAI_PAT"] = "CLARIFAI_PAT_TOKEN"
CLARIFAI_PAT = getpass()

