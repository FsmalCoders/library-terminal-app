import sqlite3 as sql
from os import system as sys
from time import sleep

db = sql.connect('database.db')

cur = db.cursor()

## "Books" ADINDA BİR TABLO OLUŞTURULDU
cur.execute("CREATE TABLE IF NOT EXISTS Books (Book TEXT, Author TEXT)")

## MENÜ DEĞİŞKENLERİ
mainMenu = """
[Ana Sayfa]

[0] Kitap Ekle
[1] Kitap Çıkar
[2] Kitap Ara
[3] Yazar Ara
[4] Kitapları Listele
[Q] Programı Kapat
"""

## PROGRAM SONSUZ DÖNGÜYE ALINDI
while True:

    sys('cls') ## TERMİNAL TEMİZLENİR

    print(mainMenu) ## ANA MENÜ EKRANA YAZILIR
    
    choice_mainMenu = str(input('İşlem seçiniz: ')).strip() ## İŞLEM SEÇİLİR

    ## KİTAP EKLE
    if choice_mainMenu == '0':

        sys('cls')
        
        print('\n[Kitap Ekle]')

        try:

            input_bookName = str(input('\nKitabın Adı: ')) ## EKLENMEK İSTENEN KİTABIN ADI

            input_authorName = str(input('\nYazarın Adı: ')) ## EKLENMEK İSTENEN KİTABIN YAZARI

            cur.execute(f"INSERT INTO Books VALUES ('{input_bookName}', '{input_authorName}')")  ## KİTAP VERİ TABANINA KAYDEDİLİR

            db.commit()

            print('\nKayıt başarıyla gerçekleşmiştir.')

            sleep(1)

        except sql.OperationalError: ## 'sqlite3.OperationalError' SYNTAX HATASI YAKALANIR

            print('\nGeçersiz karakter.')
            
            sleep(1.5)


    ## KİTAP ÇIKAR
    elif choice_mainMenu == '1':

        sys('cls')
        
        print('\n[Kitap Çıkar]')

        cur.execute("SELECT * FROM Books") ## TÜM KİTAPLARI VERİ TABANINDAN ÇEKER

        books = cur.fetchall() ## TÜM VERİLER BİR DEĞİŞKENE ATANIR

        if len(books) > 0: ## HERHANGİ BİR VERİ VAR MI KONTROLU YAPILIR, LİSTENİN ELEMAN SAYISI SIFIRDAN FAZLAYSA VERİ VARDIR

            for i in range(0, len(books)): ## TÜM VERİLER EKRANA YAZILIR
                print(f'\nSıra No: {i}\nKitap: {books[i][0]}\nYazar: {books[i][1]}')

            input_bookSerialNo = int(input('\nSilmek İstediğiniz Kıtabın Sıra Numarası: '))

            try:

                bookToBeDeleted = { ## SİLİNMEK İSTENEN KİTAP SÖZLÜK FORMATINDA OLUŞTURULUR
                    'bookName': books[input_bookSerialNo][0],
                    'authorName': books[input_bookSerialNo][1]
                }
            
            except IndexError: ## 'IndexError' HATASI YAKALANIR, KULLANICI KİTAP SAYISINDAN FAZLA BİR 'SIRA NO' DEĞERİ GİRERSE HATA VERİR

                print('\nGeçersiz Sıra No.')

                sleep(1.5)

                continue

            cur.execute(f"DELETE FROM Books WHERE Book='{bookToBeDeleted['bookName']}' AND Author='{bookToBeDeleted['authorName']}'") ## KİTAP SİLİNİR

            db.commit()

            print('\nKitap başarıyla silindi.')

            sleep(1.5)

        else:
            print('\nHerhangi bir kitap bulunamadı.')

            sleep(1.5)


    ## KİTAP ARA
    elif choice_mainMenu == '2':
        
        sys('cls')
        
        print('\n[Kitap Ara]')

        input_bookName = str(input('\nAramak istediğiniz kitabın adı: '))

        cur.execute(f"SELECT * FROM Books WHERE Book='{input_bookName}'") ## GİRİLEN INPUTA GÖRE KİTAP ARANIR

        searchedBooks = cur.fetchall() ## GİRİLEN İNPUTLA EŞLEŞEN KİTAP İSİMLERİ BİR DEĞİŞKENE ATANIR

        if len(searchedBooks) > 0: ## HERHANGİ BİR VERİ VAR MI KONTROLU YAPILIR, LİSTENİN ELEMAN SAYISI SIFIRDAN FAZLAYSA VERİ VARDIR

            print('\nSonuçlar:')

            for i in range(0, len(searchedBooks)): ## TÜM VERİLER EKRANA YAZILIR
                print(f'\nSıra No: {i}\nKitap: {searchedBooks[i][0]}\nYazar: {searchedBooks[i][1]}')

            input("\nAna menüye dönmek için 'Enter'a bas: ")

        else:

            print(f"\n'{input_bookName}' isimli bir kitap bulunamadı.")

            sleep(1.5)


    ## YAZAR ARA
    elif choice_mainMenu == '3':
        
        sys('cls')
        
        print('\n[Yazar Ara]')

        input_authorName = str(input('\nAramak istediğiniz yazarın adı: '))

        cur.execute(f"SELECT * FROM Books WHERE Author='{input_authorName}'") ## GİRİLEN INPUTA GÖRE YAZAR ARANIR

        searchedBooks = cur.fetchall() ## GİRİLEN İNPUTLA EŞLEŞEN YAZARLAR BİR DEĞİŞKENE ATANIR

        if len(searchedBooks) > 0: ## HERHANGİ BİR VERİ VAR MI KONTROLU YAPILIR, LİSTENİN ELEMAN SAYISI SIFIRDAN FAZLAYSA VERİ VARDIR

            print('\nSonuçlar:')

            for i in range(0, len(searchedBooks)): ## TÜM VERİLER EKRANA YAZILIR
                print(f'\nSıra No: {i}\nKitap: {searchedBooks[i][0]}\nYazar: {searchedBooks[i][1]}')

            input("\nAna menüye dönmek için 'Enter'a bas: ")

        else:

            print(f"\n'{input_authorName}' isimli bir yazar bulunamadı.")

            sleep(1.5)


    ## KİTAPLARI LİSTELE
    elif choice_mainMenu == '4':

        sys('cls')
        
        print('\n[Kitapları Listele]')

        cur.execute("SELECT * FROM Books") ## TÜM VERİLER 'Books' TABLOSUNDAN ÇEKİLİR

        allBooks = cur.fetchall() ## TÜM VERİLER BİR DEĞİŞKENE ATANIR

        if len(allBooks) > 0: ## HERHANGİ BİR VERİ VAR MI KONTROLU YAPILIR, LİSTENİN ELEMAN SAYISI SIFIRDAN FAZLAYSA VERİ VARDIR

            for i in range(0, len(allBooks)): ## TÜM VERİLER EKRANA YAZILIR
                print(f'\nSıra No: {i}\nKitap: {allBooks[i][0]}\nYazar: {allBooks[i][1]}')

            input("\nAna menüye dönmek için 'Enter'a bas: ")

        else:

            print('\nHerhangi bir kitap bulunamadı.')

            sleep(1.5)

    
    ## PROGRAMI KAPAT
    elif choice_mainMenu == 'Q' or choice_mainMenu == 'q':

        print('\nÇıkış yapılıyor...')

        sleep(1)

        sys('cls')

        break
            

db.close() ## VERİ TABANI KAPATILIR