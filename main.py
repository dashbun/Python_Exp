from contextlib import contextmanager

@contextmanager
def genericFileFunction (filename, method):
    file = open (filename, method)
    yield file
    file.close ()

if __name__ == '__main__':
    filename="Swayam.txt"
    with genericFileFunction(filename, 'w') as file:

        file.write("I am ")

    with genericFileFunction(filename, 'r') as file:

        content = file.read()
        print("Content:", content)

    with genericFileFunction(filename, 'a') as file:

        file.write("\nSwayam .")

    with genericFileFunction(filename, 'a') as file:
        updated_content = file.write("Raut")
        print("appending:", updated_content)
    '''
    Print all the output of the function.
    For better representation, please use jupyter.
    Will also aid in easy maintanence of files for submissions.
    '''


   
