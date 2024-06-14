# Implementasi Algoritma Brute force dalam Python

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_winner(board, player):
    # Cek baris, kolom, dan diagonal
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, player):
    if is_winner(board, 'X'):
        return 1  # X menang
    if is_winner(board, 'O'):
        return -1  # O menang
    if is_full(board):
        return 0  # Seri

    scores = []
    for cell in get_empty_cells(board):
        i, j = cell
        board[i][j] = player
        score = minimax(board, 'O' if player == 'X' else 'X')
        scores.append(score)
        board[i][j] = ' '

    return max(scores) if player == 'X' else min(scores)

def best_move(board, player):
    best_score = -float('inf') if player == 'X' else float('inf')
    move = None
    for cell in get_empty_cells(board):
        i, j = cell
        board[i][j] = player
        score = minimax(board, 'O' if player == 'X' else 'X')
        board[i][j] = ' '
        if player == 'X':
            if score > best_score:
                best_score = score
                move = (i, j)
        else:
            if score < best_score:
                best_score = score
                move = (i, j)
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    steps = 0

    while not is_full(board) and not is_winner(board, 'X') and not is_winner(board, 'O'):
        print(f"Langkah {steps + 1}: Pemain {current_player}")
        print_board(board)
        move = best_move(board, current_player)
        if move:
            board[move[0]][move[1]] = current_player
        current_player = 'O' if current_player == 'X' else 'X'
        steps += 1

    print("Papan Akhir:")
    print_board(board)
    if is_winner(board, 'X'):
        print("Pemain X menang!")
    elif is_winner(board, 'O'):
        print("Pemain O menang!")
    else:
        print("Permainan berakhir seri!")

# Main program
play_game()
