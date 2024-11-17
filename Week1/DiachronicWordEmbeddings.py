class DiachronicEmbedding(torch.nn.Module):
    def __init__(self, vocab_size, embed_size, num_time_periods):
        super().__init__()
        self.static_embeddings = torch.nn.Embedding(vocab_size, embed_size)
        self.temporal_embeddings = torch.nn.Parameter(torch.randn(num_time_periods, vocab_size, embed_size))

    def forward(self, input_ids, time_period):
        static_embeds = self.static_embeddings(input_ids)
        temporal_embeds = self.temporal_embeddings[time_period, input_ids]
        return static_embeds + temporal_embeds
