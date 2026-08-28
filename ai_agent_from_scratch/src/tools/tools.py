import calculator 
import get_weather
import convert_currency

TOOL_SCHEMAS =[
    {
        "type": "function",
        "function": {
            "name": "convert_currency",
            "description": "Convert currency using live exchange rates",
            "parameters": {
                "type": "object",
                "properties": {
                    "amount": {
                        "type": "number",
                        "description": "The amount to convert"
                    },
                    "from_currency": {
                        "type": "string",
                        "description": "The currency to convert from, 3 letter code e.g. USD, EUR, GBP"
                    },
                    "to_currency": {
                        "type": "string",
                        "description": "The currency to convert to, 3 letter code e.g. USD, EUR, GBP"
                    }
                },
                "required": ["amount", "from_currency", "to_currency"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a given city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The name of the city to get the weather for"
                    }
                },
                "required": ["city"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Evaluate a mathematical expression",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The mathematical expression to evaluate"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

TOOLS_BY_NAME = {
    "convert_currency": convert_currency,
    "get_weather": get_weather,
    "calculator": calculator
}