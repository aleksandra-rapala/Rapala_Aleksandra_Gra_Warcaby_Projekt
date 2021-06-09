from gui import kolory

class Guzik:
        
    """reprezentacja guzika"""
    def __init__(self, x, y, colour, dlugosc_boku1, dlugosc_boku2):
            
        #wymiary
        self.bok_1=dlugosc_boku1
        self.bok_2=dlugosc_boku2
        
        #umiejscowienie na ekranie
        
        #pomocnicza lambda
        mnozenie = lambda x, y : x * y
        
        self.x_ekranu = mnozenie(x,self.bok_1)
        self.y_ekranu = mnozenie(y,self.bok_2)
        
        
        #kolor
        self.colour_aktualny = colour
        self.colour_staly = colour
        
       
           #get   
                   
    def get_x_ekranu(self):
        """zwraca pozycje x ekranu"""
        return self.x_ekranu
    
    def get_y_ekranu(self):
        """zwraca pozycje y ekranu"""
        return self.y_ekranu
    
    def get_wiersz_planszy(self):
        """zwraca wiersz planszy na którym jest guzik"""
        return self.wiersz_planszy
    
    def get_kolumna_planszy(self):
        """zwraca kolumnę planszy na której jest guzik"""
        return self.kolumna_planszy  

    def pobierz_bok_1(self):
        """zwraca dlugosc boku1 guzika"""
        return self.bok_1
    
    def pobierz_bok_2(self):
        """zwraca dlugosc boku2 guzika"""
        return self.bok_2
        
    def get_podswietlony(self):
        """zwraca informację o tym, czy guzik jest aktualnie podświetlony"""
        return self.podswietlony
     
    def sprawdz_czy_najechany(self, mouse_width, mouse_height):
        """sprwadza czy guzik jest aktualnie najechany myszką"""
        #pomocnicza lambda
        dodawanie = lambda x, y : x + y
        
        if (self.x_ekranu < mouse_width < dodawanie(self.x_ekranu,self.bok_1)) and (self.y_ekranu < mouse_height < dodawanie(self.y_ekranu,self.bok_2)) :

            return True
        else:
            return False
            
    
    #dla GUI
    
    def draw_button(self, display):
        """maluje guzik"""
        display.maluj_guzik(self.colour_aktualny, self.x_ekranu, self.y_ekranu, self.bok_1, self.bok_2)
        
        
    def podswietl_button(self, display):
        """podświetla guzik"""
        self.colour_aktualny = kolory.color_light
        self.draw_button(display)
            
    def zgas_button(self, display):
        """gasi guzik"""
        self.colour_aktualny = self.colour_staly
        self.draw_button(display)

    
    #wirtualne
    
    def get_pionek(self):
        raise NotImplementedError
        
    def get_pusty(self):
        raise NotImplementedError
        
    def ustaw_czy_pusty(Self):
        raise NotImplementedError
            
            
 #///////////////////////////////////////////////////////////////////////////           
            
            

class Guzik_planszy(Guzik):
    """guzik planszy, a więc pole planszy"""
    def __init__(self, x, y, colour, dlugosc_boku1, dlugosc_boku2, wiersz_planszy):
        super().__init__(x, y, colour, dlugosc_boku1, dlugosc_boku2)
        
        #umiejscowie na planszy
        self.wiersz_planszy = wiersz_planszy
        self.kolumna_planszy = x
        
        self.pusty = True
        self.pionek = 0
        
        #set
        
    def ustaw_czy_pusty(self, value, pionek):
        """ustawia, czy pole jest puste, czy zajęte przez dany pionek"""
        self.pusty = value
        self.pionek = pionek
        
        
        # get
        
    def get_pionek(self):
        """zwraca pionek znajdujący się na guziku"""
        return self.pionek
    
    def get_pusty(self):
        """zwraca informację, czy na polu stoi pionek, czy nie"""
        return self.pusty
    
    
    # ewentualne metody, gdyby były potrzebne do reprezentacji w konsoli
    def __str__(self): 
        return 'obiekt button, wiersz_planszy = {}, kolumna_planszy={}'.format(self.wiersz_planszy, self.kolumna_planszy)
    
    def __repr__(self): 
        return 'BUTTON([{}][{}])'.format(self.wiersz_planszy, self.kolumna_planszy)
    
    # dla GUI
    
    #nadpisujemy metode z klasy bazowej
    def podswietl_button(self, display):
        """podświetla guzik"""
        Guzik.podswietl_button(self, display)
            
        #ustawiamy pionek
        if(self.pusty != True):
            self.pionek.maluj_pionek(display) 
        
        
       #nadopisujemy metode z klasy bazowej 
    def zgas_button(self, display):
        """gasi guzik"""
        Guzik.zgas_button(self, display)
            
            #ustawiamy pionek
        if(self.pusty != True):
            self.pionek.maluj_pionek(display) 
                
                
                
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////                
                
    
      
class Reset_button(Guzik):
    """guzik odpowiedzialny za resetowanie gry"""
    def __init__(self, width_ekranu, height_ekranu):      
    
        self.x_ekranu = width_ekranu - (1/3*height_ekranu)
        self.y_ekranu = (1+3.5)*(height_ekranu/10)       #tam gdzie zaczyna sie 4 wiersz planszy 1 to tam gdzie se zaczyna plansza
        
        #dlugosci wymiary guzika
        self.bok_2 = (height_ekranu/10)  #jak zwykly guzik 
        self.bok_1 =  1/3*2/3*height_ekranu   # taka sama 
        
        self.colour_staly = kolory.color_white
        self.colour_aktualny = kolory.color_white
        
        self.napis = 'RESET'
        
     

    #dla GUI    
        
    def podswietl_button(self, display):
        """podswietla guzik"""
        Guzik.podswietl_button(self, display)
        display.wstaw_napis_na_guziku(self.napis, self.x_ekranu, self.y_ekranu, kolory.color_black)
            
    def zgas_button(self, display):
        """gasi guzik"""
        Guzik.zgas_button(self, display)
        display.wstaw_napis_na_guziku(self.napis, self.x_ekranu, self.y_ekranu, kolory.color_black)
            

    def draw_reset_button(self, display):
        """maluje reset guzik"""
        Guzik.draw_button(self, display)
        display.wstaw_napis_na_guziku(self.napis, self.x_ekranu, self.y_ekranu, kolory.color_black)
   
        
        
       
        
        
        
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////        
        
        
        
class okey(Guzik):
    """guzik okey"""
    def __init__(self, width_ekranu, height_ekranu, gracz):
              
        self.gracz = gracz
        
        if self.gracz.get_kolor_gracza() == kolory.color_white :
            
            self.x_ekranu = width_ekranu - (1/3*height_ekranu) - (height_ekranu/10)
            self.y_ekranu = 7*(height_ekranu/10)+100        #tam gdzie zaczyna sie 4 wiersz planszy 1 to tam gdzie se zaczyna plansza
        
        else:
            self.x_ekranu = width_ekranu - (1/3*height_ekranu) - (height_ekranu/10)
            self.y_ekranu = 1*(height_ekranu/10)+100          
        
                
        #dlugosci wymiary guzika
        self.bok_2 = 80
        self.bok_1 =  190
        
        self.colour_staly = kolory.color_yellow
        self.colour_aktualny = kolory.color_yellow
        
        self.napis = 'OKEY'
        
     
   
    #dla GUI    
        
    def podswietl_button(self, display):
        """podswietla guzik"""
        Guzik.podswietl_button(self, display)
        display.wstaw_napis_na_guziku(self.napis, self.x_ekranu, self.y_ekranu, kolory.color_black) 
            
    def zgas_button(self, display):
        """gasi guzik"""
        Guzik.zgas_button(self, display)
        display.wstaw_napis_na_guziku(self.napis, self.x_ekranu, self.y_ekranu, kolory.color_black) 
        
    def draw_okey_button(self, display):
        """maluje guzik okey"""
        Guzik.draw_button(self, display)
        display.wstaw_napis_na_guziku(self.napis, self.x_ekranu, self.y_ekranu, kolory.color_black)        
        
     
        
        
        
        
    
    
    