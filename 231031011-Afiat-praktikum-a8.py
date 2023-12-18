password = ["25", "12", "04"]
percobaan = 3
a = True

while a and percobaan > 0:
    masukan = input("masukkan password: ")
    if masukan == password[0]:
        percobaan_lapisan2 = 3  
        masukkan2 = input("masukkan password ke-2: ")
        
        while percobaan_lapisan2 > 0:
            if masukkan2 == password[1]:
                percobaan_lapisan3 = 3  
                masukkan3 = input("masukkan password ke-3: ")
                
                while percobaan_lapisan3 > 0:
                    if masukkan3 == password[2]:
                        print("Selamat,anda berhasil login!")
                        a = False
                        break
                    else:
                        print("Password yang Anda masukkan salah! Harap coba lagi.")
                        print(f'Percobaan Anda sisa {percobaan_lapisan3 } kali') 
                        percobaan_lapisan3 -= 1
                        masukkan3 = input("masukkan password ke-3:")
                break
            else:
                print("Password yang Anda masukkan salah! Harap coba lagi.")
                print(f'Percobaan Anda sisa {percobaan_lapisan2 } kali')
                percobaan_lapisan2 -= 1
                masukkan2 = input("masukkan password ke-2:")
        break
    else:
        print("Password yang Anda masukkan salah! Harap coba lagi.")
        print(f'Percobaan Anda sisa {percobaan - 1} kali')
        percobaan -= 1

if percobaan == 0:
    print("Anda dibanned!")