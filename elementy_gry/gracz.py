from elementy_gry import pionek as p


class Gracz:
    
    def __init__(self, pionki_gracza, kolor):
        
        self.przegrany = False
        self.pionki = pionki_gracza  #lista  juz ustawionych i kolorowych pionkow
        self.kolor_gracza = kolor
        self.mozliwe_ruchy_bez_bicia = []  #1-skad   2-dokad
        self.mozliwe_ruchy_z_biciem = []   #1-skad  2-dokad  3-usuwane pole przeciwnik
        
   
        #set
    def ustaw_przegrany(self, value):
        self.przegrany = value
        
    def ustaw_mozliwe_ruchy_bez_bicia(self, mozliwe_ruchy_bez_bicia):
        self.mozliwe_ruchy_bez_bicia = mozliwe_ruchy_bez_bicia  
        
    def ustaw_mozliwe_ruchy_z_biciem(self, mozliwe_ruchy_z_biciem):
        self.mozliwe_ruchy_z_biciem = mozliwe_ruchy_z_biciem
        
        
        #get
        
    def get_przegrany(self):
        return self.przegrany
    
    def get_pionki(self):
        return self.pionki
    
    def get_kolor_gracza(self):
        return self.kolor_gracza
    
    def get_mozliwe_ruchy_bez_bicia(self):
        return self.mozliwe_ruchy_bez_bicia
    
    def get_mozliwe_ruchy_z_biciem(self):
        return self.mozliwe_ruchy_z_biciem
    
    
    
    
    #metody inne:
    
    
    def szukaj_mozliwe_ruchy_bez_bicia(self, net_buttons):
        
        tmp_mozliwe_ruchy_bez_bicia=[]
        
        for pionek in self.pionki:
            button = pionek.get_button()
            wiersz = button.get_wiersz_planszy()      #wiersz szachownicy
            kolumna = button.get_kolumna_planszy()    #kolumna szachownicy
            
            
            #PIONEK ZWYKŁY
            
            if isinstance(pionek, p.Zwykly_pionek):  #nie da się przekroczyć wiersza
                
                if (kolumna+1) <= 7 : #mozna isć na prawo
                    
                    if (net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna+1]).get_pusty() == True :
                        tmp_mozliwe_ruchy_bez_bicia.append([pionek, net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna+1]])
                        
                if kolumna-1 >= 0: #można isć na lewo
                    
                    if (net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna-1]).get_pusty() == True :
                        tmp_mozliwe_ruchy_bez_bicia.append([pionek, net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna-1]])       
          
        
            #DAMKA
            
            elif isinstance(pionek, p.Damka): # przy damce trzeba juz sprawdzać wiersze, aby nie przekroczyć
                
                for kierunek_damki in pionek.get_kierunek_ruchu(): #tu tablica dwuelementowa
                    
                    if( wiersz + kierunek_damki <=7 and  wiersz + kierunek_damki>=0): #nie przekracza wiersza
                            
                        if (kolumna+1) <= 7 : #mozna isc na prawo
                            if (net_buttons[wiersz + kierunek_damki][kolumna+1]).get_pusty() == True : #jezeli puste pole
                                tmp_mozliwe_ruchy_bez_bicia.append([pionek, net_buttons[wiersz + kierunek_damki][kolumna+1]])
                        
                        if kolumna-1 >= 0: #mozna isc na lewo
                            if (net_buttons[wiersz + kierunek_damki][kolumna-1]).get_pusty() == True : #jezeli puste pole
                                tmp_mozliwe_ruchy_bez_bicia.append([pionek, net_buttons[wiersz + kierunek_damki][kolumna-1]])
                                
            self.ustaw_mozliwe_ruchy_bez_bicia(tmp_mozliwe_ruchy_bez_bicia)                  
                              
  
    
    
 
        
        
        
    def szukaj_mozliwe_ruchy_z_biciem(self, net_buttons):
        
        
        tmp_mozliwe_ruchy_z_biciem=[]
        
        for pionek in self.pionki:
            
            button = pionek.get_button()

            wiersz = button.get_wiersz_planszy()      #wiersz szachownicy
            kolumna = button.get_kolumna_planszy()    #kolumna szachownicy
            
            
            #PIONEK ZWYKŁY
            
            if isinstance(pionek, p.Zwykly_pionek):        
        
                if( wiersz + 2*pionek.get_kierunek_ruchu() <=7 and  wiersz + 2*pionek.get_kierunek_ruchu()>=0): #nie przekracza wiersza   
                
                    if (kolumna+2) <= 7 : #mozna isc na prawo
                        if (net_buttons[wiersz + 2*pionek.get_kierunek_ruchu()][kolumna+2]).get_pusty() == True :   #puste miejsce
                            #ale jeszcze sprawdzamy czy na poprzednim polu stoi przeciwnik
                            if ((net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna+1]).get_pusty() == False) : #jesli cos stoi
                                #to sprawdzamy czy to przeciwnik:
                                if (net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna+1].get_pionek()).get_colour()!=pionek.get_colour():
                                   #dodaj bicie
                                    tmp_mozliwe_ruchy_z_biciem.append([pionek, net_buttons[wiersz + 2*pionek.get_kierunek_ruchu()][kolumna+2], net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna+1]])
                        
                    if kolumna-2 >= 0: #mozna isc na lewo
 
                        if (net_buttons[wiersz + 2*pionek.get_kierunek_ruchu()][kolumna-2]).get_pusty() == True :   #puste miejsce
                            #ale jeszcze sprawdzamy czy na poprzednim polu stoi przeciwnik
                            if ((net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna-1]).get_pusty() == False) : #jesli cos stoi
                                #to sprawdzamy czy to przeciwnik:
                                if (net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna-1].get_pionek()).get_colour()!=pionek.get_colour():
                                   #dodaj bicie
                                    tmp_mozliwe_ruchy_z_biciem.append([pionek, net_buttons[wiersz + 2*pionek.get_kierunek_ruchu()][kolumna-2], net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna-1]])
                        
        
        
        
        
            # DAMKA
            
            elif isinstance(pionek, p.Damka):
                
                for kierunek_damki in pionek.get_kierunek_ruchu(): #tu tablica dwuelementowa                
                
                    if( wiersz + 2*kierunek_damki <=7 and  wiersz + 2*kierunek_damki>=0): #nie przekracza wiersza   
                
                        if (kolumna+2) <= 7 : #mozna isc na prawo
                            if (net_buttons[wiersz + 2*kierunek_damki][kolumna+2]).get_pusty() == True :   #puste miejsce
                                #ale jeszcze sprawdzamy czy na poprzednim polu stoi przeciwnik
                                if ((net_buttons[wiersz + kierunek_damki][kolumna+1]).get_pusty() == False) : #jesli cos stoi
                                    #to sprawdzamy czy to przeciwnik:
                                    if (net_buttons[wiersz + kierunek_damki][kolumna+1].get_pionek()).get_colour()!=pionek.get_colour():
                                       #dodaj bicie
                                        tmp_mozliwe_ruchy_z_biciem.append([pionek, net_buttons[wiersz + 2*kierunek_damki][kolumna+2], net_buttons[wiersz + kierunek_damki][kolumna+1]])
                        
                        if kolumna-2 >= 0: #mozna isc na lewo
 
                            if (net_buttons[wiersz + 2*kierunek_damki][kolumna-2]).get_pusty() == True :   #puste miejsce
                                #ale jeszcze sprawdzamy czy na poprzednim polu stoi przeciwnik
                                if ((net_buttons[wiersz + kierunek_damki][kolumna-1]).get_pusty() == False) : #jesli cos stoi
                                    #to sprawdzamy czy to przeciwnik:
                                    if (net_buttons[wiersz + kierunek_damki][kolumna-1].get_pionek()).get_colour()!=pionek.get_colour():
                                       #dodaj bicie
                                        tmp_mozliwe_ruchy_z_biciem.append([pionek, net_buttons[wiersz + 2*kierunek_damki][kolumna-2], net_buttons[wiersz + kierunek_damki][kolumna-1]])                
                
                
        self.ustaw_mozliwe_ruchy_z_biciem(tmp_mozliwe_ruchy_z_biciem)
                
                    
                
                
                
                
                
                
                
                
                
                
                
                
        