const fs = require('fs');
const yaml = require('js-yaml');

try {
  const doc = yaml.load(fs.readFileSync('./openapi/openapi.yaml', 'utf8'));

  // Define apiTitle with your API title from the OpenAPI file
  const apiTitle = doc.info.title;

  // Extract tags from the OpenAPI file
  const tags = doc.tags.map((tag) => tag.name);

  // Generate a table of contents for paths based on tags
  const tableOfContents = tags.map((tag) => {
    const tagPaths = Object.entries(doc.paths)
      .filter(([path, pathData]) => pathData.get.tags.includes(tag))
      .map(([path, pathData]) => {
        const operations = Object.keys(pathData);
        return `- [${tag}](#${tag.toLowerCase()}-${path.replace(/\//g, '-').replace(/{/g, '').replace(/}/g, '').toLowerCase()}) (${operations.join(', ')})`;
      });

    return `## ${tag}\n${tagPaths.join('\n')}`;
  }).join('\n\n');

  // Generate the "Usage" section for each path based on HTTP methods
  let usageSection = '';
  for (const [path, pathData] of Object.entries(doc.paths)) {
    usageSection += `\n## ${path}\n`;
    
    for (const [method, methodData] of Object.entries(pathData)) {
      if (method !== 'parameters') {
        usageSection += `### ${method}\n\n`;
        
        // Add information about the method, such as request and response details
        usageSection += 'Description: ' + methodData.summary + '\n';
        
        // You can add more details about the request and response here
        
        usageSection += '\n';
      }
    }
  }

  // Customize your README content here using the 'doc', 'apiTitle', 'tableOfContents', and 'usageSection' variables
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
