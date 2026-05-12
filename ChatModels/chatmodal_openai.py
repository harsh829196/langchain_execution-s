from langchain_openai import ChatOpenAI   # contrl + click give sorce code  , this is inherited from basechatmodel  
from dotenv import load_dotenv    ##loads env variable
load_dotenv() 
## temperature is the creativity of the model , higher the temperature more creative ans will be
## max_completion_tokens is the maximum number of tokens the model can generate in response to a prompt it help to save tiken which are not free .
model =ChatOpenAI(models='gpt-4',temperature=0.7,max_completion_tokens=1024) ## we can also use gpt-3.5-turbo-instruct
result = model.invoke("what is the capital of india?")
print(result) ## this we also give metadata along with ans 
print(result.content) ## this is only ans without metadata
