# Temperature Converter

A small Python project that converts temperatures between Celsius, Fahrenheit and Kelvin. Made for Applied Robotics and AI Project, Assignment 1, to practise Git and project management.

## How to run
python converter.py

## Functions
- c_to_f(c): Celsius to Fahrenheit
- f_to_c(f): Fahrenheit to Celsius
- c_to_k(c): Celsius to Kelvin

## Workflow
1. Plan the task as a card on the Trello board (To Do, In Progress, Done)
2. Create a branch for the feature
3. Edit, then add, commit and push
4. Open a Pull Request and merge into main
5. Move the Trello card to Done and attach the PR link

## Branching strategy
- main holds the working code
- Each new feature gets its own branch (e.g. feature-kelvin, add-readme)
- Branches are merged into main through a Pull Request, then deleted

## Add vs Commit vs Push

- **git add**: I use this to pick which changed files I want to save next. Nothing is saved yet, the file is just marked as ready. Example: `git add converter.py`
- **git commit**: This saves the files I picked as a snapshot on my own computer, with a message saying what I changed. Example: `git commit -m "Add f_to_c function"`
- **git push**: This sends my saved commits to GitHub. Before I push, my work only exists on my laptop. After I push, it's backed up online and my lecturer can see it. Example: `git push`

I keep them as three steps so I can check my changes before they go online.
## Key commands
git clone <url>
git add <file>
git commit -m "message"
git push
git checkout -b <branch>