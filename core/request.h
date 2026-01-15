#pragma once
#include <string>
#include <map>

struct Request {
    std::string url;    
    std::string method = "GET";  
    std::map<std::string, std::string> headers;
    std::string body; 
};