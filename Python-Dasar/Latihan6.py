# #%% Kasus 1
# my_dict = {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": "value3"
# }
# 
# contact = {
#     "name": "Fadlan Hussein Al Utsman",
#     "phone": "081316436538",
#     "email": "husseinfadlan09@gmail.com"
# }
# 
# print(contact.get("email"))
# contact["phone"] = "081316436538"
# print(contact)
# contact["addres"] = "Jakarta Greater"
# print(contact)
# del contact["email"]
# print(contact)

#%% kasus 2
Chelsea = [
    ["Petr Chech"],
    ["Branislav Ivanovic"],
    ["John Terry"],
    ["Ashley Young"],
    ["Florient Malouda"],
    ["Frank Lampard"],
    ["Cesc Fabregas"],
    ["Eden Hazard"],
    ["William"],
    ["Diego Costa"],
    ["Alvaro Morata"]
]
#print (f"Set Penambahan Pemain")
#Chelsea.append("Willy Caballero")
#print(Chelsea)
#print(f"Set Pergantian Pemain")
#Chelsea.remove(["Ashley Young"])
Pemain_ditarik = Chelsea.pop(3)
Pemain_pengganti = ["Cesar Azpilicueta"]
Chelsea.insert(3, ["Cesar Azpilicueta"])
Pemain_dihukum = Chelsea.pop(10)
print(f"Pemain yang ditarik keluar adalah: {Pemain_ditarik}")
print(f"Pemain yang dihukum adalah: {Pemain_dihukum}")
print(f"Pemain yang diganti adalah:{Pemain_pengganti}")

#Set Tugas kedua
print(f"Set Tugas Kedua")
Pemain_undangan = ["Didier Drogba"]
Chelsea.extend(Pemain_undangan)
print(f"Pemain undangan spesial: {Pemain_undangan}")
posisi_terry = Chelsea.index(["John Terry"])
print(f"Jhon Terry berada di indeks ke: {posisi_terry}")
print(f"Jumlah pemain Chelsea yang ada dilapangan: {len(Chelsea)}")
Chelsea[0] = ["Petr Cech"]
print(Chelsea)
del Chelsea[-1]
print("Skuad Final Setelah Pemotongan", Chelsea)

#Set Tugas Ketiga

print(f"Set Tugas Ketiga")
barisan_pertahanan = Chelsea[0:5]
print(barisan_pertahanan)
cek_terry = ["John Terry"] in Chelsea
print("Apakah John Terry ada?", cek_terry)
cek_young = ["Ashley Young"] in Chelsea
print("Apakah Ashley Young ada?", cek_young)
skuad_rapi = sorted(Chelsea)
print(skuad_rapi)