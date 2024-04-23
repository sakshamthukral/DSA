def isPathCrossing(path: str) -> bool:
        x_dist=0
        y_dist=0
        traversed_coordinates = [(0,0)]
        path_step = list(path)
        for step in path_step:
            if step == "N":
                y_dist += 1
            elif step == "E":
                x_dist += 1
            elif step == "S":
                y_dist -= 1
            else:
                x_dist -= 1
            
            coordinates=(x_dist,y_dist)
            if coordinates in traversed_coordinates:
                return True
            else:
                traversed_coordinates.append(coordinates)
        return False

path = input()
print(isPathCrossing(path))