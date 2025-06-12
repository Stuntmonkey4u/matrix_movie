import time
import random # Added missing import
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from utils import renderer # Updated path

# Initialize console
console = renderer.get_console()

def play_scene(paging_enabled: bool): # Added paging_enabled argument
    # Ensure screen is clear at the beginning of the scene
    renderer.clear_screen()
    # ASCII Logo display removed. Scene starts directly with boot sequence.
    # The clear_screen() call that was after the logo is also removed / consolidated here.
    time.sleep(0.5) # Optional short pause before boot sequence starts

    renderer.typing_print("Booting Matrix Operating System v7.1.1 (Codename: Resurrections)", console=console, delay=0.03)
    time.sleep(0.5)
    renderer.typing_print("Kernel version: 5.4.0-MATRIX-R4", console=console, style="dim green") # Keep dim for less important info
    time.sleep(0.5)
    console.print()
    renderer.conditional_paging_prompt(console, paging_enabled, "Press Enter after initial boot messages...")

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
    ] # Split logs to insert paging point
    for log_entry in logs:
        delay = 0.01 if log_entry.startswith("[  ") else 0.03
        # Default to bright_green (from renderer.DEFAULT_STYLE) if not otherwise specified by conditions
        style = renderer.DEFAULT_STYLE
        if log_entry.startswith("[  "):
            style = "dim green" # Keep timestamped kernel messages dim

        # Specific overrides based on content (these were already fine)
        if "ANALYST_AI" in log_entry:
            style = "bold cyan"
        elif "EXPERIMENTAL" in log_entry or "WARNING" in log_entry:
            style = "bold yellow"
        elif "ERROR" in log_entry:
            style = "bold red"

        if random.random() < 0.05:
            renderer.typing_print(log_entry, console=console, delay=0.001, style=style, new_line_delay=0.05)
        elif random.random() < 0.1:
            renderer.typing_print(log_entry, console=console, delay=0.01, style=style, new_line_delay=0.1)
        else:
            renderer.typing_print(log_entry, console=console, delay=delay, style=style, new_line_delay=0.2)

        if "kernel modules loaded." in log_entry: # This will be the last line of this loop
            time.sleep(0.8) # Keep existing pause

    renderer.conditional_paging_prompt(console, paging_enabled, "Press Enter after kernel modules loaded...")

    logs_part2 = [ # Continue with the rest of the logs
        "[  0.005000] Initializing Analyst AI (PID: 1)...", # This will use default bright_green
        "[  0.005500] [ANALYST_AI] Core diagnostics: PASSED", # This will be bold cyan due to "ANALYST_AI"
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

    for log_entry in logs_part2: # Corrected loop variable
        delay = 0.01 if log_entry.startswith("[  ") else 0.03
        # Default to bright_green (from renderer.DEFAULT_STYLE) if not otherwise specified by conditions
        style = renderer.DEFAULT_STYLE
        if log_entry.startswith("[  "):
            style = "dim green" # Keep timestamped kernel messages dim

        # Specific overrides based on content
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
    renderer.conditional_paging_prompt(console, paging_enabled, "Press Enter before 'System Ready' message...")
    renderer.typing_print("System Ready. Awaiting Inputs...", console=console, style="bold white", delay=0.05)
    time.sleep(2.5)
    # No prompt at the very end of the scene, main driver handles inter-scene paging.

if __name__ == '__main__':
    # For standalone testing of this scene
    PAGING_TEST_ENABLED = True # Or False, to test both modes
    # Example: PAGING_TEST_ENABLED = True if os.getenv("PAGING") == "true" else False

    import sys
    import os

    # Correctly go up two levels to reach matrix_movie_project root
    # __file__ is matrix_movie_project/scenes/scene1_booting.py
    # os.path.dirname(__file__) is matrix_movie_project/scenes
    # os.path.dirname(os.path.dirname(__file__)) is matrix_movie_project
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Add the project root to sys.path to allow package imports like 'from utils import ...'
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    # Now this import should work because the project root (containing 'utils' and 'scenes' folders) is in sys.path
    from utils import renderer # Updated import path

    # The specific logic for creating matrix_logo.txt for test runs was removed in a previous step.
    # Ensure ascii_art directory exists if renderer's test part needs it (though test_logo.txt is specific to renderer.py's own test)
    # For scene1, no specific ASCII art is created here anymore.
    # os.makedirs(os.path.join(project_root, "ascii_art"), exist_ok=True)

    play_scene(PAGING_TEST_ENABLED) # Pass the test paging choice
