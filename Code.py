import os

def bypass_admin_and_install_program(program_path):
    # Creating a directory to store the program files
    os.makedirs('bypass_install', exist_ok=True)
    
    # Copying the program files to the new directory
    try:
        os.system(f'copy "{program_path}" bypass_install')
    except Exception as e:
        print(f'Error: {e}')
    
    # Adding the directory to the system PATH to make it executable
    try:
        os.system('set PATH=%PATH%;bypass_install')
    except Exception as e:
        print(f'Error: {e}')
    
    # Attempting to run the program
    try:
        os.system('program.exe')  # Replace 'program.exe' with the executable file name
    except Exception as e:
        print(f'Error: {e}')

# Example usage:
program_path = input('Enter the path to the program executable: ')
bypass_admin_and_install_program(program_path)
