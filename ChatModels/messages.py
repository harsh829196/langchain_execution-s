from langchain_core.messages import  HumanMessage, SystemMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

#human message is the message which we give to the model and system message is the message which we give to the model to set the context of the conversation and AI message is the message which we get from the model as a response.
#ai message is the message which we get from the model as a response. it also contains metadata along with the response. we can access the response by using result.content and metadata by using result.metadata
#system message is the message which we give to the model to set the context of the conversation. it is optional but it is good to set the context of the conversation to get better response from the model.


import os   
load_dotenv()   ##loads env variable    
token = os.getenv("HF_TOKEN")   
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    huggingfacehub_api_token=token,
    task="text2text-generation",
    temperature=0.5## temperature is the creativity of the model , higher the temperature more creative ans will be. 
    )   
message = [
    SystemMessage(content="You are a helpful assistant."), ## this is the system message which we give to the model to set the context of the conversation. it is optional but it is good to set the context of the conversation to get better response from the model.
    HumanMessage(content="tell me about langchain?") ## this is the human message which we give to the model as a query.
]
model = ChatHuggingFace(llm=llm) ## we are creating an instance of the ChatHuggingFace class and passing the llm object to it.
result = model.invoke(message) ## we are invoking the model with the message which we have created and getting the response from the model.
message.append(AIMessage(content=result.content)) ## we are appending the model response to the message list with the label "AIMessage" so that it will be more clear and we can easily understand the conversation history between user and model. 
print(message) ## this will print the response from the model
#we will interate it on chatbot 