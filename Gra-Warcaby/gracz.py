from pionek import *


class Gracz:
    
    def __init__(self, pionki_gracza):
        
        self.wygrany = False
        
        self.pionki = pionki_gracza  #lista  juz ustawionych i kolorowych pionkow
        
        self.kolor_gracza = self.pionki[0].get_colour()
        
        self.mozliwe_ruchy_bez_bicia = []  
        self.mozliwe_ruchy_z_biciem = []   #1-skad  2-dokad  3-usuwane pole przeciwnik
        
   
    def ustaw_wygrany(self, value):
        self.wygrany = value
        
        
    def get_wygrany(self):
        return self.wygrany
    
    def get_pionki(self):
        return self.pionki
    
    
    def get_kolor_gracza(self):
        return self.kolor_gracza
    
    
    def get_mozliwe_ruchy_bez_bicia(self):
        return self.mozliwe_ruchy_bez_bicia
    
        
    def get_mozliwe_ruchy_z_biciem(self):
        return self.mozliwe_ruchy_z_biciem
    
    
    def szukaj_mozliwe_ruchy_bez_bicia(self, net_buttons):
        
        self.mozliwe_ruchy_bez_bicia=[]
        
        for pionek in self.pionki:

            button = pionek.get_button()
 
            wiersz = button.get_wiersz_planszy()      #wiersz szachownicy
            kolumna = button.get_kolumna_planszy()    #kolumna szachownicy
            
            
            if isinstance(pionek, Zwykly_pionek):  #nie da się przekroczyc wiersza po akzdym ruchu pionek zwykly zamieniany da mke
                
                if (kolumna+1) <= 7 : #mozna isc na prawo
                    
                    if (net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna+1]).get_pusty() == True :
                        self.mozliwe_ruchy_bez_bicia.append([pionek, net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna+1]])
                        
                if kolumna-1 >= 0: #mozna isc na lewo
                    
                    if (net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna-1]).get_pusty() == True :
                        self.mozliwe_ruchy_bez_bicia.append([pionek, net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna-1]])       
        
   #mozna to jeszcze potem uproscic w petli for     
        
        
            elif isinstance(pionek, Damka): # przy damce trzeba juz sprawdzac wiersze, a by nie przekroczyc
                
                
                    
                for kierunek_damki in pionek.get_kierunek_ruchu(): #tu tablica dwuelementowa
                    
                    if( wiersz + kierunek_damki <=7 and  wiersz + kierunek_damki>=0): #nie przekracza wiersza
                            
                        if (kolumna+1) <= 7 : #mozna isc na prawo
                            if (net_buttons[wiersz + kierunek_damki][kolumna+1]).get_pusty() == True : #jezeli puste pole
                                self.mozliwe_ruchy_bez_bicia.append([pionek, net_buttons[wiersz + kierunek_damki][kolumna+1]])
                        
                        if kolumna-1 >= 0: #mozna isc na lewo
                            if (net_buttons[wiersz + kierunek_damki][kolumna-1]).get_pusty() == True : #jezeli puste pole
                                self.mozliwe_ruchy_bez_bicia.append([pionek, net_buttons[wiersz + kierunek_damki][kolumna-1]])
                                
                                
                              
  
        
    def szukaj_mozliwe_ruchy_z_biciem(self, net_buttons):
        
        self.mozliwe_ruchy_z_biciem=[] #zerują stare
        
        for pionek in self.pionki:
            
            button = pionek.get_button()

            wiersz = button.get_wiersz_planszy()      #wiersz szachownicy
            kolumna = button.get_kolumna_planszy()    #kolumna szachownicy
            
            
            
            if isinstance(pionek, Zwykly_pionek):        
        
                if( wiersz + 2*pionek.get_kierunek_ruchu() <=7 and  wiersz + 2*pionek.get_kierunek_ruchu()>=0): #nie przekracza wiersza   
                
                    if (kolumna+2) <= 7 : #mozna isc na prawo
                        if (net_buttons[wiersz + 2*pionek.get_kierunek_ruchu()][kolumna+2]).get_pusty() == True :   #puste miejsce
                            #ale jeszcze sprawdzamy czy na poprzednim polu stoi przeciwnik
                            if ((net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna+1]).get_pusty() == False) : #jesli cos stoi
                                #to sprawdzamy czy to przeciwnik:
                                if (net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna+1].get_pionek()).get_colour()!=pionek.get_colour():
                                   #dodaj bicie
                                    self.mozliwe_ruchy_z_biciem.append([pionek, net_buttons[wiersz + 2*pionek.get_kierunek_ruchu()][kolumna+2], net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna+1]])
                        
                    if kolumna-2 >= 0: #mozna isc na lewo
 
                        if (net_buttons[wiersz + 2*pionek.get_kierunek_ruchu()][kolumna-2]).get_pusty() == True :   #puste miejsce
                            #ale jeszcze sprawdzamy czy na poprzednim polu stoi przeciwnik
                            if ((net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna-1]).get_pusty() == False) : #jesli cos stoi
                                #to sprawdzamy czy to przeciwnik:
                                if (net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna-1].get_pionek()).get_colour()!=pionek.get_colour():
                                   #dodaj bicie
                                    self.mozliwe_ruchy_z_biciem.append([pionek, net_buttons[wiersz + 2*pionek.get_kierunek_ruchu()][kolumna-2], net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna-1]])
                        
        
        
        
            elif isinstance(pionek, Damka):
                
                for kierunek_damki in pionek.get_kierunek_ruchu(): #tu tablica dwuelementowa                
                
                    if( wiersz + 2*kierunek_damki <=7 and  wiersz + 2*kierunek_damki>=0): #nie przekracza wiersza   
                
                        if (kolumna+2) <= 7 : #mozna isc na prawo
                            if (net_buttons[wiersz + 2*kierunek_damki][kolumna+2]).get_pusty() == True :   #puste miejsce
                                #ale jeszcze sprawdzamy czy na poprzednim polu stoi przeciwnik
                                if ((net_buttons[wiersz + kierunek_damki][kolumna+1]).get_pusty() == False) : #jesli cos stoi
                                    #to sprawdzamy czy to przeciwnik:
                                    if (net_buttons[wiersz + kierunek_damki][kolumna+1].get_pionek()).get_colour()!=pionek.get_colour():
                                       #dodaj bicie
                                        self.mozliwe_ruchy_z_biciem.append([pionek, net_buttons[wiersz + 2*kierunek_damki][kolumna+2], net_buttons[wiersz + kierunek_damki][kolumna+1]])
                        
                        if kolumna-2 >= 0: #mozna isc na lewo
 
                            if (net_buttons[wiersz + 2*kierunek_damki][kolumna-2]).get_pusty() == True :   #puste miejsce
                                #ale jeszcze sprawdzamy czy na poprzednim polu stoi przeciwnik
                                if ((net_buttons[wiersz + kierunek_damki][kolumna-1]).get_pusty() == False) : #jesli cos stoi
                                    #to sprawdzamy czy to przeciwnik:
                                    if (net_buttons[wiersz + kierunek_damki][kolumna-1].get_pionek()).get_colour()!=pionek.get_colour():
                                       #dodaj bicie
                                        self.mozliwe_ruchy_z_biciem.append([pionek, net_buttons[wiersz + 2*kierunek_damki][kolumna-2], net_buttons[wiersz + kierunek_damki][kolumna-1]])                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        