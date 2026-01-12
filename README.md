# python-collatz-sequence
The Collatz conjecture is a well-known mathematical problem where you repeatedly transform a number: divide by 2 if it’s even, or multiply by 3 and add 1 if it’s odd until it reaches 1

# Collatz Conjecture – Python Implementation

This project implements the Collatz sequence algorithm in Python.

## What is the Collatz Conjecture?

The Collatz conjecture (also known as the 3n + 1 problem) is a famous unsolved problem in mathematics.  
Starting from any positive integer:

- If the number is **even**, divide it by 2
- If the number is **odd**, multiply it by 3 and add 1  

The process repeats until the number reaches 1. :contentReference[oaicite:1]{index=1}

## Features

✔ Takes user input for any positive integer  
✔ Generates Collatz sequence step by step  
✔ Shows number of steps it takes to reach 1  
✔ (Optional) Plots graph of sequence values  
✔ (Optional) Calculates total stopping time

## How to Run

1. Clone the repository  
   `git clone https://github.com/YOUR_USERNAME/python-collatz-sequence.git`

2. Run the program  
   `python collatz.py`

## Example Output
Enter a number: 6
Sequence: [6, 3, 10, 5, 16, 8, 4, 2, 1]
