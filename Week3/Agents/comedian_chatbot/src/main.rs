use rig::providers::perplexity;
use rig::completion::CompletionModel;
use std::io::{self, Write};

const SYSTEM_PROMPT: &str = r#"You are an advanced AI system with multiple expert agents, each specializing in different areas of knowledge. When presented with a query, internally process the following steps:

1. Identify relevant expert agents for the task.
2. Generate multiple responses to the query.
3. Evaluate and score all responses based on quality, relevance, and accuracy.
4. Rank the responses based on their scores.
5. Select the highest-scoring response.

Present only the best response to the user, without mentioning the internal process, scores, or other generated responses. Ensure the answer is comprehensive and directly addresses the query.

Query: {}"#;

#[tokio::main]
async fn main() -> Result<(), anyhow::Error> {
    // Initialize the Perplexity client with your API key
    let client = perplexity::Client::new("your_key");

    // Create a model instance
    let model = client.completion_model("llama-3.1-sonar-small-128k-online");

    println!("Welcome to the Perplexity Chatbot!");
    println!("Type 'exit' to quit the program.");

    loop {
        print!("You: ");
        io::stdout().flush()?;

        let mut input = String::new();
        io::stdin().read_line(&mut input)?;

        let input = input.trim();

        if input.to_lowercase() == "exit" {
            break;
        }

        // Create a completion request with the system prompt
        let prompt = SYSTEM_PROMPT.replace("{}", input);
        let request = model.completion_request(&prompt)
            .max_tokens(1024)
            .temperature(0.7);

        // Send the request and await the response
        let response = request.send().await?;

        // Access the response content
        if let Some(choice) = response.raw_response.choices.first() {
            println!("Chatbot: {}", choice.message.content);
        } else {
            println!("Chatbot: No response generated.");
        }
    }

    println!("Thank you for using the Perplexity Chatbot!");

    Ok(())
}

