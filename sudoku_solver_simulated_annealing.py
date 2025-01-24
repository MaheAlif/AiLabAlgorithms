import numpy as np
import matplotlib.pyplot as plt
import random
import math

def is_valid_move(board, row, col, num):
    # Check row
    if num in board[row]:
        return False
    
    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Check 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    return True

def count_conflicts(board):
    conflicts = 0
    for i in range(9):
        # Count row conflicts
        row = board[i]
        conflicts += len(row) - len(set(x for x in row if x != 0))
        
        # Count column conflicts
        col = [board[j][i] for j in range(9)]
        conflicts += len(col) - len(set(x for x in col if x != 0))
        
        # Count box conflicts
        box_row, box_col = 3 * (i // 3), 3 * (i % 3)
        box = []
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                box.append(board[r][c])
        conflicts += len(box) - len(set(x for x in box if x != 0))
    
    return conflicts

def generate_initial_solution(initial_board):
    board = [row[:] for row in initial_board]
    numbers = list(range(1, 10))
    
    # Fill each empty cell with a valid number
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                valid_numbers = [n for n in numbers if is_valid_move(board, i, j, n)]
                if valid_numbers:
                    board[i][j] = random.choice(valid_numbers)
                else:
                    board[i][j] = random.randint(1, 9)
    return board

def get_random_empty_position(initial_board):
    empty_positions = []
    for i in range(9):
        for j in range(9):
            if initial_board[i][j] == 0:
                empty_positions.append((i, j))
    return random.choice(empty_positions) if empty_positions else None

def solve_sudoku(initial_board, max_iterations=10000, initial_temperature=1.0, cooling_rate=0.99):
    current_solution = generate_initial_solution(initial_board)
    current_energy = count_conflicts(current_solution)
    best_solution = [row[:] for row in current_solution]
    best_energy = current_energy
    temperature = initial_temperature
    
    for iteration in range(max_iterations):
        if current_energy == 0:
            break
            
        # Get a random position that was empty in the initial board
        pos = get_random_empty_position(initial_board)
        if not pos:
            break
            
        i, j = pos
        current_value = current_solution[i][j]
        
        # Try a new random value
        new_value = random.randint(1, 9)
        while new_value == current_value:
            new_value = random.randint(1, 9)
            
        # Make the change and compute new energy
        current_solution[i][j] = new_value
        new_energy = count_conflicts(current_solution)
        
        # Decide if we should accept the change
        delta_energy = new_energy - current_energy
        if delta_energy < 0 or random.random() < math.exp(-delta_energy / temperature):
            current_energy = new_energy
            if current_energy < best_energy:
                best_solution = [row[:] for row in current_solution]
                best_energy = current_energy
        else:
            current_solution[i][j] = current_value
            
        temperature *= cooling_rate
        
    return best_solution, best_energy

def visualize_sudoku(board, initial_board, title="Sudoku"):
    plt.figure(figsize=(8, 8))
    plt.grid(True)
    
    # Draw the board
    for i in range(10):
        line_width = 2 if i % 3 == 0 else 0.5
        plt.axhline(y=i, color='black', linewidth=line_width)
        plt.axvline(x=i, color='black', linewidth=line_width)
    
    # Fill in numbers
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                # Use black for initial numbers, blue for solved numbers
                color = 'black' if initial_board[i][j] != 0 else 'red'
                plt.text(j + 0.5, 8.5 - i, str(board[i][j]), 
                        horizontalalignment='center',
                        verticalalignment='center',
                        fontsize=14,
                        color=color)
    
    plt.title(title)
    plt.xticks([])
    plt.yticks([])
    plt.show()

def main():
    # Replace underscores with zeros in the input board
    initial_board = [
        [1,0,0,8,0,0,3,0,0],
        [0,4,0,0,0,6,0,1,0],
        [3,0,0,5,0,0,2,0,0],
        [0,1,0,7,0,0,0,0,4],
        [5,0,0,0,8,0,0,7,0],
        [2,0,0,6,0,0,5,0,0],
        [0,0,4,0,0,7,1,0,0],
        [1,0,0,8,0,0,0,6,0],
        [0,6,0,0,0,4,0,2,0]
    ]
    
    # Visualize initial board
    visualize_sudoku(initial_board, initial_board, "Initial Sudoku")
    
    # Solve the puzzle
    solution, energy = solve_sudoku(initial_board)
    
    # Visualize solution with colored numbers
    visualize_sudoku(solution, initial_board, f"Solution (Conflicts: {energy})")
    
    return solution, energy

if __name__ == "__main__":
    solution, energy = main()