use rig::{completion::Prompt, providers::openai};
use std::io::{self, Write};

#[tokio::main]
async fn main() -> Result<(), anyhow::Error> {
    // Initialize the OpenAI client using environment variables
    let openai_client = openai::Client::from_env();

    // Create a GPT-4 model instance
    let gpt4 = openai_client.model("gpt-4").build();

    println!("Welcome to the Rig Chatbot!");
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

        // Send the user's input to GPT-4 and await the response
        let response = gpt4.prompt(input).await?;

        println!("Chatbot: {}", response);
    }

    println!("Thank you for using the Rig Chatbot!");

    Ok(())
}
