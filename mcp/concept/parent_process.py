import subprocess
import time
import os

def run_child_process_with_pipes():
    """
    Spawns the child script, sends data to its stdin, and reads from its stdout/stderr.
    """
    child_script_path = os.path.join(os.path.dirname(__file__), 'child_process.py')

    if not os.path.exists(child_script_path):
        print(f"Error: Child script not found at {child_script_path}")
        print("Please make sure 'child_process_script.py' is in the same directory as this script.")
        return

    print("Parent process: Starting child process...")

    # Use subprocess.Popen to start the child process
    # stdin=subprocess.PIPE: Create a pipe for the child's stdin (parent writes to it)
    # stdout=subprocess.PIPE: Create a pipe for the child's stdout (parent reads from it)
    # stderr=subprocess.PIPE: Create a pipe for the child's stderr (parent reads error messages)
    # text=True: Enables universal newlines and makes stdin/stdout/stderr use text mode (str)
    process = subprocess.Popen(
        [sys.executable, child_script_path], # sys.executable ensures the correct python interpreter is used
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True  # Use text mode for string communication (instead of bytes)
    )

    print("Parent process: Child process started.")

    # Data to send to the child process
    messages_to_send = [
        "hello world",
        "python pipes example",
        "", # An empty line
        "end of message queue"
    ]

    try:
        for msg in messages_to_send:
            print(f"\nParent process: Sending '{msg}' to child's stdin...")
            process.stdin.write(msg + '\n') # Write to child's stdin pipe
            process.stdin.flush() # Crucial to ensure data is sent immediately

            # Read a line from child's stdout (wait for response)
            # This is a blocking read, it will wait until the child writes a line
            response_line = process.stdout.readline().strip()
            print(f"Parent process: Received from child's stdout: '{response_line}'")

            # Check for any stderr output from child (non-blocking read)
            # Use read(size) or readline() on stderr if expecting specific error messages.
            # Here, we'll just check if anything is buffered for stderr.
            # You might want to read stderr asynchronously or after communicate() for all logs.
            # For this simple example, we'll rely on communicate() at the end to get all stderr.
            # For real-time error logging, use threading or asyncio.

            time.sleep(0.5) # Simulate some work

    except BrokenPipeError:
        print("Parent process: Pipe broken, child might have exited unexpectedly.")
    except Exception as e:
        print(f"Parent process: An error occurred - {e}")
    finally:
        print("\nParent process: Closing stdin pipe to child (signals EOF)...")
        process.stdin.close() # Close stdin pipe to signal EOF to the child

        # Wait for the child process to terminate and capture its remaining output
        # communicate() returns (stdout_data, stderr_data)
        # It also waits for the process to terminate.
        stdout_final, stderr_final = process.communicate(timeout=5) # 5-second timeout

        if stdout_final:
            print("\nParent process: Remaining stdout from child:")
            print(stdout_final.strip())

        if stderr_final:
            print("\nParent process: Remaining stderr from child:")
            print(stderr_final.strip())

        print(f"\nParent process: Child process exited with code {process.returncode}")

if __name__ == "__main__":
    import sys
    run_child_process_with_pipes()