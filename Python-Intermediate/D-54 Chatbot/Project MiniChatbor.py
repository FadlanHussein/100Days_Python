response = {
    "hai": "Halo Juga!",
    "siapa kamu": "Saya adalah chatbot.",
    "bagaimana kabarmu": "Saya baik-baik saja.",
    "apa yang bisa kamu lakukan": "Saya bisa menjawab pertanyaan sederhana.",
}

def get_response(user_input):
    user_input = user_input.lower()
    if "hai" in user_input or "hello" in user_input:
        return "Hai juga! Ada yang bisa saya bantu?"
    elif "siapa kamu" in user_input:
        return "Saya adalah chatbot."
    elif "bagaimana kabarmu" in user_input:
        return "Saya baik-baik saja."
    elif "apa yang bisa kamu lakukan" in user_input:
        return "Saya bisa menjawab pertanyaan sederhana."
    else:
        return "Saya masih dalam tahap perkembangan, mohon maaf."

def chatbot():
    print("Hello! Saya adalah chatbot, Ketike Exit untuk mengakhiri pesan.")
    while True:
        user_input = input("Anda : ").lower()
        if user_input == "exit":
            print("Chatbot :Sampai jumpa!")
            break
        elif user_input in response:
            print(f"Chatbot: {response[user_input]}")
        else:
            print("Chatbot: Saya masih dalam tahap perkembangan, mohon maaf.")

if __name__ == "__main__":
    chatbot()
