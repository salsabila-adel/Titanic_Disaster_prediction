
# 🚢 Titanic Survival Prediction Project

## 📌 Project Overview

This project aims to predict whether a passenger survived or did not survive the Titanic disaster using Machine Learning techniques.

The project includes:

- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Feature Engineering
- Model Training & Evaluation
- Model Comparison
- Building a GUI Application for Prediction

---

# 📂 Dataset

The project uses the famous Titanic dataset containing passenger information such as:

- Passenger Class
- Gender
- Age
- Fare
- Family Members
- Embarked Port
- Passenger Name
- Survival Status

---

# 🔍 Exploratory Data Analysis (EDA)

Several visualizations and analyses were performed to better understand the dataset and identify important patterns.

## ✔️ Analysis Included

### Univariate Analysis
- Survival distribution
- Gender distribution
- Passenger class distribution
- Age distribution

### Bivariate Analysis
Relationship between survival and:
- Gender
- Passenger Class
- Age
- Fare
- Embarked Port
- Family Size
- Traveling Alone

### Correlation Analysis
A heatmap was used to identify correlations between numerical features.

---

# 🛠️ Data Preprocessing

Multiple preprocessing techniques were applied to improve model performance.

## ✔️ Steps Performed

### 1. Handling Missing Values
- Filling missing ages using median grouped by title
- Filling missing embarked values using mode
- Filling missing fares using median

### 2. Feature Engineering
New features were created such as:

- `FamilySize`
- `IsAlone`
- `Title`

### 3. Encoding
Categorical variables were converted into numerical format using:
- Label Encoding
- One-Hot Encoding

### 4. Feature Scaling
StandardScaler was applied to:
- Age
- Fare
- SibSp
- Parch
- FamilySize

### 5. Feature Dropping
Unused columns were removed:
- Name
- Ticket
- Cabin
- PassengerId

### 6. Stratified Sampling
Used to preserve survival distribution between training and validation datasets.

---

# 🤖 Machine Learning Models

Several machine learning algorithms were trained and evaluated.

## 📌 Algorithms Used

### 1️⃣ Logistic Regression
- Hyperparameter tuning using GridSearchCV
- Achieved the best overall accuracy

### 2️⃣ Support Vector Machine (SVM)
- Used Pipeline with StandardScaler
- Linear and RBF kernels tested

### 3️⃣ Decision Tree
- Tree visualization performed
- Hyperparameter tuning applied

---

# 📊 Model Evaluation

The models were evaluated using:

- Accuracy Score
- Classification Report
- Confusion Matrix
- Feature Importance
- Visual Comparisons

---

# 📈 Accuracy Results

| Model | Accuracy |
|------|------|
| Logistic Regression | 85.47% |
| Decision Tree | 83.24% |
| SVM | 82.68% |

✅ Logistic Regression achieved the best performance and was selected for the GUI application.

---

# 🖥️ GUI Application

A simple and interactive GUI was developed using Tkinter to allow users to test survival predictions easily.

## ✨ GUI Features

- User-friendly interface
- Input validation
- Passenger survival prediction
- Background image support
- Clear button to reset fields
- Error handling messages

---

# 🧠 Input Features in GUI

The GUI accepts:

- Name
- Gender
- Passenger Class
- Embarked Port
- Age
- Fare
- Number of Siblings/Spouses
- Number of Parents/Children

---

# ✅ Input Validation

Validation rules were added to improve usability:

- Name must contain letters only
- Fare must be between 200 and 500

---

# 🧰 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Tkinter
- PIL
- Joblib

---

# 📊 Visualizations Included

The project contains multiple visualizations such as:

- Countplots
- Histograms
- Heatmaps
- Confusion Matrices
- Feature Importance Graphs
- Decision Tree Visualization
- Sigmoid Function Plot
- SVM Hyperplane Visualization

---

# 🚀 How to Run the Project

## 1️⃣ Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn pillow joblib
```

## 2️⃣ Run the GUI File

```bash
python gui.py
```

---

# 📁 Project Structure

```bash
Titanic-Survival-Prediction/
│
├── Titanic_train.csv
├── Titanic_test.csv
├── gui.py
├── model2.pkl
├── scaler.pkl
├── columns.pkl
├── README.md
└── images/
```

---

# 🎯 Project Goal

The goal of this project is to apply machine learning concepts to a real-world dataset while practicing:

- Data Analysis
- Data Cleaning
- Feature Engineering
- Model Training
- Hyperparameter Tuning
- GUI Development

---


# 📌 Conclusion

This project demonstrates a complete Machine Learning workflow starting from data preprocessing and visualization to model training and building an interactive prediction application.

The project also highlights the importance of feature engineering and model comparison in achieving better predictive performance.

---
````
