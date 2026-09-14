# Computer-Science-II: Distance Calculator

A simple Python program that calculates the Euclidean distance between two points on a 2D plane. This project is perfect for beginners learning about math libraries, formulas, and handling user input.

## The Formula

The program calculates the distance \(d\) between two coordinates \((x_1, y_1)\) and \((x_2, y_2)\) using the standard Euclidean distance formula:

\[d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}\]

## Requirements

* Python 3.x (Uses standard libraries; no external installations needed)

## How to Run

1. Clone or download this repository.
2. Open your terminal or command prompt.
3. Run the script using Python:
   ```bash
   D21-1FA05-NACALABAN.py
   ```

## Usage Examples

Here is how the program works in practice based on common coordinate pairs.

### Example 1: Standard Positive Integers
* **Input Point 1:** (3, 4)
* **Input Point 2:** (7, 7)

**Terminal Output:**
```text
Enter x1: 3
Enter y1: 4
Enter x2: 7
Enter y2: 7

Calculating distance...
The distance between (3.0, 4.0) and (7.0, 7.0) is 5.0
```

### Example 2: Handling Negative Coordinates
* **Input Point 1:** (-1, -3)
* **Input Point 2:** (2, 1)

**Terminal Output:**
```text
Enter x1: -1
Enter y1: -3
Enter x2: 2
Enter y2: 1

Calculating distance...
The distance between (-1.0, -3.0) and (2.0, 1.0) is 5.0
```

### Example 3: Zero Distance (Same Point)
* **Input Point 1:** (0, 0)
* **Input Point 2:** (0, 0)

**Terminal Output:**
```text
Enter x1: 0
Enter y1: 0
Enter x2: 0
Enter y2: 0

Calculating distance...
The distance between (0.0, 0.0) and (0.0, 0.0) is 0.0
```
