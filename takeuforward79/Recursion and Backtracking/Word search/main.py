class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        hei = len(board)
        wid = len(board[0])
        n = len(word)

        if(n==0):
            return True
        elif(n>hei*wid):
            return False

        memo = dict()

        for x in word:
            memo[x] = memo.get(x,0)-1

        for iy in range(hei):
            for ix in range(wid):
                memo[board[iy][ix]] = memo.get(board[iy][ix],0)+1
        
        for x in set(word):
            if(memo[x]<0):
                return False

        for iy in range(hei):
            for ix in range(wid):
                if(searchHere(board, iy, ix,hei,wid, word,0,n)):
                    return True
        return False

dydxarr = [[1,0],[0,1],[-1,0],[0,-1]]
badValue = "bad value"

def searchHere(board,iy,ix,hei,wid,word,i,n):
    if(i==n):
        return True
    elif not (0<=iy<hei and 0<=ix<wid):
        return False
    elif(board[iy][ix]!=word[i]):
        return False
    else:
        oldVal = board[iy][ix]
        board[iy][ix] = badValue
        retValue = False

        for (dy,dx) in dydxarr:
            if(searchHere(board,iy+dy,ix+dx,hei,wid,word,i+1,n)):
                retValue = True
                break

        board[iy][ix] = oldVal
        return retValue