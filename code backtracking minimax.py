#code bqcktracking minimax

player, opponent = 'x', 'o'

def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False

def evaluate(b):
    for row in range(3):
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            if b[row][0] == player:
                return 10
            elif b[row][0] == opponent:
                return -10
    for col in range(3):
        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:
            if b[0][col] == player:
                return 10
            elif b[0][col] == opponent:
                return -10
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        if b[0][0] == player:
            return 10
        elif b[0][0] == opponent:
            return -10
    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
        if b[0][2] == player:
            return 10
        elif b[0][2] == opponent:
            return -10
    return 0

def minimax(board, depth, isMax):
    score = evaluate(board)
    if score == 10:
        return score
    if score == -10:
        return score
    if not isMovesLeft(board):
        return 0
    if isMax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = player
                    best = max(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '_'
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '_'
        return best

def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player
                moveVal = minimax(board, 0, False)
                board[i][j] = '_'
                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
                print(f"Move ({i}, {j}) => Board Value: {moveVal}")
                for row in board:
                    print(" ".join(row))
                print()
    print("The value of the best Move is :", bestVal)
    print()
    return bestMove

def playGame():
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    current_player = player
    step = 1
    while isMovesLeft(board) and evaluate(board) == 0:
        print(f"Step {step}: Player {current_player}'s move")
        bestMove = findBestMove(board)
        board[bestMove[0]][bestMove[1]] = current_player
        for row in board:
            print(" ".join(row))
        print()
        current_player = opponent if current_player == player else player
        step += 1
    final_score = evaluate(board)
    if final_score == 10:
        print("Player x wins!")
    elif final_score == -10:
        print("Player o wins!")
    else:
        print("The game is a draw!")

# Driver code to start from an empty board
playGame()
