# finger-spelling-text

Convolutional Neural Network that inputs and classifies photos of fingerspelling in American Sign Language.

Summaries of file contents are as follows:


## Notebook 0: Exploration


Demonstrating CNN use with The ASL MNIST Dataset and a simple neural network

Improvement paths from starting model

Optimizing hyperparameters via grid search (useful for smaller CNN's)

Implementing Data: ASL Alphabet

Training with Validation

Test with Larger Images

Creating a single photo of my hand signing 'A' for demo purposes

Transfer Learning

Removing a dense layer to reduce overfitting and increase fitting speed.

Photo Predictions


## Notebook 1: Current Working Setup

![template from drawio](readme_images/project_map.png?raw=true)


Importing Data

CNN Model

Making Methods

Interaction


## model_3_0

Current trained model for image recognition tasks.


-----------------


## Installation instructions for the anaconda environment needed:


(open an anaconda prompt and run these lines, one at a time)


conda create -n fingerspelling

conda activate fingerspelling

conda install numpy pandas matplotlib jupyter jupyterlab seaborn

pip install tensorflow==2.4


## Launch instructions


(in order to open a notebook in this environment, open an anaconda prompt
and run these lines, one at a time. This will open jupyter notebook in a
tab of your computer's default browser.)


activate fingerspelling

jupyter notebook
