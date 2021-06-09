from elementy_gry import pionek
from elementy_gry import guzik
from elementy_gry import szachownica
from komunikaty import wyjatki
from komunikaty import messages
from gui import kolory



class Ruch:
    """reprezentacja ruchu w grze"""
    def __init__(self, aktualny_gracz, net_buttons, gra, przeciwnik):
        
        self.przeciwnik = przeciwnik
        self.skad = 0 
        self.dokad = 0
        self.ruch =0
        self.zbity = False
        
        self.dozwolony = False

        self.z_biciem=False
        self.net_buttons = net_buttons
        self.gracz = aktualny_gracz
        
        self.gra = gra
        

        #dla gui
    def zaaktualizuj_ruch(self):
        """aktualizuje ruch, aby był widoczny w oknie gry"""
        self.gra.rysuj_plansze()
        self.gra.get_display().aktualizuj_display()
        
        
        
        #set
    def ustaw_skad_ruch(self, guzik_skad):
        """ustawia z jakiego pola jest wykonywany ruch"""
        self.skad=guzik_skad
        
    def ustaw_dokad_ruch(self, guzik_dokad):
        """ustawia na jakie pole pionek zostaje przestawiony"""
        self.dokad=guzik_dokad
        
    def ustaw_czy_z_biciem(self, value):
        """ustawia czy ruch jest z biciem"""
        self.z_biciem = value 
    
    def ustaw_zbity_guzik(self, guzik):
        """ustawia, jaki pionek jest zbity, czyli do usunięcia z gry"""
        self.zbity = guzik
               
            
            
            
            
            
        #funkcje sprawdzajace
        
    def sprawdz_czy_gracz_przegrywa(self):  #true jesli przegrywa  false jeśli nie prsegrywa i może wykonać ruch
        """sprawdza czy w danych ruchu gracz przegrywa, czyli ma brak pionków lub brak ruchu"""
        if len(self.gracz.get_mozliwe_ruchy_bez_bicia()) + len(self.gracz.get_mozliwe_ruchy_z_biciem())==0:
            self.gracz.ustaw_przegrany(True)
            return True #KONIEC GRY
        
        if len(self.gracz.get_pionki()) ==0:
            self.gracz.ustaw_przegrany(True)
            return True  #KONIEC GRY
        
        return False
    
    
    def sprawdz_czy_dozwolony(self, ruch):  #tru jesli dozwolony False jesli niedozwolony
        """sprawdza czy ruch jest dozwolony"""
        for mozliwosc in self.gracz.get_mozliwe_ruchy_z_biciem():
            if ruch[0]==mozliwosc[0] and ruch[1]== mozliwosc[1]:
                self.ustaw_czy_z_biciem(True)
                self.ustaw_zbity_guzik(mozliwosc[2])  #guzik
                return True
        
        for mozliwosc in self.gracz.get_mozliwe_ruchy_bez_bicia():
            if ruch[0]==mozliwosc[0] and ruch[1] == mozliwosc[1] and  len(self.gracz.get_mozliwe_ruchy_z_biciem())==0:
                return True
        
        return False
    
    
    def czy_kolejne_bicie(self):  #zwraca czy bedzie kolejne bicie czy nie
        """sprawdza czy aktualny gracz ma mozliwy kolejny ruch z biciem"""
        if(self.z_biciem == True):
            #to sprawdzamy czy ma kolejne bicie 
                        
            self.gracz.szukaj_mozliwe_ruchy_z_biciem(self.net_buttons)
                    
            #wyczyscic czyli zostawic tylko te dla tego pionka ktory zbijal aktualnie:
            tmp_mozliwe_ruchy_z_biciem = self.gracz.get_mozliwe_ruchy_z_biciem()
                    
            for count, mozliwy_ruch_z_biciem in enumerate (self.gracz.get_mozliwe_ruchy_z_biciem()):
                if mozliwy_ruch_z_biciem[0] != self.dokad.get_pionek():
                    tmp_mozliwe_ruchy_z_biciem.pop(count)
                           
            self.gracz.ustaw_mozliwe_ruchy_z_biciem(tmp_mozliwe_ruchy_z_biciem)
    
                    
            if len(self.gracz.get_mozliwe_ruchy_z_biciem())>0:   
                return True 
            
        return False

    
    
    
    
    
    
   #PODSTAWOWA FUNKCJA WYKONYWANIE RUCHU
    
    def pobierz_ruch_uzytkownika(self):
        """pobiera ruch użytkownika"""
        self.gracz.szukaj_mozliwe_ruchy_z_biciem(self.net_buttons)
        self.gracz.szukaj_mozliwe_ruchy_bez_bicia(self.net_buttons)
        
        if self.sprawdz_czy_gracz_przegrywa() == True:
            return False #koniec gry -> ktorys gracz przegral status zakonczenia bez ustawienia reset
        
        
        while(1):        
            self.ustaw_skad_ruch(self.wybierz_swoj_pionek())            #albo zwraca guzik albo false gdy reset
        
            #byc moze ktos wcisnal reset
            if(self.skad==False):
                self.gra.resetuj_gre()
                return False #status zakonczenia gry przez reset (False) czyli reset tez ustawiony
            
            #w przeciwnym wypadku gracz wybral prawidlowo pionek wiec idziemy dalej:
            
            self.ustaw_dokad_ruch(self.wybierz_pole(self.skad)) #tutaj nie mozemy gasic guzika wybranego w skad, zwraca guzik lub F if rest
            if(self.dokad==False):
                self.gra.resetuj_gre()
                return False #status zakonczenia gry przez reset (False) czyli reset tez ustawiony

        #////  WŁAŚCIWE WYKONYWANIE RUCHU
        
            ruch = [self.skad.get_pionek(), self.dokad]
            self.dozwolony = self.sprawdz_czy_dozwolony(ruch)
            try:
                if self.dozwolony == True:
                    self.wykonaj_ruch()
                    self.zaaktualizuj_ruch() 
                
                    #SPRAWDZA CZY KOLEJNE BICIE SKOK JESLI ZBIL KOGOS (uwaga jesli to damka to już nie moze byc kolejnego ruchu!)
                    
                    if(self.czy_kolejne_bicie()==True and isinstance(self.dokad.get_pionek(), pionek.Zwykly_pionek)):  #rekurencja
                        ruch_kolejny = Ruch(self.gracz, self.net_buttons, self.gra, self.przeciwnik)
                        status = ruch_kolejny.pobierz_ruch_uzytkownika()
                        return status  #true gdy OK, false gdy RESET LUB false gdy przegral ale tu nie moze przgerac! bo to ewentualny dodatkowy ruch! 
                    else:
                        return True

                else:
                    raise wyjatki.ErrorRuchNiedozwolony("Ruch nie dozwolony! Sprobuj jeszcze raz!")
            except wyjatki.ErrorRuchNiedozwolony as error0:
                wyjatki.wyswietl_wyjatek(self.gra, self.gracz, error0)
                    
                    
                
                


    


        
        #ważna funkcja wykonująca ruch, a więc zmieniające dane gry na aktualne
    

    def wykonaj_ruch(self):
        """wykonanie ruchu, czyli zamiana danych na aktualne"""
        #WYKONANIE RUCHU
        self.skad.get_pionek().ustaw_na_polu(self.dokad)  #przenosimy pionek
        self.skad.ustaw_czy_pusty(True, None) #stary guzik robi sie pusty

        # EWENTUALNE ZMIANY WYKONANE PO WYKONANIU RUCHU
        if self.z_biciem == True: # to trzeba usunac pionek uzytkownika z pola miedzy stad a dokad
            self.przeciwnik.get_pionki().remove(self.zbity.get_pionek())  #usuwamy ale u przeciwnika!!!!!
            self.zbity.ustaw_czy_pusty(True, None) #stary guzik robi sie pusty 

        if isinstance(self.dokad.get_pionek(), pionek.Zwykly_pionek) and (self.dokad.get_wiersz_planszy()==0 or self.dokad.get_wiersz_planszy()==7):   #zamiana na krolowke
            
            self.dokad.get_pionek().zamien_na_damke(self.gracz.get_pionki())

            


            
    
    #dla GUI (interface użytkownika wybieranie przycisków podczas wykonywania ruchu)
    

    def wybierz_swoj_pionek(self):
        """wybor pionka w pierwszym etapie wykonania ruchu"""
        while(1):   
            klik=False
            klik = self.gra.get_display().sprawdz_czy_klikniecie()
            mouse = self.gra.get_display().zwroc_pozycje_myszki()
            szereg_guzikow = szachownica.wygeneruj_net_jako_szereg(self.net_buttons)
            
            for guzik in szereg_guzikow:
                najechany = guzik.sprawdz_czy_najechany(mouse[0], mouse[1])
                if(najechany == True):
                    guzik.podswietl_button(self.gra.get_display())
                    if klik==True:
                        prawidlowy = self.sprawdz_czy_prawidlowy_pionek(guzik)
                        if prawidlowy==True:
                            return guzik #GUZIKA NIE GASIMY!!!!!!! Bo oznacza podniesienie pionka
                else:
                    guzik.zgas_button(self.gra.get_display())
          
            if(self.gra.get_reset_button().sprawdz_czy_najechany(mouse[0], mouse[1]) == True):
                self.gra.get_reset_button().podswietl_button(self.gra.get_display())
                if(klik==True):
                    return False  #gdy przycisnięto reset!!!!! status gry = False  
            else:
                self.gra.get_reset_button().zgas_button(self.gra.get_display())        
            self.gra.get_display().aktualizuj_display()
            
            
   

    def wybierz_pole(self, wylaczony_guzik):
        """wybiera pole w drugim etapie wykonywania ruchu"""
        while(1):        
            klik=False
            klik = self.gra.get_display().sprawdz_czy_klikniecie()
            mouse = self.gra.get_display().zwroc_pozycje_myszki()
            szereg_guzikow = szachownica.wygeneruj_net_jako_szereg(self.net_buttons)
            for guzik in szereg_guzikow:     
                najechany = guzik.sprawdz_czy_najechany(mouse[0], mouse[1]) 
                if(najechany == True):
                    if wylaczony_guzik != guzik:
                        guzik.podswietl_button(self.gra.get_display())
                        if klik==True:                               
                            return guzik #GUZIKA NIE GASIMY!!!!!!
                else:
                    if wylaczony_guzik != guzik:
                        guzik.zgas_button(self.gra.get_display())
            self.gra.get_display().aktualizuj_display() 
        
            if(self.gra.get_reset_button().sprawdz_czy_najechany(mouse[0], mouse[1]) == True):
                self.gra.get_reset_button().podswietl_button(self.gra.get_display())
                if(klik==True):
                    return False  #gdy przycisnięto reset!!!!! status gry = False  
            else:
                self.gra.get_reset_button().zgas_button(self.gra.get_display())      
            self.gra.get_display().aktualizuj_display() 
            
            
            
            
               
        
        
        
   #sprawdza czy gracz wybral w pierwszym etapie swojego ruchu swoj pionek (dla GUI)
    
    def sprawdz_czy_prawidlowy_pionek(self, button):
        """sprawdza czy wybrany pionek jest prawidłowy podczas wykonywania ruchu"""
        try:
                if(button.get_pusty() == True):
                    raise wyjatki.ErrorPolePuste("Brak twojego pionka!-To pole jest puste!")
                    
                if(button.get_pionek().get_colour() != self.gracz.get_kolor_gracza()):
                    raise wyjatki.ErrorPolePrzeciwnika("Brak twojego pionka!-To pole przeciwnika!")
       
        except wyjatki.ErrorPolePuste as error2:
            wyjatki.wyswietl_wyjatek(self.gra, self.gracz, error2 )
            return False   
        except wyjatki.ErrorPolePrzeciwnika as error3:
            wyjatki.wyswietl_wyjatek(self.gra, self.gracz, error3)
            return False
        else:
            return True
        
        
        
        
        
        
        
            
            