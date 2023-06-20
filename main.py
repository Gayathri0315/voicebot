from chat import collect_messages_text
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def main():
    return FileResponse("index.html")

# @app.post("/chat")
# async def chat(message: Message):
#     user_message = message.content
#     response = collect_messages_text(user_message)

#     return {"message": response}


@app.post("/process_voice")
async def process_voice(voice_input: dict):
    text = voice_input.get('input')
    # Process the voice input as needed
    print("Voice input:", text)
    response = collect_messages_text(text)
    print(response)
    return response
