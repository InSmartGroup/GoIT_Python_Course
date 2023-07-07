# Given the fact that one page can contain maximum 10 records,
# specify the number of pages for a specific number of records
import math

num_records = int(input("Enter the number of records: "))  # mustn't be equal to zero

records_per_page = 10

num_pages = num_records // records_per_page + 1

print(f"You need {num_pages} pages to keep {num_records} records")
