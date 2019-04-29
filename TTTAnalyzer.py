from ThreeDTTT import *
from random import choice

class TTTAnalyzer(object):

    def __init__(self, dim):
        super(TTTAnalyzer, self).__init__()
        self.game=ThreeDTTT(dim)
        self.moves=[]
        self.playerOneMoves=[]
        self.playerTwoMoves=[]

    def greedyAlg(self):
        # type: () -> list
        moves=[]
        bestMoves=self.bestMoves()
        while len(bestMoves)>0:
            moves.append(choice(bestMoves))
            bestMoves=self.bestMoves((moves))
        return moves


    def bestMoves(self,moves=[]):
        '''Takes in a set of moves places that are not available and that block wins.
        And returns a list of moves with the highest number of possible wins.'''
        max=0
        bestmoves=[]
        for point in self.game.points:
            if point not in moves:
                score=self.game.countwinlines(point, moves)
                if score==max:
                    bestmoves.append(point)
                if score>max:
                    max=score
                    bestmoves=[point]
        if max==0:
            bestmoves=[]
        return bestmoves


if __name__ == "__main__":
    analyzer=TTTAnalyzer(5)
    #print(analyzer.bestMoves())
    #print(analyzer.bestMoves([TTTPoint([0,0,0])]))
    for i in range(20):
        ans=analyzer.greedyAlg()
        bestmoves=analyzer.greedyAlg()
        if len(ans)>len(bestmoves):
            ans=bestmoves
    print(ans)

    print(analyzer.game.displayGame(ans))
    print(len(ans))