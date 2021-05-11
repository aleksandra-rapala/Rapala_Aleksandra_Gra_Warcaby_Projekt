import pygame
import os


# klasa -> okno gry

class Screen:   
    
    def __init__(self):
        
        #okno
        self.pygame_screen = 0   #okno typu pygame
        
        #umiejscowienie na ekranie
        self.x = 0  
        self.y = 0 
        
        #rozmiar okienka
        self.width = 0 
        self.height = 0 

        #podpis okienka
        self.napis = '' #'Gra -> Warcaby'
        
        #zainicjowanie
        pygame.init()
        
        
        
    #ZWRACAJĄCE FUNKCJE
    
    def get_typ_pygame(self):
        return self.pygame_screen
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    #inne
    
    #miejsce pojawienia sie okna z grą
    def umiesc_okno(self, x, y):
    
        self.x = x
        self.y = y
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (self.x,self.y)

    #rozmiar okna
    def nadaj_rozmiar(self, width, height):
        
        self.width = width
        self.height = height
        
        s=(self.width, self.height)
        self.pygame_screen = pygame.display.set_mode(s)
        
        
    #nazwa okienka
    def nadaj_nazwe(self, napis):
    
        self.napis = napis
        pygame.display.set_caption(napis)
        
        
        
        
#Tworzy okno o zadanych parametrach
def create_screen():
    
    #tworzymy okno gdy
    screen = Screen()
    
    #nadaje parametry okna
    screen.umiesc_okno(500, 70)
    height = 900
    screen.nadaj_rozmiar(height+int(height/3), height)
    screen.nadaj_nazwe('Gra -> Warcaby angielskie')
    
    return screen  #zwraca stworzony obiekt
    
    