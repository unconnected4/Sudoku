from enum import Enum
from math import sqrt

ElementType=Enum('ElementType', ['ROW','COLUMN','SQUARE'])

class Element:
  def __init__(self, value, type, index, unresolved):
    self.value = value
    self.type = type
    self.index = index
    self.unresoled = unresolved
  def __str__(self):
    s=",".join(str(e) for e in self.value)+'\n'
    s+=str(self.type)+" Index: "+str(self.index)+". Unresolved: "+str(self.unresoled)
    return s
  
class Sudoku:
    def __init__(self):
        self.Board=[]
        self.Options=[]
    def __str__(self):
        s=""
        for row in self.Board:
            for c in row:
                s+=c
                if (c==""):
                    s+=" "
            s+="\n"
        return s

def get_row(rowIndex, sudocu):
    return sudocu.Board[rowIndex]

def get_column(columnIndex, sudocu):
    result=[]
    for row in sudocu.Board:
        result.append(row[columnIndex])
    return result

def get_square(squereIndex, sudocu):
    result=[]

    dimension=int(sqrt(len(sudocu.Board)))
    rShift=(squereIndex // dimension)*dimension
    cShift=(squereIndex % dimension)*dimension

    for r in range(dimension):
        for c in range(dimension):
            result.append(sudocu.Board[r+rShift][c+cShift])

    return result    

def get_square_index(rowIndex,columnIndex, sudocu):
    dimension=int(sqrt(len(sudocu.Board)))
    return (rowIndex//dimension)*dimension+(columnIndex//dimension)     

def options(rowIndex, columnIndex, sudocu):
 
    #rise error instead
    if (sudocu.Board[rowIndex][columnIndex]!=""):
       return [sudocu.Board[rowIndex][columnIndex]]
    
    awailable=sudocu.Options
    #print(awailable)
    awailable=[e for e in awailable if e not in get_row(rowIndex,sudocu)]
    #print(awailable)
    awailable=[e for e in awailable if e not in get_column(columnIndex,sudocu)]
    #print(awailable)
    #print ("sqr")
    #print (get_square(get_square_index(rowIndex, columnIndex), sudocu))
    awailable=[e for e in awailable if e not in get_square(get_square_index(rowIndex, columnIndex, sudocu), sudocu)]
    #print(awailable)
    return awailable

class Cell:
    def __init__(self, rowIndex, columnIndex, options):
        self.rowIndex = rowIndex
        self.columnIndex = columnIndex
        self.options=options
    def __str__(self):
        s="("+str(self.rowIndex)+","+str(self.columnIndex)+") -> ["+",".join(str(e) for e in self.options)+"]"
        return s
    
def find_esiest_cell(sudocu):
    buffer=[]
    for rowIndex in range(len(sudocu.Board)):
        for columnIndex in range(len(sudocu.Board)):
            if (sudocu.Board[rowIndex][columnIndex]==""):
                cell=Cell(rowIndex,columnIndex,options(rowIndex,columnIndex,sudocu))
                buffer.append(cell)
                #print (cell)


    buffer.sort(key=lambda x: len(x.options))
    
    if (len(buffer)==0):
        return None 
    return buffer[0]

        
        


   
   






        