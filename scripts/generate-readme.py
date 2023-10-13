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

# Define a function to generate the API documentation for a specific path and method
def generate_method_documentation(path, method_data):
    documentation = []

    # Extract method-specific information
    method = method_data['method']
    method_summary = method_data.get('summary', 'No summary available')
    method_description = method_data.get('description', 'No description available')

    documentation.append(f"# {title} (Version: {version})")
    documentation.append(f"{summary}\n")
    documentation.append(f"{description}\n")

    # Add contact information
    documentation.append("Contact:")
    documentation.append(f"- Name: {contact_name}")
    documentation.append(f"- Email: {contact_email}\n")

    # Add license information
    documentation.append(f"License: {license}\n")

    documentation.append(f"## {method} {path}")

    # Add method-specific summary and description
    documentation.append(f"{method_summary}\n")
    documentation.append(f"{method_description}\n")

    # Input parameters
    if 'parameters' in method_data:
        documentation.append("Input parameters:")
        for param in method_data['parameters']:
            param_name = param['name']
            param_description = param.get('description', 'No description available')
            documentation.append(f"- {param_name} ({param['in']}): {param_description}")

    # Output
    if 'responses' in method_data:
        documentation.append("Output:")
        for status_code, response in method_data['responses'].items():
            if 'description' in response:
                documentation.append(f"- {status_code} ({response['description']})")

    documentation.append("Example usage:")
    documentation.append(f"{method} {path}\n")

    if 'responses' in method_data:
        for status_code, response in method_data['responses'].items():
            if 'example' in response:
                documentation.append(response['example'])

    documentation.append("\n")

    return "\n".join(documentation)

# Define a function to generate the full API documentation
def generate_api_documentation(openapi_data):
    documentation = []

    # Loop through the paths in the OpenAPI definition
    for path, path_data in openapi_data['paths'].items():
        for method_data in path_data.values():
            method_data['method'] = method_data['method'].upper()
            documentation.append(generate_method_documentation(path, method_data))

    return "\n".join(documentation)

# Generate the documentation
api_documentation = generate_api_documentation(openapi_data)

# Write the documentation to the README file
with open('README.md', 'w') as readme_file:
    readme_file.write(api_documentation)
