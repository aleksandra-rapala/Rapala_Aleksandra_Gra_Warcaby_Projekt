from gui import kolory
from elementy_gry import gracz
from elementy_gry import szachownica
from elementy_gry import pionek
from elementy_gry import ruch
from elementy_gry import gra

    #TEST NUMER 1
        
def wykonanie_po_dwa_ruchy_przez_kazdego_z_graczy():    
    
    gracz_bialy = gracz.Gracz([], kolory.color_white)
    gracz_czarny = gracz.Gracz([], kolory.color_black)
    

    #tworzy guziki unikalne dla każdego przycisku (POLA PLANSZY)
    szachownica1 = szachownica.Szachownica()
    szachownica1.set_net_buttons()
    net_buttons = szachownica1.get_net_buttons()
    
    pionek1 = pionek.Zwykly_pionek(kolory.color_white, 1)  #przykładowy pionek gracza 1
    pionek2 = pionek.Zwykly_pionek(kolory.color_black, 2)  #przykładowy pionek gracza 2
    
    #SPECJALNE POCZATKOWE ROZSTAWIENIA PIONKÓW
    pionek1.ustaw_na_polu(net_buttons[5][2])  #bialy
    pionek2.ustaw_na_polu(net_buttons[2][5])  #czarny
    
    #Szukamy graczom ich mozliwych ruchów
    gracz1 = gracz.Gracz([pionek1], kolory.color_white)
    gracz1.szukaj_mozliwe_ruchy_bez_bicia(net_buttons)
    gracz1.szukaj_mozliwe_ruchy_z_biciem(net_buttons)
    
    gracz2 = gracz.Gracz([pionek2], kolory.color_black)
    gracz2.szukaj_mozliwe_ruchy_bez_bicia(net_buttons)
    gracz2.szukaj_mozliwe_ruchy_z_biciem(net_buttons)    
    
    
    #SPECJALNE DANE RUCHY DO SPRAWDZENIA
    
    ruch1_bialego = [pionek1, net_buttons[4][1]]
    ruch2_bialego = [pionek1, net_buttons[3][0]]
    
    ruch1_czarnego = [pionek2, net_buttons[3][4]]
    ruch2_czarnego = [pionek2, net_buttons[4][5]]
    
    
    
    # pętla wykonuje sie dwa razy (2 kolejki po 2 ruchy)
    licznik = 0
    for dany_ruch in [[ruch1_bialego, ruch1_czarnego], [ruch2_bialego, ruch2_czarnego]]:
        
        #gracz pierwszy biały:
        
        ruch_aktualny = ruch.Ruch(gracz1, 0, 0, gracz2)
        assert ruch_aktualny.sprawdz_czy_dozwolony(ruch1_bialego)  #assert dla pewności, ze ruch jest prawidłowy (ustawia czy z biciem )
               
        ruch_aktualny.ustaw_skad_ruch(dany_ruch[0][0].get_button())
        ruch_aktualny.ustaw_dokad_ruch(dany_ruch[0][1])
        ruch_aktualny.wykonaj_ruch()
            
        #po każdym ruchu sprwadzamy, czy pionek przeniósł się na odpowiednie miejsce
        if(licznik==0):
            assert (net_buttons[4][1].get_pionek() == pionek1)
        elif(licznik==1):
            assert (net_buttons[3][0].get_pionek() == pionek1)
        
        
        #gracz drugi czarny:
        
        ruch_aktualny = ruch.Ruch(gracz2, 0, 0, gracz2) 
        assert ruch_aktualny.sprawdz_czy_dozwolony(ruch1_czarnego)  #assert dla pewności, ze ruch jest prawidłowy
        
        ruch_aktualny.ustaw_skad_ruch(dany_ruch[1][0].get_button())
        ruch_aktualny.ustaw_dokad_ruch(dany_ruch[1][1])
        ruch_aktualny.wykonaj_ruch()  
            
        #po każdym ruchu sprwadzamy, czy pionek przeniósł się na odpowiednie miejsce
        if(licznik==0):
            assert (net_buttons[3][4].get_pionek() == pionek2)
        elif(licznik==1):
            assert (net_buttons[4][5].get_pionek() == pionek2)  
    

        licznik = licznik +1
        
       
    
    
    #TEST NUMER 2
    
def niepowodzenie_blednego_ruchu_pionkiem():
    
    #tworzy guziki unikalne dla każdego przycisku (POLA PLANSZY)
    szachownica1 = szachownica.Szachownica() 
    szachownica1.set_net_buttons() 
    net_buttons = szachownica1.get_net_buttons()
    
    pionek1 = pionek.Zwykly_pionek(kolory.color_white, 1)  #przykładowy pionek
    
    #przykladowe mozliwe ruchy prawdidłowe:
    mozliwe_ruchy_z_biciem = []
    mozliwe_ruchy_bez_bicia = [[pionek1, net_buttons[2+1][5-1]], [pionek1, net_buttons[2-1][5-1]]]
          
    #przekazujemy graczowi jego mozliwe prawidłowe ruchy:    
    gracz1 = gracz.Gracz([pionek1], kolory.color_white)
    gracz1.ustaw_mozliwe_ruchy_bez_bicia(mozliwe_ruchy_bez_bicia)
    gracz1.ustaw_mozliwe_ruchy_z_biciem(mozliwe_ruchy_z_biciem)
                           
   
    #tworzymy ruch dla użytkownika
    ruch1 = ruch.Ruch(gracz1, 0, 0, 0)  
    
    #sprawdzenie mozliwosci danego ruchu przez niego, wtym wypadku nieprawidłowego, więc zwraca False 
    ruch_uzytkownika = [pionek1, net_buttons[2+3][5-1]]
    
    result = ruch1.sprawdz_czy_dozwolony(ruch_uzytkownika)  #zwraca True lub False czy dozwolony czy nie
    
    assert not result
    
    
    
    
    
    #TEST NUMER 3
    
def wykonanie_bicia_pojedynczego_pionka():
    
    szachownica1 = szachownica.Szachownica()
    szachownica1.set_net_buttons()
    net_buttons = szachownica1.get_net_buttons()
    
    #SPECJALNE PRZYKŁADOWE ROZSTAWIENIA PIONKÓW NA PLANSZY
    pionek_zbijajacy = pionek.Zwykly_pionek(kolory.color_white, 1)  #przykładowy pionek zbijający
    pionek_zbijajacy.ustaw_na_polu(net_buttons[4][3])
    
    pionek_zbity = pionek.Zwykly_pionek(kolory.color_black, 2)  #przykładowy pionek, który będzie zbity
    pionek_zbity.ustaw_na_polu(net_buttons[3][4])
    
    
     #przekazujemy graczom pionki ustawione
    gracz1 = gracz.Gracz([pionek_zbijajacy], kolory.color_white)
    gracz2 = gracz.Gracz([pionek_zbity], kolory.color_black)
    
        
        #przeszukanie możliwych ruchów gracza, który będzie zbijał
    gracz1.szukaj_mozliwe_ruchy_bez_bicia(net_buttons)
    gracz1.szukaj_mozliwe_ruchy_z_biciem(net_buttons)    
    

    #uzytkownik bialy wykonuje ruch ktorym zbija czarnego
    
    #dajemy ruch zbijający
    ruch_bialego = [pionek_zbijajacy, net_buttons[2][5], net_buttons[4][3]]
    
    ruch_aktualny = ruch.Ruch(gracz1, 0, 0, gracz2)  
    assert ruch_aktualny.sprawdz_czy_dozwolony(ruch_bialego)  #dla pewności sprawdzamy czy ruch prawidłowy
    
    ruch_aktualny.ustaw_skad_ruch(net_buttons[4][3])
    ruch_aktualny.ustaw_dokad_ruch(net_buttons[2][5])
    
    ruch_aktualny.wykonaj_ruch()
    

    #po zbiciu pionek zbity nie istnieje w puli pionków gracza czarnego
    result = pionek_zbity not in gracz2.get_pionki()  #zwraca True gdy pionka już nie ma w puli pionków gracza
    
    #then
    assert result
    
    
    
    
    
    
    
        
     #TEST NUMER 4   
        
        
def wykonanie_bicia_przynajmniej_dwoch_pionkow():          
        
        
    szachownica1 = szachownica.Szachownica()
    szachownica1.set_net_buttons() 
    net_buttons = szachownica1.get_net_buttons()
    
    #SPECJALNE PRZYKŁADOWE ROZSTAWIENIA PIONKÓW
    
    pionek_zbijajacy = pionek.Zwykly_pionek(kolory.color_white, 1)  #przykładowy pionek zbijający
    pionek_zbijajacy.ustaw_na_polu(net_buttons[4][3])
    
    pionek_zbity = pionek.Zwykly_pionek(kolory.color_black, 2)  #przykładowy pionek, który będzie zbity
    pionek_zbity.ustaw_na_polu(net_buttons[3][4])
    
    pionek_zbity_drugi = pionek.Zwykly_pionek(kolory.color_black, 2)  #przykładowy drugi pione, który będzie zbity
    pionek_zbity_drugi.ustaw_na_polu(net_buttons[1][6])    
    
    
    
 #przekazujemy graczom pionki ustawione

    gracz1 = gracz.Gracz([pionek_zbijajacy], kolory.color_white)
    gracz2 = gracz.Gracz([pionek_zbity, pionek_zbity_drugi], kolory.color_black)
    
    gracz1.szukaj_mozliwe_ruchy_bez_bicia(net_buttons)
    gracz1.szukaj_mozliwe_ruchy_z_biciem(net_buttons)    
    
    
    #nadajemy 2 ruchy bijące, które wykonają się pod rząd
    dany_ruch_gracza_pierwsze_bicie = [pionek_zbijajacy, net_buttons[2][5], net_buttons[3][4]]
    dany_ruch_gracza_drugie_bicie = [pionek_zbijajacy, net_buttons[0][7], net_buttons[1][6]]
    
    
    ruch1 = ruch.Ruch(gracz1, net_buttons,0, gracz2)  
    assert ruch1.sprawdz_czy_dozwolony(dany_ruch_gracza_pierwsze_bicie)  #dla pewności sprawdzamy czy ruch bijący dozwolony
        
    ruch1.ustaw_skad_ruch(dany_ruch_gracza_pierwsze_bicie[0].get_button())
    ruch1.ustaw_dokad_ruch(dany_ruch_gracza_pierwsze_bicie[1])
    ruch1.wykonaj_ruch()
        
    assert ruch1.czy_kolejne_bicie()  #dla pewnosci, jesli po pierwszym ruchu wyłapana informacja, że możliwe bicie kolejne 
    assert ruch1.sprawdz_czy_dozwolony(dany_ruch_gracza_drugie_bicie) #sprawdzamy dla pewności drugi ruch
       
    ruch1.ustaw_skad_ruch(dany_ruch_gracza_drugie_bicie[0].get_button())
    ruch1.ustaw_dokad_ruch(dany_ruch_gracza_drugie_bicie[1])
    ruch1.wykonaj_ruch()            
        

    #when
    #oba pionki nie powinny już znajdowac sie w puli gracza czarnego
    result1 = pionek_zbity not in gracz2.get_pionki()  #zwraca True gdy pionka już nie ma w puli pionków gracza
    result2 = pionek_zbity_drugi not in gracz2.get_pionki()
    
    #then
    assert  (result1 and result2)  
    
    
    
    
    
    
    #TEST NUMER 5
    
def zamiana_pionka_w_damke():
        
    szachownica1 = szachownica.Szachownica()
    szachownica1.set_net_buttons()
    net_buttons = szachownica1.get_net_buttons()
        
        #SPECJALNE POCZATKOWE ROZSTAWIENIE PIONKA
        
    pionek_zwyczajny = pionek.Zwykly_pionek(kolory.color_white,1)
    pionek_zwyczajny.ustaw_na_polu(net_buttons[1][2])
        
    gracz1 = gracz.Gracz([pionek_zwyczajny], kolory.color_white)
    ruch1 = ruch.Ruch(gracz1, 0, 0, 0)  
    ruch1.ustaw_skad_ruch(net_buttons[1][2])
    ruch1.ustaw_dokad_ruch(net_buttons[0][3])    
   
    ruch1.wykonaj_ruch() #tu tworzą się zmiany w czasie ruchu, a więc powinna pojawic sie zamiana pionka na damke
    
    result =  isinstance(gracz1.get_pionki()[0], pionek.Damka) 
   
    assert result    
    
    
    
    
   



   #TEST NUMER 6 
    
    
def bicie_damka():
    
        
    szachownica1 = szachownica.Szachownica()
    szachownica1.set_net_buttons()
    net_buttons = szachownica1.get_net_buttons()
    
    #SPECJALNE PRZYKŁADOWE ROZSTAWIENIA PIONKÓW
    
    pionek_zbijajacy = pionek.Damka(kolory.color_white, 1)  #przykładowy pionek zbijający
    pionek_zbijajacy.ustaw_na_polu(net_buttons[4][3])
    
    pionek_zbity = pionek.Zwykly_pionek(kolory.color_black, 2)  #przykładowy pionek, który będzie zbity
    pionek_zbity.ustaw_na_polu(net_buttons[3][4])
    
    
 #przekazujemy graczom pionki ustawione

    gracz1 = gracz.Gracz([pionek_zbijajacy], kolory.color_white)
    gracz2 = gracz.Gracz([pionek_zbity], kolory.color_black)
    
    
    #szukamy dozwolonych ruchuów dla gracza zbijającego białą damką
    
    gracz1.szukaj_mozliwe_ruchy_bez_bicia(net_buttons)
    gracz1.szukaj_mozliwe_ruchy_z_biciem(net_buttons)      
    
                             
    #uzytkownik bialy wykonuje ruch ktorym zbija czarnego
    
    #dany ruch
    ruch_bialej_damki = [pionek_zbijajacy, net_buttons[2][5], net_buttons[3][4]]
    ruch_aktualny = ruch.Ruch(gracz1, 0, 0, gracz2)  
    assert ruch_aktualny.sprawdz_czy_dozwolony(ruch_bialej_damki)  #dla pewności sprawdzamy czy ruch prawidłowy
    ruch_aktualny.ustaw_skad_ruch(ruch_bialej_damki[0].get_button())
    ruch_aktualny.ustaw_dokad_ruch(ruch_bialej_damki[1])
    
    ruch_aktualny.wykonaj_ruch()
    
    # pionka przeciwnika czyli gracza czarnego nie powinno być w jego puli pionków
    result = pionek_zbity not in gracz2.get_pionki()  #zwraca True gdy pionka już nie ma w puli pionków gracza
    
    #then
    assert result        








    #TEST NUMER 7
    
def wygrana_gracza_grajacego_czarnymi_pionkami():
    
    gra1 = gra.Gra(None)   #nie przekazujemy ekranu GUI , ale objekt gra potrzebny dla metody zwroc_wygranego_gracza
    gra1.utworz_graczy()
       
    szachownica1 = szachownica.Szachownica()
    szachownica1.set_net_buttons()
    net_buttons = szachownica1.get_net_buttons()
    
    #SPECJALNE PRZYKŁADOWE ROZSTAWIENIA PIONKÓW
    
    pionek_zbijajacy = pionek.Zwykly_pionek(kolory.color_black, 1)  #przykładowy pionek zbijający
    pionek_zbijajacy.ustaw_na_polu(net_buttons[2][5])
    
    pionek_zbity = pionek.Zwykly_pionek(kolory.color_white, 2)  #przykładowy pionek, który będzie zbity
    pionek_zbity.ustaw_na_polu(net_buttons[3][4])
    
 #przekazujemy graczom pionki ustawione

    gra1.get_lista_graczy()[1].get_pionki().append(pionek_zbijajacy)
    gra1.get_lista_graczy()[0].get_pionki().append(pionek_zbity)
    
    
    #dajemy graczom prawidłowe ruchy
    gra1.get_lista_graczy()[1].szukaj_mozliwe_ruchy_bez_bicia(net_buttons)
    gra1.get_lista_graczy()[1].szukaj_mozliwe_ruchy_z_biciem(net_buttons) 
     
        
    #pierwszy ruch wykonuje gracz czarny
    ruch_zbijajacy = [pionek_zbijajacy, net_buttons[4][3], net_buttons[3][4]]
    
    ruch_aktualny = ruch.Ruch(gra1.get_lista_graczy()[1], 0, 0, gra1.get_lista_graczy()[0])
    assert ruch_aktualny.sprawdz_czy_dozwolony(ruch_zbijajacy)  #dla pewności sprawdzamy czy ruch prawidłowy  
    ruch_aktualny.ustaw_skad_ruch(ruch_zbijajacy[0].get_button())
    ruch_aktualny.ustaw_dokad_ruch(ruch_zbijajacy[1])
    
    ruch_aktualny.wykonaj_ruch()
    
    #teraz bialy gracz probuje wykonac ruch (sprawdzamy czy ma jeszcze pionki i czy ma moziwe ruchy , jesli nie ma to przegral)
    ruch2 = ruch.Ruch(gra1.get_lista_graczy()[0], 0, 0, gra1.get_lista_graczy()[1])
    
    #podczas rozpoczęcie ruchu zawsze sprawdzenie czy mozwe wykonac ruch czy jednak przegrywa
    result = 0
    if (ruch2.sprawdz_czy_gracz_przegrywa() == True):  #jesli gracz w swoim ruchu przegrywa to True tutaj zwracene
        result = gra1.zwroc_wygranego_gracza()
    
    assert (result == gra1.get_lista_graczy()[1])
    
    



  
        
    
    
    
    
     #NUMER 8   
        
        
def rozpoczecie_nowej_gry_po_zwyciestwie_jednego_gracza():
    
    gra1 = gra.Gra(None)
    gra1.utworz_graczy()
    
    #SYMULACJA BICIA
    
            
    szachownica1 = szachownica.Szachownica() #przekazujemy None, gdyż nie działa tutaj GUI
    #tworzy i tworzy guziki unikalne dla kazdego przycisku
    szachownica1.set_net_buttons() #dzięki unikalnym guzikom prawidłowe porównywanie guzików w metodzie sprawdz_czy_dozwolony
    net_buttons = szachownica1.get_net_buttons()
    
    #przykladowe rozstawienie pionkow
    pionek_zbijajacy = pionek.Zwykly_pionek(kolory.color_black, 1)  #przykładowy pionek zbijający
    pionek_zbijajacy.ustaw_na_polu(net_buttons[2][5])
    
    pionek_zbity = pionek.Zwykly_pionek(kolory.color_white, 2)  #przykładowy pionek, który będzie zbity
    pionek_zbity.ustaw_na_polu(net_buttons[3][4])
    
 #przekazujemy graczom pionki ustawione

    gra1.get_lista_graczy()[1].get_pionki().append(pionek_zbijajacy)
    gra1.get_lista_graczy()[0].get_pionki().append(pionek_zbity)
     
        
        #pierwszy ruch wykonuje gracz czarny
    ruch1 = ruch.Ruch(gra1.get_lista_graczy()[1], 0, 0, gra1.get_lista_graczy()[0])
                             
    #uzytkownik bialy wykonuje ruch ktorym zbija czarnego
    
    #od razu przyjmujemy ze ruch dozwolony
    
    ruch1.ustaw_czy_z_biciem(True)
    ruch1.ustaw_zbity_guzik(net_buttons[3][4])
    ruch1.ustaw_skad_ruch(net_buttons[2][5])
    ruch1.ustaw_dokad_ruch(net_buttons[4][3])
    
    ruch1.wykonaj_ruch()
    
    #teraz bialy gracz probuje wykonac ruch (sprawdzamy czy ma jeszcze pionki i czy ma moziwe ruchy , jesli nie ma to przegral)
    ruch2 = ruch.Ruch(gra1.get_lista_graczy()[0], 0, 0, gra1.get_lista_graczy()[1])

    #GRA SKONCZONA PO TYM RUCHU POWINNA BYC WIEC SPRAWDZAMY:
    
    #podczas ruchu sprawdzenie czy przegrywa  "mamy wygranego"
    tmp_gracz1 = gra1.get_lista_graczy()[1]
    tmp_gracz2 = gra1.get_lista_graczy()[0]
    
    if (ruch2.sprawdz_czy_gracz_przegrywa() == True):  #jesli gracz w swoim ruchu przegrywa to True tutaj zwracene
        result = gra1.zwroc_wygranego_gracza()
        gra1.zakoncz_gre()

    
    #wygrywa jeden gracz
    result0 = (result==tmp_gracz1 or result==tmp_gracz2)
    assert result0 
    
    # dowod gry skonczonej jej status to False
    result1 = gra1.get_status_gry()
    assert not result1
    
    #nowa gra zwraca true to znaczy ze sie zaczela po zakonczeniu
    result2 = gra1.nowa_gra()   #nowa gra zwraca True jezeli jest w stanie sie zaczac po zakonczeniu
    assert result2
        
   
    
    
    
 
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    