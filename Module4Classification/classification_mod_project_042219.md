# End of Module Project ds-042219

## Applying Classification Modeling

For this module's project, you will answer a classification data science question using multiple models and present the results of your project. In doing so, we want you to utilize all of the different tools we have learned over the course: data cleaning, EDA, feature engineering/transformation, feature selection, hyperparameter tuning, and model evaluation. Each student will give a 4 minute presentation on Friday to explain their project to their fellow classmates.


#### Data Set Information:

- [Drug Use dataset](https://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29)
- [Wine Quality dataset](https://archive.ics.uci.edu/ml/datasets/wine+quality)
- [Bach Choral dataset](https://archive.ics.uci.edu/ml/datasets/Bach+Choral+Harmony)
- [Forest Cover dataset](https://www.kaggle.com/uciml/forest-cover-type-dataset)
- [Pima Indians dataset](https://www.kaggle.com/uciml/pima-indians-diabetes-database)
- [Breast Cancer Wisconsin (Diagnostic) dataset](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data)
- [Pulsar Star dataset](https://www.kaggle.com/pavanraj159/predicting-a-pulsar-star)



You will fit at least four different classification models (KNN, Logistic Regression, Decision Trees, Random Forest, XGBoost, etc.) to make respective predictions for the data you choose to work with. Then you will compare the performance of those four models on a test set to find the best one.  


## Process/Expectations


1. Clean up your data set so that you can perform an EDA.
    - This includes handling null values, categorical variables, removing unimportant columns, and removing outliers.


2. Perform EDA to identify opportunities to create new features. EDA is a critical part of your process. Not only does it help you to think about new features to create, but it allows you to develop hypothesis about each variable.
    - [Great Example of EDA for classification](https://www.kaggle.com/stephaniestallworth/titanic-eda-classification-end-to-end)
    - [Using Pairplots with Classification](https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166)


3. Engineer new features.
    - Create **at least three non-linear features** (polynomial, log transformations, and/or interaction features).
    - Additionally, you must also create **at least three more new features** *that are not* interactions or polynomial transformations.
        - *For example, you can create a new dummy variable that is based on the value of a continuous variable (billamount6 >2000) or take the average of some past amounts.*


4. Perform some feature selection. This will be an iterative process where you can try different versions and eventually settle on the best version.

5. You must fit **four** models to your data and tune **at least two hyperparameters** per model.

6. Decide on which evaluation metric you think is most appropriate for your project, evaluate how well your models perform, and identify your best model.

7. Use the outputs of your different models, along with your EDA work, to provide insight to your original question.
  - *What made people more likely to survive the titanic?*
  - *What is a big predictor of a person's likelihood to default on a credit card?*

8. Explain how your model can be used to in the real world to solve a problem.   
