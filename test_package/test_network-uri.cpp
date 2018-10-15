// Test for HowardHinnant/date Conan package
// Dmitriy Vetutnev, ODANT, 2018


#include <network/uri.hpp>
#include <iostream>


int main(int, char**) {
    const std::string uriStr = "http://user@www.example.com:80/path?query#fragment";
    std::cout << "uriStr: " << uriStr << std::endl;
    const network::uri uri{uriStr};
    std::cout << "uri.scheme(): " << uri.scheme() << std::endl;
    std::cout << "uri.host(): " << uri.host() << std::endl;
    std::cout << "uri.user_info(): " << uri.user_info() << std::endl;
    std::cout << "uri.port(): " << uri.port() << std::endl;
    std::cout << "uri.user_info(): " << uri.user_info() << std::endl;
    std::cout << "uri.query(): " << uri.query() << std::endl;
    std::cout << "uri.fragment(): " << uri.fragment() << std::endl;
}