import torch
import matplotlib.pyplot as plt
import numpy as np
from transformers import DistilBertTokenizer, DistilBertModel

# Load model/tokenizer
model_name = "distilbert-base-uncased"
tokenizer = DistilBertTokenizer.from_pretrained(model_name)
model = DistilBertModel.from_pretrained(model_name, output_attentions=True)
model.eval()

# Input sentence
sentence = "my cat shat on a hat"
inputs = tokenizer(sentence, return_tensors="pt")
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

# Get attention weights
with torch.no_grad():
    outputs = model(**inputs)
    attentions = outputs.attentions  # shape: (num_layers, batch_size, num_heads, seq_len, seq_len)

# Extract first layer (layer 0), first 3 heads
layer = attentions[0][0]  # shape: (num_heads, seq_len, seq_len)

# Strip CLS and SEP (index 0 and -1)
keep_idxs = list(range(1, len(tokens) - 1))
tokens_clean = [tokens[i] for i in keep_idxs]

# Plot 3 heads
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for i in range(3):
    # Select only the rows/cols we care about (ignore CLS and SEP)
    attn_clean = layer[i][keep_idxs][:, keep_idxs].numpy()

    ax = axes[i]
    im = ax.imshow(attn_clean, cmap="viridis")

    ax.set_xticks(np.arange(len(tokens_clean)))
    ax.set_yticks(np.arange(len(tokens_clean)))
    ax.set_xticklabels(tokens_clean, rotation=45, ha="right")
    ax.set_yticklabels(tokens_clean)
    ax.set_title(f"Head {i}")

fig.suptitle("DistilBERT Attention (Layer 1, Heads 0–2)", fontsize=16)
plt.tight_layout()
plt.show()
