### Sentenance Transformers
This required installing ```python3 -m pip install -U sentence-transformers```
```bash
python3 computing_embeddings.py
0it [00:00, ?it/s]
2024-11-18 20:01:07 - Use pytorch device_name: mps
2024-11-18 20:01:07 - Load pretrained SentenceTransformer: all-MiniLM-L6-v2
Batches: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:07<00:00,  7.46s/it]
Sentence: This framework generates embeddings for each input sentence
Embedding: [-0.01371735 -0.0428516  -0.01562862 ...  0.10017828  0.12365725
 -0.04229669]

Sentence: Sentences are passed as a list of string.
Embedding: [ 0.05645246  0.05500241  0.03137955 ...  0.06650877  0.08491525
 -0.03328493]

Sentence: The quick brown fox jumps over the lazy dog.
Embedding: [0.04393355 0.05893441 0.04817837 ... 0.0521628  0.05610653 0.10206389]
```

(https://github.com/UKPLab/sentence-transformers/tree/master)
(https://github.com/UKPLab/EasyNMT)

Characteristics of Sentence Transformer (a.k.a bi-encoder) models:

Calculates a fixed-size vector representation (embedding) given texts or images.

Embedding calculation is often efficient, embedding similarity calculation is very fast.

Applicable for a wide range of tasks, such as semantic textual similarity, semantic search, clustering, classification, paraphrase mining, and more.

Often used as a first step in a two-step retrieval process, where a Cross-Encoder (a.k.a. reranker) model is used to re-rank the top-k results from the bi-encoder.

Once you have installed Sentence Transformers, you can easily use Sentence Transformer models:

```python
from sentence_transformers import SentenceTransformer

# 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# The sentences to encode
sentences = [
    "The weather is lovely today.",
    "It's so sunny outside!",
    "He drove to the stadium.",
]

# 2. Calculate embeddings by calling model.encode()
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# 3. Calculate the embedding similarities
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.6660, 0.1046],
#         [0.6660, 1.0000, 0.1411],
#         [0.1046, 0.1411, 1.0000]])
```
