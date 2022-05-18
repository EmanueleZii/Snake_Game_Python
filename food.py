from turtle import Turtle  # importa il modulo grafico Turtle
import random  # importa il modulo random


# eredita dalla classe Turtle
class Food(Turtle):

    def __init__(self):  # costruttore
        super().__init__()  # superclasse
        self.shape("circle")  # la forma del cibo
        self.penup()  # nasconde la linea di default di Turtle
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # le dimensione del cibo
        self.color("blue")  # il colore del cibo
        self.speed("fastest")  # la velocita di posizionamento e apparizione
        self.refresh()  # aggiorna la posizione del cibo sullo schermo

    # riposiziona il cibo nello schermo
    def refresh(self):
        rand_x = random.randint(-280, -280)  # evita che il cibo si posizioni nel muro del game over
        rand_y = random.randint(-280, -280)  # evita che il cibo si posizioni nel muro del game over
        self.goto(rand_x, rand_y)  # generazione casuale della posizione del cibo
