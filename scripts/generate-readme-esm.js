import fs from 'fs';
import markdownTable from 'markdown-table';
import swaggerJSDoc from 'swagger-jsdoc';

// Define options for swagger-jsdoc
const options = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'User Authentication API',
      version: '1.0.0',
    },
  },
  apis: ['./openapi/openapi.yaml'],
};

const swaggerSpec = swaggerJSDoc(options);

// Generate a markdown table from the Swagger spec
const markdown = markdownTable([
  ['Endpoint', 'Method', 'Description'],
  ...swaggerSpec.paths.flatMap((path, pathName) =>
    Object.entries(path).map(([method, endpoint]) => [
      pathName,
      method.toUpperCase(),
      endpoint.summary,
    ])
  ),
]);

// Write the markdown to the README.md file
fs.writeFileSync('./README.md', markdown);

console.log('README generated successfully');
