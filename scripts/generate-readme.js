const fs = require('fs');
const yaml = require('js-yaml');

try {
  // Read the OpenAPI YAML file
  const openapiYAML = fs.readFileSync('openapi/openapi.yaml', 'utf8');
  const openapiObject = yaml.safeLoad(openapiYAML);

  // Extract information from the OpenAPI object
  const apiTitle = openapiObject.info.title;
  const apiVersion = openapiObject.info.version;
  const apiDescription = openapiObject.info.description;

  // Extract paths and descriptions
  const paths = openapiObject.paths;
  const pathDescriptions = Object.keys(paths).map((path) => {
    const pathItem = paths[path];
    const pathDescription = pathItem.get ? pathItem.get.summary : '';
    return `  - ${path}: ${pathDescription}`;
  });

  // Generate README content
  const readmeContent = `
  # ${apiTitle}

  **Version**: ${apiVersion}

  ${apiDescription}

  ## Endpoints

  ${pathDescriptions.join('\n')}

  ## Example Usage

  You can use this API to...

  ## Changelog

  - Version ${apiVersion}: Initial release
  `;

  // Write the README content to a README.md file
  fs.writeFileSync('README.md', readmeContent, 'utf8');

  console.log('README.md generated successfully.');
} catch (e) {
  console.error('Error reading or generating the README.md:', e);
  process.exit(1);
}
