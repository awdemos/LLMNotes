# This enhanced version offers several improvements:
# Individual Macron Encodings: Instead of a single macron encoding, we now have separate encodings for each macron-bearing vowel (ā, ē, ī, ō, ū). This allows the model to learn different representations for different macron-vowel combinations.
# Learnable Scaling Factor: The macron_scale parameter allows the model to learn how much influence the macron information should have relative to the standard positional encoding.
# Macron Mask Generation: The get_macron_mask method automatically generates masks for each macron-bearing vowel in the input text. This makes it easy to use the encoder with raw Latin text input.
# Flexible Input Handling: The forward method now accepts a dictionary of macron masks, allowing for batch processing of variable-length sequences.
# Case Insensitivity: The macron detection in get_macron_mask is case-insensitive, handling both uppercase and lowercase macron vowels.

import torch
import math

class EnhancedMacronPositionalEncoding(torch.nn.Module):
    def __init__(self, d_model, max_len=5000):
        super().__init__()
        self.d_model = d_model
        
        # Standard positional encoding
        position = torch.arange(max_len).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2) * (-math.log(10000.0) / d_model))
        pe = torch.zeros(max_len, d_model)
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        self.register_buffer('pe', pe)
        
        # Specific encodings for each macron-bearing vowel
        self.macron_encodings = torch.nn.ParameterDict({
            'a': torch.nn.Parameter(torch.randn(1, d_model)),
            'e': torch.nn.Parameter(torch.randn(1, d_model)),
            'i': torch.nn.Parameter(torch.randn(1, d_model)),
            'o': torch.nn.Parameter(torch.randn(1, d_model)),
            'u': torch.nn.Parameter(torch.randn(1, d_model))
        })
        
        # Learnable scaling factor for macron influence
        self.macron_scale = torch.nn.Parameter(torch.tensor(0.1))

    def forward(self, x, macron_masks):
        """
        x: input tensor of shape (seq_len, batch_size, d_model)
        macron_masks: dict of boolean tensors for each vowel, each of shape (seq_len, batch_size)
        """
        seq_len, batch_size, _ = x.size()
        
        # Add standard positional encoding
        x = x + self.pe[:seq_len]
        
        # Add specific macron encodings for each vowel
        for vowel, mask in macron_masks.items():
            if vowel in self.macron_encodings:
                encoding = self.macron_encodings[vowel]
                x = x + self.macron_scale * encoding * mask.unsqueeze(-1)
        
        return x

    def get_macron_mask(self, text):
        """
        Generate macron masks for a given text.
        text: list of strings, each string is a sequence of Latin words
        returns: dict of boolean tensors for each vowel
        """
        macron_vowels = 'āēīōū'
        regular_vowels = 'aeiou'
        masks = {v: torch.zeros(len(text), len(max(text, key=len))) for v in regular_vowels}
        
        for i, sequence in enumerate(text):
            for j, char in enumerate(sequence):
                if char.lower() in macron_vowels:
                    vowel = regular_vowels[macron_vowels.index(char.lower())]
                    masks[vowel][i, j] = 1
        
        return masks

# Usage example
d_model = 512
max_len = 1000
encoder = EnhancedMacronPositionalEncoding(d_model, max_len)

# Example input
latin_text = [
    "Arma virumque canō, Trōiae quī prīmus ab ōrīs",
    "Ītaliam fātō profugus Lāvīniaque vēnit"
]

# Generate macron masks
macron_masks = encoder.get_macron_mask(latin_text)

# Create a dummy input tensor
seq_len = len(max(latin_text, key=len))
batch_size = len(latin_text)
x = torch.randn(seq_len, batch_size, d_model)

# Apply enhanced macron positional encoding
encoded_x = encoder(x, macron_masks)
