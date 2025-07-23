def binary_battleship():
    print("Welcome to Binary Battleship! Find ships (1s) in an 8-bit grid.")
    print("Positions are 0-7, right-to-left (0 = rightmost (2^0), 7 = leftmost (2^7)).")
    print("Enter a bit position (0-7) as a number (e.g., '7') or a mask (e.g., '1 << 7' or '0b10000000').")
    print("Type 'exit' to quit the game or 'restart' to reset the current level.\n")

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
            mask_input = input("Enter bit position (0-7) or mask (e.g., '1 << 7') or 'exit'/'restart': ")
            
            # Check for exit or restart commands
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
                    ships_remaining = bin(grid).count('1')
                    if ships_remaining == 0:
                        print("All ships toggled to 0!")
                elif level["mode"] == "not":
                    # NOT: Show inverted grid, check hit on original grid, clear ship if hit
                    print(f"Inverted grid after shot: {bin(~grid & 0xFF)[2:].zfill(8)}")
                    if grid & mask:
                        print(f"Hit at position {position} (mask: {bin(mask)[2:].zfill(8)})!")
                        grid &= ~mask  # Clear the ship (set bit to 0)
                        ships_remaining = bin(grid).count('1')  # Update remaining ships
                        print(f"Updated grid: {bin(grid)[2:].zfill(8)}")
                    else:
                        print(f"Miss at position {position} (mask: {bin(mask)[2:].zfill(8)})!")

            except Exception as e:
                print(f"Error in your input: {e}. Enter a position (0-7), '1 << n', 'exit', or 'restart'.")
                continue

        print(f"\nLevel {i} complete! Took {moves} moves to find all ships.")

    print("\nCongratulations! You sank all ships in all levels!")

# Run the game
if __name__ == "__main__":
    binary_battleship()