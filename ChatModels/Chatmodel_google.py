from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv    ##loads env variable
load_dotenv()
model =ChatGoogleGenerativeAI(model='gemini-pro')
result = model.invoke("what is the capital of india?")
print(result) ## this we also give metadata along with ans 
print(result.content) ## this is only ans without metadata      