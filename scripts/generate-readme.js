const fs = require('fs');
const yaml = require('js-yaml');

try {
  const doc = yaml.load(fs.readFileSync('./openapi/openapi.yaml', 'utf8'));


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
