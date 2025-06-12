import time
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
# Ensure matrix_movie_project is in PYTHONPATH or handle imports carefully
# For direct execution, sys.path manipulation is often needed.
import sys
import os

# Determine project_root and add to sys.path if not already there
# This is for allowing 'from matrix_movie_project.utils import renderer'
# when the script might be run directly.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir) # Assumes scenes is one level down from project root

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import renderer # Updated path

console = renderer.get_console()

def generate_glitch_text(length=50):
    # Correctly include literal backslash and quote
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[];',./<>?:{}\\|\""
    return ''.join(random.choice(chars) for _ in range(length))

def generate_corrupted_memory_dump(lines=5, line_length=70):
    dump = "[MEMORY_DUMP_CORRUPTED - ADDRESS: 0x" + ''.join(random.choice("0123456789ABCDEF") for _ in range(8)) + "]\n"
    for _ in range(lines):
        line = ""
        for _ in range(line_length // 3): # Mix of hex and garbage
            if random.random() > 0.7:
                line += ''.join(random.choice("0123456789ABCDEF") for _ in range(2)) + " "
            else:
                # Ensure generated glitch text here is simple and does not contain problematic characters
                glitch_char_options = ["#ERR!", "??", "xx00", generate_glitch_text(2).replace('\\','')]
                line += random.choice(glitch_char_options) + " "
        dump += line.strip() + "\n"
    dump += "[END_DUMP]\n"
    return dump

def play_scene():
    renderer.clear_screen()

    renderer.typing_print("[SYSTEM_MONITOR] Unusual process activity detected for Subject #31415 (NEO_INSTANCE_7)...", style="bold yellow", delay=0.03)
    time.sleep(1.5)

    renderer.typing_print("[KERNEL] Forking new containment process for NEO_INSTANCE_7: PID_NEO_WATCHER_47332", style="yellow", new_line_delay=0.3)
    time.sleep(0.5)
    renderer.typing_print("[KERNEL]   Parent PID: 1 (ANALYST_AI_CORE)", style="dim yellow")
    time.sleep(0.5)
    renderer.typing_print("[KERNEL]   Memory allocation: 256MB (Restricted)", style="dim yellow")
    time.sleep(1)

    renderer.typing_print("\n[REALITY_ENGINE] Anomaly detected in NEO_INSTANCE_7's perceptual sub-system.", style="bold orange1", new_line_delay=0.4)
    renderer.typing_print("[REALITY_ENGINE] Attempting to apply cognitive recalibration patch: 'd_j__vu_suppressor_v3.1.patch'", style="orange1") # Removed accent
    time.sleep(1)
    console.print("Injecting patch sequence: [", Text("||||||||||||||||||||", style="grey50"), Text("]", style="white"), end="")
    for _ in range(20):
        console.print(Text("█", style="green"), end="")
        time.sleep(random.uniform(0.05, 0.15))
    console.print(Text("] PATCH APPLIED.", style="green")) # Removed leading space
    time.sleep(0.5)
    renderer.typing_print("[REALITY_ENGINE] Patch status: PARTIALLY_SUCCESSFUL. Residual instability detected.", style="bold yellow")
    time.sleep(1.5)

    renderer.typing_print("\n[SYSTEM_ALERT] High CPU usage on NEO_INSTANCE_7 threads. Possible cognitive loop.", style="bold red", new_line_delay=0.4)
    renderer.typing_print("[DEBUG] Dumping stack trace for thread NEO_PERCEPTION_001:", style="red")
    time.sleep(0.5)
    stack_trace = [
        "0x7f4d0c00ae70 in ?? () from /matrix/lib/libperception_filter.so",
        "0x7f4d0c00b123 in filter_sensory_input (input=0xdeadbeef" + generate_glitch_text(8) + ") at sensory_filter.c:1337",
        "0x7f4d0c00b8ef in process_reality_stream (stream_id=7, data=0x" + ''.join(random.choice("0123456789ABCDEF") for _ in range(12)) + ") at reality_processor.c:512",
        "0x7f4d0c00c000 in neo_cognitive_loop () at neo_simulation_core.c:888",
        "   WARNING: Max recursion depth likely exceeded. Possible stack overflow.",
        "   CONTEXT: Subject attempting to 'see beyond the code'.",
        "0x7f4d0c00c1a0 in main_simulation_thread (subject_id=31415) at main.c:42",
        "   ERROR: Segmentation Fault (core dumped) -- SIMULATED_RECOVERY_ATTEMPTED"
    ]
    for trace_line in stack_trace:
        style = "red"
        if "WARNING" in trace_line:
            style = "bold yellow" # Simpler color name
        elif "ERROR" in trace_line or "Segmentation Fault" in trace_line:
            style = "bold bright_red"
        elif "CONTEXT" in trace_line:
            style = "italic magenta"
        renderer.typing_print(trace_line, style=style, delay=0.01, new_line_delay=0.1)
    time.sleep(2)

    renderer.typing_print("\n[MEMORY_MANAGER] Corrupted memory blocks detected in NEO_INSTANCE_7's assigned heap.", style="bold red on black", new_line_delay=0.4)
    time.sleep(0.5)

    for _ in range(3):
        console.print(Text(generate_glitch_text(random.randint(60,80)), style=random.choice(["red", "bright_red", "yellow"])))
        time.sleep(random.uniform(0.1,0.3))

    corrupted_dump = generate_corrupted_memory_dump()
    renderer.typing_print(corrupted_dump, style="red", delay=0.005, new_line_delay=0.05)
    time.sleep(1.5)

    renderer.typing_print("[ANALYST_AI_WATCHDOG] Subject #31415 is exhibiting Class-3 dissociative behavior. Not good for business.", style="bold cyan", new_line_delay=0.3)
    renderer.typing_print("[ANALYST_AI_WATCHDOG]   Recommendation: Increase dosage of 'blue_pill_routine_v5.2'.", style="cyan")
    renderer.typing_print("[ANALYST_AI_WATCHDOG]   If instability persists, schedule for full modal reset.", style="cyan")
    time.sleep(3)

# Main execution block: Keep it extremely simple.
if __name__ == "__main__":
    play_scene()
