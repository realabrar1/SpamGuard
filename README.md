# Spam_Classifier

[![GitHub last commit](https://img.shields.io/github/last-commit/FirdausJawed/engage-project?style=for-the-badge&logo=git)](https://github.com/FirdausJawed/) 
[![GitHub stars](https://img.shields.io/github/stars/FirdausJawed/engage-project?style=for-the-badge)](https://github.com/FirdausJawed/Spam-Classifier/stargazers) 
[![GitHub forks](https://img.shields.io/github/forks/FirdausJawed/engage-project?style=for-the-badge&logo=git)](https://github.com/FirdausJawed/Spam-Classifier/network)
[![GitHub issues](https://img.shields.io/github/issues/FirdausJawed/engage-project?style=for-the-badge)](https://github.com/FirdausJawed/Spam-Classifier/issues)
[![GitHub stars](https://img.shields.io/github/stars/FirdausJawed/engage-project?style=for-the-badge)](https://github.com/FirdausJawed/Spam-Classifier/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/FirdausJawed/engage-project?color=%230000ff&style=for-the-badge)](https://github.com/FirdausJawed/Spam-Classifier/network)
[![GitHub license](https://img.shields.io/github/license/FirdausJawed/engage-project?style=for-the-badge)](https://github.com/FirdausJawed/Spam-Classifier)


## **_Index_**
- [About](#About)
- [How to commit in CLI](#Instruction)
- [How to sync your forked repository](#Instruction)
- [Libraries/modules Used](#Libraries/modules-used)
- [Concept used](#Concept-used)
- [Frequently used terms](#Frequently-used-terms)
- [Data-set used](#Data-set-used)
- [Demo & Screenshots](#Demo)
- [Project References](#project-references)
- [License](#license)
- [Connect with me](#connect-with-me)


## About
In an era where digital communication is ubiquitous, the influx of unsolicited spam messages has become a significant annoyance, compromising not only user experience but also data security. The Email/SMS Message Spam Classifier emerges as a potent solution designed to mitigate this issue, harnessing the power of the Naive Bayes algorithm to distinguish between spam and legitimate messages (ham) with remarkable accuracy.

This machine learning project encapsulates a refined model trained on a comprehensive dataset consisting of diverse email and SMS messages. By analyzing the textual patterns and characteristics inherent to spam, the classifier adeptly identifies and filters out intrusive content, thereby safeguarding user inboxes and contributing to a cleaner, more secure digital communication environment.

#### Key Features and Benefits:

- **Efficient Spam Detection:** Utilizing the Naive Bayes algorithm, the classifier offers a high accuracy rate, adeptly distinguishing between spam and ham messages.
- **Versatile Application:** Designed with adaptability in mind, the classifier can be seamlessly integrated into various email clients and messaging applications, offering wide-ranging applicability.
- **User-Friendly Interface:** The project provides an intuitive mechanism for users to train the model on new data and classify messages, ensuring ease of use regardless of technical proficiency.
- **Resource-Efficient:** Optimized for minimal computational resource consumption, the classifier delivers exceptional performance without imposing significant system load.

### How to commit in CLI

```sh
$ git clone https://github.com/FirdausJawed/engage-project.git
$ git checkout -b Branch_Name
$ git add .
$ git commit -m 'message'
$ git push -u origin Branch_Name

```

### How to sync your forked repository

```sh
$ git fetch --all --prune
$ git checkout master
$ git reset --hard upstream/master
$ git push origin master

```
### Libraries/Modules used 

- Numpy
- Pandas
- Scikit-learn
- NLTK
- Streamlit

### Algorithm used
#### Naive Bayes
The Naive Bayes algorithm is a probabilistic classifier based on applying Bayes' theorem with strong (naive) independence assumptions between the features. It is surprisingly effective and is especially useful in text classification problems, including spam detection, sentiment analysis, and categorizing news articles. Despite its simplicity, Naive Bayes can outperform more sophisticated classification methods.

**Naive Bayes' Assumption**
The 'naive' aspect of the Naive Bayes classifier comes from the assumption that all features are independent of each other, given the class label. In other words, the presence or absence of a particular feature does not influence the presence or absence of any other feature, given the class category. This assumption simplifies the computation, and while it may seem oversimplified, Naive Bayes has shown to work well in practice, especially for text classification.

**Types of Naive Bayes Classifier**
There are mainly three types of Naive Bayes models, each designed for a specific type of data distribution:
Gaussian: Assumes that the continuous values associated with each feature are distributed according to a Gaussian (normal) distribution.
Multinomial: Typically used for document classification, where the features are the frequencies with which certain words or phrases appear in the document.
Bernoulli: Useful if your feature vectors are binary (i.e., zeros and ones). An example might be text classification with a bag-of-words model where the 0s 1s are "word occurs in the document" and "word does not occur in the document" respectively.

### Data-set used
[here](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

### Steps involved
- Data cleaning
- Data analysis
- Data preprocessing
- Model Building
- Making Predictions

## Demo
[Click to play](https://drive.google.com/file/d/1pkwjNYDk-bx5OC60pD4NqwfPZjTwZHcl/view?usp=sharing)

## Project References
- [Streamlit Docs](https://docs.streamlit.io)
- [Rapid APIs](https://www.rapitapi.com/)
- [Python basics Datacamp](https://www.datacamp.com/courses/intro-to-python-for-data-science)
- [CampusX YouTube numpy playlist](https://www.youtube.com/playlist?list=PLKnIA16_Rmvb-ToL3RQ_bwxG4_ND-0-DT)
- [CampusX YouTube pandas playlist](https://youtube.com/playlist?list=PLfP3JxW-T70Gf4iJXPb0Yw5_-tDRCD6LB)
- [CampusX Youtube Naive Bayes playlist](https://www.youtube.com/playlist?list=PLKnIA16_RmvZ67wQaHoBuzXaDAfPz-a6l)

## License

Spam Classifier is released under the [MIT License](https://github.com/FirdausJawed/Spam-Classifier/blob/main/LICENSE).

## Connect with me
Drop by and say hello!

[<img height="30" src="https://img.shields.io/badge/linkedin-0077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />][LinkedIn]
[<img height="30" src="https://img.shields.io/badge/twitter-1DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" />][twitter]

[linkedIn]:https://www.linkedin.com/in/firdaus-jawed/

[twitter]: https://twitter.com/jawedfirdaus01
