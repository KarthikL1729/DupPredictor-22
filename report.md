---
title: "SMAI Project Report - Team 40"
subtitle: "Multi-Factor Duplicate Question Detction in Stack Overflow"
author:
- Ananya Sane
- L Lakshmanan
- Poorva Pisal
- Sneha Raghava Raju
abstract: This report details our implementation of the paper titled “Multi-Factor Duplicate Question Detection in Stack Overflow” by Y. Zhang et al. The objective of the paper is to create and train a model that is able to take a new question from a user as an input, compute certain weighted measures and give a list of k questions that are most similar to the input question. The similarity between two questions is calculated by using four distinct parameters, that are used in computing the measures, that stem from the four components in a stack overflow question - Title, Description, Tags and Topics. The similarity score is calculated and then used as a metric for ranking and creating the output list. We implement the model using Python due to its extensive library support. We also train and test the model on a smaller dataset due to hardware limitations, however the model has the same architecture and hence, should scale well. We conclude by showing results and listing some limitations.
urlcolor: blue

---

---
geometry:
- top=25mm
- left=25mm
- right=25mm
- heightrounded
...

## Introduction and Motivation


## Dataset

The dataset for the predictor is taken from [Stack Exchange Data Explorer for Superuser](https://data.stackexchange.com/superuser). A set of 20,000 questions are taken along with 8811 past question and duplicate pairs. 

For every question four fields are taken into consideration, namely Question ID, Title, Tags and Body. 

The queries to get the dataset for duplicate questions are as follows:

![Query to get the past questions](query1.png)

To find duplicate questions we are checking if the question has been closed and checking if the reason for closing was ‘Duplicate’ (i.e ph.Comment = 101).

To get the main dataset of past questions, we run the following queries.

