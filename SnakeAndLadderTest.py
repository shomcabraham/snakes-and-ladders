import unittest
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
            newPosition = SnakeAndLadderService.PositionAfterHittingSnakeLadder(self,newPosition)
        print('Player rolled %d and moved to position %d in board' %(steps,newPosition))
        return newPosition
    
    def getDiceValue(self):
        dice = Dice()
        return dice.roll_dice()

    def getCrookedDiceValue(self):
        dice = CrookedDice()
        return dice.roll_dice()

    def hasPlayerWon(self,position):
        if(position == int(self.SnakeAndLadderBoardInstance.size)):
            return True

    def startGame(self):
        print('Game Started')
        currentPosition = 0
        for x in range(1,11):
            if(self.dice_choice == 1):
                dice_value = SnakeAndLadderService.getDiceValue(self)
            else:
                dice_value = SnakeAndLadderService.getCrookedDiceValue(self)

            print('Dice Roll %d' % dice_value)
            newPosition = SnakeAndLadderService.move(self,currentPosition, dice_value)
            if(SnakeAndLadderService.hasPlayerWon(self,newPosition)):
                print('Player won the Game')
                break
            currentPosition = newPosition

class TestMethods(unittest.TestCase):
    def setup(self): # Set up the board
        self.board_size = 25
        self.snakes_list = []
        self.ladders_list = []
        self.dice_type = 1
        snake = Snake(14,8)
        self.snakes_list.append(snake)
        snake = Snake(12,1)
        self.snakes_list.append(snake)
        snake = Snake(23,7)
        self.snakes_list.append(snake)
        ladder = Ladder(13,2)
        self.ladders_list.append(ladder)
        ladder = Ladder(9,3)
        self.ladders_list.append(ladder)
        ladder = Ladder(20,4)
        self.ladders_list.append(ladder)     

    def testMovement(self): # Check if the position moves from 6 to 9 on a dice value of 3
        self.setup()
        SnakeAndLadderServiceInstance = SnakeAndLadderService(self.board_size,self.snakes_list,self.ladders_list,self.dice_type)
        currentPosition = 6
        dice_value = 3
        newPosition = SnakeAndLadderServiceInstance.move(currentPosition, dice_value)
        self.assertEqual(newPosition,9)

    def testSnakeBite(self): # According to the current board Snake head is at position 12 and tail at 1
        self.setup()
        SnakeAndLadderServiceInstance = SnakeAndLadderService(self.board_size,self.snakes_list,self.ladders_list,self.dice_type)
        currentPosition = 10
        dice_value = 2
        newPosition = SnakeAndLadderServiceInstance.move(currentPosition, dice_value)
        self.assertEqual(newPosition,1)

    def testLadderJump(self): # According to the current configuration there is a ladder jump from 4 to 20
        self.setup()
        SnakeAndLadderServiceInstance = SnakeAndLadderService(self.board_size,self.snakes_list,self.ladders_list,self.dice_type)
        currentPosition = 2
        dice_value = 2
        newPosition = SnakeAndLadderServiceInstance.move(currentPosition, dice_value)
        self.assertEqual(newPosition,20)

    def testWinning(self): #Check if the player is declared a winner on reaching board size (i.e., 25)
        self.setup()
        SnakeAndLadderServiceInstance = SnakeAndLadderService(self.board_size,self.snakes_list,self.ladders_list,self.dice_type)
        currentPosition = 23
        dice_value = 2
        newPosition = SnakeAndLadderServiceInstance.move(currentPosition, dice_value)
        result = SnakeAndLadderServiceInstance.hasPlayerWon(newPosition)
        self.assertEqual(result,True)

    def testMovementAfterReachingBoardEnd(self): # Check that it stays at same position after reaching board end for the next round
        self.setup()
        SnakeAndLadderServiceInstance = SnakeAndLadderService(self.board_size,self.snakes_list,self.ladders_list,self.dice_type)
        currentPosition = 25
        dice_value = 4
        newPosition = SnakeAndLadderServiceInstance.move(currentPosition, dice_value)
        self.assertEqual(newPosition,25)




    
    
    


