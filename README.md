<h3>Kwame and Gabby, Codeup Darden Cohort, Oct 2020</h3>

<h1 style= 'font: chalkduster'> Regression Project: Estimating Home Value </h1>

<img src="https://www.underconsideration.com/brandnew/archives/zillow_logo.png">

<h2> About the project</h2>
<h3>Background</h3>
Kwame and Gabby want to predict the values of single unit properties that the tax district assessments using the property data from those whose last transaction was during the peak real estate demand months of May and June 2017. <br>

---

<h3>Goals</h3>
<ol>
<li>Gabby and Kwame want to present to the Zillow Team regarding the findings and prediction models about the drivers of the single unit property values.</li>
<li> Kwame and Gabby want to produce deliverables acquire.py, prepare.py, explore.py and model.py so that people who are interested in the data and those who want to verify the validity of their findings may do so.</li><br>
  
---
  
<h3> Data Dictionary</h3>

<table>
<thead>
  <tr>
    <th>Term</th>
    <th>Definition</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Co-Op</td>
    <td>A unit of a housing co-operative; a purchased apartment where the apartment owners collectively are responsible for maintenance of common areas and upkeep.</td>
  </tr>
  <tr>
    <td>Single Unit Property</td>
    <td>The term housing unit refers to a single unit within a larger structure that can be used by an individual or household to eat, sleep, and live. The unit can be in any type of residence such as a house, apartment, mobile home, or may also be a single unit in a group of rooms.</td>
  </tr>
  <tr>
    <td>Logistic Regression</td>
    <td>A regression algorithm used to predict discrete outcomes.</td>
  </tr>
  <tr>
    <td>Decision Tree</td>
    <td>A sequence of rules that can be used to classify 2 or more classes using supervised machine learning processes.</td>
  </tr>
  <tr>
    <td>Random Forest</td>
    <td>A learning method that constructs a multitude of decision trees at training time and outputting the classification.</td>
  </tr>
  <tr>
    <td>K-Nearest Neighbor (KNN)</td>
    <td>A lazy algorithm in that it does not attempt to construct a general internal model, but simply stores instances of the training data. Classification is computed from a simple majority vote of the k nearest neighbours of each point. Makes predictions based on how close a new data point is to known data points.</td>
  </tr>
  <tr>
    <td>Precision</td>
    <td>the higher this number is, the more you were able to pinpoint all positives correctly. If this is a low score, you predicted a lot of positives where there were none. tp / (tp + fp)</td>
  </tr>
  <tr>
    <td>Recall</td>
    <td>If this score is high, you didn’t miss a lot of positives. But as it gets lower, you are not predicting the positives that are actually there. tp / (tp + fn)</td>
  </tr>
  <tr>
    <td>f1-score</td>
    <td>The balanced harmonic mean of Recall and Precision, giving both metrics equal weight. The higher the F-Measure is, the better.</td>
  </tr>
  <tr>
    <td>Support</td>
    <td>The number of occurrences of each class in where y is true.</td>
  </tr>
  <tr>
    <td>Min-Max Scaling</td>
    <td>A linear scaling method that transforms our features such that the range is between 0 and 1.</td>
  </tr>
  <tr>
    <td>Standardization</td>
    <td>A linear transformation of our data such that is looks like the standard normal distribution. That is, it will have a mean of 0 and a standard deviation of 1.</td>
  </tr>
  <tr>
    <td>Regression Line</td>
    <td>Also known as a line of best fit, a linear regression algorithm that returns the slope and y-intercept of the line that most accurately predicts y, given the x and y provided to the algorithm.</td>
  </tr>
  <tr>
    <td>Baseline</td>
    <td>Predicting the target variable without using any features. Take the mean or median value and predict all future values to be that constant value.</td>
  </tr>
  <tr>
    <td>Residual</td>
    <td>The difference between the observed value and the estimated value.</td>
  </tr>
  <tr>
    <td>Sum of the Squared Errors (SSE)</td>
    <td>Also known as, RSS, Residual Sum of Squares will be used as the final metric to evaluate. The value of the SSE is derived by simply squaring each of the errors computed in step one and summing them all together.</td>
  </tr>
  <tr>
    <td>Mean Squared Error (MSE)</td>
    <td>The average of the errors that have each been squared.</td>
  </tr>
  <tr>
    <td>Root Mean Squared Error (RMSE)</td>
    <td>Simply take the square root of the MSE. Used to see the error in the actual units of the y variable.</td>
  </tr>
  <tr>
    <td>K-Best</td>
    <td>Features using a statistical test to compare each X with y and find which X's have the strongest relationship with y.</td>
  </tr>
  <tr>
    <td>Recursive Feature Elimination (RFE)</td>
    <td>Creates a model with all the features, evaluates the performance metrics, find the weakest feature, removes it, then creates a new model with the remaining features, evaluate the performance metrics, find the weakest feature, remove it, and so on, until it gets down to the number of features indicated when creating the rfe object.</td>
  </tr>
  <tr>
    <td>Regression</td>
    <td>A supervised machine learning technique used to model the relationships between one (simple) or more (multiple) features (independent) and how they contribute to one (univariate) or more (multivariate) target variables (dependent), represented by a continuous variable.</td>
  </tr>
</tbody>
</table>

---

<h3>Hypothesis Testing </h3><br>

First Hypothesis<br>
𝐻0: The number of bathrooms has no correlation on the tax estimated property value.<br>
𝐻𝑎: The number of bathrooms has a correlation with the tax estimated property value.<br>

Second Hypothesis<br>
𝐻0: There is no correlation between finished square feet and tax estimated property value.<br>
𝐻𝑎: There is a correlation between finished square feet and tax estimated property value.<br>

---

<h3>Data Science Pipeline Used</h3>

<b><u>acquire.py </b></u> <br>
 * acquire data from csv gathered from sql. <br>

<b><u> prepare.py </b></u> <br>
* address missing data <br>
* address outliers <br>
* scale numeric data <br>
* split into train, validate, test <br>

<b><u>explore </b></u> <br>
* plot correlation matrix of all variables<br>
* test each hypothesis<br>

<b><u>model</b></u> <br>
* feature engineering to construct new features <br>
* try different algorithms: Feature Elimination, Multiple Linear Regression Model, Polynomial Regression Model, Baseline Model
* which features are most influential?<br>
* evaluate on train<br>
* select top 3 +/- models to evaluate on validate<br>
* select top model<br>
* run model on test to verify.<br>
* conclusion
* summarize findings
* make recommendations
* next steps
* how to run with new data.


<h3>Conclusion</h3>
The conclusions of the hypotheses tests are Since p is less than α, we reject our null hypothesis that bathroom has no effect on the tax estimated property value and that since p is less than α, we reject our null hypothesis that there is no correlation between finished square feet and tax estimated property value. <br><br>
Initially we found that bathroom count has a slightly stronger correlation with tax property value assessments but upon further modeling found that bedroom count and bath/bedroom count have a higher correlation.<br>
Further exploration and modeling can be done to assess differences is estimated prices  in counties, between lot sizes and between the two months of May and June 2017.<br>



<h3>How to reproduce the results</h3>
You may download acquire.py and prepare.py. You will need your own env.py file with your SQL credentials in order to access the SQL server.
