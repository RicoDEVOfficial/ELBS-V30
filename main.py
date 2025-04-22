from Core.Networking.Server import Server
from colorama import init, Fore, Style
import threading

def start_server():
    Server("0.0.0.0", 9339).start()

def main():
    init(autoreset=True)

    print(
        f"{Style.BRIGHT + Fore.WHITE}Welcome "
        f"{Fore.GREEN}to "
        f"{Fore.LIGHTBLUE_EX}ELBS "
        f"{Fore.LIGHTMAGENTA_EX}V30\n"
        f"{Fore.LIGHTYELLOW_EX}Made "
        f"{Fore.LIGHTWHITE_EX}by "
        f"{Fore.LIGHTBLUE_EX}Rico"
        f"{Style.BRIGHT + Fore.WHITE}DEV"
    )

    threading.Thread(target=start_server).start()

if __name__ == "__main__":
    main()