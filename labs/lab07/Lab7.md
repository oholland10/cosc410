# Lab 7: CNN Classifier

### COSC 410B: Spring 2025, Colgate University

#### Goals for this lab: 

* (Re)Familiarize yourself with argumenet parser in Python

* Interpret code involving loading and preprocessing image data

* Intepret code involving more complex training settings including the use of GPUs

* Build and train CNN classifiers

#### Submission instructions

You should submit the following files: 

* `Lab7.py`
* `CNN.py`
* `util.py`
* A pdf of [the google doc template](https://docs.google.com/document/d/1Ya9fOFjm8mxQyWiVCD4rFuwDdmLnvKs0DakeQK7u4HU/edit?usp=sharing) with answers to the questions. 



#### Before you start the lab

Activate the `cosc410` environment and then install torchvision by typing: `conda install torchvision`


## Part 1: Describe the process of training a model through the command line

Read through `Lab7.py`. Answer the following questions: 

* What arguments can you pass into `Lab7.py`? How would you pass in these arguments when running the script? What would happen if you did not pass in any arguments and just ran python `Lab7.py`?

* What is a `device`? How is it used? 

* What preprocessing steps are being applied to the `FashionMNIST` data? 

* What is the difference between an optimizer and a scheduler?

## Part 2: Implement functions in `util.py` 
Implement functions in `util.py`. 


## Part 3: Implement `Net1`

Implement a simple CNN with two convolutional layers and a single linear layer. Train your model for 5 epochs. In your google doc template, include: 

* Screeshot of the command you used to train and evalute the model

* Screenshot of the model accuracy 


## Part 4: Implement the other networks

Implement the other CNNs: `Net2` and `Net3`. Train and evaluate each model for 5 epochs. 

In your google doc template, include: 

* Screeshot of the command you used to train and evalute the model

* Screenshot of the model accuracy 


## Part 5: Design a new network

Based on your observations, describe at least one change to any of the networks that you think might be helpful. Make this change in a new network `Net4` and report the model accuracy on teh test set for this network in the google doc template. 




