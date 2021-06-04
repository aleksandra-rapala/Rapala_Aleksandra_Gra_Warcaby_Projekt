from gui import kolory

class Guzik:
        
    
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
        
    def get_podswietlony(self):
        return self.podswietlony
     
    def sprawdz_czy_najechany(self, mouse_width, mouse_height):
        
        #pomocnicza lambda
        dodawanie = lambda x, y : x + y
        
        if (self.x_ekranu < mouse_width < dodawanie(self.x_ekranu,self.bok_1)) and (self.y_ekranu < mouse_height < dodawanie(self.y_ekranu,self.bok_2)) :

            return True
        else:
            return False
            
    
    #dla GUI
    
    def draw_button(self, display):
        display.maluj_guzik(self.colour_aktualny, self.x_ekranu, self.y_ekranu, self.bok_1, self.bok_2)
        
        
    def podswietl_button(self, display):
            self.colour_aktualny = kolory.color_light
            self.draw_button(display)
            
    def zgas_button(self, display):

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
    
    def __init__(self, x, y, colour, dlugosc_boku1, dlugosc_boku2, wiersz_planszy):
        super().__init__(x, y, colour, dlugosc_boku1, dlugosc_boku2)
        
        #umiejscowie na planszy
        self.wiersz_planszy = wiersz_planszy
        self.kolumna_planszy = x
        
        self.pusty = True
        self.pionek = 0
        
        #set
        
    def ustaw_czy_pusty(self, value, pionek):
        self.pusty = value
        self.pionek = pionek
        
        
        # get
        
    def get_pionek(self):
        return self.pionek
    
    def get_pusty(self):
        return self.pusty
    
    
    # ewentualne metody, gdyby były potrzebne do reprezentacji w konsoli
    def __str__(self): 
        return 'obiekt button, wiersz_planszy = {}, kolumna_planszy={}'.format(self.wiersz_planszy, self.kolumna_planszy)
    
    def __repr__(self): 
        return 'BUTTON([{}][{}])'.format(self.wiersz_planszy, self.kolumna_planszy)
    
    # dla GUI
    
    #nadpisujemy metode z klasy bazowej
    def podswietl_button(self, display):
        
        Guzik.podswietl_button(self, display)
            
        #ustawiamy pionek
        if(self.pusty != True):
            self.pionek.maluj_pionek(display) 
        
        
       #nadopisujemy metode z klasy bazowej 
    def zgas_button(self, display):

        Guzik.zgas_button(self, display)
            
            #ustawiamy pionek
        if(self.pusty != True):
            self.pionek.maluj_pionek(display) 
                
                
                
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////                
                
    
      
class Reset_button(Guzik):
    
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
        Guzik.podswietl_button(self, display)
        display.wstaw_napis_na_guziku(self.napis, self.x_ekranu, self.y_ekranu, kolory.color_black)
            
    def zgas_button(self, display):
        Guzik.zgas_button(self, display)
        display.wstaw_napis_na_guziku(self.napis, self.x_ekranu, self.y_ekranu, kolory.color_black)
            

    def draw_reset_button(self, display):
        Guzik.draw_button(self, display)
        display.wstaw_napis_na_guziku(self.napis, self.x_ekranu, self.y_ekranu, kolory.color_black)
   
        
        
       
        
        
        
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////        
        
        
        
class okey(Guzik):
    
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
        Guzik.podswietl_button(self, display)
        display.wstaw_napis_na_guziku(self.napis, self.x_ekranu, self.y_ekranu, kolory.color_black) 
            
    def zgas_button(self, display):
        Guzik.zgas_button(self, display)
        display.wstaw_napis_na_guziku(self.napis, self.x_ekranu, self.y_ekranu, kolory.color_black) 
        
    def draw_okey_button(self, display):
        Guzik.draw_button(self, display)
        display.wstaw_napis_na_guziku(self.napis, self.x_ekranu, self.y_ekranu, kolory.color_black)        
        
     
        
        
        
        
    
    
    