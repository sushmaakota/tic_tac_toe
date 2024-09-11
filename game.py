import streamlit as st
import numpy as np

def check_winner(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != "":
            return row[0]
    for col in board.T:
        if len(set(col)) == 1 and col[0] != "":
            return col[0]
    if len(set(board.diagonal())) == 1 and board[0, 0] != "":
        return board[0, 0]
    if len(set(np.fliplr(board).diagonal())) == 1 and board[0, 2] != "":
        return board[0, 2]
    return None

def check_draw(board):
    return not np.any(board == "")

def main():
    st.title("Tic-Tac-Toe")
    board = np.array(st.session_state.get("board", [["" for _ in range(3)] for _ in range(3)]))
    current_player = st.session_state.get("current_player", "X")
    winner = check_winner(board)

    if winner is not None:
        st.write(f"Player {winner} wins!")
    elif check_draw(board):
        st.write("Draw!")
    else:
        for row in range(3):
            cols = st.columns(3)
            for col in range(3):
                if board[row, col] == "":
                    if cols[col].button(" ", key=f"button_{row}_{col}"):
                        board[row, col] = current_player
                        st.session_state.board = board
                        st.session_state.current_player = "O" if current_player == "X" else "X"
                        st.rerun()
                else:
                    cols[col].write(board[row, col], key=f"button_{row}_{col}")

    if st.button("Reset game"):
        st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
        st.session_state.current_player = "X"
        st.rerun()

if __name__ == "__main__":
    main()
