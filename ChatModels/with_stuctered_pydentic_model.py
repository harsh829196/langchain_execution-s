
#### this not working becouse structeroutpout with pydentic is not suported in hugging fase chat 
from pydantic import BaseModel, Field, EmailStr # pydentic is a library which is used to validate the response from the model and also to convert the response into a python object. it will also help us to handle the error if the response from the model is not in the expected format. it will raise an error if the response from the model is not in the expected format. it will also help us to convert the response into a python object so that we can easily access the data from the response. it will also help us to handle the optional fields in the response. if the optional fields are not present in the response then it will set the value of those fields to None.
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from typing import Optional
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
class Review(BaseModel):
    key_themes: list[str] = Field(description="the key themes of the movie") ## this is the new way to guide our model to give the response in a specific format. we are using the Field class from pydantic to define the type of the key_themes and also providing a description of the key_themes which will help the model to understand what kind of response we are expecting from it.
    pros: Optional[list[str]] = Field(default=None, description="the pros of the movie") ## this is
    sentiment: str = Field(description="the sentiment of the review") ## this is the new way to guide our model to give the response in a specific format. we are using the Field class from pydantic to define the type of the sentiment and also providing a description of the sentiment which will help the model to understand what kind of response we are expecting from it.
    summary: str = Field(description="a brief summary of the review") ## this is the new way to guide our model to give the response in a specific format. we are using the Field class from pydantic to define the type of the summary and also providing a description of the summary which will help the model to understand what kind of response we are expecting from it.
    cons: Optional[list[str]] = Field(default=None, description="the cons of the movie") ## this is 
    name: str = Field(description="the name of the reviewer") ## this is the new way to guide our model to give the response in a specific format. we are using the Field class from pydantic to define the type of the name and also providing a description of the name which will help the model to understand what kind of response we are expecting from it.
structured_model = model.with_structured_output(Review) ## we are creating a new model with structured output
#by passing the Review class to the with_structured_output method of the model. this will
result = structured_model.invoke("write a review for the movie kalo") ## we are invoking the structured model with the query and getting the response in a structured format as defined in the Review class.
print(result) ## this will print the response from the model in a structured format as defined in the Review class.
print(result.key_themes) ## this will print the key themes of the movie from the response
print(result.pros) ## this will print the pros of the movie from the response
print(result.sentiment) ## this will print the sentiment of the review from the response    


#### this not working becouse structeroutpout with pydentic is not suported in hugging fase chat 