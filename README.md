# fastfuzz
High-performance web fuzzer (C++ + Python)

## Dependencies

Before building this project, make sure you have installed the required libraries:

- **Linux (Debian/Ubuntu)**:
```bash
sudo apt-get install libcurl4-openssl-dev
```

Day 1 - Project skeleton

📋 TODO

 ✔️ Create a repository

 ✔️ Connect pybind11

 ✔️ Organized the file structure

 ✔️CMake build shared library

 ✔️ Check module import in Python

📌 Minimal test:

```python
import fastfuzz_core
print(fastfuzz_core.func())