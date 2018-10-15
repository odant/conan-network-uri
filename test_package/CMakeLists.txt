# Test for HowardHinnant/date Conan package
# Dmitriy Vetutnev, ODANT, 2018


project(PackageTest CXX)
cmake_minimum_required(VERSION 3.0)


include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)


enable_testing()


# Conan imported targets

add_executable(test_network-uri_CONAN_PKG test_network-uri.cpp)
target_link_libraries(test_network-uri_CONAN_PKG CONAN_PKG::network-uri)
set_target_properties(test_network-uri_CONAN_PKG
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_network-uri_CONAN_PKG
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_network-uri_CONAN_PKG
)
