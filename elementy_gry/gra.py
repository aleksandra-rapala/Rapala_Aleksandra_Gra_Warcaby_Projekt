from elementy_gry import szachownica
from elementy_gry import guzik
from elementy_gry import pionek
from elementy_gry import gracz
from elementy_gry import ruch
from gui import *
from komunikaty import messages



class Gra:
    """ odpowiedzialna za cały przebieg gry  """
    def __init__(self, display):  #dostaje jako argument obiekt mający screen gry
        
        self.display = display
        
        self.status = False  #czy gra aktualna, czy zakończona
        
        self.czyja_tura = 0
        self.tura_czarnego = messages.Message_czyja_kolej("TURA GRACZA: 2 CZARNEGO")
        self.tura_bialego = messages.Message_czyja_kolej("TURA GRACZA: 1 BIALEGO")
                
        self.lista_graczy = [] 
        
        self.ilosc_pionkow = 12
        
        self.pionki_biale = []
        self.pionki_czarne = []
        
        self.szachownica = 0   #tutaj dostep do net_buttons
        self.reset_button = 0
        
        self.ilosc_wierszy_ustawien = 3   # w ilu wierszach stoją pionki jednego przeciwnika
        
        self.window_message_gracz_czarny = 0
        self.window_message_gracz_bialy = 0
        
        self.reset = True
        
        

        
        #get
    
    def get_lista_graczy(self):
        """ zwraca listę graczy """
        return self.lista_graczy
    
    def get_display(self):
        """ zwraca obiekt display - dzięki niemu ułatwienie malowania po oknie (gui)"""
        return self.display
        
    def get_czy_reset(self):
        """ zwraca informację, czy został wcisniety przycisk reset """
        return self.reset        
        
    def get_reset_button(self):
        """ zwraca przycisk resetujący grę """
        return self.reset_button        
    
    def get_status_gry(self):
        """ zwraca status gry - True-oznacza, że gra trwa aktualnie, False - gra nie jest aktywna """
        return self.status
        
           #dla GUI
    def get_window_message_gracz(self, ktory_gracz):
        """ zwraca okna na komunikaty dla graczy """
        
        if ktory_gracz == "czarny":
            return self.window_message_gracz_czarny
        else:
            return self.window_message_gracz_bialy     
        
    
    
    # tworzenie ważnych elementów gry:
    
    def utworz_szachownice(self):
        """tworzy szachownicę """
        self.szachownica = szachownica.create_szachownica(self.display) 
       
    
    def utworz_pionki(self):  #pionki sa ponumerowane od 1 do 24
            """tworzy pionki do gry"""
            self.pionki_biale =[pionek.Zwykly_pionek(kolory.color_white, i+1) for i in range(0, self.ilosc_pionkow)]         
            self.pionki_czarne=[pionek.Zwykly_pionek(kolory.color_black, self.ilosc_pionkow+12-i)for i in range(0, self.ilosc_pionkow)]

            
    def utworz_graczy(self):   #gracze otrzymują liste pionków
        """tworzy graczy """
        gracz_bialy = gracz.Gracz(self.pionki_biale, kolory.color_white)
        gracz_czarny = gracz.Gracz(self.pionki_czarne, kolory.color_black)
        
        self.lista_graczy = [gracz for gracz in [gracz_bialy, gracz_czarny]]
        

      #ustawianie pionków :    
            
    def ustaw_pionki(self):
        """ustawia pionki do rozpoczęcia gry """
        net_buttons = self.szachownica.get_net_buttons()
 
        # dla gracza białego (u dołu planszy)
        licznik = 0
        for wiersz_planszy in range(self.szachownica.get_ilosc_wierszy()-self.ilosc_wierszy_ustawien, self.szachownica.get_ilosc_wierszy()):   
            if(wiersz_planszy%2!=0):
                start_kolumna=0
            else:
                start_kolumna=1
                
            for kolumna_planszy in range (start_kolumna, self.szachownica.get_ilosc_kolumn(), 2):
                self.pionki_biale[licznik].ustaw_na_polu(net_buttons[wiersz_planszy][kolumna_planszy])
                licznik += 1
            
        #dla gracza czarnego (u góry planszy)
        licznik = 0           
        for wiersz_planszy in range (0, self.ilosc_wierszy_ustawien):
            if(wiersz_planszy%2!=0):
                start_kolumna=0
            else:
                start_kolumna=1
            for kolumna_planszy in range (start_kolumna, self.szachownica.get_ilosc_kolumn(), 2):
                self.pionki_czarne[licznik].ustaw_na_polu(net_buttons[wiersz_planszy][kolumna_planszy])
                licznik += 1
        
        
    def create_reset_button(self):
        """tworzy przycisk do resetowania gry """
        width = self.display.get_okno().get_width()
        height = self.display.get_okno().get_height()
        self.reset_button = guzik.Reset_button(width, height)    
        
        
    def create_windows_message(self):
        """tworzy okna na komunikaty o błędach dla graczy"""
        self.window_message_gracz_czarny = messages.Window_message(self.lista_graczy[1], self.display)
        self.window_message_gracz_bialy = messages.Window_message(self.lista_graczy[0], self.display)   

        
        
    def przygotuj_gre(self):  #TA METODA NIC NIE MALUJE DLA GUI
        """przygotowywuje grę przed rozpoczęciem """
        self.utworz_szachownice()
        self.utworz_pionki()
        self.ustaw_pionki()
        self.utworz_graczy()  #gracze otrzymują już ustawione pionki
        self.create_reset_button()
        self.create_windows_message()  #tworzy okienka dla komunikatów graczy 
        
            
        
        
    #///////////////////////////////////////////////////////////////////////////////////////////////
    

        
        #dla GUI
    def rysuj_plansze(self):
        """rysuje planszę """
        self.display.rysuj_tlo(kolory.color_tla)
       
        if self.czyja_tura != 0:
            if self.czyja_tura == self.lista_graczy[0]:
                self.tura_bialego.wyswietl_komunikat(self.display, 50, kolory.color_black, 1/5*(self.display.get_okno().get_width()), 0,)
            else:
                self.tura_czarnego.wyswietl_komunikat(self.display, 50, kolory.color_black, 1/5*(self.display.get_okno().get_width()), 0)
        else:
             self.tura_bialego.wyswietl_komunikat(self.display, 50, kolory.color_black, 1/5*(self.display.get_okno().get_width()), 0)
            
        for wiersz_guzikow in self.szachownica.get_net_buttons():
            for guzik in wiersz_guzikow:
                    
                guzik.draw_button(self.display)
                
                if(guzik.get_pusty() != True):
                    guzik.get_pionek().maluj_pionek(self.display)

        self.reset_button.draw_reset_button(self.display)     
        self.display.aktualizuj_display()


        
    def aktualizuj_plansze(self):
        """aktualizuje planszę"""
        self.rysuj_plansze()        
        
           
    #zakonczenie gry dla GUI
    
    def gui_zakoncz_gre(self, wygral):
        """koniec gry widoczny na ekranie"""
        window_koniec = messages.Window_message(None, self.display)
        window_koniec.draw_window_message(self.display)
        
        if wygral == self.lista_graczy[0]:
            napis = "WYGRAL GRACZ BIALY"
        else:
            napis = "WYGRAL GRACZ CZARNY"
        
        window_koniec.wstaw_komunikat_dla_gracza(self.display, napis)
        
        #czekanie na obslugę guzika reset
        self.display.obsluga_reset(self.reset_button)      
        
        
        

        #/////INNE:
        
        
    def resetuj_gre(self):
        """resetuje grę """
        self.__init__(self.display)         
        

    def zwroc_wygranego_gracza(self):
        """zwraca gracza, który wygrał grę"""
        if self.lista_graczy[0].get_przegrany() == False:
            wygrany = self.lista_graczy[0]
        else:
            wygrany = self.lista_graczy[1]
        return wygrany        
        
        
        
        

    
 #WŁAŚCIWY PZREBIEG GRY:
    
    
    def start(self):
        """przebieg gry """
        while(1):
                       
                #WSTĘP GRY- JEJ PRZYGOTOWANIE
                if(self.nowa_gra()==True):  # -> tu czeka na reset gry
                    self.przygotuj_gre()
                    self.rysuj_plansze()
                    
                while(self.status==True): #czyli dopoki gra dziala
                    for gracz_aktualny in self.lista_graczy:
                        
                        if(self.status==True):
                            
                            if gracz_aktualny == self.lista_graczy[0]:
                                przeciwnik = self.lista_graczy[1]
                                self.czyja_tura = self.lista_graczy[0]
                            else:
                                przeciwnik = self.lista_graczy[0]
                                self.czyja_tura = self.lista_graczy[1]
                    
                            self.aktualizuj_plansze()  #dla aktualizacji napisów czyja tura
                
                            #wykonanie ruchu
                            ruch1 = ruch.Ruch(gracz_aktualny, self.szachownica.get_net_buttons(), self, przeciwnik)  # self to gra
                            self.status = ruch1.pobierz_ruch_uzytkownika()   #ruch zwraca status gry
                            
                            #gdy status False -> albo gracz przegrał albo włączył reset
                            
                #jesli gra się zakonczyla przegraniem, to komunikat :
                if(self.reset==False): #nie zresetowane 
                    
                    #funkcja gui czeka na wcisniecie reset
                    self.gui_zakoncz_gre(self.zwroc_wygranego_gracza())
                    self.zakoncz_gre()



  

    def zakoncz_gre(self):
        """koniec gry, czyli resetuje"""
        self.resetuj_gre()

        
            
    def nowa_gra(self):
        """nowa gra, czyli ustawia status gry na znów aktywny, o ile zresetowano gre"""
        #self status w tym momencie zawsze jest False gdyż gra nie dziala
        
        if(self.reset==True):    #gdy gra zresetowana, czyli gotowa do rozpoczęcia nowej rozgrywki
            self.reset=False
            self.status = True
                
        return self.status   #false gdy gra sie nie zaczela  true - gdy sie zaczela
        

        
        
        
        
        
        
        
        
        
        
        
        
        
            