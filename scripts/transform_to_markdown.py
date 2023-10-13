import json

# Load the structured JSON from the redoc-cli output
with open('../structured.json', 'r') as json_file:
    data = json.load(json_file)

# Define a function to format a single path
def format_path(path, path_data):
    formatted_path = f'**{path}**\n----\n{path_data["description"]}\n'
    formatted_path += f'* **URL Params**\n{path_data.get("url_params", "None")}\n'
    formatted_path += f'* **Data Params**\n{path_data.get("data_params", "None")}\n'
    formatted_path += f'* **Headers**\n{path_data.get("headers", "None")}\n'
    formatted_path += f'* **Success Response**\n{path_data.get("success_response", "None")}\n'
    formatted_path += f'* **Error Response**\n{path_data.get("error_response", "None")}\n'
    return formatted_path

# Define a function to format the entire API documentation
def format_api(api_data):
    formatted_api = ""
    for path, path_data in api_data.items():
        formatted_api += f'#{path_data["tag"]}\n'
        for method, method_data in path_data['methods'].items():
            formatted_api += f'* **{method} {path}**\n----\n{format_path(path, method_data)}\n'
    return formatted_api

# Transform the structured JSON into the desired Markdown format
markdown_content = format_api(data)

# Write the formatted content to the README.md file
with open('README.md', 'w') as readme_file:
    readme_file.write(markdown_content)
