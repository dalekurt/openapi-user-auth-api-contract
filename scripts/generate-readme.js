const fs = require('fs');
const swaggerJSDoc = require('swagger-jsdoc');
const markdownTable = require('markdown-table');

// Define options for swagger-jsdoc
const options = {
  definition: {
    openapi: '3.0.0', // specify the OpenAPI version
    info: {
      title: 'Your API Title',
      version: '1.0.0',
    },
  },
  apis: ['./openapi/openapi.yaml'], // path to your OpenAPI file
};

const swaggerSpec = swaggerJSDoc(options);

// Generate a markdown table from the Swagger spec
const table = markdownTable([
  ['Endpoint', 'Method', 'Description'],
  ...swaggerSpec.paths.map((path, pathName) =>
    Object.entries(path).map(([method, endpoint]) => [
      pathName,
      method.toUpperCase(),
      endpoint.summary,
    ])
  ),
]);

// Write the table to the README.md file
fs.writeFileSync('./README.md', table);

console.log('README generated successfully');
