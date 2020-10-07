<h1 style= 'font: chalkduster'> Regression Project: Estimating Home Value </h1><br><br>

<b><u>

<h2> About the project</h2><br>
<h3>Background</h3><br><br>
Kwame and Gabby want to predict the values of single unit properties that the tax district assesses using the property data from those whose last transaction was during the peak real estate demand months of May and June 2017. <br><br><br><br>
<h3>Goals</h3>
<ol>
<li>Gabby and Kwame want to present to the Zillow Team regarding the findings and prediction models about the drivers of the single unit property values.</li>
<li> Kwame and Gabby want to produce deliverables [] so that people who are interested in the data and those who want to verify the validity of their findings may do so.</li><br><br><br>
<h3> Data Dictionary</h3><br><br>
<b><u>Co-op:</b></u> A unit of a housing co-operative; a purchased apartment where the apartment owners collectively are responsible for maintenance of common areas and upkeep.<br>
<b><u>Logistic Regression: </b></u>  A regression algorithm used to predict discrete outcomes.<br>
<b><u>Decision Tree: </b></u> A sequence of rules that can be used to classify 2 or more classes using supervised machine learning processes.<br>
<b><u>Random Forest: </b></u> A learning method that constructs a multitude of decision trees at training time and outputting the classification.<br>
<b><u>K-Nearest Neighbor (KNN): </b></u> A lazy algorithm in that it does not attempt to construct a general internal model, but simply stores instances of the training data. Classification is computed from a simple majority vote of the k nearest neighbours of each point. Makes predictions based on how close a new data point is to known data points.<br>
<b><u>Precision: </b></u> the higher this number is, the more you were able to pinpoint all positives correctly. If this is a low score, you predicted a lot of positives where there were none. tp / (tp + fp)
<b><u>Recall: </b></u> If this score is high, you didn’t miss a lot of positives. But as it gets lower, you are not predicting the positives that are actually there. tp / (tp + fn) <br>
<b><u>f1-score: </b></u> The balanced harmonic mean of Recall and Precision, giving both metrics equal weight. The higher the F-Measure is, the better. <br>
<b><u>Support: </b></u> The number of occurrences of each class in where y is true. <br>
<b><u>Min-Max Scaling: </b></u> A linear scaling method that transforms our features such that the range is between 0 and 1.<br>
<b><u>Standardization: </b></u> A linear transformation of our data such that is looks like the standard normal distribution. That is, it will have a mean of 0 and a standard deviation of 1.<br>
<b><u>Regression Line: </b></u> Also known as a line of best fit, a linear regression algorithm that returns the slope and y-intercept of the line that most accurately predicts y, given the x and y provided to the algorithm. <br>
<b><u>Baseline: </b></u> Predicting the target variable without using any features. Take the mean or median value and predict all future values to be that constant value.<br>
<b><u>Residual: </b></u> The difference between the observed value and the estimated value.<br>
<b><u>Sum of the Squared Errors (SSE): </b></u> Also known as, RSS, Residual Sum of Squares will be used as the final metric to evaluate. The value of the SSE is derived by simply squaring each of the errors computed in step one and summing them all together<br>
<b><u>Mean Squared Error (MSE): </b></u> The average of the errors that have each been squared.<br>
<b><u>Root Mean Squared Error (RMSE): </b></u> Simply take the square root of the MSE. Used to see the error in the actual units of the y variable.<br>
<b><u>Select the K best: features using a statistical test to compare each X with y and find which X's have the strongest relationship with y.<br>
<b><u>Recursive Feature Elimination: </b></u> Creates a model with all the features, evaluates the performance metrics, find the weakest feature, removes it, then creates a new model with the remaining features, evaluate the performance metrics, find the weakest feature, remove it, and so on, until it gets down to the number of features indicated when creating the rfe object.<br>
<b><u>Regression: </b></u> Asupervised machine learning technique used to model the relationships between one (simple) or more (multiple) features (independent) and how they contribute to one (univariate) or more (multivariate) target variables (dependent), represented by a continuous variable. <br>
<br><br><br>


<h3>Hypothesis Testing </h3>
First Hypothesis 𝐻0 : Lot square footage has no effect on the property values.<br>
𝐻𝑎 : Lot square footage has an effect on the property values.<br><br>
Second Hypothesis
𝐻0 : There is no difference in property values between properties with last the transaction in May 2017 and June 2017.<br>
𝐻𝑎 : There is a higher property value for properties with a last transaction in May 2017. 



<h3>Data Science Pipeline Used</h3>
<b><u>acquire.py </b></u> <br>
acquire data from csv gathered from sql. <br><br>
prepare.py </b></u> <br>
address missing data <br>
address outliers <br>
scale numeric data <br>
split into train, validate, test <br><br>
<b><u>explore </b></u> <br>
plot correlation matrix of all variables<br>
test each hypothesis<br><br>
<b><u>model</b></u> <br>
feature engineering to construct new features <br>
try different algorithms: Feature Elimination, Multiple Linear Regression Model, Polynomial Regression Model, Baseline Model
which features are most influential?<br>
evaluate on train<br>
select top 3 +/- models to evaluate on validate<br>
select top model<br>
run model on test to verify.<br>
conclusion
summarize findings
make recommendations
next steps
how to run with new data.


<h3>Conclusion</h3>
Conclusion to be added here.



<h3>How to reproduce the results</h3>
You may download acquire.py and prepare.py. You will need your own env.py file with your SQL credentials in order to access the SQL server.
