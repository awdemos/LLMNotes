from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "win10/EVA-QwQ-32B-Coder-Preview"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = "Write a Python function to calculate the factorial of a number"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_length=200)
generated_code = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_code)
