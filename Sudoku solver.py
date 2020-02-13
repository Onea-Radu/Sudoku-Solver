import requests
import json

html = requests.get("http://www.cs.utep.edu/cheon/ws/sudoku/new/?size=9&level=1")
table=json.loads(html.text)

sudoku=[[0 for i in range(9)] for j in range(9)]
sudokubool=[[True for i in range(9)] for j in range(9)]

for sq in table['squares']:
    sudoku[sq['y']][sq['x']]=sq['value']
    sudokubool[sq['y']][sq['x']]=False

def printSudoku():
    global sudoku
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j],end=' ')
        print()

printSudoku()


print()
print('*****************')
print()





def solveSudoku(n=0):
    global sudoku
    global sudokubool
    if n==81:
        printSudoku()
    else:
        i=n//9
        j=n%9
        if sudokubool[i][j]:
            for z in range(1,10):
                ok=True
                for k in range(9):
                    if sudoku[k][j]==z:
                        ok=False
                    if sudoku[i][k]==z:
                        ok=False
                for h in range(3):
                    for k in range(3):
                        if sudoku[(i//3)*3+h][(j//3)*3+k]==z:
                            ok=False
                if ok:
                    sudoku[i][j]=z
                    solveSudoku(n+1)
                    sudoku[i][j]=0
        else:
            solveSudoku(n+1)    


solveSudoku()
