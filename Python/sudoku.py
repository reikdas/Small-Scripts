import time


def disp(grid):
    """
    Display a sudoku grid.

    Parameters:

        grid (nested list): sudoku grid

    Returns:

        None
    """
    for i, row in enumerate(grid):
        if i%3 == 0:
            print()
        for j, element in enumerate(row):
            if j%3 == 0:
                print('\t', end=' ')
            print(element, end=' ')
        print()
    print()


def legal(puzzle, i, j, k, diagonal=False):
    """
    Check if k can be placed at the jth column of ith row.

    Parameters:

        puzzle (nested list): sudoku grid

        i (int): row to be checked

        j (int): column to be checked

        k (int): number to be placed in puzzle[i][j]

        diagonal (bool): True if diagonal sudoku, False otherwise (default: False)

    Returns:

        bool: True if k can be placed in puzzle[i][j], False otherwise.
    """
    for a in range(9):
        if a != j and puzzle[i][a] == k:
            return False
        if a != i and puzzle[a][j] == k:
            return False
    for a in range((i//3)*3, (i//3)*3+3):
        for b in range((j//3)*3, (j//3)*3+3):
            if puzzle[a][b] == k:
                return False
    if diagonal:
        diag_left = [0]*10
        diag_right = [0]*10
        temp = puzzle[i][j]
        puzzle[i][j] = k
        for a in range(9):
            diag_left[puzzle[a][a]] += 1
            diag_left[puzzle[a][8-a]] += 1
        puzzle[i][j] = temp
        if not all([diag_left[a] <= 1 for a in range(1, 10)]):
            return False
        if not all([diag_right[a] <= 1 for a in range(1, 10)]):
            return False
    return True


def solve(puzzle, edit, n, diagonal=False):
    """
    Solve the Sudoku puzzle.

    Parameters:

        puzzle (nested list): sudoku grid

        edit (nested list): denotes which cells in the puzzle can be edited by player

        n (int): cell to be filled, in row-major format

        diagonal (bool): True if diagonal sudoku, False otherwise (default: False)

    Returns:

        bool: True if the given sudoku puzzle is solved, False otherwise
    """
    if n == 81:
        return True
    else:
        i = n // 9
        j = n % 9
        if edit[i][j] == 1:
            for k in range(1, 10):
                if legal(puzzle, i, j, k, diagonal):
                    puzzle[i][j] = k
                    if solve(puzzle, edit, n+1, diagonal):
                        return True
                    puzzle[i][j] = 0
            else:
                return False
        else:
            return solve(puzzle, edit, n+1, diagonal)


if __name__ == '__main__':
    puzzle = list()
    edit = [[0]*9 for _ in range(9)]
    print('Enter the Sudoku puzzle, with 0 for blanks, in 9 lines, using any delimiters: ')
    for k in range(9):
        s = [int(i) for i in input() if ord(i)>=48 and ord(i)<=57]
        if len(s) == 9:
            puzzle.append(s)
            for j, i in enumerate(s):
                if i == 0:
                    edit[k][j] = 1
        else:
            print('Error in input!')
    else:
        c = int(input('Enter 1 for Diagonal Sudoku, 0 for Standard Sudoku: '))
        if c!=0 and c!=1:
            print(' Assuming entered Sudoku to be of Standard variant.')
        print()
        print('Entered Sudoku puzzle: ')
        disp(puzzle)
        print('Variant:', end=' ')
        start = time.time()
        if c == 1:
            print('Diagonal')
            if solve(puzzle, edit, 0, True):
                end = time.time()
                print('Solved Sudoku puzzle: ')
                disp(puzzle)
                print('Time taken: ', end-start, ' seconds')
            else:
                end = time.time()
                print('Oops! This puzzle cannot be solved!')
                print('Time spent: ', end-start, ' seconds')
        else:
            print('Standard')
            if solve(puzzle, edit, 0, False):
                end = time.time()
                print('Solved Sudoku puzzle: ')
                disp(puzzle)
                print('Time taken: ', end-start, ' seconds')
            else:
                end = time.time()
                print('Oops! This puzzle cannot be solved!')
                print('Time spent: ', end-start, ' seconds')
        
'''
490 000 100
000 702 803
807 000 000
000 025 009
008 000 600
700 430 000
000 000 406
203 804 000
001 000 028
'''
'''
490000100
000702803
807000000
000025009
008000600
700430000
000000406
203804000
001000028
'''
'''
492 386 157
156 792 843
837 541 962
314 625 789
528 179 634
769 438 215
985 213 476
273 864 591
641 957 328
'''
'''
Diagonal:
000 000 000
005 428 100
060 000 020
010 000 050
090 000 040
080 000 030
070 000 090
004 182 600
000 000 000
'''
'''
241 695 387
735 428 169
869 731 425
413 879 256
692 513 748
587 246 931
178 364 592
954 182 673
326 957 814
'''
