import random
import timeit

class Board:
    def __init__(self, size):
        self.board = list(range(size))
        self.size = size
        self.scramble()

    def scramble(self):
        for i in range(self.size):
            pos_to_swap = random.randint(0, self.size - 1)
            
            self.board[i], self.board[pos_to_swap] = self.board[pos_to_swap], self.board[i]

    def conflicts(self, queen_row, queen_col):
        conflicts = 0
        for col in range(self.size):
            if col == queen_col:
                continue
            row = self.board[col]
            if row == queen_row or abs(row - queen_row) == abs(col - queen_col):
                conflicts += 1
        return conflicts

    def solve(self):
        moves = 0
        while True:
            max_conflicts = 0
            max_conflict_pos = []
            for pos in range(self.size):
                conflicts = self.conflicts(self.board[pos], pos)
                if conflicts == max_conflicts:
                    max_conflict_pos.append(pos)
                elif conflicts > max_conflicts:
                    max_conflicts = conflicts
                    max_conflict_pos = [pos]

            if max_conflicts == 0:
                return

            queen_column = random.choice(max_conflict_pos)
            min_conflicts = self.size
            candidates = []
            for r in range(self.size):
                conflicts = self.conflicts(r, queen_column)
                if conflicts == min_conflicts:
                    candidates.append(r)
                elif conflicts < min_conflicts:
                    min_conflicts = conflicts
                    candidates = [r]

            if candidates:
                self.board[queen_column] = random.choice(candidates)

            moves += 1

            #If the moves are more than the size * 2 (it can be other value as well) then the board is stuck 
            if moves == self.size * 2:
                self.scramble()
                moves = 0

    def print_board(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[col] == row:
                    print("*", end="")
                else:
                    print('_', end="")
            print()

if __name__ == "__main__":
    size = int(input())

    start = timeit.default_timer()

    #The index of the board is the column and the value is the row
    board = Board(size)
    board.solve()

    end = timeit.default_timer()

    #Print for testing tool
    #print(board.board)

    if size > 100:
        print("{}".format(round(end-start,2)))
    else:
        #Print the whole board
        board.print_board()