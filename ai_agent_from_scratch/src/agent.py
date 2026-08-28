import os
import json
from dotenv import load_dotenv

from ai_projects.ai_agent_from_scratch.src.tools.tools import TOOL_SCHEMAS, TOOLS_BY_NAME
load_dotenv()

def get_client_model():
    ''' Picks whichever openai compatible provider has a key set in the environment variables. Raises an error if none are set. '''
    from openai import OpenAI
    if os.environ.get("GROK_API_KEY"):
        return(
            OpenAI(api_key=os.environ["GROK_API_KEY"], base="https://api.grok.com/openapi/v1"),
            "qwen/qwen3.6-27b"
        )
    if os.environ.get("OPENROUTER_API_KEY"):
        return(
            OpenAI(api_key=os.environ["OPENROUTER_API_KEY"], base="https://api.openrouter.ai/api/v1"),
            "openrouter/free"
        )
    
    raise RuntimeError("No API key found for any OpenAI compatible provider. Please set GROK_API_KEY or OPENROUTER_API_KEY in your environment variables.")

def run_agent(messages: list, max_turns: int = 5) -> str:
    '''Loops through choose -> execute -> observe -> repeat, until 
    the model returns a final answer or max_turns is reached. Returns the final answer.'''
    
    client, model = get_client_model()
    
    for _ in range(max_turns):
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=300,
            tools=TOOL_SCHEMAS
        )
    message = response.choices[0].message
    
    if not message.tool_calls:
        messages.append({"role": "assistant", "content": message.content})
        return message.content
    
    messages.append(
        {"role": "assistant", 
         "content": message.content, 
         "tool_calls": [
             {
                 "id": call.id,
                 "type": "function",
                 "function": {"name": call.function.name, "aruguments": call.function.arguments}
             }
             for call in message.tool_calls
         ]}
    )
    
    for call in message.tool_calls:
        arguments = json.loads(call.function.arguments)
        tool_function = TOOLS_BY_NAME[call.function.name]
        result = tool_function(**arguments)
        messages.append({"role": "tool", "tool_call_id": call.id, "content": str(result)})
    
    return "Reached max_turns without a final answer."
    