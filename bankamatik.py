eren = {
    "name": "Eren",
    "kartNum": "4444 5555 6666",
    "bakiye": 10000
}

yy = {
    "name": "yy",
    "kartNum": "1111 4444 5555",
    "bakiye": 10000
}

def paracek(mik, bakiye):
    bakiye = bakiye - mik
    print(f"Şu anki bakiye {bakiye}")
    return bakiye

def parayatir(mik, bakiye):
    bakiye = bakiye + mik
    print(f"Şu anki bakiye {bakiye}")
    return bakiye

while True:
    kartisim = input("Kart ismini girin: ")
    
    # Kullanıcının girdisine dayalı olarak hangi sözlüğün kullanılacağını belirle
    if kartisim == "eren":
        kullanici = eren
    elif kartisim == "yy":
        kullanici = yy
    else:
        print("Hatalı kart ismi, tekrar deneyin.")
        continue
    
    kulkart = input("Kart numarası girin: ")
    
    if kulkart == kullanici["kartNum"]:
        print(f"""
        [1] Para Çek
        [2] Para Yatır
        [3] Bakiye sorgula
        
        İsim:           {kullanici['name']}
        KartNum:        {kullanici['kartNum']}
        Hesap Bakiyesi: {kullanici['bakiye']}
        
        [7] Çıkış
        [8] Program Kapat
        """)
        
        cevap = int(input("> "))
        
        if cevap == 1:
            miktar = int(input("Miktar> "))
            kullanici["bakiye"] = paracek(mik=miktar, bakiye=kullanici["bakiye"])
        
        elif cevap == 2:
            miktar = int(input("Miktar> "))
            kullanici["bakiye"] = parayatir(mik=miktar, bakiye=kullanici["bakiye"])
        
        elif cevap == 3:
            print(f"Şu anki bakiye: {kullanici['bakiye']}")
        
        elif cevap == 7:
            continue
        elif cevap == 8:
            exit()