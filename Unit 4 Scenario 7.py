
import numpy as np
import pandas as pd

# Create patient details
patients = ['Rahul', 'Priya', 'Amit', 'Neha', 'Rohit']

# Create NumPy array of treatment costs
costs = np.array([15000, 25000, 18000, 35000, 22000])

# Calculate mean, maximum and minimum costs
mean_cost = np.mean(costs)
max_cost = np.max(costs)
min_cost = np.min(costs)

print("----- Hospital Treatment Cost Analysis -----")

print("Treatment Costs:", costs)
print("Mean Treatment Cost: ₹", mean_cost)
print("Maximum Treatment Cost: ₹", max_cost)
print("Minimum Treatment Cost: ₹", min_cost)

# Create Pandas DataFrame
df = pd.DataFrame({
    'Patient Name': patients,
    'Treatment Cost': costs
})

# Display all patient details
print("\n----- All Patient Details -----")
print(df)

# Display patients whose cost exceeds ₹20,000
print("\n----- Patients with Treatment Cost Above ₹20,000 -----")

high_cost = df[df['Treatment Cost'] > 20000]

print(high_cost)
