import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loading data - notice the second filename is corrected
list_of_companies_by_profit = pd.read_csv(
    r"E:\CodeAlpha_DataAnalytics_tasks\CodeAlpha_DataAnalytics_Tasks\Task1\list_of_companies_by_profit.csv"
)

list_of_largest_companies_by_revenue = pd.read_csv(
    r"E:\CodeAlpha_DataAnalytics_tasks\CodeAlpha_DataAnalytics_Tasks\Task1\list_of_largest_companie_by_revenue.csv"
)  # Changed "companies" to "companie" to match actual filename

list_of_largest_private_companies = pd.read_csv(
    r"E:\CodeAlpha_DataAnalytics_tasks\CodeAlpha_DataAnalytics_Tasks\Task1\list_of_largest_private_companies.csv"
)

# Cleaning data
#Format colomn headers to lowercase and replace spaces with underscores
list_of_companies_by_profit.columns = ["Index","Company", "Industry", "Revenue"]
list_of_largest_companies_by_revenue.columns = ["Index","Company", "Industry", "Revenue", "Revenue_Growth", "Employees", "Headquarters"]
list_of_largest_private_companies.columns = ["Index","Company","Industry", "Revenue", "Employees", "Headquarters"]


# Since data is already clean, we will just convert their types if necessary
print(list_of_companies_by_profit)
print("\n")
print(list_of_largest_companies_by_revenue)
print("\n")
print(list_of_largest_private_companies)