import yaml

# Load the OpenAPI specification (assuming it's in YAML format)
with open('openapi/openapi.yaml', 'r') as yaml_file:
    openapi_spec = yaml.safe_load(yaml_file)

# Define a function to format a single path
def format_path(path, path_data):
    formatted_path = f'**{path}**\n----\n{path_data.get("description", "No description provided")}\n'
    formatted_path += f'* **URL Params**\n{path_data.get("parameters", "None")}\n'
    formatted_path += f'* **Data Params**\n{path_data.get("requestBody", "None")}\n'
    # Add more sections as needed, e.g., headers, responses
    return formatted_path

# Define a function to format the entire API documentation
def format_api(api_data):
    formatted_api = ""
    paths = api_data.get("paths", {})
    for path, path_data in paths.items():
        formatted_api += f'# {path_data.get("summary", "No summary provided")}\n'
        for method, method_data in path_data.items():
            if method not in ["parameters", "summary", "description"]:
                formatted_api += f'* **{method.upper()} {path}**\n'
                formatted_api += format_path(path, method_data)
    return formatted_api

# Transform the OpenAPI specification into the desired Markdown format
markdown_content = format_api(openapi_spec)

# Write the formatted content to the README.md file
with open('README.md', 'w') as readme_file:
    readme_file.write(markdown_content)
