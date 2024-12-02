from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "brucethemoose/Yi-34B-200K-RPMerge"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

system_message = "You are a helpful AI assistant. Provide accurate and concise answers to user queries."

def generate_response(user_input):
    prompt = f"SYSTEM: {system_message}\nUSER: {user_input}\nASSISTANT:"
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    
    outputs = model.generate(
        inputs,
        max_length=2048,
        do_sample=True,
        temperature=1,
        top_p=1,
        top_k=0,
        repetition_penalty=1.1,
        mirostat_mode=0,
        mirostat_tau=5,
        mirostat_eta=0.1
    )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.split("ASSISTANT:")[-1].strip()

print("Chatbot initialized. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    
    response = generate_response(user_input)
    print("Chatbot:", response)
