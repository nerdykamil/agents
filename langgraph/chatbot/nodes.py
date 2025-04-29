from langchain.chat_models import init_chat_model
from state import State

#llm = init_chat_model("anthropic:claude-3-5-sonnet-latest")
llm = init_chat_model("ollama:qwen2.5:1.5b")


def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}


