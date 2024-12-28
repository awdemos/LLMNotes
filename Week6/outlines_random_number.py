import requests
import os
import struct
from pydantic import BaseModel, Field
import json
from openai import OpenAI
from datetime import datetime

def get_random_float32():
    random_bytes = os.urandom(4)
    float32_value = struct.unpack('f', random_bytes)[0]
    return float32_value

class DynamicResponse(BaseModel):
    content: dict = Field(..., alias="root")

# Generate the float32 salt using Random.org
salt = get_random_float32()

# Initialize the OpenAI client for Ollama
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

# Prepare the query with the salt included in the prompt
query = f"""Using the salt value {salt}, generate a response.
Your response must be a valid JSON object with two key-value pairs.
Do not include any text before or after the JSON object."""

# Generate the structured output and parse the JSON response
try:
    response = client.chat.completions.create(
        model="llama3.2",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that responds in JSON format."},
            {"role": "user", "content": query}
        ],
        temperature=0.7,
    )
    print(f"Raw response: {response.choices[0].message.content}")
    
    content = response.choices[0].message.content.strip()
    parsed_content = json.loads(content)
    result = DynamicResponse(root=parsed_content)
    status = "success"
except json.JSONDecodeError as e:
    print(f"JSON Decode Error: {str(e)}")
    result = f"Error: Invalid JSON response - {content[:100]}..."
    status = "error"
except (AttributeError, IndexError, KeyError) as e:
    result = f"Error: Unexpected response structure - {str(e)}"
    status = "error"
except Exception as e:
    print(f"API call failed: {str(e)}")
    result = f"Error: API call failed - {str(e)}"
    status = "error"

# Prepare the output
output = {
    "timestamp": datetime.now().isoformat(),
    "salt": salt,
    "response": result.content if isinstance(result, DynamicResponse) else str(result),
    "status": status
}

# Print the JSON output
print(json.dumps(output, indent=2))

