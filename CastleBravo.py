import sys  # Importing the sys module to access system-specific parameters and functions
import time  # Importing the time module to add delays (simulate loading time)

# Print the welcome message at the start
print("\nWelcome to InfoTechCenter V1.0\n")

x = 0  # Initial counter for the number of iterations
ellipsis = 0  # Counter for the number of dots in the ellipsis animation

# Loop to simulate the booting process (runs 20 times)
while x != 20:
    x += 1  # Increment the counter for each iteration
    # Create the message that includes the animated ellipsis (increases the number of dots each time)
    message = ("InfoTech Center System Booting" + "." * ellipsis)

    # Increment the ellipsis counter for the next dot
    ellipsis += 1

    # Use sys.stdout.write to overwrite the current line with the new message
    sys.stdout.write("\r" + message)

    # Add a delay to slow down the loop, so the animation looks smooth
    time.sleep(0.5)

    # Reset the ellipsis counter after 3 dots, so it loops back to 0
    if ellipsis == 4:
        ellipsis = 0

    # Once 20 iterations have passed, print the final message
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted")
