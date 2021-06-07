import random

class Snake:
    def __init__(self, head, tail):
        self._head = head
        self._tail = tail
    @property
    def head(self):
        return self._head
    @head.setter 
    def head(self,head):
        self._head = head
    @property
    def tail(self):
        return self._tail
    @tail.setter
    def tail(self,tail):
        self._tail = tail

class Ladder:
    def __init__(self, head, tail):
        self._head = head
        self._tail = tail
    @property
    def head(self):
        return self._head
    @head.setter 
    def head(self,head):
        self._head = head
    @property
    def tail(self):
        return self._tail
    @tail.setter
    def tail(self,tail):
        self._tail = tail

class SnakeAndLadderBoard:
    _size = 0
    def __init__(self,size,snakes_list, ladders_list, position = -1):
        self._size = size
        self._snakes = snakes_list
        self._ladders = ladders_list
        self._position = position

    @property
    def size(self):
        return self._size
    @property
    def position(self):
        return self._position
    @property
    def snakes(self):
        return self._snakes
    @property
    def ladders(self):
        return self._ladders

class Dice:
    def roll_dice(self):
        return random.randint(1,6)

class CrookedDice:
    def roll_dice(self):
        return random.randrange(2,7,2)

class SnakeAndLadderService:
   
    def __init__(self,size,snakes_list,ladders_list,dice_choice):
        self.SnakeAndLadderBoardInstance =SnakeAndLadderBoard(size,snakes_list,ladders_list,-1)
        self.dice_choice = dice_choice

    def PositionAfterHittingSnakeLadder(self,currentPosition):
        #print('enter')
        previousPosition = -1
        while (currentPosition != previousPosition):
            previousPosition = currentPosition
            for snake in self.SnakeAndLadderBoardInstance.snakes:
                #print(snake.head)
                if(int(snake.head) == currentPosition):
                    #print('bingo')
                    currentPosition = int(snake.tail)
            for ladder in self.SnakeAndLadderBoardInstance.ladders:
                #print(ladder.tail)
                if(int(ladder.tail) == currentPosition):
                    #print('bingo')
                    currentPosition = int(ladder.head)
        return currentPosition

    def move(self,currentPosition,steps):
        size = self.SnakeAndLadderBoardInstance.size
        boardSize = int(size)
        newPosition = currentPosition + steps 
        if(newPosition > boardSize):
            newPosition = currentPosition
        else:
            newPosition = SnakeAndLadderService.PositionAfterHittingSnakeLadder(newPosition)
        print('Player rolled %d and moved to position %d in board' %(steps,newPosition))
        return newPosition
    
    def getDiceValue(self):
        dice = Dice()
        return dice.roll_dice()

    def getCrookedDiceValue(self):
        dice = CrookedDice()
        return dice.roll_dice()

    def hasPlayerWon(self):
        if(self.SnakeAndLadderBoardInstance.position == self.SnakeAndLadderBoardInstance.size):
            return True

    def startGame(self):
        print('Game Started')
        currentPosition = 0
        for x in range(1,11):
            if(self.dice_choice == 1):
                dice_value = SnakeAndLadderService.getDiceValue()
            else:
                dice_value = SnakeAndLadderService.getCrookedDiceValue()

            print('Dice Roll %d' % dice_value)
            newPosition = SnakeAndLadderService.move(currentPosition, dice_value)
            if(SnakeAndLadderService.hasPlayerWon()):
                print('Player won the Game')
                break
            currentPosition = newPosition

board_size = int(input("Enter the board size:"))
num_snakes = int(input("Enter the number of snakes:"))
snakes_list = []

print('Enter head position followed by tail position for each snake: ')
for i in range(1,num_snakes+1):
    x, y = [x for x in input().split()]
    snake = Snake(x,y)  
    snakes_list.append(snake)

for snake in snakes_list:
    print(snake)

num_ladders = int(input("Enter the number of ladders:"))
ladders_list  = []
print('Enter head position followed by tail position for each ladder: ')
for i in range(1,num_ladders+1):
    x, y = [x for x in input().split()]  
    ladder = Ladder(x,y)
    ladders_list.append(ladder)

a= int(input('Enter 1 to use normal dice and 2 to use crooked dice: '))



SnakeAndLadderService = SnakeAndLadderService(board_size,snakes_list,ladders_list,a)
SnakeAndLadderService.startGame()
