[Colab Notebook](https://colab.research.google.com/drive/1DFUU9gAha6aJN_LvIsDP_HZYBpsRDSDP?usp=sharing)

# Text Classification using LSTMs

# Handling Text Data
Think of text like a timeserie, x_t is word at time t. Following is the data pipeline to feed text data into neural networks:
![](assets/text_classification.png)

# LSTMs and GRUs
- LSTM: Long Short-Term Memory
- GRU: Gated Recurrent Unit
- LSTM and GRU are types of RNN
- They are good with long sequences, unlike regular RNNs.
- Why? Read more [here](http://dprogrammer.org/rnn-lstm-gru)
- We are ignoring the small details for now
![](assets/RNN-vs-LSTM-vs-GRU.png)
