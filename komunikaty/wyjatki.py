from elementy_gry import gra
from gui import kolory
from komunikaty import messages

#sytuacja

class Error(Exception):
    pass

#///////////////////////////////////

class ErrorRuchNiedozwolony(Error):
    def __init__(self, message):
        self.message = message

#/////////////////       
        
class ErrorWyborPionka(Error):
    pass
     

class ErrorPolePuste(ErrorWyborPionka):
    def __init__(self, message):
        self.message = message 

        
class ErrorPolePrzeciwnika(ErrorWyborPionka):
    def __init__(self, message):
        self.message = message

        
#///////////////////////////      
        

    
    #dla GUI wyswietla wyjątek uzytkownikowi w przeznaczonym dla niego okienku
    
def wyswietl_wyjatek(gra, gracz, error_opis):
    
    if(gracz.get_kolor_gracza() == kolory.color_white):
        gra.get_window_message_gracz("bialy").draw_window_message(gra.get_display())
    else:
        gra.get_window_message_gracz("czarny").draw_window_message(gra.get_display())            
            
            
    error = messages.Window_message(gracz, gra.get_display())
    error.wstaw_komunikat_dla_gracza(gra.get_display(), error_opis.message)
            
    gra.get_display().czekaj_na_okey_komunikatu(gracz)
    gra.aktualizuj_plansze()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    