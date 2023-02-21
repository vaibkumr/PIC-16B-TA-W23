# Neural Networks
- `nn.html`
- A neural network is a type of machine learning algorithm inspired by the structure and function of the human brain.
- It is composed of layers of interconnected nodes, or neurons, that perform mathematical operations on input data to produce an output.
- The connections between neurons are represented by weights, which are adjusted during training to improve the network's performance.

## Training:
- Updating weights iteratively based on the feedback from a loss function  
- Feedback = gradient of a loss function wrt weights
- Updation is typically done using an optimization algorithm
- When to stop the update? After n epochs or after update is very small.
- Foward pass: Data -> weights -> output
- Backward pass: loss -> gradient -> updated weights

## Designing a neural net
1. Identify Task -- Regression? Classification?
2. Identify Data type -- Tabular data? Time series data? Images? Text? Audio? ECG waves?
3. Identify model type based on data and task, some recommendations:
    - DNNs for tabular
    - CNNs for images
    - CNNs for Audio
    - RNNs for Time series data
    - Transformers for Time series data
    - Transformers for Audio
    - CNNs + Transformers for Audio
    - Transformers for Text
    - TRANSFORMERS FOR EVERYTHING (if you have a lot of data)! THEY JUST WORK!!
    - DNN = Deep Neural Network
    - CNN = Convolutional Neural Network
    - RNN = Recurrent Neural Network
4. Identify the loss function based on task, some recommendations:
    - Regression: mean squared error, mean absolute error
    - Classification: Cross entropy, Kullback–Leibler divergence
5. Identify Metrics to evaluate performance, some recommendations:
    - Regression: mean squared error, mean absolute error
    - Binary Classification: Precision, Recall, F1 Score, Accuracy, AUC-ROC
    - Multi-Class Classification: Macro F1, Micro F1, Accuracy
6. Identify Optimizer based on... intuition and latest research, some recommendations:
    - None, just use `adam` it works, almost always. 
7. (Optional) Identify Learning Scheduler based on... intuition.

# Keras Callbacks
[Colab Notebook](https://colab.research.google.com/drive/1AzSezlsHrovE4T5jDjvs3kWMfETUhyJW?usp=sharing)

# Train-Validation-Test Split
1. Train on training data
2. Use Validation data as a feedback to change hyperparameters and improve performance. 
3. Manually keep doing step 1 and 2 until satisfied
4. Use Test data to report final results

# What hyperparameters?
Hyperparameters are model/training parameters we control (they are not learned). Parameters such as model weights are learned. 
- learning rate, 
- number of hidden layers
- number of neurons in each layer
- regularization strength
- more...

# Tracking Losses
[Colab Notebook](https://colab.research.google.com/drive/1T29gYRrgLw6-vrueFtT22YvPltTONcta?usp=sharing)
