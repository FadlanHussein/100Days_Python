import time
import random

# ============================================================
# DATA TIM
# ============================================================
CHELSEA_DATA = {
    "match_player": [
        "Petr Cech",
        "Branislav Ivanovic",
        "John Terry",
        "Bosingwa",
        "Ashley Cole",
        "Franks Lampard",
        "Michael Essien",
        "Salomon Kalou",
        "Arjen Robben",
        "Eden Hazard",
        "Fernando Torres",
    ],
    "subtitute_player": [
        "Willy Cabalore",
        "Garry Cahill",
        "John Mikel Obi",
        "Ramires",
        "Florent Malouda",
        "Cesc Fabregas",
        "Daniel Sturridge",
        "Didier Drogba",
    ],
    "match_coach": ["Carlo Ancelotti"]
}

ARSENAL_DATA = {
    "match_player": [
        "Lukas Podolski",
        "Mathieu Debuchy",
        "Per Mertesacker",
        "Laurent Koscielny",
        "Nacho Monreal",
        "Mathieu Flamini",
        "Alex Iwobi",
        "Jack Wilshere",
        "Santi Carzola",
        "Alexis Sanchez",
        "Theo Walcott",
    ],
    "subtitute_player": [
        "Emiliano Martinez",
        "Shkodran Mustafi",
        "Calum Chambers",
        "Francis Coquelin",
        "Kevin GroBkreutz",
        "Podolski",
        "Timo Horn",
    ],
    "match_coach": ["Arsene Wenger"]
}

# ============================================================
# FUNGSI MENU
# ============================================================
def show_menu():
    print("\n ### Football Squad Manager ###")
    print("1. Untuk memilih tim")
    print("2. Melihat skuat utama yang dipilih")
    print("3. Melihat skuat cadangan")
    print("4. Pergantian pemain")
    print("5. Check bangku cadangan yang masih tersedia")
    print("6. Menjalankan Match otomatis")
    print("7. Skor Akhir")
    print("8. Kembali ke Menu Tim")
    print("9. Keluar")

# Fungsi untuk memilih tim dan mengembalikan salinan data baru
def name_team():
    while True:
        input_user = input("Masukkan nama team (Chelsea / Arsenal): ").strip().title()
        # .strip() = menghapus spasi di awal/akhir input
        # .title() = huruf pertama tiap kata menjadi kapital
        if input_user == "Chelsea":
            print("Tim Chelsea berhasil dipilih")
            # Kembalikan SALINAN data agar data asli tidak berubah tiap pertandingan
            import copy
            return copy.deepcopy(CHELSEA_DATA), "Chelsea"
        elif input_user == "Arsenal":
            print("Tim Arsenal berhasil dipilih")
            import copy
            return copy.deepcopy(ARSENAL_DATA), "Arsenal"
        else:
            print("Tim tidak ditemukan. Silahkan pilih tim yang ada (Chelsea / Arsenal)")

# ============================================================
# VARIABEL GLOBAL STATE
# ============================================================
tim_aktif = None
nama_tim_aktif = ""
skor_terakhir_kita = 0
skor_terakhir_lawan = 0
lawan_terakhir = ""
sudah_pernah_tanding = False

# ============================================================
# LOOP UTAMA
# ============================================================
show_menu()
while True:
    choice = input("\nSilahkan pilih menu: ").strip()

    # Validasi input
    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("\nPilihan tidak valid. Silakan ketik angka 1-9.")
        show_menu()
        continue

    # --- Menu 9: Keluar ---
    if choice == "9":
        print("Keluar dari permainan!!!")
        break

    # --- Menu 1: Pilih Tim ---
    elif choice == "1":
        tim_aktif, nama_tim_aktif = name_team()

    # --- Validasi tim harus sudah dipilih untuk menu 2-8 ---
    elif tim_aktif is None:
        print("[Peringatan] Silahkan pilih tim terlebih dahulu dengan ketik 1")

    # --- Menu 2: Skuat Utama ---
    elif choice == "2":
        print(f"\n### Skuad Utama {nama_tim_aktif} ###")
        for i, pemain in enumerate(tim_aktif["match_player"], 1):
            print(f"  {i}. {pemain}")
        print(f"  Pelatih: {tim_aktif['match_coach'][0]}")

    # --- Menu 3: Skuat Cadangan ---
    elif choice == "3":
        print(f"\nBerikut ini skuat cadangan {nama_tim_aktif}:")
        for i, pemain in enumerate(tim_aktif["subtitute_player"], 1):
            print(f"  {i}. {pemain}")

    # --- Menu 4: Pergantian Pemain ---
    elif choice == "4":
        print(f"\nSkuad utama: {', '.join(tim_aktif['match_player'])}")
        print(f"Skuad cadangan: {', '.join(tim_aktif['subtitute_player'])}")
        pemain_keluar = input("\nNama pemain yang keluar dari skuad: ").strip().title()
        if pemain_keluar not in tim_aktif["match_player"]:
            print(f"[PERINGATAN] '{pemain_keluar}' tidak ditemukan di skuad utama.")
        else:
            pemain_masuk = input("Masukkan nama pemain pengganti dari cadangan: ").strip().title()
            if pemain_masuk not in tim_aktif["subtitute_player"]:
                print(f"[PERINGATAN] '{pemain_masuk}' tidak ditemukan di skuad cadangan.")
            else:
                # Lakukan pergantian
                tim_aktif["match_player"].remove(pemain_keluar)
                tim_aktif["subtitute_player"].remove(pemain_masuk)
                tim_aktif["match_player"].append(pemain_masuk)
                tim_aktif["subtitute_player"].append(pemain_keluar)
                print(f"[SUKSES] {pemain_masuk} masuk ke skuad utama menggantikan {pemain_keluar}")

    # --- Menu 5: Cek Bangku Cadangan ---
    elif choice == "5":
        jumlah_pergantian_maksimal = 3
        jumlah_cadangan_sekarang = len(tim_aktif["subtitute_player"])
        slot_tersisa = max(0, jumlah_cadangan_sekarang - jumlah_pergantian_maksimal)
        print(f"\n=== Ketersediaan Bangku Cadangan ===")
        print(f"Jumlah pemain cadangan saat ini : {jumlah_cadangan_sekarang} pemain")
        print(f"Slot pergantian yang tersedia   : {slot_tersisa} pergantian")

    # --- Menu 6: Simulasi Match ---
    elif choice == "6":
        # Daftar tim lawan
        klub_liga_inggris = [
            "Manchester United", "Liverpool", "Tottenham Hotspur",
            "Leicester City", "Everton", "West Ham United",
            "Southampton", "Stoke City", "Newcastle United",
            "Sunderland", "Crystal Palace", "Watford",
            "West Bromwich Albion", "Swansea City", "Hull City",
            "Bournemouth", "Burnley", "Middlesbrough",
        ]
        # Pastikan tim aktif tidak melawan dirinya sendiri
        if nama_tim_aktif == "Chelsea":
            klub_liga_inggris.append("Arsenal")
        else:
            klub_liga_inggris.append("Chelsea")

        komputer_klub = random.choice(klub_liga_inggris)
        print(f"\n Pertandingan dimulai antara {nama_tim_aktif} vs {komputer_klub}\n")
        print("Match dimulai dalam... 3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1  KICK OFF!\n")
        time.sleep(1)

        skor_tim_aktif = 0
        skor_komputer = 0

        # Tentukan menit terjadinya gol dan pergantian pemain secara acak
        menit_mencetak_gol = random.randint(1, 89)
        menit_kemasukan = random.randint(1, 89)
        # Pastikan dua menit gol tidak sama
        while menit_kemasukan == menit_mencetak_gol:
            menit_kemasukan = random.randint(1, 89)

        menit_pergantian_pemain = sorted(random.sample(range(20, 89), 3))

        # Rencanakan pergantian pemain secara acak
        rencana = []
        temp_match = list(tim_aktif["match_player"])
        temp_sub = list(tim_aktif["subtitute_player"])
        for m in menit_pergantian_pemain:
            if temp_match and temp_sub:
                p_keluar = random.choice(temp_match)
                p_masuk = random.choice(temp_sub)
                rencana.append({"menit": m, "keluar": p_keluar, "masuk": p_masuk})
                temp_match.remove(p_keluar)
                temp_sub.remove(p_masuk)

        # Jalankan simulasi per menit
        for menit in range(1, 91):
            time.sleep(0.05)

            if menit % 10 == 0:
                print(f"Menit ke-{menit}...")

            if menit == menit_mencetak_gol:
                pencetak_gol = random.choice(tim_aktif["match_player"])
                skor_tim_aktif += 1
                print(f"\nGOOOLLLL !!!")
                print(f"Pemain {pencetak_gol} berhasil mencetak gol untuk {nama_tim_aktif}!")
                print(f"Skor sementara: {nama_tim_aktif} {skor_tim_aktif} - {skor_komputer} {komputer_klub}")

            elif menit == menit_kemasukan:
                skor_komputer += 1
                print(f"\nGOOOLLLL !!!")
                print(f"Gol untuk lawan! {komputer_klub} berhasil mencetak gol.")
                print(f"Skor sementara: {nama_tim_aktif} {skor_tim_aktif} - {skor_komputer} {komputer_klub}")

            for r in rencana:
                if r["menit"] == menit:
                    pk = r["keluar"]
                    pm = r["masuk"]
                    if pk in tim_aktif["match_player"] and pm in tim_aktif["subtitute_player"]:
                        tim_aktif["match_player"].remove(pk)
                        tim_aktif["subtitute_player"].remove(pm)
                        tim_aktif["match_player"].append(pm)
                        tim_aktif["subtitute_player"].append(pk)
                        print(f"\n[PERGANTIAN PEMAIN] Menit {menit}: {pk} -> {pm}")

        print("\n" + "=" * 35)
        print("           FINAL SCORE")
        print("=" * 35)
        print(f"  {nama_tim_aktif:<20} : {skor_tim_aktif}")
        print(f"  {komputer_klub:<20} : {skor_komputer}")
        print("=" * 35)

        if skor_tim_aktif > skor_komputer:
            print("\nSelamat! Tim Anda menang!")
        elif skor_tim_aktif < skor_komputer:
            print("\nTim Anda kalah.")
        else:
            print("\nPertandingan berakhir seri.")

        time.sleep(2)

        # Simpan skor ke variabel global
        skor_terakhir_kita = skor_tim_aktif
        skor_terakhir_lawan = skor_komputer
        lawan_terakhir = komputer_klub
        sudah_pernah_tanding = True

    # --- Menu 7: Skor Akhir ---
    elif choice == "7":
        if sudah_pernah_tanding:
            print("\n=== Skor Akhir Pertandingan Terakhir ===")
            print(f"  {nama_tim_aktif} {skor_terakhir_kita} - {skor_terakhir_lawan} {lawan_terakhir}")
            if skor_terakhir_kita > skor_terakhir_lawan:
                print(f"  Status: {nama_tim_aktif} Menang!")
            elif skor_terakhir_kita < skor_terakhir_lawan:
                print(f"  Status: {nama_tim_aktif} Kalah.")
            else:
                print("  Status: Seri.")
        else:
            print("\n[PERINGATAN] Belum ada pertandingan. Jalankan match dulu dengan ketik 6.")

    # --- Menu 8: Kembali ke Menu Tim ---
    elif choice == "8":
        tim_aktif = None
        nama_tim_aktif = ""
        print("\nBerhasil kembali ke Menu Tim. Silakan pilih tim baru dengan ketik 1.")
        show_menu()