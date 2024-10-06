# credit-default-predictor
A project on machine learning . where credit card default of user is predicted

# A credit card default prediction model is a machine learning or statistical model designed to predict the likelihood that a credit card holder will default on their payments. Default occurs when a cardholder is unable to make the required minimum payment on their credit card debt.

# 1. First the raw data is taken from website like https://www.kaggle.com/
 Data Preprocessing sanity test is performed which gives us information of the data like is there any null values . data type , dupliacted values if any . 

After sanity check is been performed
# 2.  EDA (Exploratry data analysis) is performed 
Key Components of EDA:
# Understanding the Data:

Data Types: Identifying the type of each feature (e.g., categorical, numerical, date/time).
Structure: Inspecting the dataset for number of rows, columns, and understanding the variables (features).
Descriptive Statistics: Calculating summary statistics such as:
 Mean, median, mode
 Standard deviation, variance
 Minimum, maximum, percentiles
 Skewness and kurtosis

# Data Visualization: 
Visualizations help uncover patterns, trends, and relationships that might not be obvious from numerical data alone. Common visual tools include:

Histograms: To understand the distribution of numerical data.
Box plots: For detecting outliers and comparing distributions.
Scatter plots: To investigate relationships between two continuous variables.
Bar charts: To visualize the distribution of categorical data.
Correlation Heatmaps: To identify correlations between features in the dataset.
Pair plots: To explore relationships between multiple features at once.

After EDA one hot encoding is performed:
# 3.  One-Hot Encoding :
is a technique used in machine learning and data preprocessing to convert categorical variables into a numerical format that algorithms can understand. This is particularly important because many machine learning algorithms require numerical inputs rather than categorical (non-numeric) data.

then data is balanced as there is possibility of data being imbalanced 
which is done by 
#  4. SMOTE-(SMOTE (Synthetic Minority Over-sampling Technique) :
is a method used to address the problem of class imbalance in datasets, which is common in classification problems. In an imbalanced dataset, one class (often the minority class) has significantly fewer instances than another class (majority class). SMOTE generates synthetic samples to increase the number of instances in the minority class, balancing the dataset and improving model performance.

After this 
# 5.  Data  transformation is done which is to split data into training ad testing phase.

#  6. Model Implementation : 
Model implementation refers to the process of taking a trained machine learning model and making it operational in a real-world setting, such as in a web application, a mobile app, or an automated system. It involves multiple steps, including model development, integration, deployment, and monitoring  . 

# Model used : Linear Regression ->
Linear regression is a basic yet powerful statistical method used to model the relationship between a dependent variable (target) and one or more independent variables (features). It’s a supervised learning algorithm widely used for predicting continuous values.

# Decision Tree Classifiaction -> 
A Decision Tree is a popular and interpretable machine learning algorithm used for both classification and regression tasks. It models decisions in the form of a tree structure, where each internal node represents a decision based on a feature, each branch represents the outcome of the decision, and each leaf node represents the final output (a class label or a regression value).

# Random forest classificattion -->
Random Forest is an ensemble learning algorithm that builds multiple decision trees and combines their predictions to produce more accurate and stable results. It is used for both classification and regression tasks and addresses some of the limitations of individual decision trees, such as overfitting and sensitivity to small changes in the data.

# 7. Model comparission --> 
Model comparison is the process of evaluating and contrasting different machine learning models to determine which one performs best for a given task or dataset. This involves analyzing various metrics, understanding the strengths and weaknesses of each model, and choosing the most appropriate one based on specific criteria.

# 8. Cross-validation and hyperparameter tuning --> Cross-Validation
Cross-validation is a technique used to assess the generalization ability of a machine learning model. It helps ensure that the model performs well on unseen data and reduces the risk of overfitting. The most common method is k-fold cross-validation.

# Hyperparameter Tuning
Hyperparameter tuning is the process of optimizing the hyperparameters of a machine learning model to improve its performance. Hyperparameters are settings that control the learning process and are not learned from the data itself (unlike model parameters).

# 9. Final model comparission --> 
Final model comparison is the last step in the machine learning pipeline where different trained models are evaluated against each other to determine which one performs best for a specific task or dataset. This comparison is crucial for selecting the most effective model before deployment or further analysis. Here’s how to conduct a final model comparison effectively 

# 10. Conclusion :
which model gives the best results and accuracy 








