
import numpy as np
import pandas as pd

# Create book details
books = ['Python', 'Java', 'C Programming',
         'Data Science', 'Web Development']

# Create NumPy array of book prices
prices = np.array([450, 650, 350, 800, 550])

# Calculate average book price
average_price = np.mean(prices)

print("----- Book Price Analysis -----")
print("Book Prices:", prices)
print("Average Book Price: ₹", average_price)

# Create Pandas DataFrame
df = pd.DataFrame({
    'Book Name': books,
    'Price': prices
})

# Display all books
print("\n----- All Book Details -----")
print(df)

# Display books costing more than ₹500
print("\n----- Books Costing More Than ₹500 -----")
expensive_books = df[df['Price'] > 500]

print(expensive_books)
