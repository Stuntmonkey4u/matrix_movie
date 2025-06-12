import time
import sys
import os
from rich.console import Console
from rich.text import Text # Import Text

# Setup sys.path correctly from the outset
# This script is matrix_movie_project/matrix_resurrections_terminal_movie.py
# To use 'from matrix_movie_project.scenes...', the dir *containing* 'matrix_movie_project' must be in sys.path
script_path = os.path.abspath(__file__)
project_root_directory = os.path.dirname(script_path) # This is /app/matrix_movie_project
parent_dir_of_project_root = os.path.dirname(project_root_directory) # This is /app

if parent_dir_of_project_root not in sys.path:
    sys.path.insert(0, parent_dir_of_project_root)

# Main import block for scenes and utilities
try:
    from matrix_movie_project.utils import renderer
    from matrix_movie_project.scenes import scene1_booting
    from matrix_movie_project.scenes import scene2_analyst_ai
    from matrix_movie_project.scenes import scene3_neo_awakening
    from matrix_movie_project.scenes import scene4_mirror_glitch
    from matrix_movie_project.scenes import scene5_trinity_signal
    from matrix_movie_project.scenes import scene6_process_merge
    from matrix_movie_project.scenes import scene7_system_overload # Add Scene 7 import
    from matrix_movie_project.scenes import scene8_reboot
except ModuleNotFoundError as e_orig:
    print(f"Error: A required module was not found. This script expects to be part of the 'matrix_movie_project' structure.")
    print(f"Please run this script from the directory *containing* the 'matrix_movie_project' directory,") # User guidance
    print(f"or ensure 'matrix_movie_project' and its submodules (scenes, utils) are correctly installed or in PYTHONPATH.")
    print(f"Details: {e_orig}")
    sys.exit(1) # Exit if imports fail


console = renderer.get_console() # Global console instance from renderer

def main():
    scenes = [
        ("Booting the New Matrix", scene1_booting.play_scene, 45),
        ("Analyst AI Online", scene2_analyst_ai.play_scene, 60),
        ("Neo’s Awakening Process", scene3_neo_awakening.play_scene, 50),
        ("Mirror Glitch Exception", scene4_mirror_glitch.play_scene, 50),
        ("Trinity’s Signal Detected", scene5_trinity_signal.play_scene, 50),
        ("Process Merge: Neo + Trinity", scene6_process_merge.play_scene, 60),
        ("System Overload & Analyst Panic", scene7_system_overload.play_scene, 60), # Add Scene 7 to the list
        ("Reboot and Hope", scene8_reboot.play_scene, 60)
    ]

    # Initial setup: clear screen, introductory message, and initial code rain.
    renderer.clear_screen()
    console.print("Preparing The Matrix Experience...", style="bold green", justify="center")
    time.sleep(1.5)
    renderer.matrix_code_rain(duration=15, console=console) # Adjusted: Initial rain duration (as per subtask instruction)

    total_scenes = len(scenes)
    # Calculate and display the estimated total runtime.
    # Formula: Sum of all scene durations + initial rain + sum of all inter-scene rains.
    initial_rain_duration = 15 # Duration of the first code rain (matches above)
    inter_scene_rain_duration = 10 # Duration of code rain between scenes (matches below)
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

        scene_function() # Execute the current scene's play_scene() function

        if i < total_scenes - 1: # If it's not the last scene, play a transition
            time.sleep(2) # Pause AFTER scene completion, before clearing for transition
            renderer.clear_screen()
            console.print(f"Transitioning from {scene_name}...", style="bold dim green", justify="center")
            time.sleep(1) # Keep this brief pause before rain
            renderer.matrix_code_rain(duration=inter_scene_rain_duration, console=console) # Use defined inter-scene rain duration
        else:
            # After the last scene (scene8 already ends with a blinking cursor), no transition needed.
            pass # Scene 8 handles the final blinking cursor, and the movie concludes.

    # Final completion messages after all scenes have played.
    renderer.clear_screen()
    console.print("The Matrix Resurrections: Terminal Movie Experience - Complete.", style="bold green", justify="center")
    console.print("Thank you for watching. Reality is what you make it.", style="dim green", justify="center") # Corrected style
    time.sleep(3)
    renderer.clear_screen()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        renderer.clear_screen()
        console.print("System override: User initiated shutdown. Exiting The Matrix.", style="bold yellow", justify="center")
    except Exception as e:
        renderer.clear_screen()
        console.print(f"An unexpected error occurred in The Matrix:", style="bold red", justify="center")
        console.print(Text(str(e), style="red"), justify="center")
        # For developer debugging, uncomment below:
        # import traceback
        # console.print_exception(show_locals=True)
    finally:
        renderer.clear_screen()
        console.print("Connection Terminated.", style="dim white", justify="center")

# Ensure a single newline at the end of the file.
