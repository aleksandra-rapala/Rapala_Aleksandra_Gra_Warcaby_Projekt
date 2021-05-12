
from kolory import *
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
        self.pionek = 0
        
        #self.draw_button()
        
    def __str__(self): 
        return 'obiekt button, wiersz_planszy = {}, kolumna_planszy={}'.format(self.wiersz_planszy, self.kolumna_planszy)
    
    def __repr__(self): 
        return 'BUTTON([{}][{}])'.format(self.wiersz_planszy, self.kolumna_planszy)
    
    def ustaw_czy_pusty(self, value, pionek):
        self.pusty = value
        self.pionek = pionek
        
    def get_pionek(self):
        return self.pionek
    
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
    
    def get_podswietlony(self):
        return self.podswietlony
    
    
    
        
    def sprawdz_czy_najechany(self, mouse_width, mouse_height):
        
        if (self.x_ekranu < mouse_width < self.x_ekranu+self.bok_1) and (self.y_ekranu < mouse_height < self.y_ekranu+self.bok_2) :

            return True
        else:
            return False
            
    
    def draw_button(self):
        
        #rysuje guzik
        pygame.draw.rect(self.screen,self.colour,[self.x_ekranu, self.y_ekranu, self.bok_1, self.bok_2])
        
        
    def podswietl_button(self):
        
        if(self.podswietlony == False):
            self.podswietlony = True
            
            #malujemy
            pygame.draw.rect(self.screen,color_light,[self.x_ekranu, self.y_ekranu, self.bok_1, self.bok_2])
            #ustawiamy pionek
            if(self.pusty != True):
                self.pionek.maluj_pionek() 
        
        
    def zgas_button(self):
        if(self.podswietlony == True):
            self.podswietlony = False
            self.draw_button()
            if(self.pusty != True):
                self.pionek.maluj_pionek() 
        
            