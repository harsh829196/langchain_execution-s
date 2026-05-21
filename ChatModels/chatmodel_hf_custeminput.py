from langchain_core.messages import  HumanMessage, SystemMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from dotenv import load_dotenv

from langchain_core.messages import  HumanMessage, SystemMessage, AIMessage

import os #for accessing env variable
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
    task="text2text-generation",
    temperature=0.5
)

model = ChatHuggingFace(llm=llm)
chat_history = [] ## this is the list which will store the conversation history between user and model
while True:
    query = input("Hello how i can assist you: ")
    chat_history.append( HumanMessage(content =query)) ## we are appending the user query to the chat history list with the label "user"  
    if query.lower() == 'exit':
        print(chat_history) ## this will print the conversation history between user and model when user exit the chat
        break
    
    result = model.invoke(chat_history) ## we are passing the chat history to the model so that it can connect the two query together and give us the correct ans which is 90.
    
    chat_history.append(AIMessage(content=result.content)) ## we are appending the model response to the chat history list with the label "model"
    
    print(f"AI: {result.content}")
    

# Hello how i can assist you: tell me which is greater 5, 9?
# AI: 9 is greater than 5.
# Hello how i can assist you: now multipy this number with 10 
# AI: However, I don't see a number provided. Please provide the number you'd like to multiply by 10.
# Hello how i can assist you: _______- this means it dont remenber the previous conversation and it is not able to connect the two query together.  
# there for we need to give the conversation history to the model so that it can connect the two query together and give us the correct ans which is 90.

# Hello how i can assist you: which is greater 5 or 6
# AI: 6 is greater than 5.
# Hello how i can assist you: now multiply it with 10 
# AI: 6 multiplied by 10 is 60.
# Hello how i can assist you: 

# there is a problem we dont know that which is user qurey and which is model response so we can give label to the user query and model response in the chat history list so that it will be more clear and we can easily understand the conversation history between user and model. 
# so we can append the user query to the chat history list with the label "user" and model response with the label "model" so that it will be more clear and we can easily understand the conversation history between user and model.    
# we will move toweards dynamic msg 
#we will use chatprompttemplte to create dynamic message and we will use system message to set the context of the conversation.