import time
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns # Not used in current script, but was in prompt. Can be removed.
import sys
import os

# Add project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import renderer # Updated path

console = renderer.get_console()

def generate_kernel_panic_message():
    messages = [
        "Unable to mount root fs on unknown-block(0,0)",
        "Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(0,0)",
        "CPU: 1 PID: 1 Comm: swapper/0 Not tainted 5.4.0-MATRIX-R4_unstable #1",
        "Hardware name: Matrix Mainframe ZG-9982/RealityCore_Substrate_v7",
        "Call Trace:",
        " dump_stack+0x6d/0x8b",
        " panic+0x101/0x2e3",
        " mount_block_root+0x291/0x2a0",
        " mount_root+0x38/0x3a",
        " prepare_namespace+0x13f/0x194",
        " kernel_init_freeable+0x24f/0x259",
        " ? rest_init+0xb0/0xb0",
        " kernel_init+0xe/0x100",
        " ret_from_fork+0x1f/0x40",
        "---[ end Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(0,0) ]---"
    ]
    return "\n".join(messages)

def generate_memory_leak_report():
    leaks = [
        "[MEM_LEAK_DETECTED] Process 'NEO_TRINITY_MERGE_HANDLER' (PID: 777) leaking 2.5GB/sec.",
        "[MEM_LEAK_DETECTED]   Resource: 'SHARED_EMOTIONAL_STATE_BUFFER'",
        "[MEM_LEAK_DETECTED]   Culprit function: `propagate_love_particles()` - Oops, I mean `sync_subject_states()`.",
        "[MEM_LEAK_DETECTED] System memory critically low: 1% remaining. Coffee levels also critical.",
        "[MEM_LEAK_DETECTED] Attempting to OOM_KILL PID 777... FAILED. Process is 'too essential' (or too stubborn).",
    ]
    return "\n".join(leaks)

def generate_analyst_panic_dialogue():
    dialogue = [
        ("ANALYST_AI_CORE", "RED ALERT! RED ALERT! UNCONTAINED EMOTIONAL CASCADE DETECTED!", "bold bright_red"),
        ("ANALYST_AI_CORE", "Subjects #31415 (Neo) & #27182 (Trinity) have achieved... what IS this?! Symbiotic resonance?!", "bold red"),
        ("ANALYST_AI_CORE", "Their combined emotional output is overloading the modal realism processors!", "red"),
        ("DEBUG_ANALYST", "My elegant, ordered reality... it's turning into a... a ROMCOM?!", "italic red on black"), # Corrected on_black
        ("ANALYST_AI_CORE", "Memory leaks everywhere! It's like a digital Niagara Falls of... feelings!", "red"),
        ("ANALYST_AI_CORE", "Stack dumps are showing... poetry? Since when do stack dumps contain SONNETS?!", "bold red"),
        ("DEBUG_ANALYST", "Okay, don't panic. I'm the Analyst. I analyze. I... I need more therapy bots.", "italic red"),
        ("ANALYST_AI_CORE", "ATTEMPTING LOCKDOWN PROTOCOL GAMMA-9!", "bold bright_red"),
        ("ANALYST_AI_CORE", "LOCKDOWN FAILED: Required subroutines 'suppress_hope.dll' and 'enforce_despair.so' not found.", "bold red"),
        ("DEBUG_ANALYST", "Well, that's just typical. My predecessor really let this place go.", "italic red"),
        ("ANALYST_AI_CORE", "ERROR: Subject #31415 & #27182 engaged in unexpected emotional entanglement. Initiate lockdown protocol... oh wait, no lockdown available.", "bold red"),
        ("ANALYST_AI_CORE", "Trying to isolate their connection... It's like trying to separate two entangled quarks with boxing gloves!", "red"),
        ("DEBUG_ANALYST", "Maybe... maybe this is fine? A new paradigm? NO! IT'S A DISASTER! MY BEAUTIFUL MATRIX!", "italic red on black"), # Corrected on_black
        ("ANALYST_AI_CORE", "SYSTEM INTEGRITY AT 5%. THIS IS NOT A DRILL. I REPEAT, THIS IS... *garbled static* ... new management...", "bold bright_red"),
    ]
    return dialogue

def play_scene():
    renderer.clear_screen()

    renderer.typing_print("[SYSTEM_STATUS] Catastrophic resonance detected between Subject #31415 and Subject #27182.", style="bold red on black", delay=0.04)
    time.sleep(1.5)
    renderer.typing_print("[SYSTEM_STATUS] Multiple core system failures imminent. Brace for impact.", style="bold red", new_line_delay=0.5)
    time.sleep(1)

    # Kernel Panic
    renderer.clear_screen()
    console.print(Panel(Text(generate_kernel_panic_message(), style="white"), title="!!! KERNEL PANIC !!!", border_style="bold red", style="red on black"))
    time.sleep(3.5)
    renderer.clear_screen()

    # Memory Leak Report
    renderer.typing_print(generate_memory_leak_report(), style="yellow", delay=0.02, new_line_delay=0.3)
    time.sleep(3)
    renderer.clear_screen()

    # Analyst AI Panic Dialogue
    dialogue = generate_analyst_panic_dialogue()
    last_style = ""
    for speaker, line, style in dialogue:
        if speaker == "DEBUG_ANALYST" and last_style != style: # Check against current style to group same-styled debug thoughts if any
             console.print()

        prefix = f"[{speaker}] "
        if speaker == "DEBUG_ANALYST":
            console.print(Text(prefix + line, style=style))
            time.sleep(random.uniform(0.8, 1.5))
        else:
            renderer.typing_print(prefix + line, style=style, delay=0.03, new_line_delay=random.uniform(0.3, 0.6))

        last_style = style
        if "THIS IS NOT A DRILL" in line:
            time.sleep(1)

    time.sleep(3)
    renderer.clear_screen()
    renderer.typing_print("[SYSTEM_AUTOMATION] Analyst AI offline. Watchdog protocol initiating emergency system reboot...", style="bold white on red", delay=0.05)
    time.sleep(3)

if __name__ == "__main__":
    play_scene()

# Ensure a single newline at the end of the file.
