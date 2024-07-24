from openai import OpenAI

# Configuración de OpenAI (apuntando al servidor local)
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# Parámetros de conversación
conversation = []
# Leer el system prompt desde el archivo
with open("system_prompt.txt", "r", encoding="utf-8") as f: 
    system_prompt = f.read()

def chat_with_gemma():
    conversation.append({"role": "system", "content": system_prompt})

    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            break

        conversation.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="lmstudio-ai/gemma-2b-it-GGUF",  # Reemplaza con el nombre exacto de tu modelo en LM Studio
            messages=conversation,
            temperature=0.7, 
            max_tokens=150  
        )

        gemma_response = response.choices[0].message.content
        print("Gemma:", gemma_response)
        conversation.append({"role": "assistant", "content": gemma_response})

if __name__ == "__main__":
    chat_with_gemma()
