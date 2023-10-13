import json

import yaml

# Load the OpenAPI specification (assuming it's in YAML format)
with open('openapi/openapi.yaml', 'r') as yaml_file:
    openapi_spec = yaml.safe_load(yaml_file)

# Define a function to format a single path
def format_path(path, path_data):
    formatted_path = f'**{path_data.get("summary", "No summary provided")}**\n----\n'
    formatted_path += f'  {path_data.get("description", "No description provided")}.\n'
    formatted_path += f'* **URL Params**\n'

    parameters = path_data.get("parameters", [])
    if parameters:
        formatted_path += '  *Required:* ' + ', '.join([f'`{param["name"]}' + (f'=[{param.get("type", "")}]`' if "type" in param else '`[type]`') for param in parameters]) + '\n'
    else:
        formatted_path += '  None\n'

    formatted_path += '* **Data Params**\n'
    if "requestBody" in path_data:
        try:
            # Serialize the dictionary to a JSON-formatted string
            json_data = json.dumps(path_data["requestBody"], indent=2)
            formatted_path += f'  ```json\n{json_data}\n  ```\n'
        except json.JSONDecodeError:
            formatted_path += '  None\n'
    else:
        formatted_path += '  None\n'

    formatted_path += '* **Headers**\n'
    formatted_path += '  Content-Type: application/json\n'
    formatted_path += '  Authorization: Bearer `<OAuth Token>`\n'
    
    formatted_path += '* **Success Response:**\n'
    formatted_path += '* **Code:** 200\n'
    formatted_path += '  **Content:**  `{ <user_object> }`\n'
    
    formatted_path += '* **Error Response:**\n'
    formatted_path += '  * **Code:** 404\n'
    formatted_path += '  **Content:** `{ error : "User doesn\'t exist" }`\n'
    formatted_path += '  OR\n'
    formatted_path += '  * **Code:** 401\n'
    formatted_path += '  **Content:** `{ error : error : "You are unauthorized to make this request." }`\n'

    return formatted_path

# Define a function to format the entire API documentation
def format_api(api_data):
    formatted_api = ""
    paths = api_data.get("paths", {})
    for path, path_data in paths.items():
        formatted_api += format_path(path, path_data)

    return formatted_api

# Transform the OpenAPI specification into the desired Markdown format
markdown_content = format_api(openapi_spec)

# Write the formatted content to the README.md file
with open('README.md', 'w') as readme_file:
    readme_file.write(markdown_content)
