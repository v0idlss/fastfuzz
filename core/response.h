#pragma once
#include <string>

struct Response {
    long statusCode = 0;
    std::string body;
};