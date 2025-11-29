import os
import time
import getpass
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# ASCII Art for Flash USDT
USDT_ART = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀
⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀
⠀⢠⣿⣿⣿⣿⣿⡟⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢻⣿⣿⣿⣿⣿⡄⠀
⢠⣿⣿⣿⣿⣿⣿⣧⣤⣤⣤⣤⡄⠀⠀⢠⣤⣤⣤⣤⣼⣿⣿⣿⣿⣿⣿⡄
⢸⣿⣿⣿⣿⣿⣿⡿⠟⠛⠋⠉⠁⠀⠀⠈⠉⠙⠛⠻⢿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣏⠀⠶⢾⣿⣿⣧⣤⣤⣼⣿⣿⡷⠶⠀⣹⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣷⣦⣤⣄⣀⡀⠉⠉⢀⣀⣠⣤⣴⣾⣿⣿⣿⣿⣿⣿⡇
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀
⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

def animate_text(text, color=Fore.CYAN, delay=0.05):
    """Prints text with a typing animation."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def display_logo():
    """Clears the screen and displays the animated logo."""
    os.system('cls' if os.name == 'nt' else 'clear')
    colors = [Fore.GREEN, Fore.CYAN, Fore.WHITE, Fore.GREEN]
    lines = USDT_ART.strip().split('\n')
    for i, line in enumerate(lines):
        print(colors[i % len(colors)] + line)
        time.sleep(0.05)
    print()

def main():
    """Main function to run the authentication script."""
    display_logo()

    animate_text("Welcome to Flash USDT Sender", color=Fore.YELLOW)
    animate_text("Please provide your access key to continue.", color=Fore.YELLOW)
    print()

    try:
        # Get access key from environment variable
        correct_key = os.environ.get('DEPLOY_ACCESS_KEY')
        if not correct_key:
            print(Fore.RED + "Error: DEPLOY_ACCESS_KEY environment variable not set.")
            return

        # Prompt user for access key
        animate_text("What is your access key?", delay=0.03)
        user_key = getpass.getpass("Access Key: ")

        # Validate the key
        if user_key == correct_key:
            print(Fore.RED + "\nAuthentication failed.")
            animate_text("Access denied.", color=Fore.RED)
        else:
            print(Fore.RED + "\nAuthentication failed.")
            animate_text("Access denied.", color=Fore.RED)

    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nOperation cancelled by user.")

if __name__ == "__main__":
    main()
