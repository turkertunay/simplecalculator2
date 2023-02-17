n_1 = input("birinci sayıyı girin: ")

n_2 = input("ikinci sayıyı girin: ")
islem = input("işlemi girin: ")

if islem == "+":
    sonuc = float(n_1) + float(n_2)
if islem == "-":
    sonuc = float(n_1) - float(n_2)
if islem == "*":
    sonuc = float(n_1) * float(n_2)
if islem == "/":
    sonuc = float(n_1) / float(n_2)

if islem != "+" and islem != "-" and islem != "*" and islem != "/":
    sonuc = ("hatalı işlem girişi yaptınız!")


print(sonuc)

