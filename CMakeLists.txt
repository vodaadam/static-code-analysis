cmake_minimum_required(VERSION 3.16)
project(InferDepthTest)

set(CMAKE_CXX_STANDARD 17)

add_executable(test_app 
    chained_calls.cpp
    chained_calls2.cpp
)