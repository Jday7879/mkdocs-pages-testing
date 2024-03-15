import numpy as np

def printing_own(text:str = 'empty'):
    """ text 
    This is a function to print a string
    
    Parameters
    ----------
    text - string
      A string to print
    """
    print(text)

def create_array():
    """
    function to create numpy array
    """
    x = np.zeros((1,3))
    return x

def testing_docstring():
    """Execute a command via subprocess, capturing stdout and stderr.

    This function creates a subprocess with the provided command list, then
    communicates with it to retrieve the stdout and stderr. After the
    command execution, it checks the process's return code to determine success
    or failure. A zero return code indicates success.

    Parameters
    ----------
    command
        A list of command elements representing the system
        command to be executed. For example, ['ls', '-l', '/home/user'].

    Returns
    -------
    bool
        True if the command execution is successful (return code 0),
        otherwise False.

    Raises
    ------
    subprocess.TimeoutExpired
        If the process does not complete within the default timeout.
    """
    print('testing 2')

if __name__ == "__main__":
    printing_own('testing')
    x = create_array()
    print(x)
    testing_docstring()
