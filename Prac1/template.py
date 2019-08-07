#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Dylan
Student Number: MLLDYL002
Prac: Practical 1
Date: 7/21/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time

# Define board pins
# Inputs
INPUT_0 = 15
INPUT_1 = 36

# Leds
LED_0 = 7
LED_1 = 11
LED_2 = 13

# Global count variable
count = 0

# Function to apply LED states using bitmask
def writeLEDS(state):
    GPIO.output(LED_0, count & 0x1)
    GPIO.output(LED_1, count & 0x2)
    GPIO.output(LED_2, count & 0x4)

# Routine to handle decrementing count variable
# Update LED states using writeLEDS
def decrement(pin):
    # Access global variable
    global count
    # Reset counter at extent
    if(count <=0):
        count = 0x7
    else:
        count = count - 1
    # Update LED states
    writeLEDS(count)

# Routine to handle incrementing count variable
# Update LED states using writeLEDS
def increment(pin):
    # Access global variable
    global count
    if(count >=0x7):
        count = 0
    else:
        count = count + 1
        
    # Update LED states
    writeLEDS(count)
    
# Logic that you write
def main():
    # Define pin layout
    GPIO.setmode(GPIO.BOARD)
    
    # Setup outputs
    # Set GPIO to type OUTPUT
    GPIO.setup(LED_0, GPIO.OUT)
    GPIO.setup(LED_1, GPIO.OUT)
    GPIO.setup(LED_2, GPIO.OUT)
    
    # Setup Inputs
    # Set GPIO to type INPUT
    # Enable pull-up resistors for both inputs
    GPIO.setup(INPUT_0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(INPUT_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    # Add interrupt handlers for both inputs
    # Set debounce time
    GPIO.add_event_detect(INPUT_0, GPIO.FALLING, callback=decrement, bouncetime=300 )
    GPIO.add_event_detect(INPUT_1, GPIO.FALLING, callback=increment, bouncetime=300 )
    
    # Initialize LED to rest state (0x0)
    writeLEDS(count)
    
    # Infinite loop, wait for events
    while True:
        time.sleep(5)


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
