use rig::{completion::Prompt, providers::perplexity};

#[tokio::main]
async fn main() -> Result<(), anyhow::Error> {
    // Initialize the Perplexity client with your API key
    let perplexity = perplexity::Client::new("your_key");

    // Create an agent using a Perplexity model
    let comedian_agent = perplexity
        .agent("pplx-7b-chat")  // Use an appropriate Perplexity model
        .preamble("You are a comedian here to entertain the user using humour and jokes.")
        .temperature(0.9)
        .build();

    // Use the agent to generate a response
    let response = comedian_agent.prompt("Entertain me!")
        .await
        .expect("Failed to prompt the agent");

    println!("Agent's response: {}", response);

    Ok(())
}
