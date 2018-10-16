# C++ Network URI Conan package
# Dmitriy Vetutnev, ODANT 2018

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

enable_testing()
add_subdirectory(src)
