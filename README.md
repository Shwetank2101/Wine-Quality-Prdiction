# Wine Quality Prediction -
[Website of our project](https://wine-quality-prdiction.herokuapp.com/)


![Image](https://github.com/Shwetank2101/Wine-Quality-Prdiction/blob/master/static/images/wine.jpg)

Our main objective is to predict the wine quality using machine learning through Python programming language.
A large dataset is considered and wine quality is modelled to analyse the quality of wine through different parameters like fixed acidity, volatile acidity etc. 
All these parameters will be analysed through Machine Learning algorithms which will helps to rate the wine on scale 1 - 10 or bad - good. 
Output obtained would further be checked for correctness and model will be optimized accordingly. 
We have to create a beautiful interface for interaction between the user and our ML model which is done through the Django framework.
It can support the wine expert evaluations and ultimately improve the production.


## Dataset Description -

We have taken our datasets from UCI Machine learning Repository. 
Two datasets are included, related to red and white vinho verde wine samples, from the north of Portugal.
White wine consists of 4898 samples and red wine contains 1599 samples. Each sample of both types of wine consists of 12 physicochemical variables:
1. Fixed acidity 
2. Volatile acidity
3. Citric acid 
4. Residual sugar 
5. Chlorides 
6. Free sulfur dioxide 
7. Total sulfur dioxide
8. Density 
9. pH 
10. Sulphates 
11. Alcohol 
12. Quality

## Technologies Used -
1. Python programming Language
2. Advanced Python libraries:

       a. Pandas      
       b. matplotlib      
       c. numpy      
       d. scikit-learn
      
3. Machine Learning Algorithms 
4. Django Framework
5. HTML
6. CSS

## Methodology -

We have followed a step by step procedure for the analysis of our dataset. We have undertaken the following steps while performing data analysis:

1. Data Pre-Processing
2. Data Visualization
3. Applying Machine Learning Algorithms
4. Building an Interface using Django

## Results -

Accuracy from Decision Tree Classifier is 73.74 %

Accuracy from RandomForestClassifier is 80.43 %

Accuracy from Adaboost classifier is 76.76 %

Accuracy from Gradient Boosting Algorithm is 80.64 %

Accuracy from XGBoost Classifier is 80.43 %

Accuracy from Naive Bayes is 70.36 %

Accuracy from K-Nearest Neighbours is 78.06 %

Accuracy from Support Vector Machine algorithm is 70.36 %

## Conclusion -
Both red and white wine dataset consists of 12 physicochemical characteristics. One (quality) is dependent variable and the other 11 are predictors. The experiments show that the value of the dependent variable can be predicted more accurately if only important features are considered in prediction rather than considering all features.
In this work, machine learning techniques are used to determine dependency of wine quality on other variables and  in  wine  quality predictions. We have analysed that there are some variables which have a strong effect on our output variables and they are: alcohol, density, volatile acidity. There are also variables which affect these variables and they are chloride, residual sugar, volatile aciditfy, Sulphide oxide. After applying all the Machine Learning Algorithms, we have realised that Gradient Boosting Algorithm gives the best result in terms of accuracy of 80.64 %.

## Developers -
Shwetank Dixit

Srishti Rastogi

