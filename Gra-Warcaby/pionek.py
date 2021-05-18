import kolory
import pygame

class Pionek:
    
    def __init__(self, kolor, id_pionka):
        
        self.id_pionka = id_pionka  #numeracja od 1 do 12 (gdy powtaje królówka nadal ma to samo id
        
        self.button = 0  #na ktorym stoi
        self.colour = kolor
        
        self.smallfont = pygame.font.SysFont('Arial',80) 
        self.podniesiony = False
        

        
        
    def ustaw_na_polu(self, button):
        
            print("ustawiam")
            button.ustaw_czy_pusty(False, self)
            self.button = button
        
            #self.button.get_pygame_screen().blit(self.cialo, (self.button.get_x_ekranu(),self.button.get_y_ekranu())) 
            # nakłada tekst na przycisk
            self.ustawiony=True

    

    
    def get_id_pionka(self):
        return self.id_pionka
    
    def maluj_pionek(self):
         self.button.get_pygame_screen().blit(self.cialo, (self.button.get_x_ekranu(),self.button.get_y_ekranu()))
        
    def get_colour(self):
        return self.colour
    
    def get_button(self):
        return self.button
        
    def __str__(self): 
        return 'obiekt pionek, id_pionka = {},'.format(self.id_pionka)
    
    def __repr__(self): 
        return 'PIONEK({})'.format(self.id_pionka)
         
        
class Zwykly_pionek(Pionek):
    
    def __init__(self, kolor, id_pionka):
        super().__init__(kolor, id_pionka)
        
        if(self.colour == kolory.color_white):
            self.kierunek_ruchu = -1
            self.cialo = self.smallfont.render('B' , True , kolory.color_white) 
        else:
            self.kierunek_ruchu = 1
            self.cialo = self.smallfont.render('C' , True , kolory.color_white)
            
        
    def ustaw_na_polu(self, button):
        return Pionek.ustaw_na_polu(self, button)
    
    def get_button(self):
        return Pionek.get_button(self)
        
    def get_kierunek_ruchu(self):
        return self.kierunek_ruchu
    
    def zamien_na_damke(self, pionki_gracza):
        
        damka = Damka(self.get_colour(), self.get_id_pionka())
        damka.ustaw_na_polu(self.get_button())
        
        pionki_gracza.remove(self)  
        pionki_gracza.append(damka)
        
           
        
        return damka    
    
    
    
class Damka(Pionek):
    
    def __init__(self, kolor, id_pionka):
        super().__init__(kolor, id_pionka)
        
        self.kierunek_ruchu = [-1,1]
        
        if self.colour == kolory.color_white:
            self.cialo = self.smallfont.render('Db' , True , kolory.color_white)
        else:
            self.cialo = self.smallfont.render('Dc' , True , kolory.color_white)            
        
        
    def ustaw_na_polu(self, button):
        return Pionek.ustaw_na_polu(self, button)    
        
    def get_button(self):
        return Pionek.get_button(self)        
        
    def get_kierunek_ruchu(self):
        return self.kierunek_ruchu        
        
    def __str__(self): 
        return 'obiekt damka, id_pionka = {},'.format(self.id_pionka)
    
    def __repr__(self): 
        return 'DAMKA({})'.format(self.id_pionka)        
        