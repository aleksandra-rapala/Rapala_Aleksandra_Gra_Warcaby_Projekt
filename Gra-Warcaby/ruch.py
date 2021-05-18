import pygame
import pionek
import messages

class Ruch:
    
    def __init__(self, aktualny_gracz, net_buttons, gra, przeciwnik):
        
        
        self.proby = 3
        self.przeciwnik = przeciwnik
        self.czas = 500000
        self.skad = 0 
        self.dokad = 0
        self.ruch =0
        self.zbity = False
        
        self.dozwolony = False

        
        self.z_biciem=False
        self.net_buttons = net_buttons
        self.gracz = aktualny_gracz
        
        
        self.gra = gra
        


    
    def zaaktualizuj_ruch(self):
        
        self.gra.rysuj_plansze()
        pygame.display.update()
        
    
    def pobierz_ruch_uzytkownika(self):
        
        
        self.gracz.szukaj_mozliwe_ruchy_z_biciem(self.net_buttons)
        self.gracz.szukaj_mozliwe_ruchy_bez_bicia(self.net_buttons)
        
        #print("Moje ruchy bez biciem: ",self.gracz.get_mozliwe_ruchy_bez_bicia())
        #print("Moje ruchy z bicia: ",self.gracz.get_mozliwe_ruchy_z_biciem())
        
        #tu mozna and
        
        if len(self.gracz.get_mozliwe_ruchy_bez_bicia()) + len(self.gracz.get_mozliwe_ruchy_z_biciem())==0:
            self.przeciwnik.ustaw_wygrany(True)
            return False #koniec gry
        
        if len(self.gracz.get_pionki()) ==0:
            self.przeciwnik.ustaw_wygrany(True)
            return False  #koniec gry
        
        
        
        while(self.proby!=0):
            
            #print("hej while")
            
            self.skad = self.wybierz_swoj_pionek() 
            if(self.skad) == False:     #nie udalo sie pobrac, minął czas
                return True #gra idzie dalej
            
            self.dokad= self.wybierz_pole(self.skad) #tutaj nie mozemy gasic guzika wybranego w skad!
            if(self.dokad) == False:     #nie udalo sie pobrac minal czas
                return True
        
        #////
        
            ruch = [self.skad.get_pionek(), self.dokad]
            #print("Ruch: ", ruch)
            self.dozwolony = self.sprawdz_czy_dozwolony(ruch)
        
            if self.dozwolony == True:
                self.wykonaj_ruch()
                
                #hmm ale tylko moze wykonac ruch jesli jest z biciem
                if(self.z_biciem == True):
                    #to sprawdzamy czy ma kolejne bicie 
                    self.gracz.szukaj_mozliwe_ruchy_z_biciem(self.net_buttons)
                    if len(self.gracz.get_mozliwe_ruchy_z_biciem())>0:    
                        ruch_kolejny = Ruch(self.gracz, self.net_buttons, self.gra, self.przeciwnik)
                        status = ruch_kolejny.pobierz_ruch_uzytkownika()
                        
                        if status==False:
                            self.przeciwnik.ustaw_wygrany(True)
                            
                        return status
                    
                return True
            
            else:
                self.gra.aktualizuj_plansze()
                error = messages.Window_message(self.gra.get_screen(), self.gracz)
                error.wstaw_komunikat_dla_gracza("Ruch nie dozwolony! Sprobuj jeszcze raz!")
                self.proby -= 1
                error.wstaw_komunikat_dla_gracza(f"Masz jeszcze prob: {self.proby}")
        
        return True
        
        
        
        
        
    def sprawdz_czy_dozwolony(self, ruch):

            #tu moze podobny przyklad poprawic jak z wielbladem na lekcji#sprawdzic czy dziala in tak jak bylo poprzednio
            
        for mozliwosc in self.gracz.get_mozliwe_ruchy_z_biciem():
            if ruch[0]==mozliwosc[0] and ruch[1]== mozliwosc[1]:
               # print("ok:", ruch[0], mozliwosc[0], ruch[1], mozliwosc[1])
                self.z_biciem = True
                self.zbity = mozliwosc[2]
                return True
            #else:
               # print("nie ok:", ruch[0], mozliwosc[0], ruch[1], mozliwosc[1])
        
        for mozliwosc in self.gracz.get_mozliwe_ruchy_bez_bicia():
            if ruch[0]==mozliwosc[0] and ruch[1] == mozliwosc[1] and  len(self.gracz.get_mozliwe_ruchy_z_biciem())==0:
                return True
        
        return False

   
    
    def wykonaj_ruch(self):
        
        #print("wykonuje sie ruch ")
        #pionek dostaje przypisany guzik, a guzik przypisany pionek i ze jest zajety
        
        #WYKONANIE RUCHU
        self.skad.get_pionek().ustaw_na_polu(self.dokad)  #przenosimy pionek
        self.skad.ustaw_czy_pusty(True, None) #stary guzik robi sie pusty

        # EENTUALNE ZMIANY WYKONANE PO WYKONANIU RUCHU
        if self.z_biciem == True: # to trzeba usunac pionek uzytkownika z pola miedzy stad a dokad
            
            
            print(self.przeciwnik.get_pionki())
            print(self.zbity.get_pionek())
            self.zbity.get_pionek()
            
            self.przeciwnik.get_pionki().remove(self.zbity.get_pionek())  #usuwamy ale u przeciwnika!!!!!
            self.zbity.ustaw_czy_pusty(True, None) #stary guzik robi sie pusty 
            
            
            
            
        if isinstance(self.dokad.get_pionek(), pionek.Zwykly_pionek) and (self.dokad.get_wiersz_planszy()==0 or self.dokad.get_wiersz_planszy()==7):   #zamiana na krolowke
            

            #print("ZAMIENIAM NA DAMKE:")
                  
            #kopia = self.dokad.get_pionek().copy()
            
            damka = self.dokad.get_pionek().zamien_na_damke(self.gracz.get_pionki()) #dokad ma juz przesuniety pionek obecny ktory staje damka
                  
                
                
            #print("z damka bez pionka:",self.gracz.get_pionki() )
            

              
        
        self.zaaktualizuj_ruch()   
        
        
    
    
    
    
    
    def wybierz_swoj_pionek(self):

        while(self.czas!=0):   
            klik=False
            #print(self.czas)
            
            for e in pygame.event.get():      
                if e.type == pygame.QUIT: 
                    pygame.quit() 
                if e.type == pygame.MOUSEBUTTONDOWN:  #sprawdza czy mysz jest klikana
                    klik=True
            
            mouse = pygame.mouse.get_pos() 
            
            for wiersz_guzikow in self.net_buttons:
                for guzik in wiersz_guzikow:
                    
                    najechany = guzik.sprawdz_czy_najechany(mouse[0], mouse[1])
                
                    if(najechany == True):
                        guzik.podswietl_button()
                        if klik==True:
                            prawidlowy = self.sprawdz_czy_prawidlowy_pionek(guzik)
                            if prawidlowy==True:
                                return guzik #GUZIKA NIE GASIMY!!!!!!!

                    else:
                        guzik.zgas_button()
            pygame.display.update() 
            self.czas -= 1
            
        #jezeli czas sie skonczyl to zgasmy ostatnio najechany guzik:
        
        
        for wiersz_guzikow in self.net_buttons:
            for guzik in wiersz_guzikow:
                
                if guzik.get_podswietlony() == True:
                    guzik.zgas_button() 
        
        return False #nie udalo sie pobrac danych
            
            
            
            
    #sprawdza czy gracz wybral w pierwszym etapie swojego ruchu swoj pionek
    
    def sprawdz_czy_prawidlowy_pionek(self, button):
        
        if(button.get_pusty() == True):

            self.gra.aktualizuj_plansze()
            error = messages.Window_message(self.gra.get_screen(), self.gracz)
            error.wstaw_komunikat_dla_gracza("Blad tu nie ma twojego pionka!")
            error.wstaw_komunikat_dla_gracza("To pole jest puste!")
            error.wstaw_komunikat_dla_gracza("Sprobuj jeszcze raz!")
            return False
        
        #nie jest pusty to czy jest to pionek gracza:
        
        if(button.get_pionek().get_colour() != self.gracz.get_kolor_gracza()):
            self.gra.aktualizuj_plansze()
            error = messages.Window_message(self.gra.get_screen(), self.gracz)
            error.wstaw_komunikat_dla_gracza("Blad tu nie ma twojego pionka!")
            error.wstaw_komunikat_dla_gracza("To pionek twojego przeciwnika!")
            error.wstaw_komunikat_dla_gracza("Sprobuj jeszcze raz!")
            return False
        
        else:
            return True
       
            
        
        
        
        
        
        
        
        
        
            
          #wybiera pole dokad postawic wybrnay wczzesniej pionek  
            
    def wybierz_pole(self, wylaczony_guzik):

        while(self.czas!=0):
            klik=False
            #print(self.czas)
            
            for e in pygame.event.get():      
                if e.type == pygame.QUIT: 
                    pygame.quit() 
                if e.type == pygame.MOUSEBUTTONDOWN:  #sprawdza czy mysz jest klikana
                    klik=True
            
            mouse = pygame.mouse.get_pos() 
            
            for wiersz_guzikow in self.net_buttons:
                for guzik in wiersz_guzikow:
                    
                    najechany = guzik.sprawdz_czy_najechany(mouse[0], mouse[1])
                
                    if(najechany == True):
                        if wylaczony_guzik != guzik:
                            guzik.podswietl_button()
                            if klik==True:
                                prawidlowe = self.sprawdz_czy_prawidlowe_pole(guzik)
                                if prawidlowe==True:                                
                                    return guzik #GUZIKA NIE GASIMY!!!!!!!
 
                    else:
                        if wylaczony_guzik != guzik:
                            guzik.zgas_button()
            pygame.display.update() 
            self.czas -= 1
        
        
        #wychodzmy z petli i gasimy guzik jesli zostal najechany bo gracz juz nie ma wyrou skonczyla sie jego kolej
        for wiersz_guzikow in self.net_buttons:
            for guzik in wiersz_guzikow:
                
                if guzik.get_podswietlony() == True:
                    guzik.zgas_button() 
            
        return False  #nie udlo sie pobrac danych    
            
            
            
    def sprawdz_czy_prawidlowe_pole(self, button):
        
        if(button.get_pusty() == True):
            return True
        else:
            self.gra.aktualizuj_plansze()
            error = messages.Window_message(self.gra.get_screen(), self.gracz)
            error.wstaw_komunikat_dla_gracza("To pole jest już zajęte!")
            return False
        

            
            