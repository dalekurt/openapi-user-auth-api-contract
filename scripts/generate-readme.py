import json

# Load the structured JSON from the redoc-cli output
with open('structured.json', 'r') as json_file:
    data = json.load(json_file)

# Define a function to format a single path
def format_path(path, path_data):
    formatted_path = f'**{path}**\n----\n{path_data.get("description", "No description provided")}\n'
    formatted_path += f'* **URL Params**\n{path_data.get("url_params", "None")}\n'
    formatted_path += f'* **Data Params**\n{json.dumps(path_data.get("data_params", "None"), indent=2)}\n'
    formatted_path += f'* **Headers**\n{path_data.get("headers", "None")}\n'
    formatted_path += f'* **Success Response**\n{json.dumps(path_data.get("success_response", "None"), indent=2)}\n'
    formatted_path += f'* **Error Response**\n{json.dumps(path_data.get("error_response", "None"), indent=2)}\n'
    return formatted_path

# Define a function to format the entire API documentation
def format_api(api_data):
    formatted_api = ""
    paths = api_data.get("paths", {})
    for path, path_data in paths.items():
        # Ensure the path is not duplicated for multiple HTTP methods
        unique_paths = set()
        for method, method_data in path_data.items():
            if method not in ["parameters", "summary", "description"]:
                if path not in unique_paths:
                    formatted_api += f'**{path}**\n'
                    unique_paths.add(path)
                formatted_api += f'* **{method.upper()} {path}**\n'
                formatted_api += format_path(path, method_data)
    return formatted_api

# Transform the structured JSON into the desired Markdown format
markdown_content = format_api(data)

# Write the formatted content to the README.md file
with open('README.md', 'w') as readme_file:
    readme_file.write(markdown_content)
