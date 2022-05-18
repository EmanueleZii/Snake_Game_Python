from turtle import Turtle  # importa il modulo grafico Turtle

# variabili
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


# eredita dalla classe Turtle
class Scoreboard(Turtle):

    def __init__(self):  # costruttore
        super().__init__()  # crea la super class
        self.score = 0  # punteggio del player
        self.color("white")  # colore della scritta
        self.penup()  # toglie la linea di movimento
        self.goto(0, 270)  # posiziona la scritta
        self.hideturtle()  # nasconde le movenze delle tartaruge di default del module turtle (per far sembrare che strisciano)
        self.update_scoreboard()  # aggiorna la scritta

    # scrive Score con il punteggio aggiornato
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # incrementa il punteggio del player
    def increase_score(self):
        self.score += 1  # aumenta di 1 il punteggio
        self.clear()  # pulisce la scritta dalle vecchie scritte
        self.update_scoreboard()  # aggiorna la scritta

    # fa apparire la scritta Game Over
    def game_over(self):
        self.goto(0, 0)  # posiziona la scritta nello schermo
        self.color("white")  # colore della scritta
        self.write(f"Game Over!", align=ALIGNMENT, font=FONT)  # scrive la scritta al centro Game Over
