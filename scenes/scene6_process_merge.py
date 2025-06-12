import time
import random
from rich.console import Console
from rich.text import Text
from rich.markup import escape
import sys
import os

# Add project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import renderer # Updated path

console = renderer.get_console()

# Define PIDs for Neo and Trinity for consistency in this scene
PID_NEO = 31415
PID_TRINITY = 27182

def generate_syscall_args(syscall_name):
    if syscall_name == "connect":
        return f"({PID_TRINITY}, {{sa_family=AF_INET, sin_port=htons(1337), sin_addr=inet_addr(\"127.0.0.1\")}})"
    elif syscall_name == "sendto":
        return f"({PID_TRINITY}, \"{escape(random.choice(['HELO_N30', 'SYNC_REQ_TR1N', 'ARE_YOU_REAL?']))}\", {random.randint(10,20)}, 0, NULL, 0)"
    elif syscall_name == "recvfrom":
        return f"({PID_NEO}, \"{escape(random.choice(['ACK_TR1N', 'WHO_IS_THIS?', 'I_KNOW_YOU.']))}\", {random.randint(10,20)}, 0, NULL, NULL)"
    elif syscall_name == "shmget": # Shared memory
        key = f"0x{random.choice(['c0ffee', 'decade', '10ve', 'ba5eba11'])}{random.randint(1000,9999)}"
        return f"({key}, {random.choice([1024, 2048, 4096])}, IPC_CREAT|0666)"
    elif syscall_name == "shmat":
        return f"({random.randint(10000, 50000)}, NULL, 0)" # Attach to some shared memory ID
    elif syscall_name == "semop": # Semaphore operation for synchronization
        return f"({random.randint(1,10)}, {{sembuf: {{sem_num:0, sem_op:{random.choice([-1,1])}, sem_flg:0}}}}, 1)"
    elif syscall_name == "futex": # Fast userspace mutex
        return f"(0x{random.randint(0,0xFFFFFFFF):08x}, FUTEX_WAIT_PRIVATE, 1, NULL)"
    else:
        return "..."

def play_scene(paging_enabled: bool): # Added paging_enabled argument
    renderer.clear_screen()

    renderer.typing_print(f"[KERNEL_SCHEDULER] High inter-process communication detected between PID {PID_NEO} (NEO_INSTANCE_7) and PID {PID_TRINITY} (TRINITY_RECOVERY_INSTANCE_1)...", style="bold yellow", delay=0.025)
    time.sleep(1.5)
    renderer.typing_print("[KERNEL_SCHEDULER]   Attaching strace-like monitor to both processes...", style="yellow", new_line_delay=0.4)
    time.sleep(1)

    console.print(Text(f"--- strace -p {PID_NEO} -p {PID_TRINITY} ---", style="dim white"))
    time.sleep(0.5)

    syscalls_neo = ["sendto", "recvfrom", "futex", "shmget", "shmat", "semop"]
    syscalls_trinity = ["recvfrom", "sendto", "futex", "shmat", "semop"] # Trinity might react more

    for i in range(12): # Simulate a sequence of syscalls
        pid = random.choice([PID_NEO, PID_TRINITY])
        syscall_name = ""
        if pid == PID_NEO:
            syscall_name = random.choice(syscalls_neo)
        else:
            syscall_name = random.choice(syscalls_trinity)

        args = generate_syscall_args(syscall_name)
        result = random.choice([str(random.randint(0,1000)), f"0x{random.randint(0,0xFFFFFFFF):08x}", "-1 ENOENT (No such file or directory)", "-1 EAGAIN (Resource temporarily unavailable)"])
        duration = random.uniform(0.0001, 0.0050)

        log_line = f"[{pid:<5}] {syscall_name}{args:<60} = {result:<20} <{duration:.4f}>"

        style = "bright_green" if pid == PID_NEO else "magenta" # Changed green to bright_green
        if "ERROR" in result or "ENOENT" in result or "EAGAIN" in result:
            style = "bold red"
        elif "shmget" in syscall_name or "shmat" in syscall_name:
            style = "bold cyan"
        elif "semop" in syscall_name or "futex" in syscall_name:
            style = "bold yellow"

        console.print(Text(log_line, style=style))
        time.sleep(random.uniform(0.1, 0.35))

        if i == 5:
            renderer.typing_print(f"[{PID_NEO}] --- SIGUSR1 {{si_signo=SIGUSR1, si_code=SI_USER}} ---", style="italic orange1", new_line_delay=0.2)
            renderer.typing_print(f"[{PID_TRINITY}] --- SIGUSR1 {{si_signo=SIGUSR1, si_code=SI_USER}} ---", style="italic orange1", new_line_delay=0.3)
            time.sleep(0.5)
            renderer.conditional_paging_prompt(console, paging_enabled, "Press Enter after SIGUSR1 signals...")

        if "shmget" in syscall_name and "c0ffee" in args:
            time.sleep(0.5)
            renderer.typing_print(f"[KERNEL] PID {pid} accessed shared memory segment 'c0ffee_love_protocol'. Unusual.", style="bold bright_magenta", new_line_delay=0.3)
            renderer.typing_print("[KERNEL]   Loading associated subroutine: /matrix/lib/subroutines/love_actually.exe ...or_is_it.dll", style="bright_magenta", new_line_delay=0.2)
            console.print(Text("love_actually.exe: [", style="magenta"), Text("||||||||||", style="grey50"), Text("]", style="magenta"), end="")
            for _ in range(10):
                console.print(Text("█", style="hot_pink"), end="")
                time.sleep(random.uniform(0.05, 0.2))
            console.print(Text("] LOADED & ACTIVE.", style="bold hot_pink"))
            time.sleep(1)
            renderer.conditional_paging_prompt(console, paging_enabled, "Press Enter after 'love_actually.exe' sequence...")


    time.sleep(1.5) # Pause after strace block finishes
    renderer.conditional_paging_prompt(console, paging_enabled, "Press Enter before Resource Manager warnings...")
    renderer.typing_print(f"\n[RESOURCE_MANAGER] Warning: High contention for shared resource 'RES_HEARTBEAT_SYNC'.", style="bold yellow", new_line_delay=0.3)
    renderer.typing_print(f"[RESOURCE_MANAGER]   PID {PID_NEO} and PID {PID_TRINITY} attempting simultaneous lock.", style="yellow", new_line_delay=0.2)
    renderer.typing_print("[RESOURCE_MANAGER]   This typically ends in a deadlock or... something more interesting.", style="italic yellow", new_line_delay=0.4)
    time.sleep(1)

    renderer.typing_print(f"\n[ANALYST_AI_OBSERVER] Processes {PID_NEO} and {PID_TRINITY} are exhibiting... 'emergent resonant behavior'.", style="bold cyan", new_line_delay=0.3)
    renderer.typing_print("[ANALYST_AI_OBSERVER]   Cross-referencing with historical data on 'The One' and 'The Anomaly_Prime_Female_Counterpart'...", style="cyan", new_line_delay=0.2)
    renderer.typing_print("[ANALYST_AI_OBSERVER]   Oh, not this again. My predecessor was so dramatic about it.", style="italic cyan", new_line_delay=0.2)
    renderer.typing_print("[ANALYST_AI_OBSERVER]   Just let them have their little shared memory segment. What's the worst that could happen?", style="italic cyan")
    time.sleep(4)

if __name__ == "__main__":
    PAGING_TEST_ENABLED = True # Or False
    play_scene(PAGING_TEST_ENABLED)

# Ensure a single newline at the end of the file.
