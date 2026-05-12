from dotenv import load_dotenv
import os

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

token = os.getenv("HF_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    huggingfacehub_api_token=token,
    task="text2text-generation",
    temperature=0.5## temperature is the creativity of the model , higher the temperature more creative ans will be. 
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("explain the theory of relativity in simple terms.")

print(result.content)

