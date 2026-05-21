from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Create a chat template
chat_template = ChatPromptTemplate.from_messages([
    ('system', "You are a helpful assistant."),
    ('human', "Explain in simple terms, what is {query}")
])

# Replace {query} with actual value
prompt = chat_template.format_prompt(query="LangChain")

# Convert prompt into message objects
print(prompt.to_messages())