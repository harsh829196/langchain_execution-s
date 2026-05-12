from langchain_openai import OpenAI
from dotenv import load_dotenv    ##loads env variable     

load_dotenv()
llm = OpenAI(model= 'gpt-3.5-turbo-instruct')
result = llm.invoke("what is the capital of india") ## we will communicate thought this 
print(result)


## this is very old school , llm take sting and give string 