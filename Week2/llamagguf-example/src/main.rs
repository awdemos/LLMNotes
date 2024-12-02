use actix_web::{web, App, HttpServer, HttpResponse, Error};
use futures::{stream::{Stream}, channel::mpsc::UnboundedReceiver};
use serde::{Deserialize, Serialize};
use std::sync::Mutex;
use std::collections::VecDeque;
use std::pin::Pin;
use std::task::{Context, Poll};


#[derive(Clone, Serialize, Deserialize)]
struct ChatMessage {
    role: String,
    content: String,
}

#[derive(Deserialize)]
struct ChatRequest {
    message: String,
}

struct Chatbot {
    model: Llama,
    conversation_history: VecDeque<ChatMessage>,
    max_history: usize,
}

impl Chatbot {
    let config = LlamaConfig {
        model_path: model_path.to_string(), // Use the passed parameter here
        context_size: 2048,
        max_tokens: 256,
        temperature: 0.7,
        ..Default::default()
    };

    Ok(bot) => bot,
    Err(e) => {
        eprintln!("Failed to initialize chatbot: {}", e);
        return Ok(());
    }
};

    fn generate_prompt(&self, user_message: &str) -> String {
        let mut prompt = String::new();
        for message in &self.conversation_history {
            prompt.push_str(&format!("{}: {}\n", message.role, message.content));
        }
        prompt.push_str(&format!("User: {}\nAssistant:", user_message));
        prompt
    }

    fn process_message(&mut self, message: &str) -> impl Stream<Item = Result<String, Box<dyn std::error::Error + Send>>> {
        let (tx, rx) = futures::channel::mpsc::unbounded();
        let prompt = self.generate_prompt(message);
        let tx_clone = tx.clone();

        std::thread::spawn(move || {
            let response = "This is a sample response broken into chunks.";
            for chunk in response.split_whitespace() {
                std::thread::sleep(std::time::Duration::from_millis(100));
                if tx_clone.unbounded_send(Ok(format!("{} ", chunk))).is_err() {
                    break;
                }
            }
        });

        StreamWrapper { rx }
    }

struct StreamWrapper {
    rx: UnboundedReceiver<Result<String, Box<dyn std::error::Error + Send>>>,
}

impl Stream for StreamWrapper {
    type Item = Result<String, Box<dyn std::error::Error + Send>>;

    fn poll_next(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Option<Self::Item>> {
        Pin::new(&mut self.rx).poll_next(cx)
    }
}

type WebChatbot = web::Data<Mutex<Chatbot>>;

async fn chat_stream(
    chatbot: WebChatbot,
    request: web::Json<ChatRequest>,
) -> Result<HttpResponse, Error> {
    let mut chatbot = chatbot.lock().unwrap();
    let stream = chatbot.process_message(&request.message)
        .map(|result| match result {
            Ok(text) => Ok(web::Bytes::from(text)),
            Err(e) => Err(actix_web::error::ErrorInternalServerError(e.to_string())),
        });

    Ok(HttpResponse::Ok()
        .content_type("text/event-stream")
        .streaming(stream))
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let chatbot = match Chatbot::new() {
        Ok(bot) => bot,
        Err(e) => {
            eprintln!("Failed to initialize chatbot: {}", e);
            return Ok(());
        }
    };
    
    let chatbot_data = web::Data::new(Mutex::new(chatbot));
    
    println!("Starting chatbot server on http://127.0.0.1:8080");
    
    HttpServer::new(move || {
        App::new()
            .app_data(chatbot_data.clone())
            .route("/chat/stream", web::post().to(chat_stream))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}
