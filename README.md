# Reddit-Flair-Prediction-IIITD
A Web Application that ineURLs from r/india as inputs and predicts the flair of the post based on a Machine Learning model created using the Linear Support Vector Machine Algorithm. The application is hosted on Heroku Cloud Platform and could be tried at https://sai9.herokuapp.com/ . It also has an Automated_Testing facility when POST requests are sent remotely in a text file(each .txt file should contain 1 URL).
## Directory Structure
Python has been used to develop the application and several libraries have been implemented. The libraries are :
* PRAW
* SCIKITLEARN
* NUMPY
* NLTK
* PANDAS
* PICKLE
* STOPWORDS
* STRING
* RE
* FLASK

The scraped data is saved and loaded as a .CSV file and loaded as a .pkl file

The directory is a FLASK web application hosted on Heroku servers. The description of  files and folders can be found below:
* Models: Folder containing the saved model.pkl file.
* Templates: Folder containing the HTML files.
* App.py: Main file responsible for starting up the Flask application.
* Procfile: File needed to host the application to Heroku.
* Requiremnets.txt:Containing all Python dependencies of the project.
* Data: Folder containing CSV files with scraped data that is pre-processed and cleaned.
* Jupyter Notebooks: Folder containing Jupyter Notebooks to collect Reddit India data, EDA and training of the Machine Learning model. Notebooks can be opened in Colaboratory by Google. Even Flair Detector and Predictors scripts are present here.

## Project Workflow and Execution
The web-application allows the user to enter a r/india URL and displays the predicted flair for the submitted post.
1. Clone the repository using terminal 
https://github.com/Tamoghna-Sarkar/Reddit-Flair-Prediction-IIITD 
2. Make sure that Python3 and pip are installed on the system.
3. Create a virtual environment:
~~~~
python3 -m venv *name* 
source *name* /bin/activate 
cd *name_of_yourenv*/
~~~~
4. Install all the dependencies in the root directory  by executing pip install -r requirements.txt and imExecute the app.py to run the FLask application on the local server.
## Approach
After understanding the task in depth, and going through various opensource documentations available for text processing, text analysis and suitable ML Algorithms for text classification, I based my final approach using Linear Support Vector Machine Algorithm which demonstrated optimum accuracy during the training and testing phase. I have also tried implementing the Naive Bayes, Logistic Regression, MLP Classifier and Random Forest algorithms to check the accuracy of the model with these algorithms. The test accuracies that I obtained are attached below. The approach taken for the task are as follows:
1. Collect R/India data keeping the limit as 80 posts per flair among the flairs present in R/India reddit page using the PRAW module. [1]
2. Include attributes like the flair title, body, comments, and the url of the flair.
3. Pre-process the title, comments, url and body by converting everything into format by using *EMPHASIZE* “astype(str)”.
## Results
#### Title as Feature
| Machine Learning Algorithms  | Test Accuracy |
| --------  | -------- |
| Naive Bayes <br />       | 0.6704 |
| Linear SVM <br />       | 0.7424 |
| Logistic Regression <br />       | 0.7272 |
| Random Forest <br />       | 0.7272 |
| MLP <br />       | 0.5227 |

#### Body as Feature
| Machine Learning Algorithms  | Test Accuracy |
| --------  | -------- |
| Naive Bayes <br />       | 0.2765 |
| Linear SVM <br />       | 0.3257 |
| Logistic Regression <br />       | 0.3636 |
| Random Forest <br />       | 0.2651 |
| MLP <br />       | 0.2689 |

#### URL as Feature
| Machine Learning Algorithms  | Test Accuracy |
| --------  | -------- |
| Naive Bayes <br />       | 0.2777 |
| Linear SVM <br />       | 0.3636 |
| Logistic Regression <br />       | 0.2992 |
| Random Forest <br />       | 0.2651 |
| MLP <br />       | 0.2537 |

#### Comments as Feature
| Machine Learning Algorithms  | Test Accuracy |
| --------  | -------- |
| Naive Bayes <br />       | 0.3560 |
| Linear SVM <br />       | 0.4280 |
| Logistic Regression <br />       | 0.4356 |
| Random Forest <br />       | 0.4242 |
| MLP <br />       | 0.3219 |

#### COMBINED: Title + Comments as Feature
| Machine Learning Algorithms  | Test Accuracy |
| --------  | -------- |
| Naive Bayes <br />       | 0.5189 |
| Linear SVM <br />       | 0.6477 |
| Logistic Regression <br />       | 0.6098 |
| Random Forest <br />       | 0.6439 |
| MLP <br />       | 0.4583 |
