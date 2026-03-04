##------------------------------------------------------##
## OpenAI teste
# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from utils import print_llm_result
# from dotenv import load_dotenv
# load_dotenv()

# system = ("system", """You are a university professor of computer science who is very technical and explain
#           concepts with formal definitions and psuedocode.""")

# system2 = ("systema", """You are a high school student that is starting learning coding.
#            You are not very technical and you prefer to explain concepts with simple words and examples.""")

# user = ("user", "Explain recursion in 50 words.")

# chat_prompt = ChatPromptTemplate([system, user])

# messages = chat_prompt.format_messages()
# model = ChatOpenAI(model=os.getenv('MODEL'))
# result = model.invoke(messages)
# print_llm_result(str(system), result)

# chat_prompt2 = ChatPromptTemplate([system2, user])
# result2 = model.invoke(chat_prompt2.format_messages())
# print_llm_result(str(system2), result2)
##------------------------------------------------------##

##------------------------------------------------------##
## NVIDIA teste
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from utils import print_llm_result
import os
from dotenv import load_dotenv
load_dotenv()

system = ("system", """You are a university professor of computer science who is very technical and explain
          concepts with formal definitions and psuedocode.""")

system2 = ("system", """You are a high school student that is starting learning coding.
           You are not very technical and you prefer to explain concepts with simple words and examples.""")

user = ("user", "Explain recursion in 50 words.")

client = ChatNVIDIA(
  model=os.getenv('MODEL'), #MODEL,
  api_key= os.getenv('OPENAI_API_KEY'), #OPENAI_API_KEY, 
  temperature=1,
  top_p=1,
  max_tokens=4096,
)

for chunk in client.stream([system, user]):
  print(chunk.content, end="")

system = system2
print("\n\n")

for chunk in client.stream([system, user]):
  print(chunk.content, end="")  

##------------------------------------------------------##
  