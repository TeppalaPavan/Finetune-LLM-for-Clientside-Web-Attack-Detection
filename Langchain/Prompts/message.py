# system message is used to set the behavior of the AI assistant
# human message is the input from the user
# AI message is the response from the AI assistant
# by doing this, we can maintain the context of the conversation over multiple turns (like who is sending what message)

# if we dont include the human and AI messages, the model will not remember the previous messages in the conversation (it will get confused by which message is from whom)


from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
