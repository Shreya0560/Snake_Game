from turtle import Turtle
#These are constants
square_positions = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
#The Snake class is responsible for creating and moving the snake
class Snake:

    def __init__(self):
        #Creating a new attribute which holds all the squares
        self.squares = []
        self.create_snake()
        #attribute which refers to the first square
        self.head = self.squares[0]


    def create_snake(self):
        for position in square_positions:
            self.add_square(position)


    def add_square(self, position):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square) 
        
    def extend(self):
        self.add_square(self.squares[-1].position())

    def reset(self):
        for square in self.squares:
            #Previous snake disappears when game resets
            square.goto(1000,1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]


    #Using self as a parameter allows different instances of the Snake class or different Snake objects to have different attributes and states. Allows us to perform functions on each instance indepedently
    def move(self):
        # start        #stop,#step
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)
        self.squares[0].forward(20)

    #In the snake game, snakes cannot move in the opposite direction they are facing in, bc it would cause them to touch themselves
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
