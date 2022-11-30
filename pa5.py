import math

def spiralOrder(matrix: list[list[int]]) -> list[int]:
    visited = set()

    results = list()

    n = len(matrix)
    m = len(matrix[0])

    #index starting from the last square
    index = n*m-1
    nextIndex = 0
    direction = [-m, -1, m, 1]
    diIndex = 0
    for i in range(n*m):
        #8 = matrix[Math.floor(8/3)][8%3] = matrix[2][2]
        #4 = matrix[Math.floor(4/3)][4%3] = matrix[1][1]
        #1d index = matrix[Math.floor(index/m)][index%m] 
                
        #Append current value to results
        results.append(matrix[math.floor(index/m)][index%m])
        #Add coordinate to visited list
        visited.add(index)

        #Calculate next step
        nextIndex = index + direction[diIndex]

        #Check inbound or not visited
        if nextIndex >= 0 and nextIndex <= n*m-1 and nextIndex not in visited:
            #Update index if valid
            index = nextIndex
        else:
            #Change direction
            diIndex = (diIndex + 1) % 4 # 0-3
            index = index + direction[diIndex]
    
    return results
    
if __name__ == "__main__":
    a = [[1,2,3], [4,5,6], [7,8,9]]
    b = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(spiralOrder(a))
    print(spiralOrder(b))
