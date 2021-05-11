from pionek import *

class Gracz:
    
    def __init__(self, pionki_gracza):
        
        self.pionki = pionki_gracza  #lista  juz ustawionych i kolorowych pionkow
        
        self.mozliwe_ruchy_bez_bicia = []
        self.mozliwe_ruchy_z_biciem = []
        
    
    def get_mozliwe_ruchy_bez_bicia(self):
        
        self.szukaj_mozliwe_ruchy_bez_bicia()
        return self.mozliwe_ruchy_bez_bicia
    
    
    def szukaj_mozliwe_ruchy_bez_bicia(self):
        
        for pionek in self.pionki:
            
            button = pionek.get_button()
            #print(button)
            wiersz = button.get_wiersz_planszy()      #wiersz szachownicy
            kolumna = button.get_kolumna_planszy()    #kolumna szachownicy
            
            
            if isinstance(pionek, Zwykly_pionek):  #nie da się przekroczyc wiersza po akzdym ruchu pionek zwykly zamieniany da mke
                
                if (kolumna+1) <= 7 : #mozna isc na prawo
                    
                    if (net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna+1]).get_pusty() == True :
                        mozliwy_ruch.append(pionek, net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna+1])
                        
                elif kolumna-1 >= 0: #mozna isc na lewo
                    
                    if (net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna-1]).get_pusty() == True :
                        mozliwy_ruch.append(pionek, net_buttons[wiersz + pionek.get_kierunek_ruchu()][kolumna-1])       
        
        
        
        
            elif isinstance(pionek, Damka): # przy damce trzeba juz sprawdzac wiersze, a by nie przekroczyc
                
                
                    
                for kierunek_damki in pionek.get_kierunek(): #tu tablica dwuelementowa
                    
                    if( wiersz + kierunek_damki <=7 and  wiersz + kierunek_damki>=0): #nie przekracza wiersza
                            
                        if (kolumna+1) <= 7 : #mozna isc na prawo
                            if (net_buttons[wiersz + kierunek_damki][kolumna+1]).get_pusty() == True : #jezeli puste pole
                                mozliwy_ruch.append(pionek, net_buttons[wiersz + kierunek_damki][kolumna+1])
                        
                        elif kolumna-1 >= 0: #mozna isc na lewo
                            if (net_buttons[wiersz + kierunek_damki][kolumna-1]).get_pusty() == True : #jezeli puste pole
                                mozliwy_ruch.append(pionek, net_buttons[wiersz + kierunek_damki][kolumna-1])
                                
                                
                              
  
        
    def szukaj_mozliwe_ruchy_z_biciem(self):
        
        def __init__(self):
            self.nic = 0
        
        
        
        
        