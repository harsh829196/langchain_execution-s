from langchain_core.messages import  HumanMessage, SystemMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from typing import TypedDict,Annotated,Optional # we are importing the Annotated class from the typing module to create a new type which will be used to define the structure of the response from the model.
from dotenv import load_dotenv
import os #for accessing env variable
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
    task="text2text-generation",
    temperature=0.5
)  
model= ChatHuggingFace(llm=llm) 
class Review(TypedDict): # behind the seen a prompts creats by own to creatre a json format in class 
                         #difined by us and then it will pass to the model and model will give the response in the same format as defined in the class. 
    #summary: str -- this also works but we can guide our modle
    summary: Annotated[str,"a brief summary of the review"] ## this is the new way to guide our model to give the response in a specific format. we are using the Annotated class to define the type of the summary and also providing a description of the summary which will help the model to understand what kind of response we are expecting from it.
    sentiment: Annotated[str,"the sentiment of the review"] ## this is the new way to guide our model to give the response in a specific format. we are using the Annotated class to define the type of the sentiment and also providing a description of the sentiment which will help the model to understand what kind of response we are expecting from it.
    #we do many things here # optional becouse when no prons ? exixtes 
    pros: Annotated[Optional[list[str]],"the pros of the movie"] ## this is the new way to guide our model to give the response in a specific format. we are using the Annotated class to define the type of the pros and also providing a description of the pros which will help the model to understand what kind of response we are expecting from it.
    keys: Annotated[Optional[list[str]],"the key features of the movie"] ## this is the new way to guide our model to give the response in a specific format. we are using the Annotated class to define the type of the keys and also providing a description of the keys which will help the model to understand what kind of response we are expecting from it.
structured_model = model.with_structured_output(Review) ## we are creating a new model with structured output
#by passing the Review class to the with_structured_output method of the model. this will allow us to get the 
# response from the model in a structured format as defined in the Review class.
result = structured_model.invoke("write a review for the movie Inception") ## we are invoking the structured model with the query and getting the response in a structured format as defined in the Review class.
print(result) ## this will print the response from the model in a structured format as defined in
print(result["summary"]) ## this will print the summary of the review from the response    
print(result["sentiment"]) ## this will print the sentiment of the review from the response
print(result["pros"]) ## this will print the pros of the movie from the response
print(result["keys"]) ## this will print the key features of the movie from the response    
