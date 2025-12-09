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

1. Ask Meaningful Questions
Pricing Trends: Is there a significant price difference between genres? 
For example, are "Travel" books consistently more expensive than "Mystery" books?

Inventory Efficiency: Which genre has the highest Amount_Available compared to its average price?
Does a high stock level correlate with a lower price to encourage sales?

Inventory Balance (Market Concentration): Is the inventory heavily skewed toward one or two genres?

Why it matters: If 50% of your stock is just "Travel" books, your business is risky if travel trends die down. we want to know if your portfolio is diverse.

Capital Allocation (High-Value Assets): Which specific book titles represent the most "tied-up" money?

Why it matters: A single book priced at £50 with 20 copies in stock (£1,000 value) is a bigger financial risk than a £10 book with 5 copies. we need to identify your "VIP" products.
 
 2. Explore the Data Structure Redundancy Check: Does the Type column contain any value other than "Books"?
  If it is a constant value, can we remove it to simplify the dataset?

  Variable Consistency: Are the columns Price, Price_Excl, and Price_Incl mathematically identical in every row? If so, why does the system generate three separate columns for the same value?
  
  3. Identify Trends, Patterns & Anomalies 
  Category Domination: Which genre represents the largest portion of the total inventory value (Price * Amount_Available)?

  Outlier Detection: Are there any "Luxury" books that have a price significantly higher than the average for their genre (e.g., a Travel book priced at £200)?

  4. Test Hypotheses & Validate Assumptions
  The Tax Hypothesis: Can we validate that this dataset represents a tax-free region? 
  We can test this by checking if the Tax column is exactly $0.00$ for all records.

  UPC Uniqueness: Is every Upc (Universal Product Code) unique? 
  We assume each row is a unique book edition, but we must validate that no duplicates exist in this identifier column.
  
  5. Detect Potential Data IssuesInformation Gaps: Why is the Review_Num column empty (or zero) in the preview? 
  Does this mean the books haven't been reviewed yet, or is the data connection to the reviews broken?
  
  Precision Issues: Do any books have an Amount_Available of zero? If so, should these be excluded from pricing analysis to avoid skewing "active" market trends?

**Task 3 (Data Visualization)**


Before coding, we need to decide what story we are telling. Based on our data, here are the three most compelling stories we can visualize:

1. Story A (The Market Overview): How are books priced? Are most cheap or expensive?

2. Story B (The Genre Wars): Which genres dominate your inventory?

3. Story C (Inventory Risk): Do we have too much stock of expensive items?

Visual 1: The Price Distribution (Histogram)

Visual 2: Top 10 Genres by Inventory (Bar Chart)

Visual 3: Price Range by Genre (Box Plot)

Visual 4: Inventory Value Heatmap (Correlation)
