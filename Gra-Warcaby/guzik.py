
#import kolory
import pygame

class Guzik:
        
    
    def __init__(self, x, y, wiersz_planszy, colour, dlugosc_boku, okno):
            
        self.screen = okno.get_typ_pygame()   #okno ale typu pygame
        
        #wymiary
        self.bok_1=dlugosc_boku
        self.bok_2=dlugosc_boku
        
        #umiejscowienie na ekranie
        self.x_ekranu = x*self.bok_1
        self.y_ekranu = y*self.bok_2
        
        #umiejscowie na planszy
        self.wiersz_planszy = wiersz_planszy
        self.kolumna_planszy = x
        
        #kolor
        self.colour = colour
        
        #czy aktualnie wybierane
        self.podswietlony = False
        self.pusty = True
    
    def get_pusty(self):
        return self.pusty
        
    def get_x_ekranu(self):
        return self.x_ekranu
    
    def get_y_ekranu(self):
        return self.y_ekranu
    
    def get_wiersz_planszy(self):
        return self.wiersz_planszy
    
    def get_kolumna_planszy(self):
        return self.kolumna_planszy  
    
    def pobierz_bok_1(self):
        return self.bok_1
    
    def pobierz_bok_2(self):
        return self.bok_2
    
    def get_pygame_screen(self):
        return self.screen
        
    
    
    def draw_button(self):
        
        #rysuje guzik
        pygame.draw.rect(self.screen,self.colour,[self.x_ekranu, self.y_ekranu, self.bok_1, self.bok_2])
        
        
    def podswietl_button(self):
        
        if(self.podswietlony == False):
            self.podswietlony = True
            pygame.draw.rect(self.screen,color_light,[self.x_ekranu, self.y_ekranu, self.bok_1, self.bok_2])
        
    def zgas_button(self):
        if(self.podswietlony == True):
            self.podswietlony = False
            pygame.draw.rect(self.screen, self.colour,[self.x_ekranu, self.y_ekranu, self.bok_1, self.bok_2])
        
        
            