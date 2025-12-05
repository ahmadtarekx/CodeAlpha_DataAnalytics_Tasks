# CodeAlpha_DataAnalytics_Tasks

**TASK 1 (WEB SCRAPPING):**

For my first task, I was tasked with web scraping data and formatting it for later analysis.
 Initially, I leaned towards coding the scraper myself, as I already have HTML knowledge and the desire for custom data manipulation using tools like Pandas. 
 However, I encountered several sites that actively blocked scraping attempts. 
 To overcome this, I adapted my approach and utilized the user-friendly tool, ParseHub,
  which allowed me to efficiently scrape the necessary data without further technical hurdles

Target Website: http://books.toscrape.com/

Tool Used: ParseHub (A visual, desktop-based web scraping application).

Methodology: The data was acquired by defining a project in the ParseHub desktop client, which handled navigation and extraction logic.

Scraping Configuration:

Pagination: ParseHub was configured to click the 'Genre' button and iterate through all 50 pages of the catalog to ensure complete collection.

Template Logic: A main template was created to select the product container, and nested commands were used to extract specific data elements.

Data Points Extracted: The following features were successfully extracted into the raw output file:

Book Title (Extracted from the <a> tag text)

Product Price (Raw String, including the currency symbol)

Stock Status (Text indicating availability)

Book Category/Genre (Extracted by navigating up to the breadcrumb or category link)

Output: The raw, uncleaned data was exported directly from the ParseHub platform as a JSON or CSV file named raw_books_data.csv (or raw_books_data.json).

**TASK 2 (EDA Questions & Objectives):**

The primary goal of this analysis is to uncover trends in the US corporate landscape by analyzing revenue, profitability, and workforce efficiency.

--1. Efficiency Analysis--
Question: Which industry sectors generate the highest revenue per employee?
Goal: To move beyond raw revenue numbers and identify which industries are the most labor-efficient versus labor-intensive.

--2. Growth Dynamics--
Question: Is there a correlation between a company's current size (Revenue) and its growth rate?
Goal:To test the hypothesis that "megacaps" grow slower than smaller competitors, or if the largest players are accelerating their dominance.

--3. Geographic Distribution--
Question: How does the distribution of corporate headquarters differ between Public and Private companies?
Goal: To visualize state-level clusters and see if private giants (like Cargill) are located in different regions than public tech/finance giants.

--4. Profitability vs. Volume--
Question: Which companies rank high in top-line Revenue but fail to appear in the top Profit rankings?
Goal: To distinguish between high-volume/low-margin businesses (like Retail) and high-margin powerhouses (like Tech).

--5. Sector Dominance--
Question: What percentage of the total top corporate profits is driven solely by the Technology sector?
Goal: To quantify the impact of Big Tech on the overall US corporate profit pool compared to traditional industries like Energy or Finance.