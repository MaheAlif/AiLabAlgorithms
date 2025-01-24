# Required Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Emulating dataset
data = {
    'Hours_Studied': [2.0, 3.5, 5.0, 1.0, 4.0, 6.0, 1.5, 3.0, 2.5, 4.5],
    'Hours_Slept': [7.0, 6.0, 8.0, 5.0, 6.5, 8.5, 6.0, 7.0, 5.0, 7.5],
    'Prior_Grade': [70, 65, 80, 50, 78, 85, 60, 75, 55, 82],
    'Result': ['fail', 'fail', 'pass', 'fail', 'pass', 'pass', 'fail', 'pass', 'fail', 'pass']
}

df = pd.DataFrame(data)

# Data Exploration
print("First few rows of the dataset:")
print(df)

# Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# Convert categorical Result to binary

df['Result'] = df['Result'].map({'pass': 1, 'fail': 0})

# 3D Scatter Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting dataset points
scatter = ax.scatter(
    df['Hours_Studied'], df['Hours_Slept'], df['Prior_Grade'],
    c=df['Result'], cmap='coolwarm', s=100, edgecolor='k', label='Dataset Points'
)

# Adding the new student point
new_student_point = [3, 6.5, 77]
ax.scatter(
    new_student_point[0], new_student_point[1], new_student_point[2],
    c='gold', s=150, edgecolor='k', label='New Student'
)

# Setting axis labels
ax.set_title('3D Scatter Plot of Dataset with New Student', fontsize=16)
ax.set_xlabel('Hours Studied', fontsize=12)
ax.set_ylabel('Hours Slept', fontsize=12)
ax.set_zlabel('Prior Grade', fontsize=12)

# Adding a color bar for dataset points
cbar = plt.colorbar(scatter, pad=0.1, aspect=10, label='Result (0 = Fail, 1 = Pass)')

# Adding legend
ax.legend()

# Show the plot
plt.show()

# Feature-target split
X = df[['Hours_Studied', 'Hours_Slept', 'Prior_Grade']]
y = df['Result']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split with stratification
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

# Train KNN
k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Predict
y_pred = knn.predict(X_test)

# Metrics
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, zero_division=1))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Fail', 'Pass'], yticklabels=['Fail', 'Pass'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Example Prediction
new_student_df = pd.DataFrame([new_student_point], columns=['Hours_Studied', 'Hours_Slept', 'Prior_Grade'])
new_student_scaled = scaler.transform(new_student_df)
prediction = knn.predict(new_student_scaled)
print("\nPrediction for new student:", 'Pass' if prediction[0] == 1 else 'Fail')

# Hyperparameter Tuning
print("\nHyperparameter Tuning Results:")
max_k = len(X_train)
for k in range(1, max_k + 1):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print(f"k={k}, Accuracy={accuracy_score(y_test, y_pred)}")
