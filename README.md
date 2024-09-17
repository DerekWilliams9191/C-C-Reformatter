# C/C++Reformatter
Moves all the '{' '}' ';' to the edge of the file while keeping everything working

# Fun C Code Formatter

## Introduction

Ever looked at C code and thought: "What if all the braces (`{}`, `;`) were just a bit more... eccentric?" Well, now they can be!

This Python script takes your C files and moves all those pesky `{`, `}`, and `;` characters way off to the right, giving your code a whole new quirky look! The logic and structure remain the same, but the formatting becomes delightfully *weird*.

### What It Does:

- Moves all opening and closing curly braces (`{`, `}`) and semicolons (`;`) to the far right of each line.
- Doesn't change the functionality of the code, just makes it look... different!
- Great for pranks or spicing up your usual code review routine.

## How It Works:

This script:
1. Reads a C file you provide.
2. Scans each line for any `{`, `}`, or `;`.
3. Moves these symbols to a "distant" right-hand location on the same line.
4. Saves the newly formatted code to a new file for your amusement.

## Requirements

- Python 3
- A sense of humor 😄

## Installation

Simply clone this repository, move your c files to aand run the Python script!

```bash
git clone https://github.com/your-repo/fun-c-formatter.git
cd C-Reformatter

```

## Usage

Create two directories

-input
-output

.
├── main.py
├── input/
└── output/

Place the working C code to into the input folder, the run the program and view the output folder

```bash
python3 main.py
```



Example
Before:
```bash
int main() {
    printf("Hello, World!");
    return 0;
}
```

After:
```bash
int main()                                             {
    printf("Hello, World!")                            ;
    return 0                                           };
```

Why Would I Want This?
Because why not?! Life is short, code is serious, and this is your chance to make your colleagues smile (or scream).
It's also a neat way to explore string manipulation in Python if you're learning!
Contributing
Feel free to contribute by:

Improving the code
Right now, comments after a '{' mess things up, so making the code work with comments.
Adding features (maybe move parentheses next?)


License
This project is licensed under the MIT License - see the LICENSE file for details.


