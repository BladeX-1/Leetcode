from typing import *

def graphColoring(mat: List[List[int]], maxColor: int) -> str:
    n = len(mat)
    components = []
    visited = [False]*n
    for i in range(n):
        if(visited[i]==False):
            oneComponent = []
            visited[i] = True
            dfs(mat,i,n,visited,oneComponent)
            components.append(oneComponent)

    colors = [-1]*n
    for oneComponent in components:
        isSolved = fillColors(mat,0,len(oneComponent),oneComponent,colors,maxColor)
        if(isSolved == False):
            return 'NO'
    return 'YES'

def notPossibleColors(mat,i,n,colors):
    ans = []
    for j in range(n):
        if(mat[i][j]==1 or mat[j][i]==1):
            ans.append(colors[j])
    return ans

def possibleColors(mat,i,n,colors,maxColor):
    allColors = set(range(maxColor))
    notPossible = set(notPossibleColors(mat,i,n,colors))
    return list(allColors.difference(notPossible))


def dfs(mat,i,n,visited,component):
    component.append(i)
    for j in range(n):
        # assert(mat[i][j]==mat[j][i])
        if((mat[i][j] or mat[j][i]) and visited[j]==False):
            visited[j]=True
            dfs(mat,j,n,visited,component)


def fillColors(mat,i,n,oneComponent,colors,maxColor):
    if(i==n):
        return True
    myIndex = oneComponent[i]
    myColor = colors[myIndex]
    if(myColor==-1):# unfilled
        myPossibles = possibleColors(mat,myIndex,n,colors,maxColor)
        for myFillColor in myPossibles:
            colors[myIndex] = myFillColor
            issolved = fillColors(mat,i+1,n,oneComponent,colors,maxColor)
            if(issolved):
                return True
            else:
                colors[myIndex]=-1
        return False
    else:# already filled
        return fillColors(mat,i+1,n,colors,maxColor)







