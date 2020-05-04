# -*- coding: utf-8 -*-
"""
Created on Mon May  4 08:16:18 2020

@author: Sichao
"""
import copy
import sys

def manhatten(a,b,c,d):
    return abs(a-c)+abs(b-d)

def same(node1,node2):
    for i in range(3):
        for j in range(3):
            if node1.puzzle[i][j]!=node2.puzzle[i][j]:
                return False
    return True

class Node:
    def __init__(self,puzzle,g=0,h=0):
        self.puzzle=puzzle
        self.father=None
        self.neighbors=[]
        self.g=g
        self.h=h
        
    def set_father(self,node):
        self.father=node
    
    def set_g(self,g):
        self.g=g
        
    def switch_space(self,i,j,newi,newj):
        Node(self.puzzle,self.g+1)
        self.puzzle[i][j]=self.puzzle[newi][newj]
        self.puzzle[newi]
    
    def display(self):
        for i in range(3):
            for j in range(3):
                print(" "+self.puzzle[i][j],end="")
            print("\n")
        print("\n")
        print("\n")
    
    def create_neighbor(self,x,y,newx,newy):
        basic_puzzle=[["0","0","0"],["0","0","0"],["0","0","0"]]
        neighbor=Node(basic_puzzle,self.g+1)
        neighbor.puzzle=copy.deepcopy(self.puzzle)
        neighbor.puzzle[x][y]=copy.copy(neighbor.puzzle[newx][newy])
        neighbor.puzzle[newx][newy]="_"
        neighbor.set_father(self)
        neighbor.calculate_h()
        return neighbor
    
    def set_father(self,node):
        self.father=node
    
    def find_neighbors(self):
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j]=="_":
                    x=i
                    y=j
                    break
        move_direction=[[x-1,y],[x+1,y],[x,y-1],[x,y+1]];
        for move in move_direction:
            if 0<=move[0]<3 and 0<=move[1]<3:
                self.neighbors.append(self.create_neighbor(x,y,move[0],move[1]))
    
    def calculate_h(self):
        heuristic=0
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j]=="_":
                    heuristic+=manhatten(i,j,0,0)
                if self.puzzle[i][j]=="1":
                    heuristic+=manhatten(i,j,0,1)
                if self.puzzle[i][j]=="2":
                    heuristic+=manhatten(i,j,0,2)
                if self.puzzle[i][j]=="3":
                    heuristic+=manhatten(i,j,1,0)    
                if self.puzzle[i][j]=="4":
                    heuristic+=manhatten(i,j,1,1)
                if self.puzzle[i][j]=="5":
                    heuristic+=manhatten(i,j,1,2)
                if self.puzzle[i][j]=="":
                    heuristic+=manhatten(i,j,2,0)
                if self.puzzle[i][j]=="":
                    heuristic+=manhatten(i,j,2,1)
                if self.puzzle[i][j]=="":
                    heuristic+=manhatten(i,j,2,2)
        self.h=heuristic

class Astar:
    def __init__(self):
        self.startNode=None
        self.endNode=Node([["_","1","2"],["3","4","5"],["6","7","8"]])
        self.openlist=[]
        self.closelist=[]
        self.currentNode=None
        
    def getNextNode(self):
        minimum=100
        for target in self.openlist:
            guess=target.g+target.h
            if guess<=minimum:
                minimum=guess
                nextNode=target
        return nextNode
    
    def not_in_close(self,node):
        for completedNode in self.closelist:
            if same(node,completedNode):
                return False
        return True
    
    def not_in_open(self,node):
        for potentialNode in self.openlist:
            if same(node,potentialNode):
                if node.g<potentialNode.g:
                    potentialNode.set_g(copy.copy(node.g))
                return False
        return True
    
    def searchCurrentNode(self):
        self.currentNode.find_neighbors()
        self.closelist.append(self.currentNode)
        for neighbor in self.currentNode.neighbors:
            if self.not_in_open(neighbor) and self.not_in_close(neighbor):
                self.openlist.append(neighbor)
        self.currentNode=self.getNextNode()
        self.openlist.remove(self.currentNode)
        
    def search(self):
        self.currentNode=self.startNode
        while(not same(self.currentNode,self.endNode)):
            self.searchCurrentNode()
            self.currentNode.display()
            if len(self.openlist)==0:
                print("No answers")
                return False
        
    
        
    

if __name__ == "__main__":
    startpoint=[["0","0","0"],["0","0","0"],["0","0","0"]]
    for i in range(3):
        for j in range(3):
            index=i*3+j+1
            startpoint[i][j]=sys.argv[index]  
    a=Astar()
    a.startNode=Node(startpoint)
    a.startNode.display()
    a.search()