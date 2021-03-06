from random import shuffle

class Blackjack:
 values={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
  
 def play(self):
  '''play a game'''   
  d = GameOfCards()
  d.mix()
  
  bank = Main('Bank')
  player = Main('Player')

  # gives two cards to the player and two to the bank
  for i in range(2):  
    player.addCard(d.getCard())
    bank.addCard(d.getCard())


  # show the hands
  bank.showMain()
  player.showMain()

  # as long as the player ask for a Card!, The bank gets cards
  response = input('Card? Oui or non? (By defautt oui) ')
  while response in ['','o','O','oui','Oui']:
    c = d.getCard()
    print("You have:")
    print(c)
    player.addCard(c)
    if self.total(player) > 21:
       print("You have passed 21. You have lost.")
       return   
    response = input('Card? Oui or non? (by default oui) ')

  # the bank play with those rules  
  while self.total(bank) < 17:
    c = d.getCard()
    print("The bank has:")
    print(c)
    bank.addCard(c)
    if self.total(bank) > 21:
       print("The bank has passed 21. You have won.")
       return

  # if 21 is has not been passed, compare the hands to find the winner  
  self.compare(bank, player)

      
 def total(self, main):
    ''' (Main) -> int
    calculate the sum of all the cards' values in the hand
    '''
    
    # to be completed
    
    # calculate the sum of all the cards' values in the hand
    
    # while the sum > 21 and there are Aces, deduct 10 points for each Ace

    #Calling class
    a = Blackjack
    b = Card

    #Initializing varbiables
    total_sum = 0
    counter = 0


    #Adding all the values in the players hand
    for i in range (len(main.card_list)):
        b = main.card_list[i]
        c = a.values[b.value]
        if b.value == "A":
            counter += 1
        total_sum += c


        #Subtract from sum if there is an ace when sum is greater than 21
        if total_sum>21 and b.value == "A" and counter != 0:
            total_sum -= 10
            counter = 0

    return total_sum

    

 def compare(self, bank, player):
    ''' (Main, Main) -> None
    Compare the main of the player with the hand of the bank
    et affiche de messages
    '''

    total_player = self.total(player)
    total_bank = self.total(bank)

    #Comparing total values of player and bank
    if total_bank > total_player:
        print ("You have lost")

    elif total_bank < total_player:
        print ('You have won')

    #If neither is bigger it compares game conditions
    else:

        #Tie if bank and player both have 21 and 2 cards 
        if total_bank == 21 and len(Bank.Cards) == 2 and total_player == 21  and len(Player.Cards) ==2:
            print ('Equality')

        #Since player doesn't have 2, bank will win with 21 and 2 cards 
        elif total_bank == 21 and len(Bank.Cards) == 2:
            print ('You have lost')

        #Means bank has >2 cards and player wins if total is 21 
        elif total_player == 21:
            print ('You have won')

        #Regular tie 
        else:
            print ('Equality')
            
    

       
class Main(object):
    '''represents a main of cards to play'''

    def __init__(self, player):
        '''(Main, str)-> none
        initializes the player's name and the card list with list being empty'''

        self.player = player
        self.card_list = []

    def addCard(self, card):
        '''(Main, Card) -> None
        add a card to the hand'''

        self.card_list.append(card)
        
    def showMain(self):
        '''(Main)-> None
        display the player's name and the hand'''

        print(self.player, self.card_list)
                
    def __eq__(self, other):
        '''returns True if the hands have the same cards in the same order'''
        
        return self.card == other.card

    def __repr__(self):
        '''returns a representation of the object'''
        
        return str(self.card)

class Card:
    '''represente a card to play'''

    def __init__(self, value, color):
        '''(Carte,str,str)->None        
        initializes the value and the color of the card'''
        self.value = value
        self.color = color  # spade, heart, club or diamond

    def __repr__(self):
        '''(Carte)->str
        returns the representation of the object'''
        return 'Card('+self.value+', '+self.color+')'

    def __eq__(self, other):
        '''(Card,Card)->bool
        self == other if the value and color are the same'''
        return self.value == other.value and self.color == other.color

class GameOfCards:
    '''represente the game of 52 cards'''
    # values and colors are variables of class
    values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    colors = ['\u2660', '\u2661', '\u2662', '\u2663']
    # colors is a set of 4 symbols Unicode that represents the 4 colors
    # spade, heart, club ou diamond
    
    def __init__(self):
        'initializes the packet of 52 cards'
        self.packet = []          # packet is empty at the start
        for color in GameOfCards.colors: 
            for value in GameOfCards.values: # variables of the class
                # add a card of value and color
                self.packet.append(Card(value,color))

    def getCard(self):
        '''(GameOfCards)->Card
        distribute a card, the first from the packet'''
        return self.packet.pop()

    def mix(self):
        '''(GameOfCards)->None
        to mix the card game'''
        shuffle(self.packet)

    def __repr__(self):
        '''returns a representation of the object'''
        return 'Packet('+str(self.packet)+')'

    def __eq__(self, other):
        '''return True if the packets are the same cards in the same order'''
        return self.packet == other.packet
    
    
b = Blackjack()
b.play()

