import time
import os
import random
import shutil
from rich.console import Console
from rich.text import Text
from rich.live import Live
# from rich.panel import Panel # Not used yet

DEFAULT_STYLE = "bold green"
KATAKANA_CHARS = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
ALPHANUMERIC_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
MATRIX_CHARS = KATAKANA_CHARS + ALPHANUMERIC_CHARS

def get_console():
    return Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_print(text: str, delay: float = 0.03, style: str = DEFAULT_STYLE, console=None, new_line_delay: float = 0.2):
    console = console or get_console()
    lines = text.splitlines()
    for i, line in enumerate(lines):
        for char_idx, char in enumerate(line):
            console.print(Text(char, style=style), end="")
            time.sleep(delay)
        # Only print newline if it's not the last line of the input text
        # and the original line had a newline (implicit from splitlines)
        # or if it's the last line and the original text doesn't end with a newline character
        if i < len(lines) - 1:
            console.print()
            time.sleep(new_line_delay)
        elif i == len(lines) -1 and not text.rstrip('\n\r').endswith(line): # handles if last line is not the full end of text
             console.print()
             time.sleep(new_line_delay)


    # If the input text itself ends with a newline, splitlines will produce an empty string at the end
    # if text.endswith(('\n', '\r', '\r\n')):
    #      console.print()
    #      time.sleep(new_line_delay)


def display_ascii_art(filepath: str, console=None, style: str = DEFAULT_STYLE, print_method: str = "direct", typing_delay: float = 0.001, line_delay: float = 0.01):
    console = console or get_console()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            art = f.read()
        if print_method == "typing":
            # For typing art, we want minimal delay between characters of the same line, but some delay after each line.
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
    height -=1 # Adjust for potential off-by-one with console height

    # stores the state of each column, each char is a tuple (char, style_name)
    columns = [[(" ", "default") for _ in range(height)] for _ in range(width)]
    # stores how long a char has been 'bright' to transition to trail
    head_age = [[0 for _ in range(height)] for _ in range(width)]


    with Live(console=console, refresh_per_second=refresh_rate, transient=True, screen=True) as live:
        start_time = time.time()

        while time.time() - start_time < duration:
            # Create the text for the current frame
            current_frame_text = Text()

            for j in range(width): # Iterate over columns
                # Shift characters down
                for i in range(height - 1, 0, -1):
                    columns[j][i] = columns[j][i-1]
                    head_age[j][i] = head_age[j][i-1]

                # Generate new character at the top of the column
                if random.random() < 0.075:  # Chance to start a new drop
                    char = random.choice(MATRIX_CHARS)
                    columns[j][0] = (char, "bold bright_green")
                    head_age[j][0] = 0 # It's new
                else: # Potentially continue an existing drop or leave blank
                    if columns[j][0][0] != " ": # If not blank, update age and style
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


                if columns[j][0][0] == " " and random.random() < 0.01: # very dim, quick flicker
                    columns[j][0] = (random.choice(MATRIX_CHARS), "dim green")
                    head_age[j][0] = 5 # Make it fade quickly

            # Assemble the frame for Rich Live
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
    # Live(transient=True, screen=True) clears the screen on exit

if __name__ == '__main__':
    con = get_console()

    art_dir = "matrix_movie_project/ascii_art"
    test_art_file = os.path.join(art_dir, "test_logo.txt")
    os.makedirs(art_dir, exist_ok=True)
    if not os.path.exists(test_art_file):
        with open(test_art_file, "w", encoding='utf-8') as f:
            f.write("  /\\_/\\  \n")
            f.write(" ( o.o ) \n")
            f.write("  > ^ <  \n")

    clear_screen()
    typing_print("Renderer Test Sequence Initiated...", console=con, style="bold yellow")
    time.sleep(1)

    typing_print("\n--- Testing typing_print ---", console=con, style="bold cyan")
    typing_print("This is a single line test.", console=con)
    typing_print("This is a multi-line test.\nSecond line here.\nAnd a third.", console=con, delay=0.02, new_line_delay=0.1)
    time.sleep(1)

    typing_print("\n--- Testing display_ascii_art (direct) ---", console=con, style="bold cyan")
    display_ascii_art(test_art_file, console=con, style="yellow")
    time.sleep(1)

    typing_print("\n--- Testing display_ascii_art (typing) ---", console=con, style="bold cyan")
    display_ascii_art(test_art_file, console=con, style="magenta", print_method="typing", typing_delay=0.005, line_delay=0.05)
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
