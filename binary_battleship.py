import random

def show_bitwise_operators(num):
    # Using a second number for operations that require two operands
    num2 = 5
    print(f"Original number: {num} (Binary: {bin(num)[2:].zfill(8)})")
    print(f"Second number for operations: {num2} (Binary: {bin(num2)[2:].zfill(8)})")
    print("\nBitwise Operations:")
    
    # Bitwise AND (&)
    result = num & num2
    print(f"AND (&): {num} & {num2} = {result} (Binary: {bin(result)[2:].zfill(8)})")
    
    # Bitwise OR (|)
    result = num | num2
    print(f"OR (|): {num} | {num2} = {result} (Binary: {bin(result)[2:].zfill(8)})")
    
    # Bitwise XOR (^)
    result = num ^ num2
    print(f"XOR (^): {num} ^ {num2} = {result} (Binary: {bin(result)[2:].zfill(8)})")
    
    # Bitwise NOT (~)
    result = ~num
    print(f"NOT (~): ~{num} = {result} (Binary: {bin(result)[2:].zfill(8)})")
    
    # Bitwise Left Shift (<<)
    shift = 2
    result = num << shift
    print(f"Left Shift (<<): {num} << {shift} = {result} (Binary: {bin(result)[2:].zfill(8)})")
    
    # Bitwise Right Shift (>>)
    result = num >> shift
    print(f"Right Shift (>>): {num} >> {shift} = {result} (Binary: {bin(result)[2:].zfill(8)})")

def random_number_generator():
    number = random.randint(0, 255)
    result = is_power_of_two(number)
    x = result
    ## if it is even then a power of 2
    if is_even(x):
        print(f"Just so you know the random value is {(lambda x: 'a power of 2!' if (x > 0 and (x & (x - 1)) == 0) else 'not a power of 2')(x)}")    
    return number
  
def is_even(n):
    return True if (n & 1) == 0 else False

def is_power_of_two(n):
    return n != 0 and (n & (n - 1)) == 0

def check_if_bit_is_set(grid, position):
    print("check_if_bit_is_set called!")
    num = int(grid, 2)
    is_set = (num & (1 << position)) != 0
    print(f"Is bit {position} set in {num}? {is_set}")

def clear_bit(grid, position):
    print("clear_bit called!")
    byte_to_number = int(grid, 2)
    number_result = byte_to_number
    number_result &= ~(1 << position) 
    print(f"Clear bit {position} in {byte_to_number} : {number_result}") 

def flip_bit(grid, position):
    byte_to_number = int(grid, 2)
    mask = 1 << position
    result = byte_to_number ^ mask
    print(
        f"Flipping bit at position {position}:\n"
        f"  x      = {bin(byte_to_number)} ({byte_to_number})\n"
        f"  mask   = {bin(mask)} ({mask})\n"
        f"  result = {bin(result)} ({result})"
    )
    return result

def set_bit(grid, position):
    byte_to_number =  int(grid, 2)
    mask = 1 << position
    result = byte_to_number | mask
    print(f"Setting bit at position {position}: x = {bin(byte_to_number)}, mask = {bin(mask)}, result = {bin(result)}")
    return result

def count_set_bits(n):
    count = 0
    while n:
        n &= (n - 1)  
        count += 1
    return count

# grid = '0b00000010'
def tutorial_mode(grid):
    tutorial_mode_var = input("Do you want to be in tutorial mode? y/n: ")
    if tutorial_mode_var == 'y':
        while True:
            end_tutorial_mode = input("Do you want to quit tutorial mode? y/n: ")
            if end_tutorial_mode == 'y':
                print('tutorial ended!')
                break
            bitwise_operation_primer = input("Do you want a primer on bitwise operators? y/n: ")
            if bitwise_operation_primer == 'y':
                user_input = int(input(" Please provide an integer between 0-255 (inclusive) ")) 
                show_bitwise_operators(user_input)
            else:
                pass
            # Prompt for checking if a bit is set
            check_input = input("Do you want to know if a position is set? y/n: ").strip().lower()
            if check_input == 'y':
                position = int(input("Ok! At which position? Enter a bit position (0-7) as a number (e.g., '7')!"))
                check_if_bit_is_set(grid, position)  # Position is placeholder for now
            else:
                pass

            # Prompt for clearing a bit
            clear_input = input("Do you want me to clear a bit? y/n: ").strip().lower()
            if clear_input == 'y':
                position = int(input("Ok! At which position? Enter a bit position (0-7) as a number (e.g., '7')!"))
                clear_bit(grid, position)  # Position is placeholder for now
            else:
                pass

            # Prompt for flipping a bit
            flip_input = input("Do you want me to flip a bit? y/n: ").strip().lower()
            if flip_input == 'y':
                position = int(input("Ok! At which position? Enter a bit position (0-7) as a number (e.g., '7')!"))
                flip_bit(grid, position)  # Position is placeholder for now
            else: 
                pass

            # Prompt for setting a bit
            set_bit_var = input("Do you want me to set a bit? y/n: ").strip().lower()
            if set_bit_var == 'y':
                position = int(input("Ok! At which position? Enter a bit position (0-7) as a number (e.g., '7')!"))
                result = set_bit(grid, position)
                print(result)

            else:
                pass

            print(" More practice! No problem! ")
            print(" I'll changing the byte for use in tutorial! ")
            print("  Good luck! :) ")
            number = random_number_generator()
            grid = bin(number)
    else:
        print('Ok! Enjoy the game! :) ')
    

def binary_battleship():
    print("** Welcome to Binary Battleship! **")
    tutorial_grid = '00000101'
    tutorial_mode(tutorial_grid)
    print("---------------------------------------------------------------")
    print("Find ships (1s) in an 8-bit grid.")
    print("Positions are 0-7, right-to-left (0 = rightmost (2^0), 7 = leftmost (2^7)).")
    print("Enter a bit position (0-7) as a number (e.g., '7') or a mask (e.g., '1 << 7' or '0b10000000').")
    print("---------------------------------------------------------------")
    print("Type 'exit' to quit the game, 'restart' to reset the current level, or 'tutorial_mode' to enter tutorial_mode.\n")

    # Define levels: (grid, ship_count, description, hint, mode, initial_ships)
    levels = [
        {
            "grid": 0b00000100,  # Ship at position 2
            "ship_count": 1,
            "description": "Level 1: Find 1 ship in an 8-bit grid.",
            "hint": "Enter a position (0-7) or use '1 << n' to fire at position n.",
            "mode": "standard",
            "initial_ships": [2]
        },
        {
            "grid": 0b00100100,  # Ships at positions 2, 5
            "ship_count": 2,
            "description": "Level 2: Find 2 ships in an 8-bit grid.",
            "hint": "Enter a position (0-7) to target the corresponding bit.",
            "mode": "standard",
            "initial_ships": [2, 5]
        },
        {
            "grid": 0b10101010,  # Ships at positions 1, 3, 5, 7
            "ship_count": 4,
            "description": "Level 3: Find 4 ships in an 8-bit grid.",
            "hint": "Track hits with a separate mask and check remaining ships.",
            "mode": "standard",
            "initial_ships": [1, 3, 5, 7]
        },
        {
            "grid": 0b00110011,  # Ships at positions 0, 1, 4, 5
            "ship_count": 4,
            "description": "Level 4: Toggle 4 ships (positions 0, 1, 4, 5) to 0 using XOR.",
            "hint": "Each shot toggles the bit (1 to 0, 0 to 1). Fire at ship positions (0, 1, 4, 5) to clear them. Non-ship positions create new 1s, but you can toggle them back.",
            "mode": "xor",
            "initial_ships": [0, 1, 4, 5]
        },
        {
            "grid": 0b00001111,  # Ships at positions 0, 1, 2, 3
            "ship_count": 4,
            "description": "Level 5: Find 4 ships (positions 0, 1, 2, 3), observing NOT's effect.",
            "hint": "Each shot shows the inverted grid (~grid). Hit ships in the original grid (0, 1, 2, 3).",
            "mode": "not",
            "initial_ships": [0, 1, 2, 3]
        }
    ]

    for i, level in enumerate(levels, 1):
        print(f"\n=== {level['description']} ===")
        print(f"Grid has {level['ship_count']} ship(s) at positions {level['initial_ships']}.")
        print(f"Hint: {level['hint']}")

        # Initialize level state
        grid = level["grid"]
        ships_remaining = level["ship_count"]
        explored = 0  # Tracks fired positions
        moves = 0
        fired_positions = []  # Debug: track fired positions

        while ships_remaining > 0:
            print(f"\nGrid (hidden): {bin(grid)[2:].zfill(8)}")
            if level["mode"] == "not":
                print(f"Inverted grid (~grid): {bin(~grid & 0xFF)[2:].zfill(8)}")
            print(f"Explored: {bin(explored)[2:].zfill(8)}")
            print(f"Ships remaining: {ships_remaining}")
            print(f"Fired positions: {fired_positions}")

            # Get player's input
            mask_input = input("Enter bit position (0-7) or mask (e.g., '1 << 7') or 'exit'/'restart'/'tutorial_mode': ")
            
            # Check for exit, restart, or tutorial_mode commands
            if mask_input.strip().lower() == "exit":
                print("Thanks for playing Binary Battleship! Goodbye!")
                return
            if mask_input.strip().lower() == "restart":
                print("Level restarted!")
                grid = level["grid"]  # Reset grid
                ships_remaining = level["ship_count"]
                explored = 0
                moves = 0
                fired_positions = []
                continue
            if mask_input.strip().lower() == "tutorial_mode":
                tutorial_mode(grid)
                continue

            try:
                # Try to interpret as a position number first
                try:
                    position = int(mask_input)
                    if 0 <= position <= 7:
                        mask = 1 << position
                    else:
                        raise ValueError("Position must be 0-7")
                except ValueError:
                    # Fallback to evaluating as a mask
                    mask = eval(mask_input, {"__builtins__": {}})

                # Validate mask: must be a single bit in positions 0-7
                valid_masks = [1 << n for n in range(8)]  # 0b00000001 to 0b10000000
                if not (isinstance(mask, int) and mask in valid_masks):
                    print(f"Invalid mask: {bin(mask)[2:].zfill(8)}. Use a position (0-7) or '1 << n'.")
                    continue

                # Get position from mask
                position = valid_masks.index(mask)
                print(f"Firing at position {position} (mask: {bin(mask)[2:].zfill(8)}, value 2^{position})")

                # Check if already fired (only for standard and NOT modes)
                if level["mode"] != "xor" and explored & mask:
                    print(f"You already fired at position {position} (mask: {bin(mask)[2:].zfill(8)})! Try another.")
                    continue

                moves += 1
                explored |= mask  # Mark position as explored
                fired_positions.append(position)  # Log position

                # Handle level-specific logic
                if level["mode"] == "standard":
                    # Standard: Check for hit with AND
                    if grid & mask:
                        print(f"Hit at position {position} (mask: {bin(mask)[2:].zfill(8)})!")
                        ships_remaining -= 1
                    else:
                        print(f"Miss at position {position} (mask: {bin(mask)[2:].zfill(8)})!")
                elif level["mode"] == "xor":
                    # XOR: Toggle the bit
                    was_ship = position in level["initial_ships"]
                    grid ^= mask
                    print(f"Toggled bit at position {position} (new grid: {bin(grid)[2:].zfill(8)})")
                    if was_ship:
                        print(f"Ship at position {position} toggled {'to 0 (cleared)' if not (grid & mask) else 'to 1'}!")
                    else:
                        print(f"Non-ship position {position} toggled {'to 1' if (grid & mask) else 'to 0'}.")
                    # Count remaining ships (1s in grid)
                    ships_remaining = count_set_bits(grid)
                    if ships_remaining == 0:
                        print("All ships toggled to 0!")
                elif level["mode"] == "not":
                    # NOT: Show inverted grid, check hit on original grid, clear ship if hit
                    print(f"Inverted grid after shot: {bin(~grid & 0xFF)[2:].zfill(8)}")
                    if grid & mask:
                        print(f"Hit at position {position} (mask: {bin(mask)[2:].zfill(8)})!")
                        grid &= ~mask  # Clear the ship (set bit to 0)
                        ships_remaining = count_set_bits(grid) # Update remaining ships
                        print(f"Updated grid: {bin(grid)[2:].zfill(8)}")
                    else:
                        print(f"Miss at position {position} (mask: {bin(mask)[2:].zfill(8)})!")

            except Exception as e:
                print(f"Error in your input: {e}. Enter a position (0-7), '1 << n', 'exit', 'restart', or 'tutorial_mode'.")
                continue

        print(f"\nLevel {i} complete! Took {moves} moves to find all ships.")

    print("\nCongratulations! You sank all ships in all levels!")

# Run the game
if __name__ == "__main__":
    binary_battleship()