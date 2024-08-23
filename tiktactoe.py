import streamlit as st

def display_board(board):
    """Display the current state of the board."""
    st.write(f"{board[0]} | {board[1]} | {board[2]}")
    st.write("---------")
    st.write(f"{board[3]} | {board[4]} | {board[5]}")
    st.write("---------")
    st.write(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(board, player):
    """Check if the current player has won."""
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False

def play_game():
    """Main function to play the game."""
    st.title("Tic-Tac-Toe")
    
    # Initialize the game state
    if 'board' not in st.session_state:
        st.session_state.board = [str(i) for i in range(9)]
        st.session_state.player = 'X'
        st.session_state.winner = None

    # Display the board
    display_board(st.session_state.board)

    # Check if the game has been won or tied
    if st.session_state.winner:
        st.write(f"Player {st.session_state.winner} wins!")
        st.button("Restart Game", on_click=reset_game)
        return
    elif all(isinstance(x, str) and x in ['X', 'O'] for x in st.session_state.board):
        st.write("It's a tie!")
        st.button("Restart Game", on_click=reset_game)
        return

    # Player's turn
    move = st.number_input("Enter a position (0-8):", min_value=0, max_value=8, step=1)

    if st.button("Make Move"):
        if st.session_state.board[move] != str(move):
            st.warning("That position is already taken. Try again.")
        else:
            st.session_state.board[move] = st.session_state.player
            if check_win(st.session_state.board, st.session_state.player):
                st.session_state.winner = st.session_state.player
            # Switch players
            st.session_state.player = 'O' if st.session_state.player == 'X' else 'X'

def reset_game():
    """Reset the game state."""
    st.session_state.board = [str(i) for i in range(9)]
    st.session_state.player = 'X'
    st.session_state.winner = None

if __name__ == "__main__":
    play_game()