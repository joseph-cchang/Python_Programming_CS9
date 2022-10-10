# Lab04, Joseph Chang, CS9

from Stack import Stack

def solveMaze(maze, startX, startY):
    s = Stack()
    count = 1
    maze[startX][startY] = count
    s.push([startX, startY])
    while s.size() > 0:
        startX, startY = s.peek()
        if maze[startX-1][startY] == " ":
            count += 1
            maze[startX-1][startY] = count
            s.push([startX-1, startY])
            continue
        elif maze[startX-1][startY] == "G":
            return True

        elif maze[startX][startY-1] == " ":
            count += 1
            maze[startX][startY-1] = count
            s.push([startX, startY-1])
            continue
        elif maze[startX][startY-1] == "G":
            return True

        elif maze[startX+1][startY] == " ":
            count += 1
            maze[startX+1][startY] = count
            s.push([startX+1, startY])
            continue
        elif maze[startX+1][startY] == "G":
            return True

        elif maze[startX][startY+1] == " ":
            count += 1
            maze[startX][startY+1] = count
            s.push([startX, startY+1])
            continue
        elif maze[startX][startY+1] == "G":
            return True
        
        else:
            s.pop()
            
    return False
        
