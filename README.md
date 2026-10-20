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
- git add: selects which changes go into the next snapshot
- git commit: saves that snapshot in the local history with a message
- git push: uploads local commits to GitHub so they are backed up

## Key commands
git clone <url>
git add <file>
git commit -m "message"
git push
git checkout -b <branch>