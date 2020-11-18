import numpy as np
import termcolor
import copy
class Sudoku:
    def __init__(self):
        self.InitialData=[]
        self.Data=[]
        self.newData=[]
        self.choix=' '
    #Lecture du fichier de données
    def SplitFichier(self):
        self.InitialData=open("sudoku.txt").read().split()
        for data in self.InitialData:
            for char in data:
                self.Data.append(char)
        self.newData =np.array(self.Data).reshape(9, 9)
        return self.newData
    #Choix du joueur
    def ChoixMachineouHumain(self):
        choix = input ('\033[93m'+'Tu veux que la grille soit completée par la machine ou par l\'humain?\n(taper '+'\033[92m'+ 'M''\033[0m'+'\033[93m'+' pour machine et ' +'\033[92m'+'H' +'\033[93m'+' pour humain)'+'\033[0m')
        self.choix=choix
     # Vérification de l'absence du chiffre candidat sur la ligne, sur la colonne et dans le bloc 3x3
    def VerificationLigneColonneBlock(self,caractere,chiffre,cordX,cordY,Data):
        if caractere=='_':  

            for i in range(9):
                if  chiffre ==Data[cordX][i]:
                    return False  

            for j in range(9):
                if  chiffre ==Data[j][cordY]:
                    return False
                        
            position=[0,0]
            if cordX<=2:
                position[0]=0
            elif cordX <=5:
                position[0]=3
            else: 
                position[0]=6

            if cordY<=2:
                position[1]=0
            elif cordY<=5:
                position[1]=3
            else :
                position[1]=6
            for ligne in range (3):
                for colonne in range (3):
                    if Data[position[0]+ligne][position[1]+colonne]==chiffre:
                        return False
        else:
            return False
  #Parcours par ligne et par colonne
    def ParcourirLigneColonne(self,ligne, colonne):
        colonne+=1
        if colonne==9:
            ligne+=1
            colonne=0
        return ligne,colonne
   #Résolution de la grille 
    def ResoudreLeSudoku(self,ancienTableau, ligne=0, colonne=0):
        if self.choix=='M'or self.choix=='m':
            NouveauTableau = copy.deepcopy(ancienTableau)
            nouvelleligne, nouvellecolonne= self.ParcourirLigneColonne(ligne, colonne)
            x=NouveauTableau[ligne][colonne]
            if NouveauTableau[ligne][colonne] == "_":
                chiffrespossibles= ['1','2','3','4','5','6','7','8','9']
                while True:
                    if len(chiffrespossibles) == 0:
                        return
                    chiffre = chiffrespossibles.pop()         
                    if self.VerificationLigneColonneBlock(x,chiffre,ligne,colonne,NouveauTableau) is not False:
                        NouveauTableau[ligne][colonne] = chiffre
                        if ligne == 8 and colonne == 8:
                            for i in range(len(NouveauTableau)):
                                for j in range(len(NouveauTableau)):
                                    element=NouveauTableau[i][j]
                                    if NouveauTableau[i][j]!=self.newData[i][j]:
                                        element='\033[91m'+element+'\033[0m'
                                    print(element,end=' ')
                                print()
                            print()    
                            print('\033[93m'+'Voici la grille résolue, les chiffres rouges sont les chiffres de la solution!!\n'+'\033[0m')
                            exit()
                        else:
                            self.ResoudreLeSudoku(NouveauTableau, nouvelleligne, nouvellecolonne)
            else:
                self.ResoudreLeSudoku(NouveauTableau, nouvelleligne, nouvellecolonne)
        else:
            Testeur = False
            NouveauTableau = copy.deepcopy(ancienTableau)
            for ligne in NouveauTableau:
                for element in ligne:
                    if element=='_':
                        Testeur=True
            if Testeur==True:
                for i in range(len(NouveauTableau)):
                    for j in range(len(NouveauTableau)):
                        element=NouveauTableau[i][j]
                        if NouveauTableau[i][j]!=self.newData[i][j]:
                            element='\033[91m'+element+'\033[0m'
                        print(element,end=' ')
                    print()
                print()    
                cordX=int(input('\033[92m'+"entrer le numéro de la ligne de ta case:\n"+'\033[0m'))
                cordY=int(input('\033[92m'+"entrer le numéro de la colonne de ta case:\n"+'\033[0m'))
                chiffre=input('\033[92m'+"entrer un chiffre entre 1 et 9:\n"+'\033[0m')
                if (chiffre not in ('1','2','3','4','5','6','7','8','9'))==True:
                    chiffre=input('\033[91m'+"Chiffre non autorisé,\033[92m'+' entrer un chiffre entre 1 et 9:\n"+'\033[0m')          
                if NouveauTableau[cordX][cordY]=='_':
                    x=NouveauTableau[cordX][cordY]
                    if self.VerificationLigneColonneBlock(x,chiffre,cordX,cordY,NouveauTableau) is not False:
                        NouveauTableau[cordX][cordY] = chiffre
                        print ('\033[93m'+'Bravo, continuer!!\n'+'\033[0m')
                        self.ResoudreLeSudoku(NouveauTableau)
                    else:
                        print ('\033[91m'+'chiffre déjà dans la grille!!\n'+'\033[0m',cordX,cordY)
                        self.ResoudreLeSudoku(NouveauTableau)                           
                else:
                    print ('\033[91m'+'case occupée!!\n'+'\033[0m')
                    self.ResoudreLeSudoku(NouveauTableau)
            else:
                for i in range(len(NouveauTableau)):
                    for j in range(len(NouveauTableau)):
                        element=NouveauTableau[i][j]
                        if NouveauTableau[i][j]!=self.newData[i][j]:
                            element='\033[91m'+element+'\033[0m'
                        print(element,end=' ')
                    print()
                print()    
                print('\033[93m'+'La grille est completée, pas de case vide à résoudre!!'+'\033[0m')
                return   
data=Sudoku()
data.ChoixMachineouHumain()
GrilleAresoudre=data.SplitFichier()
data.ResoudreLeSudoku(GrilleAresoudre)
