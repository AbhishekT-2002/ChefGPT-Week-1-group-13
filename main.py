import importlib


def run_script(script_name):
    """
    Attempts to import and execute the specified script.

    Args:
        script_name (str): The name of the script (A-E) to be executed.

    Returns:
        None
    """
    try:
        module = importlib.import_module(script_name)
        # Execute the script's code directly
        exec(open(f"{script_name}.py", "r").read())
    except ModuleNotFoundError:
        print(f"Script '{script_name}' not found!")
    except Exception as e:
        print(f"Error running script '{script_name}': {e}")


if __name__ == "__main__":
    while True:
        choice = input(
            " 0. Default \n 1. Indian\n 2. Thai\n 3. South Indian\n 4. EXIT\n Choose a chef to interact with:")
        if choice == "0":
            run_script("default_chef")
        elif choice == "1":
            run_script("Abhi_mIOHa2")
        elif choice == "2":
            run_script("Ruchida_bOEXwz")
        elif choice == "3":
            run_script("rparthas_MCn2Bp")
        elif choice == "4":
            exit()
        else:
            print("Invalid input. Please try again.")
