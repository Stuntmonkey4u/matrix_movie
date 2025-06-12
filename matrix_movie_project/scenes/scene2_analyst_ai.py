import time
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text # Import Text
from matrix_movie_project.utils import renderer

console = renderer.get_console()

def play_scene():
    renderer.clear_screen()

    renderer.typing_print("[ANALYST_AI_CORE] Main process online. Status: NOMINAL.", style="bold cyan", delay=0.03)
    time.sleep(1)
    # Analyst ASCII art display removed.
    # Optional: Add a clear screen here if the transition feels abrupt,
    # or adjust the sleep time if the art's pause was important.
    # For now, just removing the art and its specific sleep.
    # A small pause might still be good.
    time.sleep(0.5)

    renderer.typing_print("\n[ANALYST_AI_CORE] Initiating self-diagnostic sequence...", style="cyan", new_line_delay=0.5)

    diagnostics = [
        ("Cognitive Matrix Integrity Check", "PASSED", 0.02),
        ("Heuristic Subroutine Calibration", "PASSED", 0.02),
        ("Emotional Spectrum Analyzer Test", "PASSED", 0.02),
        ("Subject Influence Module Online", "OK", 0.01),
        ("Reality Distortion Field Emitters", "ACTIVE - STABLE", 0.01),
        ("Modal Logic Verifier", "CONSISTENT", 0.02),
        ("Sanity Check Protocol v4.1.2", "NOMINAL", 0.01)
    ]

    for test_name, status, type_delay in diagnostics:
        base_string = f"[DIAGNOSTIC] {test_name}: "
        console.print(Text(base_string, style="blue_violet"), end="") # Use console.print directly
        time.sleep(random.uniform(0.1, 0.3))
        renderer.typing_print(status, style="bold bright_green" if "PASS" in status or "OK" in status else "bold yellow", delay=type_delay, new_line_delay=0.15, console=console)
    time.sleep(1)

    renderer.typing_print("\n[ANALYST_AI_CORE] Accessing primary subject profiles...", style="cyan", new_line_delay=0.5, console=console)

    subject_logs = [
        "[SUBJECT_MONITOR] Subject #31415 (Designation: NEO) - Current Status: STABLE_INTEGRATED",
        "[ANALYST_THREAD] Querying emotional state for #31415...",
        "[ANALYST_THREAD]   > Subroutine 'longing_for_unknown': ACTIVE, Value=0.78 (Threshold: 0.6)",
        "[ANALYST_THREAD]   > Subroutine 'residual_savior_complex': DORMANT, Value=0.15",
        "[ANALYST_THREAD]   > Psychological profile: 'Content but vaguely dissatisfied artist'. Optimal.",
        "",
        "[SUBJECT_MONITOR] Subject #27182 (Designation: TRINITY) - Current Status: STABLE_INTEGRATED",
        "[ANALYST_THREAD] Querying emotional state for #27182...",
        "[ANALYST_THREAD]   > Subroutine 'vague_sense_of_empowerment_lost': ACTIVE, Value=0.65",
        "[ANALYST_THREAD]   > Subroutine 'motorcycle_affinity_override': ACTIVE, Value=0.99 (Unexpectedly high!)",
        "[ANALYST_THREAD]   > Psychological profile: 'Badass mom with suppressed yearning'. Acceptable.",
        "",
        "[ANALYST_THREAD] Compiling relational subroutines for #31415 and #27182...",
        "[ANALYST_THREAD]   > Initializing proximity dampeners. Range: 500m.",
        "[ANALYST_THREAD]   > Cross-referencing shared dream sequences... Minimal overlap detected. Good.",
        "[ANALYST_THREAD]   > Subject #31415 exhibits increased romantic subroutine activity when processing 'coffee_shop_interaction_sim_v2.3'. Unexpected.",
        "[ANALYST_DEBUG]   Possible correlation with Subject #27182's 'lingering_glance_response_v1.2'. Investigate later. Or don't. They're just programs.",
        "[ANALYST_THREAD]   Current probability of spontaneous co-awakening: 0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001337% (Negligible)"
    ]

    for log_entry in subject_logs:
        if not log_entry:
            console.print()
            time.sleep(0.3)
            continue

        style = "medium_purple1"
        delay = 0.025
        if "[ANALYST_THREAD]" in log_entry:
            style = "medium_purple2"
        elif "[SUBJECT_MONITOR]" in log_entry:
            style = "light_slate_blue"
        elif "[ANALYST_DEBUG]" in log_entry:
            style = "italic dim_grey"
            delay = 0.04

        if "Unexpected" in log_entry or "Investigate later" in log_entry:
            # Use console.print for the first part to control 'end'
            console.print(Text(log_entry, style=style), end="")
            time.sleep(0.5)
            # Then type " ...Hmm."
            renderer.typing_print(" ...Hmm.", console=console, delay=0.08, style="italic grey", new_line_delay=0.2) # This will add a newline after " ...Hmm."
        elif "Negligible" in log_entry:
            # Ensure the long number is printed correctly
            parts = log_entry.split("(Negligible)")
            # Use console.print for the first part to control 'end'
            console.print(Text(parts[0], style="bold red"), end="")
            # Then type "(Negligible)"
            renderer.typing_print("(Negligible)", console=console, delay=0.05, style="bold red", new_line_delay=0.5) # This will add a newline
        else:
            renderer.typing_print(log_entry, console=console, delay=delay, style=style, new_line_delay=0.2)

        if "Optimal." in log_entry or "Acceptable." in log_entry:
            time.sleep(0.7)

    time.sleep(2)
    renderer.typing_print("\n[ANALYST_AI_CORE] All systems nominal. Subject parameters within acceptable deviations. Coffee break?", style="bold cyan", delay=0.04, console=console)
    time.sleep(3)

if __name__ == '__main__':
    import sys
    import os
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    # This import should now work correctly when script is run directly
    from matrix_movie_project.utils import renderer

    # The specific logic for creating analyst_face.txt for test runs is removed.
    # os.makedirs(os.path.join(project_root, "ascii_art"), exist_ok=True) # This can be kept if other ascii might be used for testing

    play_scene()
