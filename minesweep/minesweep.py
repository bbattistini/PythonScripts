import numpy as np
import sys

class MineSweep():
    def __init__(self, rows, cols):
        self.board = np.zeros((rows,cols), dtype=np.int8)
        self.leftEdges = np.arange(0,rows*cols,cols)
        self.rightEdges = np.arange(cols-1,rows*cols,cols)

    def fillBoard(self, inpFile):
        flatBoard = self.board.flatten()
        index = 0
        cols = self.board.shape[1]
        negCols = cols * -1
        countBomb = (-1,1,cols,cols+1, cols-1, negCols, negCols-1, negCols+1)
        for line in inpFile:
            for ch in line.strip():
                flatBoard[index] = -1 if ch == "#" else 0
                index += 1
        for i in range(len(flatBoard)):
            if flatBoard[i] == -1:
                for ck in countBomb:
                    if i + ck in range(len(flatBoard)):
                        flatBoard[i+ck] += 1 if flatBoard[i+ck] != -1 and self.checkEdge(i, i+ck) else 0
        self.board = flatBoard.reshape(self.board.shape)

    def checkEdge(self,point1,point2):
        if point1 in self.leftEdges and point2 in self.rightEdges:
            return False
        if point1 in self.rightEdges and point2 in self.leftEdges:
            return False
        return True

    def getBoard(self):
        print(self.board)

def main(args):
    fl = open(args[0])
    row,col = fl.readline().strip().split("-")
    x = MineSweep(int(row),int(col))
    x.fillBoard(fl)
    x.getBoard()

if __name__ == "__main__":
    main(sys.argv[1:])
