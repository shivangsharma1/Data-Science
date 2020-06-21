# CharityML Project

## Description

CharityML is a fictitious charity organization located in the heart of Silicon Valley that was established to provide financial support for people eager to learn machine learning. After nearly 32,000 letters were sent to people in the community, CharityML determined that every donation they received came from someone that was making more than $50,000 annually. To expand their potential donor base, CharityML has decided to send letters to residents of California, but to only those most likely to donate to the charity. With nearly 15 million working Californians, CharityML has brought you on board to help build an algorithm to best identify potential donors and reduce overhead cost of sending mail. Your goal will be evaluate and optimize several different supervised learners to determine which algorithm will provide the highest donation yield while also reducing the total number of letters being sent.


## Software Requirements

* Python
* Numpy
* Pandas
* scikit-learn (v0.17)
* Matplotlib
* Anaconda

## Data

### Columns          

 0  - age               
 1  - workclass          
 2  - education_level    
 3  - education-num      
 4  - marital-status     
 5  - occupation          
 6  - relationship        
 7  - race                
 8  - sex                
 9  - capital-gain       
 10 - capital-loss       
 11 - hours-per-week     
 12 - native-country      
 13 - income 
  
## Data exploration, Cleaning and Transformation

* I have used pandas and matplotlib for data exploration and understand the data pattern. The histograms are used for continuous data and bar graphs are used for categorical data. 

* The data has no null values but the data was not clean. So i clean the data using some string operations. The data features were skewed, so I have applied transformations such as log-normal, inverse operation etc which ever best suites the data.

* I have also applied the Minmaxscaler to scale the data.

## Model selection and Building.

While selecting the model for this data I have compared between ADAboost, Randomforest and SVC. The ADAboost model give the better score metrics so I have chosen that model.
The metrics which I used for comparison are accuracy_score, precision_score, recall_score and f1_score.
 
 
 
