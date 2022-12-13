FILEPATH = 'todos.txt'



#function to read the current todo items in file and return them.
def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of todo items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


#function to write the updated todo list to a file.
def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the update todo list to the todo file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == '__main__':
    print('Hello')
    print(get_todos())
