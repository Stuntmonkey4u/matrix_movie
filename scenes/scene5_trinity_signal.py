import time
import random
from rich.console import Console
from rich.text import Text
from rich.table import Table
import sys
import os

# Add project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import renderer # Updated path

console = renderer.get_console()

def generate_mac_address():
    return ":".join([f"{random.randint(0, 255):02x}" for _ in range(6)]).upper()

def generate_ip_address(subnet_prefix="10.77.X.X"):
    if "X.X" in subnet_prefix:
        return subnet_prefix.replace("X.X", f"{random.randint(1, 254)}.{random.randint(1, 254)}")
    elif ".X" in subnet_prefix:
        return subnet_prefix.replace(".X", f".{random.randint(1, 254)}")
    return "192.168." + str(random.randint(1,254)) + "." + str(random.randint(1,254)) # Default if no X

def generate_payload_snippet():
    snippets = [
        "\x00\x01\x03[TRN_ECHO_PKT]",
        "[SYN_RIFT_SIG_FRAG]",
        "QUERY: whereabouts(trinity.instance_legacy)",
        "PAYLOAD_ENCRYPTED_LVL9",
        "USER_DATA: 'RememberMe.dat'",
        "SIGNAL_TYPE: GHOST_ECHO_V2.1",
        "0xDEADBEEFCAFEBABE",
        "TRACE_ROUTE_REQUEST_ZION_01",
        "PACKET_FRAG: ...leather_jacket_sim_params...",
        "MSG: 'Follow the white rabbit. Again.'"
    ]
    return random.choice(snippets)

def play_scene():
    renderer.clear_screen()

    renderer.typing_print("[NETWORK_MONITOR_AI] Monitoring deep matrix subnet 77 (Modal Residual Zone)...", style="bold blue", delay=0.025)
    time.sleep(1.5)
    renderer.typing_print("[NETWORK_MONITOR_AI] Unusual energy signature detected. Initiating packet capture on interface mtx_deep_77...", style="blue", new_line_delay=0.4)
    time.sleep(1)

    console.print(Text("\n--- tcpdump -i mtx_deep_77 -n -c 10 'port 1337 or port 31337' ---", style="dim white"))
    time.sleep(0.5)

    packet_table = Table(title="Live Packet Feed (Subnet 77 - Potential Anomalies)", style="green_yellow", border_style="yellow")
    packet_table.add_column("Timestamp", style="dim cyan", width=12)
    packet_table.add_column("SRC IP", style="magenta", width=18)
    packet_table.add_column("DST IP", style="magenta", width=18)
    packet_table.add_column("Protocol", style="yellow", width=8)
    packet_table.add_column("Length", style="cyan", width=6)
    packet_table.add_column("Info / Payload Snippet", style="green_yellow", no_wrap=False, min_width=40)

    base_time = time.time()
    source_ips = [generate_ip_address("10.77.X.X") for _ in range(3)]
    dest_ip_analyst_server = "10.0.0.1 (ANALYST_CONTROL)"

    # Need a temporary table for live printing, or print the main table and then clear rows.
    # For simplicity here, we'll build the full table then print it.
    # The "live printing" part of the prompt is slightly complex with how Rich Tables update.
    # A simpler approach for "live feel" is to print individual lines then the full table.
    # Let's adjust for a slightly simplified "live" feel: print first few packet *details* as text lines.

    captured_packets_for_table = []

    for i in range(10):
        current_ts = f"{time.time() - base_time:.6f}"
        src_ip = random.choice(source_ips)
        dst_ip = generate_ip_address("10.77.X.X") if random.random() > 0.3 else dest_ip_analyst_server
        protocol = random.choice(["TCP", "UDP", "ICMP_ECHO"])
        length = random.randint(64, 512)
        info = generate_payload_snippet()

        is_significant = "[TRN_ECHO_PKT]" in info or "trinity" in info or "TRACE_ROUTE_REQUEST_ZION" in info

        packet_data = (current_ts, src_ip, dst_ip, protocol, str(length), info, is_significant)
        captured_packets_for_table.append(packet_data)

        if i < 3: # Print first few packets as formatted text for "live" feel
            display_info = f"[!!!] {info} [!!!]" if is_significant else info
            live_pkt_text = Text(f"{current_ts} IP {src_ip} > {dst_ip}: {protocol} {length}bytes: {display_info}", style="green_yellow")
            if is_significant:
                live_pkt_text.stylize("bold bright_magenta on black")
            console.print(live_pkt_text)
            time.sleep(random.uniform(0.5, 1.0))
        elif i == 3:
             renderer.typing_print("Capturing more packets...", style="italic dim white", delay=0.01, new_line_delay=0.1)
             time.sleep(0.3)
        else:
            time.sleep(random.uniform(0.1, 0.3))

    # Populate the table with all captured packets
    for pkt_data in captured_packets_for_table:
        current_ts, src_ip, dst_ip, protocol, length_str, info, is_significant = pkt_data
        row_style = "bold bright_magenta on black" if is_significant else ""
        display_info = f"[!!!] {info} [!!!]" if is_significant else info
        packet_table.add_row(current_ts, src_ip, dst_ip, protocol, length_str, display_info, style=row_style)

    renderer.clear_screen()
    renderer.typing_print("[NETWORK_MONITOR_AI] Packet capture complete. Analyzing results...", style="blue", new_line_delay=0.3)
    time.sleep(0.5)
    console.print(packet_table)
    time.sleep(2.5)

    renderer.typing_print("\n[ANALYST_AI_NET_OPS] Correlating packet origins...", style="bold cyan", new_line_delay=0.4)
    renderer.typing_print(f"[ANALYST_AI_NET_OPS]   Detected multiple pings from MAC addresses resolving to legacy hardware profile: {generate_mac_address()} (TRINITY_HW_SIG_GHOST)", style="cyan")
    time.sleep(1)
    renderer.typing_print("[ANALYST_AI_NET_OPS]   Payload analysis suggests fragmented echo of Subject #27182 (TRINITY).", style="cyan")
    time.sleep(0.5)
    renderer.typing_print("[ANALYST_AI_NET_OPS]   This is... unexpected. And annoying. Route these signals to /dev/null_or_something.", style="italic cyan")
    time.sleep(3.5)

if __name__ == "__main__":
    play_scene()

# Ensure a single newline at the end of the file.
