from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

hours_studied = [2.0, 3.5, 5.0, 1.0, 4.0, 6.0, 1.5, 3.0, 2.5, 4.5]
hours_slept = [7.0, 6.0, 8.0, 5.0, 6.5, 8.5, 6.0, 7.0, 5.0, 7.5]
prior_grades = [70, 65, 80, 50, 78, 85, 60, 75, 55, 82]
results = ['fail', 'fail', 'pass', 'fail', 'pass', 'pass', 'fail', 'pass', 'fail', 'pass']

results = [0 if result == 'fail' else 1 for result in results]

features = [[hours_studied[i], hours_slept[i], prior_grades[i]] for i in range(len(hours_studied))]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

X_train, X_test, y_train, y_test = train_test_split(scaled_features, results, test_size=0.2, random_state=42)

k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Fail', 'Pass']))

plt.figure()
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Fail', 'Pass'], yticklabels=['Fail', 'Pass'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show(block=False)

k_values = range(1, len(X_train) + 1)
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred_k = knn.predict(X_test)
    accuracies.append(accuracy_score(y_test, y_pred_k))

plt.figure()
plt.plot(k_values, accuracies, marker='o')
plt.title('Accuracy vs. Number of Neighbors (k)')
plt.xlabel('Number of Neighbors (k)')
plt.ylabel('Accuracy')
plt.xticks(k_values)
plt.grid()

tp = conf_matrix[1, 1]  
fp = conf_matrix[0, 1]  
precision = tp / (tp + fp) if (tp + fp) > 0 else 0
print(f"Precision: {precision:.2f}")

test_data = [[3, 6.5, 77]]  

predicted_result = knn.predict(test_data)

result_label = ['fail', 'pass']  
print(f"Prediction for input {test_data}: {result_label[predicted_result[0]]}")

plt.show()