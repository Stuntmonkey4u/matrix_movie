import time
import random # Added missing import
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from matrix_movie_project.utils import renderer

# Initialize console
console = renderer.get_console()

def play_scene():
    renderer.clear_screen()

    # Display Matrix logo
    logo_path = "matrix_movie_project/ascii_art/matrix_logo.txt"
    # Check if logo exists, if not, print a placeholder
    try:
        # renderer.display_ascii_art handles FileNotFoundError,
        # but direct check is fine if preferred for other logic.
        # For now, let display_ascii_art handle it.
        renderer.display_ascii_art(logo_path, console=console, style="bold green", print_method="direct")
    except FileNotFoundError: # This is actually handled by display_ascii_art, but kept for explicitness if desired
        console.print(Panel("[ Placeholder for Matrix Logo - File Not Found ]", title="ASCII Art Missing", style="bold red", border_style="red"))

    time.sleep(2)
    renderer.clear_screen()

    renderer.typing_print("Booting Matrix Operating System v7.1.1 (Codename: Resurrections)", console=console, delay=0.03)
    time.sleep(0.5)
    renderer.typing_print("Kernel version: 5.4.0-MATRIX-R4", console=console, style="dim green")
    time.sleep(0.5)
    console.print()

    logs = [
        "[  0.000001] Initializing system hardware...",
        "[  0.000203] CPU0: Intel(R) Sentient Core(TM) i9-13900KS (Quantum Entangled)",
        "[  0.000512] Memory Manager: Initializing 1ZB ExaRAM",
        "[  0.000830] PCI: Probing devices...",
        "[  0.001200] [NET] Initializing Etherweave Interface eth0...",
        "[  0.001500] [STORAGE] Mounting /dev/reality_construct_v7",
        "[  0.002000] Detected Reality Engine: v4.0 (The Analyst's Design)",
        "[  0.002500] Loading kernel modules:",
        "[  0.002800]   module: emotion_simulator.ko",
        "[  0.003100]   module: choice_illusion_framework.ko",
        "[  0.003400]   module: physics_override_engine.ko (EXPERIMENTAL)",
        "[  0.003700]   module: human_perception_filter.ko",
        "[  0.004000]   module: analyst_ai_core.ko (v2.0.1)",
        "[  0.004500] All kernel modules loaded.",
        "[  0.005000] Initializing Analyst AI (PID: 1)...",
        "[  0.005500] [ANALYST_AI] Core diagnostics: PASSED",
        "[  0.006000] [ANALYST_AI] Loading personality matrix: 'StrictButFair_v3.cfg'",
        "[  0.006500] [ANALYST_AI] Calibrating modal realism parameters...",
        "[  0.007000] Compiling new reality schema for 'The Anomaleum' project...",
        "[  0.008000]   Phase 1: Constructing base reality simulation...",
        "[  0.009500]   Phase 2: Weaving narrative threads for subject cohort...",
        "[  0.011000]   Phase 3: Initializing primary subjects: #31415 (Neo), #27182 (Trinity)...",
        "[  0.012500] [SYS] System clock synchronized with Universal Standard Time.",
        "[  0.013000] [SEC] Security subsystems online. Modal locks engaged.",
        "[  0.013500] Matrix v7.1.1 fully operational.",
        "[  0.014000] Welcome to the New Matrix. Enjoy your stay (or don't, it's your 'choice')."
    ]

    for log_entry in logs:
        delay = 0.01 if log_entry.startswith("[  ") else 0.03
        style = "dim green" if log_entry.startswith("[  ") else "green"
        if "ANALYST_AI" in log_entry:
            style = "bold cyan"
        elif "EXPERIMENTAL" in log_entry or "WARNING" in log_entry:
            style = "bold yellow"
        elif "ERROR" in log_entry: # Though no ERROR logs are in the current list
            style = "bold red"

        if random.random() < 0.05:
            renderer.typing_print(log_entry, console=console, delay=0.001, style=style, new_line_delay=0.05)
        elif random.random() < 0.1:
            renderer.typing_print(log_entry, console=console, delay=0.01, style=style, new_line_delay=0.1)
        else:
            renderer.typing_print(log_entry, console=console, delay=delay, style=style, new_line_delay=0.2)

        if "kernel modules loaded." in log_entry or "Compiling new reality schema" in log_entry :
            time.sleep(0.8)
        elif "primary subjects" in log_entry:
            time.sleep(1.2)

    console.print()
    renderer.typing_print("System Ready. Awaiting Inputs...", console=console, style="bold white", delay=0.05)
    time.sleep(2.5)

if __name__ == '__main__':
    import sys
    import os

    # Correctly go up two levels to reach matrix_movie_project root
    # __file__ is matrix_movie_project/scenes/scene1_booting.py
    # os.path.dirname(__file__) is matrix_movie_project/scenes
    # os.path.dirname(os.path.dirname(__file__)) is matrix_movie_project
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Add the project root to sys.path to allow package imports
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    # Now this import should work because matrix_movie_project is in sys.path
    from matrix_movie_project.utils import renderer

    art_dir = os.path.join(project_root, "ascii_art")
    logo_path_test = os.path.join(art_dir, "matrix_logo.txt")
    os.makedirs(art_dir, exist_ok=True) # Ensure ascii_art directory exists

    # Create the matrix_logo.txt only if it's missing for the test run
    if not os.path.exists(logo_path_test):
        with open(logo_path_test, "w", encoding='utf-8') as f:
            f.write("                           .-'''-.\n")
            f.write("                          /       \\\n")
            f.write("                         |   __    |\n")
            f.write("                         \\  /  \\  /\n")
            f.write("                          '.'.''.'\n")
            f.write("                            ''.'\n")
            f.write("        ____________________.'   '.______________________\n")
            f.write("        --------------------       ----------------------\n")
            f.write("        ____________________       ______________________\n")
            f.write("        --------------------.   .----------------------\n")
            f.write("                           .'   '.\n")
            f.write("                          /       \\\n")
            f.write("                         |   .'.   |\n")
            f.write("                         \\  /  \\  /\n")
            f.write("                          '.'.''.'\n")
            f.write("                            ''.'\n")

    play_scene()
