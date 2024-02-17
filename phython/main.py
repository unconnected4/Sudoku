from definition import *
from functions import *

s=Sudoku()
s.Options=["1","2","3","4","5","6","7","8","9"]
s.Board=[
    ["3","1", "", "7", "", "",  "6","9","4"],
    ["6","7","9",  "", "", "",  "8","5", ""],
    [ "", "", "", "8","6","9",  "7", "", ""],

    [ "","5", "",  "", "","8",  "4","2","9"],
    [ "", "","2",  "", "","7",  "1","8", ""],
    [ "","8","3",  "","9","1",  "5", "", ""],

    [ "1","9", "",  "","8", "",  "","6","7"],
    [  "", "","7", "1", "", "",  "", "", ""],
    [  "", "", "",  "", "", "", "2", "", ""]
]

def Solver(sudoku):
    result=[]
    esiest=find_esiest_cell(sudoku)
    if (esiest==None):
        result.append(sudoku)
        return result
    elif (len(esiest.options)==0):
        return result
    
    for option in esiest.options:
        sudoku.Board[esiest.rowIndex][esiest.columnIndex]=option
        result.extend(Solver(sudoku))

    return result

solutions=Solver(s)
print("Solutions:",len(solutions))
for s in solutions:
    print(s)

#print(s)

#print(find_esiest_cell(s))
#sudocus=[sudocu]

#counter=0


# while True:
#     print(counter)
#     print_sudocu(sudocu)

#     counter+=1
#     if (counter==100):
#         break

#     solving=find_esiest_cell(sudocu)

#     if (solving==None):
#         print("Done!")
#         break
#     elif(len(solving.options)>1):
#         print("excessive options")
#         print(solving)
#         break
#     elif (len(solving.options)==0):
#         print("no options")
#         print(solving)
#         break

#     sudocu[solving.rowIndex][solving.columnIndex]=solving.options[0]
    

#print_sudocu(sudocu)



