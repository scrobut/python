import forca
import begin
print("***********************")
print("********* game ********")
print("***********************")

print("(1) - FORCA or (2) - advin")
game = int(input("what?:"))
if(game == 1):
    print("Forca")
    forca.playGameForca()
elif(game == 2 ):
    print("Advin")
    begin.playGameAdvin()



