import argparse

from pathlib import Path
from runner import run

def args_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-u", "--url",
        required=True,
        help="URL website.",
        dest=""
    )
    parser.add_argument(
        "-t", "--threads",
        type=int,
        default=10,
        help="Threads (default: 10).",
        dest=""
    )
    parser.add_argument(
        "-p", "--payload",
        required=True,
        type=Path,
        help="Path to the file with payloads.",
        dest=""
    )
    parser.add_argument(
        "-x", "--method",
        default="GET",
        help="HTTP method for requests (default: GET).",
        dest=""
    )
    parser.add_argument(
        "--rate",
        type=int,
        default=100,
        help="Number of requests per second (default: 100).",
        dest=""
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=5,
        help="Timeout for request in seconds (default: 5).",
        dest=""
    )

    args = parser.parse_args()
    
    config = vars(args)
    
    return config

def main():

    config = args_parse()

    run(config)

if __name__ == "__main__":
    
    main()
