# finger-spelling-text

Convolutional Neural Network that inputs and classifies photos of fingerspelling in American Sign Language. 

This project has been a series of sprints. As such, notebooks contain a mix of experimentation and useful results.


## Notebook 0-1: Exploration and First Deliverable

### Notebook 0:  Early Exploration
Demonstrating CNN use with The ASL MNIST Dataset and a simple neural network

#### Table of Contents

Improvement paths from starting model

Optimizing hyperparameters via grid search (useful for smaller CNN's)

Implementing Data: ASL Alphabet

Training with Validation

Test with Larger Images

Creating a single photo of my hand signing 'A' for demo purposes

Transfer Learning

Removing a dense layer to reduce overfitting and increase fitting speed.

Photo Predictions


### Notebook 1: First Working Setup

![template from drawio](readme_images/project_map.png?raw=true)

#### Table of Contents

Importing Data

CNN Model

Making Methods

Interaction


## Notebook 2: Exploring Hand Photography with opencv-python

Planning scripts to capture hand photos from webcam.

#### Table of Contents

Opening an image via opencv-python and optionally saving

Capturing an image from my laptop camera

Capturing an image of just my hands via cropping, for now

Foreground detection

Cropping based on hand presence


## Notebook 3: Exploring Model Improvements, Video Feed Prediction functions, Further Training Models

Earlier models were difficult to evaluate and were consistently found lacking when used. 
This notebook will attempt to produce improved models given these concerns. It will also feature early UI drafts.

#### Table of Contents

Baseline Model

Trying Model Improvements: (sub-entries) Viewing image, Disabling the datagen's shuffle feature, Perhaps that warning when importing MobileNetV2 is actually not all bark and no bite, Optimizing hyperparameters via grid search

Generating New Baseline: Model 5

Trying Further Model Improvements

-----------------


## Installation instructions for the anaconda environment needed:


(open an anaconda prompt and run these lines, one at a time)

`conda create -n fingerspelling`

`conda activate fingerspelling`

`conda install numpy pandas matplotlib jupyter jupyterlab seaborn`

`pip install tensorflow==2.4`

`pip install -U keras-tuner `


## Launch instructions

(in order to open a notebook in this environment, open an anaconda prompt
and run these lines, one at a time. This will open jupyter notebook in a
tab of your computer's default browser.)

`activate fingerspelling`

`jupyter notebook`