print("^"*50)
print("Work Requirement 2 Electric Boogalo")
print("_"*50)
loop = True
import os

#Task 1
def importfilereadline():
  while loop == True:
    filename = input("Please type in your file name (full path): ")
    if not os.path.exists(filename):
      print("That file doesnt exist!")
    else:
      file = open(filename, "r")
      lines = file.readlines()
      print(lines)
      print("-"*50)
      break

#Task 2
def tasklistmanager():
  import tasks
  tasklist = []
  while loop == True:
    taskinput = input("add or remove task, if done type done: ").lower()
    if taskinput == "add":
      task = input("input task ")
      tasks.add_task(tasklist, task)
      print(tasklist)
    elif taskinput == "remove":
      try:
        task = input("input task to remove ")
        tasks.remove_task(tasklist, task)
        print(tasklist)
      except(ValueError):
        print("Task doesnt exist!")
    elif taskinput == "done":
      print("Goodbye")
      print("-"*50)
      break
    else:
      print("Input Error")

#Task 3
def simpleClassAndInheritance():
  import classes
  student = classes.Student("Joe",23,1234)
  student.greet()
  print(f"Your student id is: {student.student_id}")
  print("-"*50)

#Task 4
def mathQuizExceptionHandling():
  import random
  while loop == True:
    randomNumber1 = random.randint(1, 10)
    randomNumber2 = random.randint(1, 10)
    print(f"The numbers are: {randomNumber1}, {randomNumber2}")

    try:
      playerGuess = int(input("What is the sum?: "))
      if playerGuess == randomNumber1+randomNumber2:
        print(f"Congratulations! The answer was {playerGuess}!")
        print("-"*50)
        break
      else:
        print("Worng! Try again")
    except(ValueError):
      print("Wrong Input (only numbers please).")

#Task 5
def directoryLister():
  try:
    userDirPath = input("Please input a directory path: ")
    print(os.listdir(userDirPath))
    print("-"*50)
  except(FileNotFoundError):
    print("Error, path doesnt exist.")


while loop == True:
  try:
    taskInput = int(input("Please type a number from 1-5 to select a task, type 6 to end: "))

    if taskInput == 1:
      importfilereadline()
    elif taskInput == 2:
      tasklistmanager()
    elif taskInput == 3:
      simpleClassAndInheritance()
    elif taskInput == 4:
      mathQuizExceptionHandling()
    elif taskInput == 5:
      directoryLister()
    elif taskInput == 6:
      break
    else:
      print("Wrong Input!")
  except(ValueError):
    print("Value Error!")
