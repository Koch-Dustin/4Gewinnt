from typing import Optional
from Player import Player
from Board import Board
from StatusValidator import StatusValidator

class MainGame:
  
  def __init__(self) -> None:
    self.firstPlayer : Player = Player()
    self.secondPlayer : Player = Player()
    self.board : Board = Board()
    self.round = 0
    
  def PrepareGame(self):
    self.firstPlayer.name = self.GetUserName("Player 1")
    self.secondPlayer.name = self.GetUserName("Player 2")
    
    self.firstPlayer.marker = "X"
    self.secondPlayer.marker = "O"
    
    Player.marker = "X"
    
    print(Player.marker)
    
  def Round(self):
    self.round += 1
    if self.round > 21:
      return Player()
    print(f"Current Round: {self.round}")
    player = self.Turn(self.firstPlayer)
    if not player.won:
      player = self.Turn(self.secondPlayer)
      
    if player.won:
      return player
    
  def Play(self):
    while True:
      player = self.Round()
      print(player)
      
      if player is not None:
        break
    
    if player.name == "":
      print("Tie!")
    else:
      print(f"{player.name} has won the Game!")
  
  def GetUserName(self, playerName: str) -> str:
    userName: str = input(f"{playerName}: Please enter your name: ")

    inputIsValid: bool = userName.isalpha() and len(userName) > 0
    if inputIsValid:
        return userName
    else:
        print(f"Your input '{userName}' is unvalid. Try again!")
        
  def GetRowInput(self, playerName):
    while True:
      rowInputAsString = input(f"{playerName}: Select a row to put your coin: ")

      try:
        rowInputAsInt = int(rowInputAsString)
        minimumRowNumber = 1
        maximumRowNumber = 7
      
        if rowInputAsInt >= minimumRowNumber and rowInputAsInt <= maximumRowNumber:
          return rowInputAsInt
        else: 
          print(f"Your input '{rowInputAsInt}' is invalid. Try again!")
      except ValueError:
        print("Please enter a number")
    
  def Turn(self, player : Player) -> Player:
    self.board.ShowBoard()
    
    while True: 
      row : int  = self.GetRowInput(player.name)
      
      if self.board.IsValidTurn(row):
        self.board.AddCoinToBoard(row, player.marker)
        
        if StatusValidator.IsWin(self.board, str(player.marker), row):
          player.won = True
        break
      
      else:
        print(f"Your cant put your coin in row '{row}'. Try again!")
      
    
