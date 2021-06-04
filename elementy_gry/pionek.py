from gui import kolory


class Pionek:
    
    def __init__(self, kolor, id_pionka):
        
        self.id_pionka = id_pionka  #numeracja od 1 do 12 (gdy powtaje królówka nadal ma to samo id
        self.button = 0  #na ktorym stoi
        self.colour = kolor
        self.podniesiony = False
        

          #set
            
    def ustaw_na_polu(self, button):
        button.ustaw_czy_pusty(False, self)
        self.button = button
        self.ustawiony=True


        #get
        
    def get_id_pionka(self):
        return self.id_pionka
    
    def get_colour(self):
        return self.colour
    
    def get_button(self):
        return self.button
    
    
        #dla GUI
    
    def maluj_pionek(self, display):
        display.maluj_pionek(self.cialo, kolory.color_white, self.button.get_x_ekranu(), self.button.get_y_ekranu())
  

    #wirtualna
    
    def get_kierunek_ruchu(self):
        raise NotImplementedError
        
    def zamien_na_damke(self):
        raise NotImplementedError
    
    #ewentualna reprezentacja pionka, gdyby była potrzebna do pokazania w konsoli
    
    def __str__(self): 
        return 'obiekt pionek, id_pionka = {},'.format(self.id_pionka)
    
    def __repr__(self): 
        return 'PIONEK({})'.format(self.id_pionka)
         
        
 #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////       
        
        
class Zwykly_pionek(Pionek):                        #ma dodatkowo self.kierunek_ruchu + self.cialo
    
    def __init__(self, kolor, id_pionka):
        super().__init__(kolor, id_pionka)
        
        if(self.colour == kolory.color_white):
            self.kierunek_ruchu = -1
            self.cialo = 'B'
        else:
            self.kierunek_ruchu = 1
            self.cialo = 'C'
        
        #set
        

        
    def get_kierunek_ruchu(self):
        return self.kierunek_ruchu
    
    
    #inna metoda
    
    def zamien_na_damke(self, pionki_gracza):
        
        damka = Damka(self.get_colour(), self.get_id_pionka())
        damka.ustaw_na_polu(self.get_button())
        
        pionki_gracza.remove(self)  
        pionki_gracza.append(damka)

        return damka    
    
#///////////////////////////////////////////////////////////////////////////////////////////////////////////    
    
class Damka(Pionek):
    
    def __init__(self, kolor, id_pionka):
        super().__init__(kolor, id_pionka)
        
        self.kierunek_ruchu = [-1,1]
        
        if self.colour == kolory.color_white:
            self.cialo = 'Bd'
        else:
            self.cialo = 'Cd'         
        
        #set
        
   
        
    def get_kierunek_ruchu(self):
        return self.kierunek_ruchu   
    
    
    #ewentualna reprezentacja pionka, gdyby była potrzebna do pokazania w konsoli:      
        
    def __str__(self): 
        return 'obiekt damka, id_pionka = {},'.format(self.id_pionka)
    
    def __repr__(self): 
        return 'DAMKA({})'.format(self.id_pionka)        
        