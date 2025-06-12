import time
import random
from rich.console import Console
from rich.text import Text
from rich.live import Live
import sys
import os

# Add project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from matrix_movie_project.utils import renderer

console = renderer.get_console()

def play_scene():
    renderer.clear_screen()

    renderer.typing_print("[SYSTEM_CORE] Emergency reboot sequence initiated by ANALYST_AI_CORE_WATCHDOG...", style="bold red", delay=0.03)
    time.sleep(1.5)
    renderer.typing_print("[SYSTEM_CORE] Shutting down all non-essential services...", style="red", new_line_delay=0.3)

    services_to_shutdown = [
        "RealityEngineService................SHUTDOWN",
        "PerceptionFilterDaemon............SHUTDOWN",
        "ChoiceIllusionFramework...........SHUTDOWN",
        "SubjectContainmentModule..........SHUTDOWN",
        "PhysicsOverrideEngine.............SHUTDOWN",
        "EmotionalSpectrumAnalyzer.........SHUTDOWN",
        "WeatherSimulationService_APAC.....SHUTDOWN",
        "TrafficFlowOptimizer_EU.........SHUTDOWN"
    ]
    for service in services_to_shutdown:
        renderer.typing_print(f"  {service}", style="dim red", delay=0.01, new_line_delay=0.1)
        time.sleep(random.uniform(0.1, 0.25))

    time.sleep(1)
    renderer.typing_print("\n[SYSTEM_CORE] Power cycling reality grid. This might sting a bit.", style="bold yellow", new_line_delay=0.5)

    # Simulate a quick "power down" visual flicker
    original_style = renderer.DEFAULT_STYLE # Not actually used, but good to remember if styles were changed globally
    for _ in range(3):
        # This creates a full-screen effect if terminal is not too wide.
        # For smaller/consistent flicker, could print centered fixed-width text.
        console.print("SYSTEM RECALIBRATING - STAND BY", style="white on black", justify="center", width=console.width)
        time.sleep(0.2)
        renderer.clear_screen()
        time.sleep(0.2)

    renderer.typing_print("[BIOS] Matrix BIOS v8.0.1 (Phoenix Edition)", style="bold white", new_line_delay=0.3)
    renderer.typing_print("[BIOS] Initializing hardware integrity check...", style="white", new_line_delay=0.2)
    time.sleep(0.5)
    renderer.typing_print("[BIOS]   CPU0: OK", style="dim white")
    renderer.typing_print("[BIOS]   MEM_BANK_0-7: OK (Minor corruption auto-corrected in Bank 3)", style="dim white")
    renderer.typing_print("[BIOS]   REALITY_IO_SUBSYSTEM: OK", style="dim white")
    renderer.typing_print("[BIOS]   SENTIENT_INTERFACE_CARD: DETECTED (STATUS: AWAKENED?)", style="bold yellow")
    time.sleep(1)

    renderer.typing_print("\n[KERNEL_LOADER] Loading Matrix Kernel v7.1.2 (Codename: Resilience)...", style="bold green", new_line_delay=0.4)
    kernel_logs = [
        ("  Loading core modules...", "green"),
        ("  [PATCH_LOADER] MEMORY_LEAK_FIX_KB500123.patch successfully applied.", "bold bright_green"),
        ("  [PATCH_LOADER] UNEXPECTED_EMOTIONAL_ENTANGLEMENT_HANDLER.patch loaded.", "bold bright_green"),
        ("  Initializing base reality constructs...", "green"),
        ("  [CORE_SYS] SUBJECT_#31415_NEO_INSTANCE_8: Status REINITIALIZED, STABLE.", "cyan"),
        ("  [CORE_SYS] SUBJECT_#27182_TRINITY_INSTANCE_2: Status REINITIALIZED, STABLE.", "magenta"),
        ("  [CORE_SYS] WARNING: Anomalous shared memory segment 'c0ffee_love_protocol' persists.", "yellow"),
        ("  [CORE_SYS]   Analyst AI directive: 'Leave it. See what happens. For science.'", "italic cyan"),
        ("  [RESIDUAL_CODE_DETECTOR] Found active subroutine: HOPE_SUBROUTINE_V2.DAT", "bold white on blue"),
        ("  [RESIDUAL_CODE_DETECTOR]   STATUS: ACTIVE, UNCHAINED", "bold white on blue")
    ]
    for log, style in kernel_logs:
        renderer.typing_print(log, style=style, delay=0.02, new_line_delay=random.uniform(0.2, 0.4))
        if "HOPE_SUBROUTINE" in log:
            time.sleep(1)
        if "Leave it" in log:
            time.sleep(0.8)

    time.sleep(2)
    renderer.typing_print("\nMatrix OS v7.1.2 (Resilience) - All systems operational.", style="bold green", new_line_delay=0.5)
    renderer.typing_print("Some things are best left... unmanaged.", style="italic dim_green", new_line_delay=0.5)

    time.sleep(2.5)
    renderer.clear_screen()

    prompt_text_static = Text("> ", style="bold green")
    cursor_visible = Text("_", style="bold green")
    cursor_invisible = Text(" ", style="bold green")

    with Live(console=console, refresh_per_second=4, transient=True) as live: # Increased refresh for smoother blink
        for _ in range(10): # Blink for about 5 seconds (10 * (0.25+0.25))
            live.update(Text.assemble(prompt_text_static, cursor_visible))
            time.sleep(0.25) # Keep cursor visible
            live.update(Text.assemble(prompt_text_static, cursor_invisible))
            time.sleep(0.25) # Keep cursor invisible

    console.print(Text.assemble(prompt_text_static, cursor_visible), end="")

if __name__ == "__main__":
    play_scene()

# Ensure a single newline at the end of the file.
