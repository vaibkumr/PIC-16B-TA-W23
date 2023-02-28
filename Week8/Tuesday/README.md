# Time series data
Modeling a time series data:
![](assets/timeseries.png)

#### Q: Can you think of some time series data?

# Recurrent Neural Network

Recurrent Neural Networks have loops, which when unrolled looks as follow:
![Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/](assets/RNN-unrolled.png)

## Backpropagation Through Time (BPTT)
The gradients at propagated from from t=T to t=0 in the above network where T is the sequence length.

## What is the shape of the input to RNN?
- NN: [batch_size x num_input_features]
- RNN: ??

# Units
Number of units is just #neurons on each layer of the RNN. Following is a RNN with x units... what is x?
![Source: https://datascience.stackexchange.com/questions/12964/what-is-the-meaning-of-the-number-of-units-in-the-lstm-cell](assets/dkXgO.jpg)

# RNNs limitations:
- Gradient vanishing/explosion
- Computationally slow, to compute activations at time t, we need activations of time t-1, t-2..., can't do this in parallel.
