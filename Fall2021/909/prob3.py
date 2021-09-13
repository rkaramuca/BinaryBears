# Problem 3
# Sudoku!

for _ in range(int(input())):
    grid = []

    # Set up grid an booleans
    # Always initialize your booleans early
    full = True
    error = False
    input()
    for z in range(9):
        line = [i for i in input()]
        # Check if puzzle is incomplete (easiest to check here)
        if "." in line:
            full = False
        grid.append(line)

    # Check rows
    # sets are great for checking duplicates
    for i in range(9):
        row = [r for r in grid[i] if r != "."]
        if len(row) != len(set(row)):
            error = True

    # Transpose grid and check columns
    # Zip(*a) is an amazing tool!!!
    grid_t = list(zip(*grid))
    for i in range(9):
        row = [r for r in grid[i] if r != "."]
        if len(row) != len(set(row)):
            error = True
    
    # Here we will check the 3x3 boxes
    # First iterate in two range(3) loops...
    for i in range(3):
        for j in range(3):
            box = []
            for x in range(3):
                for y in range(3):
                    num = grid[3*i+y][3*j+x]
                    if num != ".":
                        box.append(num)
                    if len(box) != len(set(box)):
                        error = True
    # now we can end with an easy if else chain
    if full and not error:
        print("you got it!")
    if not full and error:
        print("there is an error somewhere")
    if not full and not error:
        print("ok so far")