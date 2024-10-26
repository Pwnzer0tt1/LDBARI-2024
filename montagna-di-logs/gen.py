import random
import string

flag = "LDBARI2024{sup3r_l0ng_fl4g_f0r_4_sup3r_s1mple_ch4ll3nge_i_h0pe_y0u_ar3_scr1pt1ng_this_g00d_j0b}"
num_parts = 100
num_fake_parts = 0  # Number of fake parts with incorrect lengths or indices
total_entries = 20000  # Total log entries, including both real and fake parts

# Sample phrases and devices to make logs realistic
phrases = [
    "Starting up service", "Shutting down service", "Restarting service", 
    "Service failure detected in", "Connection established with", "Connection lost with",
    "User logged in from", "User logged out", "Device enabled", "Device disabled",
    "Disabling device", "Enabling device", "Service error on port", "Updating configuration for",
    "Loading module", "Unloading module", "Critical error in module", "System update started",
    "System update completed", "Backup started", "Backup completed", "Disk space low on",
    "Memory usage high on", "CPU usage high on", "Reboot initiated by user", "Reboot completed"
]
devices = ["usb:0", "eth0", "disk1", "cpu", "memory", "gpu0"]
services = ["httpd", "nginx", "mysql", "redis", "ssh", "firewall", "systemd", "docker"]
ports = [str(p) for p in range(80, 90)] + [str(p) for p in range(8080, 8090)]
locations = ["127.0.0.1", "192.168.1.1", "10.0.0.5", "user@example.com", "localhost"]

def generate_random_log_entry():
    """Generates a random log entry in a realistic format."""
    timestamp = f"{random.randint(2023, 2025)}-{random.randint(1, 12):02}-{random.randint(1, 28):02} "
    timestamp += f"{random.randint(0, 23):02}:{random.randint(0, 59):02}:{random.randint(0, 59):02}"
    level = random.choice(["INFO", "WARN", "ERROR"])
    message = f"{random.choice(phrases)} {random.choice(services + devices + ports + locations)}"
    return f"{timestamp} {level} {message}\n"

def split_flag_into_parts(flag, num_parts):
    """Splits the flag into parts with specified lengths."""
    part_length = len(flag) // num_parts
    remainder = len(flag) % num_parts
    parts = []
    
    # Split flag into almost-equal parts
    index = 0
    for i in range(num_parts):
        length = part_length + (1 if i < remainder else 0)
        part = flag[index:index + length]
        parts.append((i, part))
        index += length
    
    return parts

def generate_flag_parts(flag_parts):
    """Formats the flag parts according to the PARTn{content} format."""
    formatted_parts = [f"PART{i}{{{content}}}" for i, content in flag_parts]
    return formatted_parts

def generate_fake_parts(num_fake_parts, max_length=10):
    """Generates fake parts with random indices and lengths."""
    fake_parts = []
    for _ in range(num_fake_parts):
        index = random.randint(0, num_parts - 1)
        length = random.randint(1, max_length)
        content = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        fake_parts.append(f"PART{index}{{{content}}}")
    return fake_parts

def generate_log_file_with_flag_parts(num_entries, flag_parts, fake_parts):
    """Generates a log file with random entries and scattered real and fake flag parts."""
    log_entries = [generate_random_log_entry() for _ in range(num_entries)]
    
    # Combine real and fake parts
    all_parts = flag_parts + fake_parts
    random.shuffle(all_parts)
    
    # Insert parts into random log entries
    for part in all_parts:
        index = random.randint(0, num_entries - 1)
        log_entries[index] = log_entries[index].strip() + f" {part}\n"
    
    return ''.join(log_entries)

# Split flag into parts and create formatted real parts
flag_parts = split_flag_into_parts(flag, num_parts)
formatted_flag_parts = generate_flag_parts(flag_parts)

# Generate some fake parts with incorrect lengths or random data
fake_parts = generate_fake_parts(num_fake_parts)

# Generate the complete log file content
log_file_content = generate_log_file_with_flag_parts(total_entries, formatted_flag_parts, fake_parts)

# Optionally write to a file
with open("generated_log_with_parts.txt", "w") as log_file:
    log_file.write(log_file_content)

print("Log file with flag parts and fake parts generated as 'generated_log_with_parts.txt'")

