import asyncio
import time

# Define a simple asynchronous function
async def print_message(message, delay):
    # Simulate some asynchronous operation, like I/O or network request
    await asyncio.sleep(delay)
    print(message)

# Define the main asynchronous function
async def main():
    # Use asyncio.gather to run multiple asynchronous functions concurrently
    # Wait for each task to complete in order
    await asyncio.gather(
        print_message("Async", 2),
        print_message("Hello", 1),
        print_message("World", 3)
    )

# Run the event loop to execute the asynchronous code
if __name__ == "__main__":
    # Record the start time for measuring execution time
    start_time = time.time()

    # Run the main asynchronous function using asyncio.run()
    asyncio.run(main())

    # Calculate and print the total execution time
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")
