#pragma once

#include "request.h"
#include "response.h"

class HttpClient {
public:
    Response sendRequest(const Request& req);
};