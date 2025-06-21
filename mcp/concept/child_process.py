import sys

def process_input():
    """
    Reads lines from stdin, converts them to uppercase, and writes to stdout.
    Stops when it reads an empty line or stdin closes.
    """
    sys.stderr.write("Child process: Starting to read from stdin...\n")
    try:
        for line in sys.stdin:
            line = line.strip()
            if not line: # Empty line can signal end or just be skipped
                sys.stderr.write("Child process: Read empty line.\n")
                continue # Process next line or break if empty line means end

            processed_line = line.upper()
            sys.stdout.write(f"PROCESSED: {processed_line}\n")
            sys.stdout.flush() # IMPORTANT: Flush stdout immediately to send data
            sys.stderr.write(f"Child process: Processed '{line}'\n")

    except BrokenPipeError:
        sys.stderr.write("Child process: Parent pipe was closed unexpectedly.\n")
    except Exception as e:
        sys.stderr.write(f"Child process: An error occurred - {e}\n")
    finally:
        sys.stderr.write("Child process: Exiting.\n")

if __name__ == "__main__":
    process_input()