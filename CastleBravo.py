


import sys  # Importing the sys module to access system-specific parameters and functions
import time  # Importing the time module to add delays (simulate loading time)

# ANSI escape sequences for colors
RESET = "\033[0m"  # Reset to default color
GREEN = "\033[32m"  # Green text
YELLOW = "\033[33m"  # Yellow text
RED = "\033[31m"  # Red text for warnings/errors

# Print the welcome message at the start with color
print(GREEN + "\nWelcome to InfoTechCenter V1.0\n" + RESET)

x = 0  # Initial counter for the number of iterations
ellipsis = 0  # Counter for the number of dots in the ellipsis animation

# Loop to simulate the booting process (runs 20 times)
while x != 20:
    x += 1  # Increment the counter for each iteration
    # Create the message that includes the animated ellipsis (increases the number of dots each time)
    message = (YELLOW + "InfoTech Center System Booting" + "." * ellipsis + RESET)

    # Increment the ellipsis counter for the next dot
    ellipsis += 1

    # Use sys.stdout.write to overwrite the current line with the new message
    sys.stdout.write("\r" + message)

    # Add a delay to slow down the loop, so the animation looks smooth
    time.sleep(0.5)

    # Reset the ellipsis counter after 3 dots, so it loops back to 0
    if ellipsis == 4:
        ellipsis = 0

# Once 20 iterations have passed, print the final message in green
if x == 20:
    print("\n\n" + GREEN + "Operating System Booted Up - Retina Scanned - Access Granted" + RESET)