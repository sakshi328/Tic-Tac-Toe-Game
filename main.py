def sum(a,b,c):
   return a + b+ c

def printBoard(xState, zState):
   zero='x' if xState[0] else ('O' if zState[0] else 0)
   One='x' if xState[1] else ('O' if zState[1] else 1)
   Two='x' if xState[2] else ('O' if zState[2] else 2)
   Three='x' if xState[3] else ('O' if zState[3] else 3)
   Four='x' if xState[4] else ('O' if zState[4] else 4)
   Five='x' if xState[5] else ('O' if zState[5] else 5)
   Six='x' if xState[6] else ('O' if zState[6] else 6)
   Seven='x' if xState[7] else ('O' if zState[7] else 7)
   Eight='x' if xState[8] else ('O' if zState[8] else 8)

   print(f"{zero} | {One} | {Two} ")
   print(f"--|---|---")
   print(f"{Three} | {Four} | {Five} ")
   print(f"--|---|---")
   print(f"{Six} | {Seven} | {Eight} ")

def checkWin(xState, zState):
   wins=[[0,1,2], [3,4,5],[6,7,8], [0,3,6], [1,4,7], [2,5,8],
          [0,4,8], [2,4,6]]
   for win in wins:
      if(sum(xState[win[0]], xState[win[1]],xState[win[2]])==3):
         print("X Won the match")
         return 1
      
      if(sum(zState[win[0]], zState[win[1]],zState[win[2]])==3):
         print("O Won the match")
         return 0
   return -1

xState=[0,0,0,0,0,0,0,0,0]
zState=[0,0,0,0,0,0,0,0,0]
turn=1 #1 for X and 0 for o
print("Welcomw to Tic Tac Toe")
while(True):
   printBoard(xState,zState)
   if(turn==1):
      print("x's Chance")
      value=int(input("Please enter a value:"))
      xState[value]=1
      
   else:
      print("O's Chance")
      value=int(input("Please enter a value:"))
      zState[value]=1
      
   cwin= checkWin(xState,zState)
   if(cwin !=-1):
      print("match Over")
      break
   turn=1- turn
      

      


