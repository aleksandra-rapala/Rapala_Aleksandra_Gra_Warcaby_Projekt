from gui import kolory
from elementy_gry import guzik
           

class Szachownica:
    """reprezentuje szachownice"""
    def __init__(self):
        
        #wymiary
        self.liczba_wierszy_planszy = 8
        self.liczba_kolumn_planszy = 8
            
        #początek szachownicy na ekranie
        self.start_wiersz_ekranu = 1
            
        #siatka guzików
        self.net_buttons = []
        
        #rozmiar pola (guzika)
        self.rozmiar_pola = 0
      
    
        #get
            
    def get_net_buttons(self):
        """zwraca siatkę przycisków"""
        return self.net_buttons
    
    def get_ilosc_wierszy(self):
        """zwraca ilość wierszy, z których zbudowana jest szachownica"""
        return self.liczba_wierszy_planszy
    
    def get_ilosc_kolumn(self):
        """zwraca ilość kolumn, z których zbudowana jest szachownica"""
        return self.liczba_kolumn_planszy
    
     
        #set
            
    def ustaw_rozmiar_pola(self, width_ekranu, height_ekranu):
        """ustawia rozmiar pola"""
        self.rozmiar_pola = height_ekranu/10   #dzieki temu wysokosc ekranu podzielona na 10 kawalkow i zaczynamy od wiersza o indeksie 1 
            
            
            
            
        #inne metody   
            
    def create_net_buttons(self):   # 8x8  buttons[8][8]
        """tworzy siatke przycisków, a więc szachownice"""
        net = [[0] * self.liczba_kolumn_planszy for i in range(self.liczba_wierszy_planszy)]
        return net
    
 
        #set

    def set_net_buttons(self):
        """ustawia guziki"""
        self.net_buttons = self.create_net_buttons()
            
        #malujemy 64 guzików, czyli tworzymy plasze 8x8
            
        wiersz_planszy = -1  #od 0 indexowane
    
        for wiersz_ekranu in range (self.start_wiersz_ekranu, self.start_wiersz_ekranu+self.liczba_wierszy_planszy):
            wiersz_planszy += 1
            for kolumna in range (0,self.liczba_kolumn_planszy):
                    
                #ustawiamy kolor guzika co drugi ciemny na przemian z białym
                
                f = wynik_modulo(2)
                if(f(wiersz_planszy)==0 and f(kolumna)==0 or f(wiersz_planszy)!=0 and f(kolumna)!=0):
                    button_colour = kolory.color_white
                else:
                    button_colour = kolory.color_dark


                object_guzik = guzik.Guzik_planszy(kolumna, wiersz_ekranu, button_colour, self.rozmiar_pola, self.rozmiar_pola, wiersz_planszy) 
            
                #wypelniamy siatkę stworzonym guzikiem
                self.net_buttons[wiersz_planszy][kolumna]= object_guzik
            
       
        
  

           
    #FUNKCJA TWORZĄCA SZACHOWNICE
    
def create_szachownica(display):
    """tworzy szachownice do gry"""
    szachownica = Szachownica()
    width_ekranu, height_ekranu = display.get_okno_pygame().get_size() 
    szachownica.ustaw_rozmiar_pola(width_ekranu, height_ekranu)
    szachownica.set_net_buttons()
        
    return szachownica
        
       
        
        #lambda do uproszczenia obliczeń modulo
def wynik_modulo(liczba):
    """dla uproszczenia wykonuje modulo"""
    return lambda val: (val % liczba)


    
    #generator dla stworzenia szeregu przycisków z siatki przycisków
def wygeneruj_net_jako_szereg(net_buttons):
    """generator, który z siatki przycisków tworzy szereg guzików"""
    for wiersz_guzikow in net_buttons:
        for guzik in wiersz_guzikow:
            yield guzik              # yield oznacza, że jest to generator - nie zwykła funkcja

               

                    
                    
                    