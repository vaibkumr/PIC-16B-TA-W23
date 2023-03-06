# Short URL for this page: rb.gy/wwnbvs

# Transformers
- Models for sequences of data
- Unlike RNNs (LSTMs, GRUs..) they can handle really long sequences and are computationally fast.

<img src="assets/transformers.jpeg" width="500">

## Some sequence modeling problems:
### 1. Token Classification (Named Entity Recognition)
<img src="assets/token_classification.png" width="500">

Try it [here](https://huggingface.co/dslim/bert-base-NER)

### 2. Sequence Classification (Sentiment Analysis)
<img src="assets/seq_classification.png" width="500">

Try it [here](https://huggingface.co/siebert/sentiment-roberta-large-english)

### 3. Language Generation -- Machine Translation
<img src="assets/translation.png" width="500">

Try it [here](https://huggingface.co/VietAI/envit5-translation)

### 4. Language Generation -- Information Engine/Chat model
<img src="assets/chatgpt.png" width="500">

- It actually generated 58 words, not 50. 
- Try it here: https://chat.openai.com/

### Sequences beyond language?
Think...

### Checkout more models and tasks here: [HuggingFace](https://huggingface.co/models)

# Paper: Attention is all you need
Investment in research pays off with $$$$
![https://arxiv.org/abs/1706.03762](assets/paper.png)

# Breaking down the model:
<img src="assets/transformers_label.png" width="500">

1. Input Representation
2. Encoder
3. Decoder

# Huggingface Transformers

For all our experiments on transformers, we will be using the huggingface transformers library.


`pip install transformers`

<img src="assets/hf.png" width="500">

# Input Representation
[Colab Notebook](https://colab.research.google.com/drive/1PQBVJRsg24U7AkCbtCB5k48MQyJ4ViPn?usp=sharing)

# Encoder
[Colab Notebook](https://colab.research.google.com/drive/1hCbNZp4La34ihGAgaVtIYNLJCuq8_WLo?usp=sharing)

<img src="assets/encoder.png" width="700">

## Use encoder only models for:
1. Sentence Classification
2. Token Classification
3. Clustering



# Decoder
[Colab Notebook](https://colab.research.google.com/drive/1O4Kr4cTzug6tMSFzzZe3AIHUCCAfrwBo?usp=sharing)

<img src="assets/decoder.png" width="700">

## Use decoder only models for:
1. Generating Text for:
    a. Continuations for a prompt
    b. Question Answering
    c. Chatbots

# Encoder Decoder Models
<img src="assets/encoder-decoder.png" width="700">

## Use encoder-decoder models for:
1. Translation
2. Style-rewriting: Formatl to informal

# Expanding Creativity with Transformers
<img src="assets/transformer_uses.png" width="700">

# Some important concepts we have skipped:
- Self-Attention
- Masked Self-Attention
- Cross Attention
- GPU Parallelizability of transformers
- Decoding Algorithms:
    - Beam Search
    -  Nucleus (Top-p) Sampling
    - Top-k Sampling


# Self Attention
## Self Attention Equation:
<img src="assets/self_attention.png" width="700">

## Self Attention Map (in Encoders):
<img src="assets/attention_map.png" width="400">

## Masked Self Attention Map (in Decoders):
<img src="assets/masked_attention_map.png" width="400">
