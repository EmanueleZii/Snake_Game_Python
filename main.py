# importare il modulo turtle grapichs e screen
from turtle import Screen
# importare le classi custom
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# importa il modulo time (framerate)
import time

# impostazioni dello schermo
screen = Screen()
screen.setup(width=600, height=600)  # risoluzione
screen.bgcolor("black")  # colore dello schermo
screen.tracer(0)
screen.title("Snake Game")  # titolo della finestra

# instanziare gli oggetti delle classi custom
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
# comandi del player
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True  # variabile bool che determina se il gioco è finito

while game_is_on:
    screen.update()  # aggiorna lo schermo
    time.sleep(0.1)  # impostare il frame e velocita del gioco
    snake.move()  # fa muovere lo snake in automatico

    # rilevare la collisione con il cibo
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # rilevare le collisioni con il muro
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # rilevare la collisione con la coda
    for segment in snake.segments[1:]:  # [1:] taglia la testa dello snake dal resto del corpo per non rilevarla
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()  # per evitare che la finestra si chiuda subito aspetta il comando...
