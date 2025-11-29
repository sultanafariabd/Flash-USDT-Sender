import os
import time
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
    animate_text("Authenticating...", color=Fore.YELLOW)
    print()

    try:
        # Get access key from environment variable
        correct_key = os.environ.get('DEPLOY_ACCESS_KEY')
        if not correct_key:
            print(Fore.RED + "Error: DEPLOY_ACCESS_KEY environment variable not set.")
            animate_text("Authentication failed.", color=Fore.RED)
            return

        # Validate the key
        if correct_key:
            print(Fore.GREEN + "\nAuthentication successful.")
            animate_text("Access granted.", color=Fore.GREEN)
        else:
            print(Fore.RED + "\nAuthentication failed.")
            animate_text("Access denied.", color=Fore.RED)

    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nOperation cancelled by user.")

if __name__ == "__main__":
    main()
