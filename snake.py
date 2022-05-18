from turtle import Turtle

# array di posizioni dei segmenti dello snake...
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

# variabili globali

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):  # costruttore
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # creazione dei segmenti e posizionamento
        for position in STARTING_POSITION:
            self.add_segment(position)

    # aggiunge segmenti allo snake
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # aggiunge un nuovo segmento allo snake
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # far mouvere i segmenti del serpente in automatico
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # comandi del player

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
