import kolory
import pygame

class Pionek:
    
    def __init__(self, kolor):
        
        
        self.button = 0  #na ktorym stoi
        self.colour = kolor
        
        self.smallfont = pygame.font.SysFont('Arial',80) 
        self.podniesiony = False
        
        
    def ustaw_na_polu(self, button):
        self.button = button
        self.button.get_pygame_screen().blit(self.cialo, (self.button.get_x_ekranu(),self.button.get_y_ekranu())) 
        # nakłada tekst na przycisk
        
        
    def get_button(self):
        return self.button
        
       
         
        
class Zwykly_pionek(Pionek):
    
    def __init__(self, kolor):
        super().__init__(kolor)
        
        if(self.colour == kolory.color_white):
            self.kierunek_ruchu = -1
            self.cialo = self.smallfont.render('B' , True , kolory.color_white) 
        else:
            self.kierunek_ruchu = 1
            self.cialo = self.smallfont.render('C' , True , kolory.color_white)
            
        
    def ustaw_na_polu(self, button):
        Pionek.ustaw_na_polu(self, button)
    
    def get_button(self):
        return Pionek.get_button(self)
        
    def get_kierunek_ruchu(self):
        return self.kierunek_ruchu
    
    
    
    
    
class Damka(Pionek):
    
    def __init__(self, kolor):
        super().__init__(kolor)
        
        self.kierunek_ruchu = [-1,1]
        self.cialo = self.smallfont.render('C' , True , kolory.color_white)
        
        
    def ustaw_na_polu(self, button):
        Pionek.ustaw_na_polu(self, button)    
        
    def get_button(self):
        return Pionek.get_button(self)        
        
    def get_kierunek_ruchu(self):
        return self.kierunek_ruchu        
        
        
        