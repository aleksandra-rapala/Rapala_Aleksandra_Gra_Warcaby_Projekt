from gui import screen
from elementy_gry import gra


screen1 = screen.create_screen_gry()    #tworzymy okno gry (okno, (wazne parametry: rozmiar_okna)) metoda create_screen zwraca to okno
display1 = screen.PygameDisplay(screen1)      #odpowiedzialne za GUI - dostepne funkcje malowania po oknie

gra1 = gra.Gra(display1)             #stworzone okno jest przekazywane dla obiektu stworzonego obiektu gry
gra1.start()                        #na obiekcie gry wykonujemy start, a więc rozpoczyna się gra