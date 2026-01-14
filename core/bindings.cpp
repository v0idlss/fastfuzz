#include <pybind11/pybind11.h>

PYBIND11_MODULE(fastfuzz_core, m) {
    m.def("func", []() {
        return "Hello World";
    });
}