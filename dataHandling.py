import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Read the CSV file
# df = pd.read_csv('soc.csv')

# # Define the columns we want to keep
# columns_to_keep = ['sl', 'mid(30)']

# # Filter the DataFrame to include only the specified columns
# filtered_df = df[columns_to_keep]

# # Save the filtered DataFrame to a new CSV file
# filtered_df.to_csv('filtered_soc_with_sl.csv', index=False)

# another ---------------------------------

# Load the existing data
data_path = 'Algorithms/filtered_soc_with_sl.csv'
data = pd.read_csv(data_path)

# Number of additional rows to add
additional_rows = 500

# Generate random student IDs (ensuring no duplicates)
existing_ids = data['sl'].values
new_ids = np.arange(max(existing_ids) + 1, max(existing_ids) + 1 + additional_rows)

# Generate random mid(30) scores between 15.0 and 30.0
new_mid_scores = np.random.uniform(15.0, 30.0, additional_rows)

# Create a DataFrame for the new data
new_data = pd.DataFrame({
    'sl': new_ids,
    'mid(30)': new_mid_scores
})

# Append the new data to the original data
data = pd.concat([data, new_data], ignore_index=True)

# Save the updated DataFrame back to the CSV file
data.to_csv(data_path, index=False)

print(f"{additional_rows} new rows have been added to {data_path}.")


# # Normalize column names
# data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')

# # Update the required_columns list to match normalized names
# required_columns = ['student_id', 'student_name', 'mid(30)']
# data = data[required_columns].dropna()


# # Map student_name to numeric labels for the y-axis
# data['student_name_numeric'] = pd.factorize(data['student_name'])[0]

# # Extract columns for plotting
# x = data['student_id']
# y = data['student_name_numeric']
# z = data['mid(30)']

# # Create a 3D scatter plot
# fig = plt.figure(figsize=(15, 10))
# ax = fig.add_subplot(111, projection='3d')

# # Plot data
# scatter = ax.scatter(x, y, z, c=z, cmap='viridis', s=20)

# # Set axis labels
# ax.set_xlabel("Student ID")
# ax.set_ylabel("Student Name")
# ax.set_zlabel("Mid(30)")
# plt.title("3D Scatter Plot of Student Data")

# # Add a color bar to indicate value scale for z-axis
# cbar = fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=10)
# cbar.set_label("Mid(30)")

# # Set y-axis tick labels
# ax.set_yticks(range(len(data['student_name'].unique())))
# ax.set_yticklabels(data['student_name'].unique(), rotation=45, ha='right')

# # Show the plot
# plt.show()
