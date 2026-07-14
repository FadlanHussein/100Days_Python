# Temperature Converter / Body Temperature Analysis

# Step 1: Define conversion function
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return (celsius + 273.15)

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
    
def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius) # <-- Tadi di sini ada bug

def cek_suhu(celsius):
    if celsius >= 38.0: 
        return 'Demam'
    elif 37.0 <= celsius < 38.0: 
        return 'Hangat'
    else: 
        return 'Normal'   

# Step 2: Get user input
def show_menu():
    print("\n==== TEMPLATE TEMPERATURE APPS ====")
    print("1. Input Suhu Tubuh (Celcius)")
    print("2. Cek Demam")
    print("3. Berapa Fahrenheit")
    print("4. Berapa Kelvin")
    print("5. Exit")


# Variabel global untuk mengingat suhu, taruh persis sebelum loop
suhu = 0.0  

while True:
    show_menu()
    choice = input("Enter Number (1-5): ") # <-- Ubah teks jadi 1-5
    
    if choice == "1":
       suhu = float(input("Masukkan Suhu Badan (Celcius): "))
       print(f"Data tersimpan! Suhu saat ini: {suhu} Celcius")
       
    elif choice == "2":
        status_demam = cek_suhu(suhu)
        print(f"Suhu Anda {suhu}C, Status: {status_demam}")
        
    elif choice == "3":
        fahrenheit = celsius_to_fahrenheit(suhu)
        print(f"{suhu} Celcius = {fahrenheit} Fahrenheit")
        
    elif choice == "4":
        kelvin = celsius_to_kelvin(suhu)
        print(f"{suhu} Celcius = {kelvin} Kelvin")
        
    elif choice == "5":
        print("Terima kasih! Keluar dari program.")
        break
    
    else:
        print("Pilihan tidak ada. Masukkan angka 1 sampai 5.")
