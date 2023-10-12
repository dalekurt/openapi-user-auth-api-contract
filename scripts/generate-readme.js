const fs = require('fs');
const yaml = require('js-yaml');

try {
  const doc = yaml.load(fs.readFileSync('./openapi/openapi.yaml', 'utf8'));

  // Define apiTitle with your API title from the OpenAPI file
  const apiTitle = doc.info.title;

  // Extract paths from the OpenAPI file
  const paths = Object.keys(doc.paths);

  // Generate a table of contents for paths based on HTTP methods
  const tableOfContents = paths.map((path) => {
    return `- [${path}](#${path.replace(/\//g, '-').replace(/{/g, '').replace(/}/g, '').toLowerCase()})`;
  }).join('\n');

  // Generate the "Usage" section for each path based on HTTP methods
  let usageSection = '';
  paths.forEach((path) => {
    usageSection += `\n## ${path}\n`;
    Object.keys(doc.paths[path]).forEach((method) => {
      if (method !== 'parameters') {
        usageSection += `### ${method}\n\n`;
        // Add information about the method, such as request and response details
        usageSection += `Description: ${doc.paths[path][method].summary}\n\n`;
        // You can add more details about the request and response here
      }
    });
  });

  // Customize your README content here using the 'apiTitle', 'tableOfContents', and 'usageSection' variables
  const readmeContent = `
  # ${apiTitle} API Documentation

  This documentation provides details about the ${apiTitle} API.

  ## Table of Contents
  ${tableOfContents}

  ## Usage
  ${usageSection}
  `;

  // Write the README.md file
  fs.writeFileSync('./README.md', readmeContent);

  console.log('README.md generated successfully.');
} catch (e) {
  console.log('Error reading or generating the README.md: ' + e.message);
  process.exit(1);
}
