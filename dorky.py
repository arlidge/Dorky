from googlesearch import search
from termcolor import colored
import pyfiglet
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def search_dork():
    clear_screen()
    banner = pyfiglet.figlet_format("Dork", font="slant")
    print(colored(banner, "cyan"))
    dork = input(colored("Enter Dork to search: ", "cyan"))
    for i in search(dork, tld="co.in", num=100, stop=100, pause=2):
        print(i)
    input(colored("\nPress Enter to continue...", "cyan"))
    clear_screen()

def search_sql():
    clear_screen()
    banner = pyfiglet.figlet_format("Dork", font="slant")
    print(colored(banner, "cyan"))
    print(colored("Potentially Sql Injectable sites ", "blue"))
    for j in search("inurl:/index.php?id=", tld="co.in", num=100, stop=100, pause=2):
        print(j)
    input(colored("\nPress Enter to continue...", "cyan"))
    clear_screen()

def search_sql_pass():
    clear_screen()
    banner = pyfiglet.figlet_format("Dork", font="slant")
    print(colored(banner,"cyan"))
    print(colored("Printers","blue"))
    for i in search("inurl:printer/main.html intext:settings", tld="co.in", num=100, stop=100, pause=2):
        print(i)
    input(colored("\nPress Enter to continue...", "cyan"))
    clear_screen()

def show_menu():
    result = pyfiglet.figlet_format("Dork", font="slant")
    print(colored(result, "cyan"))
    print(colored("1. Dork Search","green"))
    print(colored("2. Sql Inject","red"))
    print(colored("3. Printers","red"))
    print(colored("4. Exit","yellow"))

while True:
    show_menu()
    choice = input(colored("Enter your choice: ","blue"))
    if choice == "1":
        search_dork()
    elif choice == "2":
        search_sql()
    elif choice =="3":
        search_sql_pass()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print(colored("Invalid choice. Please try again.","red"))
        input(colored("\nPress Enter to continue...", "cyan"))
        clear_screen()
