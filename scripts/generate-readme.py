import yaml

# Load the OpenAPI specification from the file
with open('openapi/openapi.yaml', 'r') as openapi_file:
    openapi_data = yaml.safe_load(openapi_file)

# Extract relevant information from the OpenAPI definition
title = openapi_data.get('info', {}).get('title', 'API Title')
version = openapi_data.get('info', {}).get('version', '1.0.0')
summary = openapi_data.get('info', {}).get('summary', 'API Summary')
description = openapi_data.get('info', {}).get('description', 'API Description')

contact_name = openapi_data.get('info', {}).get('contact', {}).get('name', 'Contact Name')
contact_email = openapi_data.get('info', {}).get('contact', {}).get('email', 'contact@example.com')

license = openapi_data.get('info', {}).get('license', {}).get('name', 'License Name')

# Define a function to generate the API documentation
def generate_api_documentation(openapi_data):
    documentation = []

    # Add title, version, and description
    documentation.append(f"# {title} (Version: {version})")
    documentation.append(f"{summary}\n")
    documentation.append(f"{description}\n")

    # Add contact information
    documentation.append("Contact:")
    documentation.append(f"- Name: {contact_name}")
    documentation.append(f"- Email: {contact_email}\n")

    # Add license information
    documentation.append(f"License: {license}\n")

    # Loop through the paths in the OpenAPI definition
    for path, path_data in openapi_data['paths'].items():
        documentation.append(f"{path}\n")

        if 'parameters' in path_data.get('get', {}):
            documentation.append("Input parameters:")
            for param in path_data['get']['parameters']:
                param_name = param['name']
                param_description = param.get('description', 'No description available')
                documentation.append(f"- {param_name} ({param['in']}): {param_description}")

        if 'responses' in path_data.get('get', {}):
            documentation.append("Output:")
            for status_code, response in path_data['get']['responses'].items():
                if 'description' in response:
                    documentation.append(f"- {status_code} ({response['description']})")

        documentation.append("Example usage:")
        documentation.append(f"{path}\n")

        if 'responses' in path_data.get('get', {}):
            for status_code, response in path_data['get']['responses'].items():
                if 'example' in response:
                    documentation.append(response['example'])

        documentation.append("\n")

    return "\n".join(documentation)

# Generate the documentation
api_documentation = generate_api_documentation(openapi_data)

# Write the documentation to the README file
with open('README.md', 'w') as readme_file:
    readme_file.write(api_documentation)
