#!pip install unsloth
#!pip uninstall unsloth -y && pip install --upgrade --no-cache-dir --no-deps git+https://github.com/unslothai/unsloth.git

from unsloth import FastLanguageModel
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer 

# Load tokenizer

model_name = "unsloth/Phi-3-mini-4k-instruct"  # Adjust based on your model
tokenizer = AutoTokenizer.from_pretrained(model_name)  # Adjust based on your model

max_seq_length = 2048
dtype = None
load_in_4bit = True

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name,
    #"unsloth/Phi-3-mini-4k-instruct",
    max_seq_length=max_seq_length,
    dtype=dtype,
    load_in_4bit=load_in_4bit
)

# Now call get_peft_model with the loaded model
model = FastLanguageModel.get_peft_model(
    model,
    r=128,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj", "embed_tokens", "lm_head"],
    lora_alpha=32,
    lora_dropout=0,
    bias="none",
)

wikipedia_prompt = """위키피디아 기사 ### 제목: {} ### 기사: {}"""
EOS_TOKEN = tokenizer.eos_token

def formatting_prompts_func(examples):
    titles = examples["title"]
    texts = examples["text"]
    outputs = []
    for title, text in zip(titles, texts):
        text = wikipedia_prompt.format(title, text) + EOS_TOKEN
        outputs.append(text)
    return {
        "text": outputs,
    }

from datasets import load_dataset
dataset = load_dataset("wikimedia/wikipedia", "20231101.ko", split="train")
dataset = dataset.train_test_split(train_size=0.01)["train"]
dataset = dataset.map(formatting_prompts_func, batched=True)

from transformers import TrainingArguments
from unsloth import is_bfloat16_supported
from unsloth import UnslothTrainer, UnslothTrainingArguments

trainer = UnslothTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=max_seq_length,
    dataset_num_proc=2,
    args=UnslothTrainingArguments(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=8,
        max_steps=120,
        warmup_steps=10,
        learning_rate=5e-5,
        embedding_learning_rate=1e-5,
        fp16=not is_bfloat16_supported(),
        bf16=is_bfloat16_supported(),
        logging_steps=1,
        optim="adamw_8bit",
        weight_decay=0.01,
        lr_scheduler_type="linear",
        seed=3407,
        output_dir="outputs",
        report_to="none",
    ),
)

trainer_stats = trainer.train()

from datasets import load_dataset
alpaca_dataset = load_dataset("FreedomIntelligence/alpaca-gpt4-korean", split = "train")

print(alpaca_dataset[0])

alpaca_prompt = """다음은 작업을 설명하는 명령입니다. 요청을 적절하게 완료하는 응답을 작성하세요. ### 지침: {} ### 응답: {}"""
EOS_TOKEN = tokenizer.eos_token

def formatting_prompts_func(conversations):
    texts = []
    conversations = conversations["conversations"]
    for convo in conversations:
        text = alpaca_prompt.format(convo[0]["value"], convo[1]["value"]) + EOS_TOKEN
        texts.append(text)
    return {
        "text" : texts,
    }

alpaca_dataset = alpaca_dataset.map(formatting_prompts_func, batched = True)

trainer = UnslothTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = alpaca_dataset,
    dataset_text_field = "text",
    max_seq_length = max_seq_length,
    dataset_num_proc = 8,
    args = UnslothTrainingArguments(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 8,
        max_steps = 120,
        warmup_steps = 10,
        learning_rate = 5e-5,
        embedding_learning_rate = 1e-5,
        fp16 = not is_bfloat16_supported(),
        bf16 = is_bfloat16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.00,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
    ),
)

trainer_stats = trainer.train()

FastLanguageModel.for_inference(model)

inputs = tokenizer(
    [
        alpaca_prompt.format(
            "피보나치 수열을 계속하세요: 1, 1, 2, 3, 5, 8,",
            "",
        )
    ],
    return_tensors = "pt"
).to("cuda")

outputs = model.generate(**inputs, max_new_tokens = 64, use_cache = True)
tokenizer.batch_decode(outputs)

inputs = tokenizer(
    [
        alpaca_prompt.format(
            "한국음악은 어떤가요?",
            "",
        )
    ],
    return_tensors = "pt"
).to("cuda")

from transformers import TextStreamer
text_streamer = TextStreamer(tokenizer)
_ = model.generate(**inputs, streamer = text_streamer, max_new_tokens = 1024, repetition_penalty = 0.1)

model.save_pretrained("lora_model_v2")
tokenizer.save_pretrained("lora_model_v2")
