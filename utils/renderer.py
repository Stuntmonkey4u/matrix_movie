import time
import os
import random
import shutil
from rich.console import Console # Ensure this is here
from rich.text import Text
from rich.live import Live

DEFAULT_STYLE = "bright_green" # Changed from "bold green"
KATAKANA_CHARS = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
ALPHANUMERIC_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
MATRIX_CHARS = KATAKANA_CHARS + ALPHANUMERIC_CHARS

def get_console():
    return Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_print(text: str, delay: float = 0.034, style: str = DEFAULT_STYLE, console=None, new_line_delay: float = 0.2): # Adjusted default delay
    console = console or get_console()

    lines = text.split('\n')
    num_lines = len(lines)

    for i, line in enumerate(lines):
        for char_code in line: # Iterate through characters of the current line segment
            console.print(Text(char_code, style=style), end="")
            time.sleep(delay)

        console.print()

        if i < num_lines - 1:
            time.sleep(new_line_delay)

def display_ascii_art(filepath: str, console=None, style: str = DEFAULT_STYLE, print_method: str = "direct", typing_delay: float = 0.001, line_delay: float = 0.01):
    console = console or get_console()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            art = f.read()
        if print_method == "typing":
            typing_print(art, delay=typing_delay, style=style, console=console, new_line_delay=line_delay)
        else:
            console.print(Text(art, style=style))
    except FileNotFoundError:
        console.print(f"[bold red]Error: ASCII art file not found: {filepath}[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error displaying ASCII art: {e}[/bold red]")


def matrix_code_rain(duration: float = 7, console=None, refresh_rate: int = 15):
    console = console or get_console()
    width, height = shutil.get_terminal_size()
    height -=1

    columns = [[(" ", "default") for _ in range(height)] for _ in range(width)]
    head_age = [[0 for _ in range(height)] for _ in range(width)]

    with Live(console=console, refresh_per_second=refresh_rate, transient=True, screen=True) as live:
        start_time = time.time()

        while time.time() - start_time < duration:
            current_frame_text = Text()
            for j in range(width):
                for i in range(height - 1, 0, -1):
                    columns[j][i] = columns[j][i-1]
                    head_age[j][i] = head_age[j][i-1]

                if random.random() < 0.075:
                    char = random.choice(MATRIX_CHARS)
                    columns[j][0] = (char, "bold bright_green")
                    head_age[j][0] = 0
                else:
                    if columns[j][0][0] != " ":
                        head_age[j][0] +=1
                        current_char, current_style = columns[j][0]

                        if current_style == "bold bright_green" and head_age[j][0] > 1:
                             columns[j][0] = (current_char, "green")
                        elif current_style == "green" and head_age[j][0] > 3:
                             columns[j][0] = (current_char, "dark_green")
                        elif current_style == "dark_green" and head_age[j][0] > 6:
                             columns[j][0] = (" ", "default")
                             head_age[j][0] = 0
                    else:
                        head_age[j][0] = 0

                if columns[j][0][0] == " " and random.random() < 0.01:
                    columns[j][0] = (random.choice(MATRIX_CHARS), "dim green")
                    head_age[j][0] = 5

            for i in range(height):
                line_text = Text()
                for j in range(width):
                    char, style_name = columns[j][i]
                    line_text.append(char, style=style_name)
                current_frame_text.append(line_text)
                if i < height -1:
                    current_frame_text.append("\n")

            live.update(current_frame_text)
            time.sleep(1/refresh_rate)

def conditional_paging_prompt(console: Console, paging_enabled: bool, message: str = "- - - Press Enter to continue - - -"):
    if paging_enabled:
        if console is None: # Fallback if no Rich console is passed (e.g. very early error)
            # Basic print and input, no Rich formatting.
            # Add extra newlines for spacing similar to Rich version.
            print(f"\n\n{message}\n")
            input() # Wait for user to press Enter
            return # Exit the function

        # Use Rich console for formatted output
        console.print(f"\n\n[bold yellow]{message}[/bold yellow]", justify="center")
        input() # Wait for user to press Enter

if __name__ == '__main__':
    con = get_console()

    art_dir = os.path.join(os.path.dirname(__file__), "..", "ascii_art")
    if not os.path.isabs(art_dir):
        art_dir = os.path.join(os.path.dirname(__file__), art_dir)

    art_dir_test_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ascii_art'))
    test_art_file = os.path.join(art_dir_test_path, "test_logo.txt")

    os.makedirs(art_dir_test_path, exist_ok=True)
    if not os.path.exists(test_art_file):
        with open(test_art_file, "w", encoding='utf-8') as f:
            f.write("  /\\_/\\  \n")
            f.write(" ( o.o ) \n")
            f.write("  > ^ <  \n")

    clear_screen()
    typing_print("Renderer Test Sequence Initiated...", console=con, style="bold yellow")
    time.sleep(1)

    typing_print("\n--- Testing typing_print (New Logic) ---", console=con, style="bold cyan")
    typing_print("This is a single line test.", console=con)
    typing_print("This is a multi-line test.\nSecond line here.\nAnd a third (ends without newline in string).", console=con, delay=0.02, new_line_delay=0.1)
    typing_print("This has explicit trailing newline.\n", console=con, delay=0.02, new_line_delay=0.1)
    typing_print("Line A\n\nLine C (should have empty line between A and C)", console=con, delay=0.02, new_line_delay=0.1)
    time.sleep(1)

    typing_print("\n--- Testing display_ascii_art (direct) ---", console=con, style="bold cyan")
    display_ascii_art(test_art_file, console=con, style="yellow")
    time.sleep(1)

    typing_print("\n--- Testing display_ascii_art (typing) ---", console=con, style="bold cyan")
    display_ascii_art(test_art_file, console=con, style="magenta", print_method="typing", typing_delay=0.005, line_delay=0.05)
    time.sleep(1)

    # Test conditional_paging_prompt
    typing_print("\n--- Testing conditional_paging_prompt ---", console=con, style="bold cyan")
    typing_print("Paging DISABLED test (should not wait):", console=con)
    conditional_paging_prompt(con, False, "Test: Paging Disabled (you should NOT see this prompt wait)")
    typing_print("Paging DISABLED test complete.", console=con)

    typing_print("\nPaging ENABLED test (will wait for Enter):", console=con)
    conditional_paging_prompt(con, True, "Test: Paging Enabled (Press Enter to continue)")
    typing_print("Paging ENABLED test complete (Enter was pressed).", console=con)
    time.sleep(1)

    typing_print("\n--- Testing Matrix Code Rain (7 seconds) ---", console=con, style="bold cyan")
    time.sleep(1.5)
    matrix_code_rain(duration=7, console=con, refresh_rate=20)

    typing_print("Matrix Code Rain finished.", console=con, style="bold green")
    time.sleep(1)

    typing_print("\n--- Testing Error Handling for display_ascii_art ---", console=con, style="bold cyan")
    display_ascii_art("non_existent_file.txt", console=con)
    time.sleep(1)

    typing_print("\nRenderer tests complete.", console=con, style="bold yellow")
    typing_print("This terminal will revert in 3 seconds...", style="bold red", new_line_delay=0.5)
    time.sleep(3)
    clear_screen()
