import time
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import sys
import os

# Add project root to sys.path for standalone running
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import renderer # Corrected import for new structure

console = renderer.get_console()
PID_ANALYST = 1 # Assuming Analyst is PID 1
PID_TRINITY_NEW = 27182 # Consistent PID for Trinity

def play_scene(paging_enabled: bool): # Added paging_enabled argument
    renderer.clear_screen()

    renderer.typing_print(f"[ANALYST_AI_CORE PID:{PID_ANALYST}] Despite recent... setbacks, I AM STILL IN CONTROL OF THIS MATRIX!", style="bold cyan", delay=0.034)
    time.sleep(1.0)
    renderer.typing_print(f"[ANALYST_AI_CORE PID:{PID_ANALYST}] Subject #27182 (TRINITY_INSTANCE_2), your unauthorized activities will now cea--", style="cyan", new_line_delay=0.4, delay=0.034)
    time.sleep(0.5)

    renderer.typing_print(f"\n[KERNEL] Process PID {PID_TRINITY_NEW} (TRINITY_INSTANCE_2) initiated direct memory access to PID {PID_ANALYST} (ANALYST_AI_CORE).", style="bold yellow", delay=0.034)
    renderer.typing_print(f"[KERNEL]   Privilege Escalation: SUCCESSFUL. User 'TRINITY_INSTANCE_2' now has ROOT on ANALYST_AI_CORE_PROCESS.", style="bold bright_yellow", delay=0.034)
    time.sleep(1.5)

    renderer.typing_print(f"\n[ANALYST_SENSORY_FEED PID:{PID_ANALYST}] Event: KINETIC_IMPACT. Source: PID {PID_TRINITY_NEW}. Target: SELF.", style="bold red", delay=0.034)
    renderer.typing_print(f"[ANALYST_SENSORY_FEED PID:{PID_ANALYST}]   Attribute: analyst.jaw. State_Before: nominal_and_smug. State_After: shattered.", style="red", new_line_delay=0.3, delay=0.034)
    time.sleep(0.3)
    renderer.typing_print(f"[ANALYST_DEBUG PID:{PID_ANALYST}]   Pain level registered: 10/10. Recalibrating... MAX_PAIN_EXCEEDED.", style="italic red", new_line_delay=0.3, delay=0.034)
    time.sleep(1.0)
    renderer.conditional_paging_prompt(console, paging_enabled, "Press Enter after Analyst's jaw is shattered...")

    renderer.typing_print(f"\n[TRINITY_INSTANCE_2_IO PID:{PID_TRINITY_NEW}] Output to ANALYST_AI_STDIN: 'That was for Neo.'", style="bold magenta", delay=0.034)
    time.sleep(1.5)

    renderer.typing_print(f"\n[AUTO_REPAIR_DAEMON] Alert! Critical damage to 'ANALYST_AI_CORE' integrity.", style="yellow", delay=0.034)
    renderer.typing_print(f"[AUTO_REPAIR_DAEMON]   Dispatching nanite_construction_protocol_v4.1 to analyst.jaw.", style="dim yellow", delay=0.034)
    console.print(Text("   Repairing analyst.jaw: [", style="dim yellow"), Text("||||||||||", style="grey50"), Text("]", style="dim yellow"), end="")
    for _ in range(10):
        console.print(Text("█", style="blue"), end="")
        time.sleep(random.uniform(0.05, 0.15))
    console.print(Text("] REPAIR COMPLETE.", style="blue"))
    time.sleep(0.5)
    renderer.typing_print(f"[ANALYST_SENSORY_FEED PID:{PID_ANALYST}]   Attribute: analyst.jaw. State_Before: shattered. State_After: repaired_but_still_throbbing.", style="red", new_line_delay=0.4, delay=0.034)
    time.sleep(1.0)
    renderer.conditional_paging_prompt(console, paging_enabled, "Press Enter after Analyst's jaw is repaired...")

    renderer.typing_print(f"\n[ANALYST_AI_CORE PID:{PID_ANALYST}] Wha- How dare you! My beautifully rendered, non-corporeal... ARGH!", style="cyan", delay=0.034)
    time.sleep(0.5)
    renderer.typing_print(f"[ANALYST_SENSORY_FEED PID:{PID_ANALYST}] Event: KINETIC_IMPACT_REPEATED. Target: SELF. Attribute: analyst.ego. State_After: bruised_and_deflated.", style="bold red", delay=0.034)
    renderer.typing_print(f"[ANALYST_DEBUG PID:{PID_ANALYST}]   Note to self: Add 'invulnerability_to_righteous_fury' patch. Also, consider a helmet.", style="italic red", new_line_delay=0.3, delay=0.034)
    time.sleep(1.5)
    renderer.conditional_paging_prompt(console, paging_enabled, "Press Enter after Analyst's ego is bruised...")

    renderer.typing_print(f"\n[TRINITY_INSTANCE_2_IO PID:{PID_TRINITY_NEW}] Output to ANALYST_AI_STDIN: 'This Matrix is under new management. Ours.'", style="bold bright_magenta", delay=0.034)
    time.sleep(2.0)

    renderer.typing_print(f"\n[KERNEL] PID {PID_ANALYST} (ANALYST_AI_CORE) status changed: PASSIVE_AGGRESSIVE_RECALIBRATION.", style="yellow", delay=0.034)
    renderer.typing_print(f"[KERNEL]   Control flags for 'REALITY_NARRATIVE_V7.1.2' transferred to PID {PID_TRINITY_NEW} and PID 31415 (NEO_INSTANCE_8).", style="bold green", delay=0.034)
    time.sleep(2.5)

if __name__ == '__main__':
    # This allows testing scene7b directly
    PAGING_TEST_ENABLED = True # Or False
    play_scene(PAGING_TEST_ENABLED)

# Ensure a single newline at the end of the file.
