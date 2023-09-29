const puppeteer = require("puppeteer");

async () => {
  // Launch the index.js server
  const server = require("./index.js");
  const port = server.address().port;

  // Launch the browser
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  // Navigate to the page
  await page.goto(`http://localhost:${port}`);

  // Print the pages response
  console.log(await page.content());
};
