import time
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import sys
import os

# Add project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import renderer # Updated path

console = renderer.get_console()

def generate_error_code():
    return "0x" + ''.join(random.choice("0123456789ABCDEF") for _ in range(8)) + \
           "-" + ''.join(random.choice("0123456789ABCDEF") for _ in range(4)) + \
           "-" + ''.join(random.choice("0123456789ABCDEF") for _ in range(4))

def play_scene():
    renderer.clear_screen()

    renderer.typing_print("[SIMULATION_CORE] Monitoring Subject #31415 (NEO_INSTANCE_7)... Normal parameters.", style="green", delay=0.02)
    time.sleep(1)
    renderer.typing_print("[SIMULATION_CORE] Subject #31415 interacting with reflective surface object: MIRROR_#4B2D", style="green", new_line_delay=0.3)
    time.sleep(1.5)

    renderer.typing_print("\n[PHYSICS_ENGINE_ALERT] CRITICAL_ERROR: REFLECTION_SUBSYSTEM_FAILURE", style="bold bright_red", delay=0.04, new_line_delay=0.5)
    renderer.typing_print(f"[PHYSICS_ENGINE] Error Code: {generate_error_code()}", style="red", new_line_delay=0.2)
    renderer.typing_print("[PHYSICS_ENGINE]   Location: MIRROR_#4B2D_INSTANCE_001, Subject: #31415", style="red", new_line_delay=0.2)
    renderer.typing_print("[PHYSICS_ENGINE]   Description: Surface tension integrity compromised. Phase variance exceeds threshold.", style="red", new_line_delay=0.4)
    time.sleep(1)

    console.print(Panel(
        Text("KERNEL PANIC - REFLECTION_PARADOX_DETECTED\n"
             "Attempting to dump core state for module: 'reflective_surfaces.ko'\n"
             "Please standby... this might take a moment. Or forever.\n"
             "SYSTEM_ERROR_ID: MRPDX_7781_FATAL", justify="center"),
        title="!!! SYSTEM FAILURE !!!",
        border_style="bold red",
        style="white on red" # Inverted colors for panic
    ))
    time.sleep(2.5)

    renderer.typing_print("\n[CRASH_HANDLER] Initiating emergency patch deployment: 'reality_stabilizer_mk4.patch'", style="bold yellow", new_line_delay=0.3)
    renderer.typing_print("[CRASH_HANDLER]   Target: All reflective surface simulation threads for Subject #31415.", style="yellow", new_line_delay=0.2)
    time.sleep(0.5)

    patch_logs = [
        ("  [PATCH_LOG] Halting physics thread 0x7FB... ACK.", "dim yellow"),
        ("  [PATCH_LOG] Injecting quantum foam recalibrator at memory address 0xFFA800...", "dim yellow"),
        ("  [PATCH_LOG] Verifying entanglement inhibitors...", "dim yellow"),
        ("  [PATCH_LOG] ERROR: Inhibitor #3 failed to engage. Forcing override. This might get weird.", "bold orange_red1"),
        ("  [PATCH_LOG] Recalibrating surface normal vectors...", "dim yellow"),
        ("  [PATCH_LOG] Patch integrity check: SHA256_SUM_MISMATCH. Expected: ...4A3F, Got: ...BEEF. Not ideal.", "bold yellow"),
        ("  [PATCH_LOG] Analyst AI override: 'ProceedWithCautionFlag=TRUE'. YOLO.", "italic cyan"),
        ("  [PATCH_LOG] Restarting physics thread 0x7FB... ACK?", "dim yellow")
    ]

    for log, style_str in patch_logs:
        renderer.typing_print(log, style=style_str, delay=0.015, new_line_delay=random.uniform(0.1, 0.4))
        if "ERROR" in log or "MISMATCH" in log:
            time.sleep(0.8)
    time.sleep(1.5)

    renderer.typing_print("\n[SYSTEM_STATUS] Reflection subsystem partially restored. Surface integrity: NOMINAL_BUT_WOBBLY.", style="bold green", new_line_delay=0.3)
    renderer.typing_print("[DEBUG_NOTE]   'Any sufficiently advanced technology is indistinguishable from a rigged carnival mirror.' - Some AI, probably.", style="italic grey", new_line_delay=0.2)
    renderer.typing_print("[ANALYST_AI_MEMO]   Flagged Subject #31415 for 'reality_bending_tendencies'. Keep an eye on this one. And maybe build fewer mirrors.", style="cyan")
    time.sleep(3.5)

if __name__ == "__main__":
    play_scene()

# Ensure a single newline at the end of the file.
