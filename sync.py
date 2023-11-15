import time

# Define a simple synchronous function
def print_message(message, delay):
    # Simulate some synchronous operation, like CPU-bound task
    time.sleep(delay)
    print(message)

# Define the main synchronous function
def main():
    # Run multiple synchronous functions sequentially
    print_message("Hello", 2)
    print_message("Sync", 1)
    print_message("World", 3)

# Run the main synchronous function
if __name__ == "__main__":
    # Record the start time for measuring execution time
    start_time = time.time()
    
    # Run the main synchronous function
    main()
    
    # Calculate and print the total execution time
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")
