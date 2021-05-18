import kolory
import pygame

class Message:
    
    def __init__(self, napis):
        
        self.text = napis
        
        self.czcionka = 'Arial'
        self.rozmiar = 20
        self.kolor = kolory.color_black
        self.x_ekr = 0
        self.y_ekr = 0
        self.screen = 0
        
        self.wyswietlane = False
        
    def get_text(self):
        return self.text
    
    def wyswietl_komunikat(self, czcionka, rozmiar, kolor, x_ekr, y_ekr, screen):
        
        self.wyswietlane = True
        
        self.czcionka = czcionka
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.x_ekr = x_ekr
        self.y_ekr = y_ekr
        self.screen = screen
        
        self.smallfont = pygame.font.SysFont(self.czcionka, self.rozmiar)
        self.cialo = self.smallfont.render(self.get_text() , True , self.kolor)
        screen.get_typ_pygame().blit(self.cialo, (self.x_ekr,self.y_ekr)) 
        
    def zgas_komunikat(self):
        
        if self.wyswietlane == True:
            self.smallfont = pygame.font.SysFont(self.czcionka, self.rozmiar)
            self.cialo = self.smallfont.render(self.get_text() , True , kolory.color_green)
            self.screen.get_typ_pygame().blit(self.cialo, (self.x_ekr,self.y_ekr)) 
            self.wyswietlane = False
            
        #należące do gracza okienka
        
class Window_message:
    
    def __init__(self, screen, gracz):
        
        self.screen = screen
        self.gracz = gracz
        self.komunikat = 0
        self.ilosc_komunikatow=0
        
        self.rozmiar_czcionki = 20
        
        (width_ekranu, height_ekranu) = (self.screen.get_width(), self.screen.get_height())
                #dlugosci wymiary guzika
        self.dlugosc = 2*(height_ekranu/10)  #jak zwykly guzik 
        self.szerokosc =  height_ekranu   # taka sama 
        
        self.colour = kolory.color_white
        
        if(self.gracz.get_kolor_gracza() == kolory.color_black):
        #umiejscowienie na ekranie
        
            self.x_ekranu = width_ekranu - (1/3*height_ekranu) - (height_ekranu/10)
            self.y_ekranu = 1*(height_ekranu/10)       #tam gdzie zaczyna sie 4 wiersz planszy 1 to tam gdzie se zaczyna plansza
        
        else:
            
            self.x_ekranu = width_ekranu - (1/3*height_ekranu) - (height_ekranu/10)
            self.y_ekranu = 7*(height_ekranu/10)       #tam gdzie zaczyna sie 4 wiersz planszy 1 to tam gdzie se zaczyna plansza
        

        
    def draw_window_message(self):
        
        
        pygame.draw.rect(self.screen.get_typ_pygame(), self.colour,[self.x_ekranu, self.y_ekranu, self.szerokosc, self.dlugosc])      
        
        
        
    def wstaw_komunikat_dla_gracza(self, message):
        
        
        self.smallfont = pygame.font.SysFont('Arial',20)
        self.komunikat = message #typ klasy Message
        
        
        self.cialo = self.smallfont.render(self.komunikat , True , kolory.color_black)
        self.screen.get_typ_pygame().blit(self.cialo, (self.x_ekranu,self.y_ekranu + self.rozmiar_czcionki*self.ilosc_komunikatow)) 
        
        self.ilosc_komunikatow +=1
        
        
        
        
        
        
        
        
        
