import pygame
import os

from elementy_gry import guzik

# klasa -> okno gry

class Screen:   
    """ reprezentuje okno gry """
    def __init__(self):
        
        #okno
        self.pygame_screen = 0   #okno typu pygame przechowuje
        
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
        """ zwraca okno typu Pygame """
        return self.pygame_screen
    
    def get_width(self):
        """ zwraca szerokosc okna """
        return self.width
    
    def get_height(self):
        """ zwraca wysokosc okna """
        return self.height
    
    def get_x(self):
        """ zwraca pozycję x ekranu """
        return self.x
    
    def get_y(self):
        """ zwraca pozycję y ekranu """
        return self.y
    
    #inne
    
    #miejsce pojawienia sie okna z grą
    
    def umiesc_okno(self, x, y):
        """ umieszcza okno na ekranie """
        self.x = x
        self.y = y
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (self.x,self.y)

    #rozmiar okna
    def nadaj_rozmiar(self, width, height):
        """ nadaje rozmiary oknu gry """
        self.width = width
        self.height = height
        
        s=(self.width, self.height)  #zastosowanie krotki
        self.pygame_screen = pygame.display.set_mode(s)
        
        
    #nazwa okienka
    def nadaj_nazwe(self, napis):
        """ nadaje nazwę oknu gry """
        self.napis = napis
        pygame.display.set_caption(napis)
        



class Display():
    """ metody wirtualne, nadpisuje je klasa PygameDisplay """
    #metody wirtualne
    
    def get_okno_pygame(self):
        raise NotImplementedError
    
    def get_okno(self):
        raise NotImplementedError
        
    def maluj_guzik(self, kolor, x_ekranu, y_ekranu, bok_1, bok_2):
        raise NotImplementedError

    def wstaw_napis_na_guziku(self, napis, x_ekranu, y_ekranu, kolor):
        raise NotImplementedError
       
    def maluj_pionek(self, cialo_pionka, kolor_napisu, x_ekranu, y_ekranu):
        raise NotImplementedError
    
    def rysuj_tlo(self, kolor):
        raise NotImplementedError
    
    def wyswietl_komunikat(self, czcionka, rozmiar, kolor, x_ekr, y_ekr, text):
        raise NotImplementedError

    def draw_window_message(self, kolor, x_ekranu, y_ekranu, szerokosc, dlugosc ):
        raise NotImplementedError
                            
    def wstaw_komunikat_dla_gracza(self, message, kolor, x_ekranu, y_ekranu, ilosc_komunikatow):
        raise NotImplementedError
    
    #obsluga guzikow
    
    def obsluga_reset(self, reset_button):
        raise NotImplementedError
            
    def czekaj_na_okey_komunikatu(self, gracz):
        raise NotImplementedError   
                        
    #aktualizacja okna GUI
            
    def aktualizuj_display(self):
        raise NotImplementedError
        
        
    def sprawdz_czy_klikniecie(self):
        raise NotImplementedError
        
    def zwroc_pozycje_myszki(self):
        raise NotImplementedError
    


    
    # Pygame Display dostaje obiekt Screen
    
class PygameDisplay(Display):
    """ metody, które są odpowiedzialne za malowanie na oknie gry """
    
    def __init__(self, okno):
        self.okno = okno
        self.okno_pygame = okno.get_typ_pygame()
        
        
        #get
        
    def get_okno_pygame(self):
        """zwraca okno gry, ale typu Pygame"""
        return self.okno_pygame
    
    def get_okno(self):
        """zwraca okno gry, ale typu Screen"""
        return self.okno
    
        #metody
    
    def maluj_guzik(self, kolor, x_ekranu, y_ekranu, bok_1, bok_2):  
        """maluje guzik"""
        pygame.draw.rect(self.okno_pygame, kolor,[x_ekranu, y_ekranu, bok_1, bok_2])


    def wstaw_napis_na_guziku(self, napis, x_ekranu, y_ekranu, kolor):
        """wstawia dany opis guzika na guzik"""
        cialo = self.smallfont.render(napis , True , kolor)
        self.okno_pygame.blit(cialo, (x_ekranu,y_ekranu))
        
        
    def maluj_pionek(self, cialo_pionka, kolor_napisu, x_ekranu, y_ekranu):
        """maluje pionek na planszy"""
        smallfont = pygame.font.SysFont('Arial',50) 
        napis = smallfont.render(cialo_pionka , True , kolor_napisu)
        self.okno_pygame.blit(napis, (x_ekranu,y_ekranu))      

    
    def rysuj_tlo(self, kolor):
        """maluje tło na dany kolor"""
        pygame.draw.rect(self.okno_pygame, kolor,[0, 0, self.okno.get_width(), self.okno.get_height()])


    def wyswietl_komunikat(self, czcionka, rozmiar, kolor, x_ekr, y_ekr, text):
        """wyswietla komunikat na ekran"""
        self.smallfont = pygame.font.SysFont(czcionka, rozmiar)
        cialo = self.smallfont.render(text, True , kolor)
        self.okno_pygame.blit(cialo, (x_ekr,y_ekr)) 

        
    def draw_window_message(self, kolor, x_ekranu, y_ekranu, szerokosc, dlugosc ):
        """ maluje okno, w którym będą pojawiac się komunikaty o błędach podczas ruchu"""
        pygame.draw.rect(self.okno_pygame, kolor ,[x_ekranu, y_ekranu, szerokosc, dlugosc])  
         
            
    def wstaw_komunikat_dla_gracza(self, message, kolor, x_ekranu, y_ekranu, ilosc_komunikatow):
        """ wstawia komunikat dla gracza o błędzie podczas ruchu"""
        rozmiar_czcionki = 20
        smallfont = pygame.font.SysFont('Arial', rozmiar_czcionki)
        komunikat = message      #string
        wynik = lambda x, y: x*y
        cialo = smallfont.render(komunikat , True , kolor)
        self.okno_pygame.blit(cialo, (x_ekranu,y_ekranu + wynik(rozmiar_czcionki,ilosc_komunikatow))) 
    
    
        #obsluga guzikow
    
    def obsluga_reset(self, reset_button):    
        """ obsluguje przycisk reset gry"""
        while(1):
            klik=False
            
            klik = self.sprawdz_czy_klikniecie()
            
            mouse = self.zwroc_pozycje_myszki()
            
            if(reset_button.sprawdz_czy_najechany(mouse[0], mouse[1]) == True):
                reset_button.podswietl_button(self)
                if(klik==True):
                    return  #konczy sie gdy zresetowane!
            else:
                reset_button.zgas_button(self)   
            self.aktualizuj_display()
        
        
    def czekaj_na_okey_komunikatu(self, gracz):
        """ czeka na przyciśniecie przycisku okey przez gracza"""
        width_ekranu, height_ekranu = self.okno_pygame.get_size()
        guzik_okey = guzik.okey(width_ekranu, height_ekranu, gracz)
        guzik_okey.draw_okey_button(self)
        
        while(1):
            klik=False
            
            klik = self.sprawdz_czy_klikniecie()
            
            mouse = self.zwroc_pozycje_myszki()
            
            if(guzik_okey.sprawdz_czy_najechany(mouse[0], mouse[1]) == True):
                guzik_okey.podswietl_button(self)
                if(klik==True):
                    return  #konczy sie gdy zresetowane!
            else:
                guzik_okey.zgas_button(self)   
            self.aktualizuj_display()        
                        
                
                
      #aktualizacja GUI (obrazu)

    def aktualizuj_display(self):
        """ aktualizuje okno gry, by były widoczne nowe zmiany"""
        pygame.display.update()
        
        
        
        #sprawdza czy użytkownik kliknął myszkę
        
    def sprawdz_czy_klikniecie(self):
        """ sprawdza czy myszka jest kliknięta"""
        for e in pygame.event.get():      
            if e.type == pygame.QUIT: 
                pygame.quit() 
            if e.type == pygame.MOUSEBUTTONDOWN:  #sprawdza czy mysz jest klikana
                return True
        return False
        
        
        
        #zwraca pozycje myszki
        
    def zwroc_pozycje_myszki(self):
        """ zwraca pozycje myszki na ekranie """
        return pygame.mouse.get_pos() 
        
        
        
        
        
        
# FUNKCJA

        
#Tworzy okno o zadanych parametrach

def create_screen_gry():
    """tworzy okno gry, ustawia parametry okna"""
    
    #tworzymy okno gry
    screen = Screen()
    
    #nadaje parametry okna
    screen.umiesc_okno(500, 70)
    height = 900
    screen.nadaj_rozmiar(height+int(height/3), height)
    screen.nadaj_nazwe('Gra -> Warcaby angielskie')
    
    return screen  #zwraca stworzony obiekt screen





    
    