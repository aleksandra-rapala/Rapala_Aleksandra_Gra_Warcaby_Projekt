import kolory
from guzik import Guzik
           

class Szachownica:
        
    def __init__(self, screen):
        
        #okno na której umieszczona szachownica
        self.screen = screen
        
        #wymiary
        self.liczba_wierszy_planszy = 8
        self.liczba_kolumn_planszy = 8
            
        #początek szachownicy na ekranie
        self.start_wiersz_ekranu = 1
            
        #siatka guzików
        self.net_buttons = []
        
        #rozmiar pola (guzika)
        self.rozmiar_pola
            
            
    def get_net_buttons(self):
        return self.net_buttons
    
    def get_ilosc_wierszy(self):
        return self.liczba_wierszy_planszy
    
    def get_ilosc_kolumn(self):
        return self.liczba_kolumn_planszy
            
            
    def rozmiar_pola(self):
        
        (width_ekranu, height_ekranu) = (self.screen.get_width(), self.screen.get_height())
    
        self.rozmiar_pola = height_ekranu/10   #dzieki temu wysokosc ekranu podzielona na 10 kawalkow i zaczynamy od wiersza o indeksie 1 
            
            
    def create_net_buttons(self):   # 8x8  buttons[8][8]
            
        net = []
        for i in range(self.liczba_wierszy_planszy):
            net.append([0] * self.liczba_kolumn_planszy)
        return net
    
 
    def set_net_buttons(self):
            
        self.net_buttons = self.create_net_buttons()
            
        #malujemy 64 guzików, czyli tworzymy plasze 8x8
            
        wiersz_planszy = -1  #od 0 indexowane
    
        for wiersz_ekranu in range (self.start_wiersz_ekranu, self.start_wiersz_ekranu+self.liczba_wierszy_planszy):
            wiersz_planszy += 1
            for kolumna in range (0,self.liczba_kolumn_planszy):
                    
                #ustawiamy kolor guzika co drugi ciemny na przemian z białym
                
                if(wiersz_planszy%2==0 and kolumna%2==0 or wiersz_planszy%2!=0 and kolumna%2!=0):
                    button_colour = kolory.color_white
                else:
                    button_colour = kolory.color_dark
       
    
                #tworzymy guzik #przy twworzeniu jest amlowany
                object_guzik = Guzik(kolumna, wiersz_ekranu, wiersz_planszy, button_colour, self.rozmiar_pola, self.screen)
            
                #wypelniamy siatkę stworzonym guzikiem
                self.net_buttons[wiersz_planszy][kolumna]= object_guzik
            
                #malujemy guzik
                #object_guzik.draw_button()
                
                
  #tu soobna funkcja maluj siatke w ktorej maluj guziki! ma byc!!!! DO ZROBIENIA              
                
        

           
    
def create_szachownica(screen):
    
    szachownica = Szachownica(screen)
    szachownica.rozmiar_pola()
    szachownica.set_net_buttons()
        
    return szachownica
        
        

                    
                    
                    