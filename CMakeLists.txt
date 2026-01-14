cmake_minimum_required(VERSION 3.15)
project(fastfuzz_core LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# -------- Python --------
find_package(Python COMPONENTS Interpreter Development REQUIRED)

# -------- pybind11 includes via python -m pybind11 --------
execute_process(
    COMMAND "${Python_EXECUTABLE}" -m pybind11 --includes
    OUTPUT_VARIABLE PYBIND11_INCLUDES_RAW
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

# Convert “-I/path1 -I/path2” -> “/path1;/path2”
separate_arguments(PYBIND11_INCLUDES_RAW)
set(PYBIND11_INCLUDE_DIRS "")
foreach(arg ${PYBIND11_INCLUDES_RAW})
    if(arg MATCHES "^-I(.*)")
        list(APPEND PYBIND11_INCLUDE_DIRS "${CMAKE_MATCH_1}")
    endif()
endforeach()

message(STATUS "pybind11 include dirs: ${PYBIND11_INCLUDE_DIRS}")

# -------- Python module --------
add_library(fastfuzz_core MODULE
    core/bindings.cpp
    core/http_client.cpp
)

target_include_directories(fastfuzz_core PRIVATE
    ${PYBIND11_INCLUDE_DIRS}
    core
)

# -------- Important properties for Python --------
set_target_properties(fastfuzz_core PROPERTIES
    PREFIX ""        # remove lib
    SUFFIX ".so"     # Python module extension
)
