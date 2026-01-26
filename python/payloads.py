
from pathlib import Path

def load_payloads(file_path):
    with open(file_path,"r", encoding="utf-8") as f:
        for line in f:
            payload = line.strip()
            if payload:
                yield payload
                             