# Reddit-Flair-Prediction-IIITD
A Web Application that ineURLs from r/india as inputs and predicts the flair of the post based on a Machine Learning model created using the Linear Support Vector Machine Algorithm. The application is hosted on Heroku Cloud Platform and could be tried at https://sai9.herokuapp.com/ . It also has an Automated_Testing facility when POST requests are sent remotely in a text file(each .txt file should contain 1 URL).


 


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
