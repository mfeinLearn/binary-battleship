# Binary Battleship

```plain
__________ .__                                 
\______   \|__|  ____  _____   _______  ___.__.
 |    |  _/|  | /    \ \__  \  \_  __ \<   |  |
 |    |   \|  ||   |  \ / __ \_ |  | \/ \___  |
 |______  /|__||___|  /(____  / |__|    / ____|
        \/          \/      \/          \/     

__________           __     __   .__                   .__     .__         
\______   \_____   _/  |_ _/  |_ |  |    ____    ______|  |__  |__|______  
 |    |  _/\__  \  \   __\\   __\|  |  _/ __ \  /  ___/|  |  \ |  |\____ \ 
 |    |   \ / __ \_ |  |   |  |  |  |__\  ___/  \___ \ |   Y  \|  ||  |_> >
 |______  /(____  / |__|   |__|  |____/ \___  >/____  >|___|  /|__||   __/ 
        \/      \/                          \/      \/      \/     |__|     
```
**Binary Battleship** is an interactive Python game designed to teach bitwise operations (AND, OR, XOR, NOT) through a fun, Battleship-inspired 8-bit grid. Each level challenges you to manipulate binary digits, making it ideal for mastering bit manipulation for coding interviews or computer science fundamentals. Think of it as Conway’s Game of Life, but for binary operations!
 
### 📚 Why Learn Bitwise Operations?
Bitwise operations manipulate binary digits (bits), the foundation of computer data. They are fast, efficient, and essential for algorithms, low-level programming, and coding interview questions. Here’s a concise primer:

- **AND** (&): Outputs 1 if both bits are 1.Example: 0b1100 & 0b1010 = 0b1000.
- **OR** (|): Outputs 1 if either bit is 1.Example: 0b1100 | 0b1010 = 0b1110.
- **XOR** (^): Outputs 1 if bits differ.Example: 0b1100 ^ 0b1010 = 0b0110.
- **NOT** (~): Flips all bits (in 8 bits: ~0b00001111 = 0b11110000).  
- **Left Shift** (<<): Shifts bits left, adding zeros.Example: 1 << 2 = 0b00000100.

In **Binary Battleship**, you fire at positions in an 8-bit grid (0–7, right-to-left: position 0 = 2^0, position 7 = 2^7) to practice these operations hands-on.

### 🚀 Installation
1. Clone the Repository:
```bash

git clone https://github.com/your-username/binary-battleship.git
cd binary-battleship
```

2. Requirements:
- Python 3.x
- No external libraries required.


3. Run the Game:
```bash
python binary_battleship.py
```


### 🎮 How to Play


- **Objective**: Find or toggle ships (1s) in an 8-bit grid by firing at positions (0–7).
- **Input**:
- Enter a position (e.g., 2 for position 2, mask 0b00000100).
- Or use a mask (e.g., 1 << 2 or 0b00000100).
- Type exit to quit or restart to reset the current level.



- **Grid Layout**: Right-to-left, 0-based indexing:
```plain
Position:  7  6  5  4  3  2  1  0
Mask:      10000000 01000000 00100000 00010000 00001000 00000100 00000010 00000001
Value:     2^7  2^6  2^5  2^4  2^3  2^2  2^1  2^0
```



- **Levels**:

| Level | Operation | Ships | Goal                                 | Ship Positions     |
|-------|-----------|-------|--------------------------------------|--------------------|
| 1     | AND       | 1     | Find ships using grid & mask         | [2]                |
| 2     | AND       | 2     | Find ships using grid & mask         | [2, 5]             |
| 3     | AND       | 4     | Find ships using grid & mask         | [1, 3, 5, 7]       |
| 4     | XOR       | 4     | Toggle ships to 0 using grid ^= mask | [0, 1, 4, 5]       |
| 5     | NOT       | 4     | Find ships, clear with grid &= ~mask | [0, 1, 2, 3]       |




### 📖 Tutorial: Learn Bitwise Operations
Explore Level 1 (AND) and Level 4 (XOR) to understand bitwise operations in action.

### Level 1: Find 1 Ship with AND

**Grid**: 0b00000100 (ship at position 2).
**Goal**: Hit the ship at position 2 using grid & mask.
**Run**:
```plaintext
=== Level 1: Find 1 ship in an 8-bit grid. ===
Grid has 1 ship(s) at positions [2].
Hint: Enter a position (0-7) or use '1 << n' to fire at position n.
Grid (hidden): 00000100
Explored: 00000000
Ships remaining: 1
Fired positions: []
Enter bit position (0-7) or mask (e.g., '1 << 2') or 'exit'/'restart': 2
Firing at position 2 (mask: 00000100, value 2^2)
Hit at position 2 (mask: 00000100)!
```


- **What You Learn**:
Input 2 creates mask 1 << 2 = 0b00000100.
grid & mask = 0b00000100 & 0b00000100 = 0b00000100 confirms a hit.
AND checks if a bit is 1 (ship).



### Level 4: Toggle Ships with XOR

- **Grid**: 0b00110011 (ships at positions 0, 1, 4, 5).
- **Goal**: Toggle all 1s to 0s using grid ^= mask. Non-ship positions (e.g., 7) toggle 0 → 1, but you can toggle them back.
- **Run**:
```plaintext
=== Level 4: Toggle 4 ships (positions 0, 1, 4, 5) to 0 using XOR. ===
Grid has 4 ship(s) at positions [0, 1, 4, 5].
Hint: Each shot toggles the bit (1 to 0, 0 to 1). Fire at ship positions (0, 1, 4, 5) to clear them. Non-ship positions create new 1s, but you can toggle them back.
Grid (hidden): 00110011
Explored: 00000000
Ships remaining: 4
Fired positions: []
Enter bit position (0-7) or mask (e.g., '1 << 7') or 'exit'/'restart': 7
Firing at position 7 (mask: 10000000, value 2^7)
Toggled bit at position 7 (new grid: 10110011)
Non-ship position 7 toggled to 1.
Enter bit position (0-7) or mask (e.g., '1 << 7') or 'exit'/'restart': 7
Firing at position 7 (mask: 10000000, value 2^7)
Toggled bit at position 7 (new grid: 00110011)
Non-ship position 7 toggled to 0.
Enter bit position (0-7) or mask (e.g., '1 << 7') or 'exit'/'restart': 0
Firing at position 0 (mask: 00000001, value 2^0)
Toggled bit at position 0 (new grid: 00110010)
Ship at position 0 toggled to 0 (cleared)!
```

- **What You Learn**:
XOR toggles bits: 0 ^ 1 = 1, 1 ^ 1 = 0.
Firing at 7 (non-ship) toggles 0 → 1, then back to 0.
Firing at 0 (ship) toggles 1 → 0, reducing ships.
Goal: Toggle positions 0, 1, 4, 5 to clear the grid.



### 🤝 Contributing
This project is designed to help you learn bitwise operations! We welcome contributions to improve the game and its educational value. If you notice mistakes (e.g., bugs in gameplay, typos in the README) or have ideas for enhancements (e.g., new levels, clearer explanations), please contribute! Examples include:

- Fixing bugs, such as incorrect bit toggling in the XOR level.
- Adding levels with new bitwise operations, like bit rotation.
- Improving tutorials with better bitwise examples.
- Creating visualizations, such as grid charts.

To contribute:

1. Fork the repository.
2. Create a branch:

```bash
git checkout -b feature/fix-bug
```

3. Commit changes:
```bash
git commit -m "Fixed XOR level bug"
```

4. Push to your branch:
```bash
git push origin feature/fix-bug
```

5. Open a pull request with a clear description of your changes.

Please include comments explaining your bitwise operations to help others learn.

### 📄 License
MIT License - feel free to use and modify!

### 🙌 Acknowledgments
Inspired by Battleship and Conway’s Game of Life, this project makes bit manipulation fun and accessible for learners.