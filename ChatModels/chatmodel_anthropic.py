from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv    ##loads env variable
load_dotenv()
model =ChatAnthropic(model='claude-3-5-sonnet')
result = model.invoke("what is the capital of india?")
print(result) ## this we also give metadata along with ans 
print(result.content) ## this is only ans without metadata  