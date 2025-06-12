import sys
import os
import time # time needs to be imported before it's used in main()

# Dependency Check for 'rich'
try:
    import rich
except ImportError:
    # Using sys.stderr.write for error messages before rich might be available
    sys.stderr.write("Error: The 'rich' library is not installed. This project requires 'rich' for terminal graphics.\n")
    sys.stderr.write("Please install it by running: pip install rich\n")
    sys.stderr.write("Alternatively, install all project dependencies with: pip install -r requirements.txt\n")
    sys.exit(1)

# Rich library imports (must be after the dependency check)
from rich.console import Console
from rich.text import Text

# Setup sys.path correctly for project module imports
# Ensure the script's own directory (which is the project root) is in sys.path.
# This allows imports like 'from utils import ...' and 'from scenes import ...' when the script is run directly.
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

# Main import block for project's scenes and utilities
try:
    from utils import renderer # Updated path
    from scenes import scene1_booting # Updated path
    from scenes import scene2_analyst_ai # Updated path
    from scenes import scene3_neo_awakening # Updated path
    from scenes import scene4_mirror_glitch # Updated path
    from scenes import scene5_trinity_signal # Updated path
    from scenes import scene6_process_merge # Updated path
    from scenes import scene7_system_overload # Updated path
    from scenes import scene7b_trinity_vs_analyst # Added import for Scene 7b
    from scenes import scene8_reboot # Updated path
except ModuleNotFoundError as e_orig:
    # This error handling is for project-specific modules (scenes, utils)
    # The sys.path logic above should make 'scenes' and 'utils' directly importable
    # if the script is run from the project root (where this script itself is located).
    sys.stderr.write("\n--- ERROR: Project Module Not Found ---\n")
    sys.stderr.write(f"A required project file (e.g., a scene or utility script) could not be found.\n")
    sys.stderr.write(f"This often means the script is not being run from the correct directory, or the project's file structure has been altered.\n\n")
    sys.stderr.write(f"Details: {e_orig}\n\n")
    sys.stderr.write(f"For this script ('{os.path.basename(script_path)}') to work, it expects:\n")
    sys.stderr.write(f"1. To be located within a 'matrix_movie_project' directory (currently at: '{project_root_directory}').\n")
    sys.stderr.write(f"2. The directory *containing* 'matrix_movie_project' (which is: '{parent_dir_of_project_root}') to be in Python's search path.\n")
    sys.stderr.write(f"   (The script attempts to add this automatically.)\n\n")
    sys.stderr.write(f"Current Python search paths (sys.path):\n")
    for p in sys.path:
        sys.stderr.write(f"  - {p}\n")
    sys.stderr.write("\nPlease verify your setup and try running again from the directory that contains 'matrix_movie_project'.\n")
    sys.stderr.write("--- End of Error Report ---\n")
    sys.exit(1) # Exit if project imports fail


console = renderer.get_console() # Global console instance from renderer
PAGING_ENABLED = False # Default to False. User will be prompted.

def main():
    global PAGING_ENABLED # Declare intent to modify the global variable

    # Define all scenes to be played in order, along with their estimated durations (for display only)
    # Each tuple: (Display Name, function_to_call, estimated_duration_seconds)
    scenes = [
        ("Booting the New Matrix", scene1_booting.play_scene, 45),
        ("Analyst AI Online", scene2_analyst_ai.play_scene, 60),
        ("Neo’s Awakening Process", scene3_neo_awakening.play_scene, 50),
        ("Mirror Glitch Exception", scene4_mirror_glitch.play_scene, 50),
        ("Trinity’s Signal Detected", scene5_trinity_signal.play_scene, 50),
        ("Process Merge: Neo + Trinity", scene6_process_merge.play_scene, 60),
        ("System Overload & Analyst Panic", scene7_system_overload.play_scene, 60),
        ("Trinity vs. Analyst", scene7b_trinity_vs_analyst.play_scene, 60), # Added Scene 7b
        ("Reboot and Hope", scene8_reboot.play_scene, 60)
    ]

    # Initial setup: clear screen, introductory message, and initial code rain.
    renderer.clear_screen()
    console.print("Preparing The Matrix Experience...", style="bold bright_green", justify="center") # Updated style
    time.sleep(1.5)
    # Initial code rain is played *after* the paging prompt for a cleaner start.
    # renderer.matrix_code_rain(duration=2, console=console)

    # --- Paging Option Prompt ---
    renderer.clear_screen() # Clear screen before the prompt
    console.print("[bold cyan]Paging Option:[/bold cyan]", justify="center")
    # Using console.input which is part of Rich Console
    choice = console.input("[bold cyan]Enable manual paging (Press Enter after key moments)? (y/N): [/bold cyan]").strip().lower()
    if choice == 'y':
        PAGING_ENABLED = True
        console.print("Manual paging [bold bright_green]enabled[/bold bright_green]. Press Enter at prompts to continue.", justify="center") # Updated style
    else:
        PAGING_ENABLED = False # Explicitly set, though it's the default
        console.print("Manual paging [bold red]disabled[/bold red]. Movie will play automatically.", justify="center")

    console.print("\nPreparing to start the movie...", justify="center")
    time.sleep(2.5) # Pause for user to read the confirmation

    # Now, the initial code rain
    renderer.clear_screen() # Clear the paging prompt before rain
    renderer.matrix_code_rain(duration=2, console=console) # Initial rain duration

    total_scenes = len(scenes)
    # Calculate and display the estimated total runtime.
    # Formula: Sum of all scene durations + initial rain + sum of all inter-scene rains.
    initial_rain_duration = 15
    inter_scene_rain_duration = 10
    num_transitions = total_scenes - 1 if total_scenes > 0 else 0
    estimated_total_time = sum(s[2] for s in scenes) + initial_rain_duration + (num_transitions * inter_scene_rain_duration)

    console.print(f"Estimated Total Runtime: ~{estimated_total_time // 60} minutes {estimated_total_time % 60} seconds (excluding scene pauses).", style="dim white", justify="center")
    time.sleep(2) # Pause to let user read the estimate.

    # Iterate through scenes, playing each one with transitions.
    for i, (scene_name, scene_function, scene_duration) in enumerate(scenes):
        renderer.clear_screen()
        console.print(f"Loading Scene {i+1}/{total_scenes}: {scene_name}...", style="bold dim green", justify="center")
        console.print(f"(Approx. duration: {scene_duration}s)", style="dim green", justify="center")
        time.sleep(2) # Pause AFTER "Loading Scene" message, before scene starts

        scene_function(PAGING_ENABLED) # Pass PAGING_ENABLED to the scene function

        # Inter-scene transition logic (no more inter-scene paging here)
        if i < total_scenes - 1: # If it's not the last scene
            time.sleep(0.5) # Small breather after scene finishes, before transition

            renderer.clear_screen()
            console.print(f"Transitioning from {scene_name}...", style="bold dim green", justify="center")
            time.sleep(1) # Keep this brief pause before rain
            renderer.matrix_code_rain(duration=2, console=console) # Inter-scene rain
        else:
            # This is after the last scene (Scene 8).
            # Scene 8 handles its own ending (blinking cursor), so no "Press Enter" here.
            # And no transition rain.
            pass # Scene 8 handles the final blinking cursor, and the movie concludes.

    # Final completion messages after all scenes have played.
    renderer.clear_screen()
    console.print("The Matrix Resurrections: Terminal Movie Experience - Complete.", style="bold bright_green", justify="center") # Updated style
    console.print("Thank you for watching. Reality is what you make it.", style="dim green", justify="center")
    time.sleep(3)
    # renderer.clear_screen() # Don't clear immediately, credits will do it.

    # --- Credits Screen ---
    # This is inside the main try block, before except/finally.
    # renderer and console are guaranteed to be defined if we reached this point
    # because their import and initialization are at the top of the script or checked early.
    renderer.clear_screen()
    console.print("\n\n[bold cyan]Created by Stuntmonkey4u[/bold cyan]", justify="center")
    console.print("[cyan]Https://Github.com/Stuntmonkey4u/matrix_movie[/cyan]", justify="center")
    console.print("\n\n[bold yellow]- - - Press Enter to exit - - -[/bold yellow]", justify="center")
    input() # Mandatory pause, regardless of PAGING_ENABLED

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # Use basic print for KeyboardInterrupt if console object might not be initialized
        # (though in this structure, it should be if rich is present)
        if 'renderer' in globals() and renderer and 'console' in globals() and console:
            renderer.clear_screen()
            console.print("System override: User initiated shutdown. Exiting The Matrix.", style="bold yellow", justify="center")
        else:
            sys.stdout.write("\nSystem override: User initiated shutdown. Exiting The Matrix.\n")
    except Exception as e:
        if 'renderer' in globals() and renderer and 'console' in globals() and console:
            renderer.clear_screen()
            console.print(f"An unexpected error occurred in The Matrix:", style="bold red", justify="center")
            console.print(Text(str(e), style="red"), justify="center")
        else:
            sys.stderr.write(f"\nAn unexpected error occurred in The Matrix: {e}\n")
        # For developer debugging, uncomment below:
        # import traceback
        # traceback.print_exc() # Prints to stderr
    finally:
        if 'renderer' in globals() and renderer: # Ensure renderer was imported
            renderer.clear_screen()
        sys.stdout.write("Connection Terminated.\n") # Basic print to ensure it appears

# Ensure a single newline at the end of the file.
