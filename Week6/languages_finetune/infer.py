from unsloth import FastLanguageModel
import torch

# Set up parameters
model_name = "lora_model"  # Path to your saved model
max_seq_length = 2048
dtype = None  # None for auto detection
load_in_4bit = True

# Load the model and tokenizer
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name,
    max_seq_length=max_seq_length,
    dtype=dtype,
    load_in_4bit=load_in_4bit
)

# Enable faster inference
FastLanguageModel.for_inference(model)

# Prepare input for generation
alpaca_prompt = """Below is an instruction that describes a task. Write a response that appropriately completes the request. ### Instruction: {} ### Response: {}"""
input_text = "How to talk in Korean?"

inputs = tokenizer(
    [alpaca_prompt.format(input_text, "")],
    return_tensors="pt"
).to("cuda")

# Generate text
from transformers import TextStreamer
text_streamer = TextStreamer(tokenizer)
_ = model.generate(
    **inputs, 
    streamer=text_streamer, 
    max_new_tokens=128, 
    repetition_penalty=0.1
)

