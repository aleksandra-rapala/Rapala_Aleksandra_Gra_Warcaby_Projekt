import szachownica
import kolory
import pionek
import gracz


class Gra:

    def __init__(self, screen):
        
        self.screen = screen #ekran na ktorym jest szachownica
        
        self.status = False
        
        self.gracz_bialy = 0
        self.gracz_czarny = 0
        
        self.ilosc_pionkow = 12
        
        self.pionki_biale = []
        self.pionki_czarne = []
        
        self.szachownica = 0
        
        self.ilosc_wierszy_ustawien = 3
        
        
    def utworz_szachownice(self):
        
        self.szachownica = szachownica.create_szachownica(self.screen) 
       
    
    def utworz_pionki(self):
        
        for i in range(0, self.ilosc_pionkow):
            self.pionki_biale.append(pionek.Zwykly_pionek(kolory.color_white))
            self.pionki_czarne.append(pionek.Zwykly_pionek(kolory.color_black))
            
            
    def utworz_graczy(self):
        
        self.gracz_bialy = gracz.Gracz(self.pionki_biale)
        self.gracz_czarny = gracz.Gracz(self.pionki_czarne)
            
            
    def ustaw_pionki(self):
        
        net_buttons = self.szachownica.get_net_buttons()
 
        
        licznik = 0
        for wiersz_planszy in range(self.szachownica.get_ilosc_wierszy()-self.ilosc_wierszy_ustawien, self.szachownica.get_ilosc_wierszy()):   
            if(wiersz_planszy%2!=0):
                start_kolumna=0
            else:
                start_kolumna=1
                
            for kolumna_planszy in range (start_kolumna, self.szachownica.get_ilosc_kolumn(), 2):
                self.pionki_biale[licznik].ustaw_na_polu(net_buttons[wiersz_planszy][kolumna_planszy])
                licznik += 1
                    
        licznik = 0           
   
        for wiersz_planszy in range (0, self.ilosc_wierszy_ustawien):   #<0, 3)
            if(wiersz_planszy%2!=0):
                start_kolumna=0
            else:
                start_kolumna=1
            for kolumna_planszy in range (start_kolumna, self.szachownica.get_ilosc_kolumn(), 2):
                self.pionki_czarne[licznik].ustaw_na_polu(net_buttons[wiersz_planszy][kolumna_planszy])
                licznik += 1
        
        
        
   
    def przygotuj_gre(self):
        
        self.utworz_szachownice()
        self.utworz_pionki()
        self.ustaw_pionki()
        self.utworz_graczy()
        
        
    def start(self):
        
        self.przygotuj_gre()
        
        print(self.gracz_bialy.get_mozliwe_ruchy_bez_bicia())
        self.status = True
        
        #while(self.status==True):
            #for gracz_aktualny in [self.gracz_bialy, self.gracz_czarny]:
                #if(self.status==True):
                   # ruch=Ruch()
                    #status = ruch.pobierz_ruch_uzytkownika(gracz_aktualny)
                
        #self.zakoncz_gre()
        
        
        
        
    #def zakoncz_gre(self):
        
        
        
        
        
        
        
        
        
        
        
        
        
            