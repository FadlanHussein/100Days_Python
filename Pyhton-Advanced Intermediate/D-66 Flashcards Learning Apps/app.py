import os
import json

DATA_FILE = os.path.join(os.path.dirname(__file__), "Flashcards.json")

def load_flashcards(file_path=DATA_FILE):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_flashcards(flashcards, file_path=DATA_FILE):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(flashcards, file, indent=4)

def add_flashcard():
    question = input("Masukkan pertanyaan: ").strip()
    answer = input("Masukkan jawaban: ").strip()
    if not question or not answer:
        print("Pertanyaan dan jawaban tidak boleh kosong!")
        return

    new_flashcard = {"question": question, "answer": answer, "learned": False}
    flashcards = load_flashcards()
    flashcards.append(new_flashcard)
    save_flashcards(flashcards)
    print("Flashcard berhasil ditambahkan!")

def mark_as_learned():
    flashcards = load_flashcards()
    unlearned = [c for c in flashcards if not c.get("learned", False)]
    
    if not unlearned:
        print("Semua flashcard sudah dipelajari!")
        return

    for card in flashcards:
        if not card.get("learned", False):
            print(f"\nQuestion: {card['question']}")
            mark = input("Apakah kamu sudah mempelajarinya? (y/n): ").strip().lower()
            if mark == "y":
                card["learned"] = True
                save_flashcards(flashcards)
                print("Flashcard berhasil ditandai sebagai dipelajari!")
                return
            else:
                print("Flashcard belum ditandai.")

def review_flashcards():
    flashcards = load_flashcards()
    unlearned_cards = [card for card in flashcards if not card.get("learned", False)]

    if not unlearned_cards:
        print("\nSelamat! Anda sudah mempelajari semua flashcard!")
        return

    print(f"\n--- Review {len(unlearned_cards)} Flashcard yang belum dipelajari ---")
    for i, card in enumerate(unlearned_cards, 1):
        print(f"\n{i}. Question: {card['question']}")
        answer = input("Jawaban: ").strip()
        if answer.lower() == card['answer'].strip().lower():
            print("Benar! Jawaban tepat.")
            card['learned'] = True
            save_flashcards(flashcards)
        else:
            print(f"Salah. Jawaban yang benar: {card['answer']}")

def show_stats():
    flashcards = load_flashcards()
    total_cards = len(flashcards)
    learned_cards = sum(1 for card in flashcards if card.get("learned", False))
    unlearned_cards = total_cards - learned_cards
    percentage = (learned_cards / total_cards * 100) if total_cards > 0 else 0.0

    print("\n--- Statistik Pembelajaran ---")
    print(f"Total Flashcard          : {total_cards}")
    print(f"Flashcard Dipelajari     : {learned_cards}")
    print(f"Flashcard Belum Dipelajari: {unlearned_cards}")
    print(f"Persentase Selesai       : {percentage:.1f}%")

def main():
    while True:
        print("\n=== FLASHCARDS LEARNING APP ===")
        print("1. Review Flashcards")
        print("2. Tambah Flashcard Baru")
        print("3. Tandai Flashcard Sebagai Dipelajari")
        print("4. Lihat Statistik")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == "1":
            review_flashcards()
        elif pilihan == "2":
            add_flashcard()
        elif pilihan == "3":
            mark_as_learned()
        elif pilihan == "4":
            show_stats()
        elif pilihan == "5":
            print("Terima kasih! Sampai jumpa lagi.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()