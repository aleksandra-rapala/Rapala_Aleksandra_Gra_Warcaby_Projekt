import szachownica
import kolory
import pionek
import gracz
from ruch import *
import pygame
import guzik
import messages


class Gra:

    def __init__(self, screen):
        
        self.screen = screen #ekran na ktorym jest szachownica
        
        self.status = False
        
        self.czyja_tura = 0
        self.tura_czarnego = messages.Message("TURA GRACZA: CZARNEGO")
        self.tura_bialego = messages.Message("TURA GRACZA: BIALEGO")
        
        self.gracz_bialy = 0
        self.gracz_czarny = 0
        
        
        
        self.ilosc_pionkow = 12
        
        self.pionki_biale = []
        self.pionki_czarne = []
        
        self.szachownica = 0   #tutaj dostep do net_buttons
        self.reset_button = 0
        
        
        self.ilosc_wierszy_ustawien = 3
        self.window_message_gracz_czarny = 0
        self.window_message_gracz_bialy = 0
    
    def get_screen(self):
        return self.screen
    
    def utworz_szachownice(self):
        
        self.szachownica = szachownica.create_szachownica(self.screen) 
       
    
    def utworz_pionki(self):
        
        for i in range(0, self.ilosc_pionkow):
            self.pionki_biale.append(pionek.Zwykly_pionek(kolory.color_white, i+1))
            self.pionki_czarne.append(pionek.Zwykly_pionek(kolory.color_black, self.ilosc_pionkow+12-i))
            
            
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
        
        self.rysuj_plansze()
        pygame.display.update() 
        
    
    
    def create_reset_button(self):
        
        self.reset_button = guzik.Reset_button(self.screen)
        
    def create_windows_message(self):
        
        self.window_message_gracz_czarny = messages.Window_message(self.screen, self.gracz_czarny)
        self.window_message_gracz_bialy = messages.Window_message(self.screen, self.gracz_bialy)
        
        
    def rysuj_plansze(self):
        
            
        if self.czyja_tura == self.gracz_bialy:
            
            self.tura_czarnego.zgas_komunikat()
            self.tura_bialego.wyswietl_komunikat('Arial', 50, kolory.color_black, 1/5*self.screen.get_width(), 0, self.screen)
        else:
            self.tura_bialego.zgas_komunikat()
            self.tura_czarnego.wyswietl_komunikat('Arial', 50, kolory.color_black, 1/5*self.screen.get_width(), 0, self.screen)
            
        
        for wiersz_guzikow in self.szachownica.get_net_buttons():
            for guzik in wiersz_guzikow:
                    
                guzik.draw_button()
                
                if(guzik.get_pusty() != True):
                    guzik.get_pionek().maluj_pionek()
        
        self.create_reset_button()
        self.reset_button.draw_button()     
        
        
        self.create_windows_message()
        self.window_message_gracz_czarny.draw_window_message()
        self.window_message_gracz_bialy.draw_window_message()
                    
                
       
        
    
    def zakoncz_gre(self):
        
        print("KONIEC!!!!!")
        if self.gracz_bialy.get_wygrany() == True:
            wygrany = "BIALY"
        else:
            wygrany = "CZARNY"
        print("Wygral : ", wygrany, "!!!!!")
        
    
    
    def aktualizuj_plansze(self):
        
        self.rysuj_plansze()
        pygame.display.update()
    
    def start(self):
        
        self.przygotuj_gre()
        self.status = True
        
        while(self.status==True):
            for gracz_aktualny in [self.gracz_bialy, self.gracz_czarny]:
                
                if gracz_aktualny == self.gracz_bialy:
                    przeciwnik = self.gracz_czarny
                    
                    self.czyja_tura = self.gracz_bialy

                    
                    self.aktualizuj_plansze()
                else:
                    przeciwnik = self.gracz_bialy
                    
                    self.czyja_tura = self.gracz_czarny
                    
                    
                    self.aktualizuj_plansze()
                    
                if(self.status==True):
                    print("Ruch gracza:  ")
                    ruch = Ruch(gracz_aktualny, self.szachownica.get_net_buttons(), self, przeciwnik)  #aktualna siatka guzikow  self to gra
                    status = ruch.pobierz_ruch_uzytkownika()

                
        self.zakoncz_gre()
        
        
        
        
   # def return_game(self):
        
        #def 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            