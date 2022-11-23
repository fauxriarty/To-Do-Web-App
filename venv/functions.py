FILEPATH="C:/Users/Aditya/PycharmProjects/To-Do List/venv/todos.txt"

# to read the todos written into the file so far
def get_todos(filepath=FILEPATH):
    """read a text file and return the list of 
            to-do items """ #docstring for get_todos function

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """write the to-do items list in the text file"""

    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__=="__main__":
    print("Hello")
'''this statement means that all the fns 
under this if will only be run if this program i.e. functions.py 
is run separately, but if you import functions in a diff file then 
the code under this if name==main will not run'''