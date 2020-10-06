<h1 style= 'font: chalkduster'> Regression Project: Estimating Home Value </h1><br><br>



About the project
Goals
Kwame and Gabby want to predict the values of single unit properties that the tax district assesses using the property data from those whose last transaction was during the peak real estate demand months of May and June 2017. 


Data Dictionary
co-op: A unit of a housing co-operative; a purchased apartment where the apartment owners collectively are responsible for maintenance of common areas and upkeep.<br>
Logistic Regression: A regression algorithm used to predict discrete outcomes.<br>
Decision Tree: A sequence of rules that can be used to classify 2 or more classes using supervised machine learning processes.<br>
Random Forest: A learning method that constructs a multitude of decision trees at training time and outputting the classification.<br>
K-Nearest Neighbor (KNN): A lazy algorithm in that it does not attempt to construct a general internal model, but simply stores instances of the training data. Classification is computed from a simple majority vote of the k nearest neighbours of each point. Makes predictions based on how close a new data point is to known data points.<br>
Precision: the higher this number is, the more you were able to pinpoint all positives correctly. If this is a low score, you predicted a lot of positives where there were none. tp / (tp + fp)
Recall: If this score is high, you didn’t miss a lot of positives. But as it gets lower, you are not predicting the positives that are actually there. tp / (tp + fn) <br>
f1-score: The balanced harmonic mean of Recall and Precision, giving both metrics equal weight. The higher the F-Measure is, the better. <br>
Support: The number of occurrences of each class in where y is true. <br>
Min-Max Scaling: A linear scaling method that transforms our features such that the range is between 0 and 1.<br>
Standardization: A linear transformation of our data such that is looks like the standard normal distribution. That is, it will have a mean of 0 and a standard deviation of 1.<br>
Regression Line: Also known as a line of best fit, a linear regression algorithm that returns the slope and y-intercept of the line that most accurately predicts y, given the x and y provided to the algorithm. <br>
Baseline: Predicting the target variable without using any features. Take the mean or median value and predict all future values to be that constant value.<br>
Residual: The difference between the observed value and the estimated value.<br>
Sum of the Squared Errors (SSE): Also known as, RSS, Residual Sum of Squares will be used as the final metric to evaluate. The value of the SSE is derived by simply squaring each of the errors computed in step one and summing them all together<br>
Mean Squared Error (MSE): The average of the errors that have each been squared.<br>
Root Mean Squared Error (RMSE): Simply take the square root of the MSE. Used to see the error in the actual units of the y variable.<br>
Select the K best: features using a statistical test to compare each X with y and find which X's have the strongest relationship with y.<br>
Recursive Feature Elimination: Creates a model with all the features, evaluates the performance metrics, find the weakest feature, removes it, then creates a new model with the remaining features, evaluate the performance metrics, find the weakest feature, remove it, and so on, until it gets down to the number of features indicated when creating the rfe object.<br>
Regression: Asupervised machine learning technique used to model the relationships between one (simple) or more (multiple) features (independent) and how they contribute to one (univariate) or more (multivariate) target variables (dependent), represented by a continuous variable. <br>



Hypothesis Testing
Hypothesis Testing
First Hypothesis 𝐻0 : Lot square footage has no effect on the property values.
𝐻𝑎 : Lot square footage has an effect on the property values.<br><br>
Second Hypothesis
𝐻0 : There is no difference in property values between properties with last the transaction in May 2017 and June 2017.
𝐻𝑎 : There is a higher property value for properties with a last transaction in May 2017. 



Data Science Pipeline Used
acquire.py
acquire data from csv gathered from sql.
prepare.py
address missing data
address outliers
split into train, validate, test
explore
plot correlation matrix of all variables
test each hypothesis
model
try different algorithms: decision tree, logistic regression, random forest,knn
which features are most influential?
evaluate on train
select top 3 +/- models to evaluate on validate
select top model
run model on test to verify.
conclusion
summarize findings
make recommendations
next steps
how to run with new data.




Conclusion
Customers without dependents, on month to month contracts and who have additional features are more likely to churn. Through analyzing the data, we have found that the customers who churn are paying more. This can be explained by the additional features that many customers have. Next steps would be to find out which specific features cost the most and cause the highest churn. My recommendation to retain customers would be to investigate offering bundle deals and having customers sign contracts to reduce the churn with the company.

How to reproduce the results
You may download acquire.py and prepare.py. You will need your own env.py file with your SQL credentials in order to access the SQL server.

Organization Photo:
Image by <a href="https://pixabay.com/users/mastersenaiper-4157718/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2323278">mastersenaiper</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2323278">Pixabay</a>