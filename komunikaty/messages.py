from gui import kolory


# dla tytulu znajdującego sie nad plansza gry "tura bialego" lub "tura czarnego"

class Message_czyja_kolej:
    """ odpowiedzialna za napisy nad planszą, które informują czyja aktualnie jest tura """
    def __init__(self, napis):
        
        self.text = napis
        
        self.czcionka = 'Arial'
        self.rozmiar = 20
        self.kolor = kolory.color_black
        self.x_ekr = 0
        self.y_ekr = 0

        #get
        
    def get_text(self):
        """ zwraca tekst komunikatu """
        return self.text
    
    
        #dla GUI
    def wyswietl_komunikat(self, display, rozmiar, kolor, x_ekr, y_ekr):
        """ wyświetla komunikat """
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.x_ekr = x_ekr
        self.y_ekr = y_ekr
        display.wyswietl_komunikat(self.czcionka, self.rozmiar, self.kolor, self.x_ekr, self.y_ekr, self.text)

        
        
        
            
            
            
        #okienka na komunikaty użytkowników + okienko z komunikatem końca gry
        
        
class Window_message:
    """ okna dla graczy, w których będą się pojawiać komunikaty o błędach podczas wykonywania ruchu """
    def __init__(self, gracz, display):
        
        self.gracz = gracz
        self.komunikat = 0
        self.ilosc_komunikatow=0
        self.rozmiar_czcionki = 20
        (width_ekranu, height_ekranu) = display.get_okno_pygame().get_size()
        
                #dlugosci wymiary guzika
  
        self.dlugosc = 2*(height_ekranu/10)  #jak zwykly guzik 
        self.szerokosc =  height_ekranu   # taka sama 
        self.colour = 0
        
                
        if self.gracz!= None:  #okienko z komunikatem dla graczy (umiejscowienie zależne czy biały czy czarny gracz)
            
            if(self.gracz.get_kolor_gracza() == kolory.color_black):        
                self.x_ekranu = width_ekranu - (1/3*height_ekranu) - (height_ekranu/10)
                self.y_ekranu = 1*(height_ekranu/10)       #tam gdzie zaczyna sie 4 wiersz planszy 1 to tam gdzie se zaczyna plansza
        
            elif(self.gracz.get_kolor_gracza() == kolory.color_white):
                self.x_ekranu = width_ekranu - (1/3*height_ekranu) - (height_ekranu/10)
                self.y_ekranu = 7*(height_ekranu/10)       #tam gdzie zaczyna sie 4 wiersz planszy 1 to tam gdzie se zaczyna plansza
                
            self.colour = kolory.color_white
            
            
            #komunikat dla zakonczenia gry -> okienko z komunikatem końca gry
        else:
            self.colour = kolory.color_yellow
            self.x_ekranu = (1/4)*width_ekranu
            self.y_ekranu = (1/4)*height_ekranu       #tam gdzie zaczyna sie 4 wiersz planszy 1 to tam gdzie se zaczyna plansza
            self.dlugosc =(1/3)* height_ekranu 
            self.szerokosc = (1/3)* height_ekranu   
  
        
    #dla GUI
    
    def draw_window_message(self, display):  #rysuje okienko w  którym gracz dostaje komunikaty
        """ maluje okno """
        display.draw_window_message(self.colour, self.x_ekranu, self.y_ekranu, self.szerokosc, self.dlugosc)
        
             
        
    def wstaw_komunikat_dla_gracza(self, display, message):  #rysuje komunikaty w okienkach
        """ wstawia komunikat do okna """
        display.wstaw_komunikat_dla_gracza(message, kolory.color_black, self.x_ekranu, self.y_ekranu, self.ilosc_komunikatow)
        self.ilosc_komunikatow +=1
        
        
        
        
        
        
        
        
        
