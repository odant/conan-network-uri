# C++ Network URI Conan package
# Dmitriy Vetutnev, ODANT 2018


from conans import ConanFile, CMake, tools


class NetworkURIConan(ConanFile):
    name = "network-uri"
    version = "1.1.0+0"
    license = "Boost Software License - Version 1.0 https://raw.githubusercontent.com/cpp-netlib/uri/master/LICENSE_1_0.txt"
    description = "C++ Network URI"
    url = "https://github.com/odant/conan-network-uri"
    settings = {
        "os": ["Windows", "Linux"],
        "compiler": ["Visual Studio", "gcc"],
        "build_type": ["Debug", "Release"],
        "arch": ["x86_64", "x86", "mips"]
    }
    options = {
        "with_unit_tests": [False, True],
    }
    default_options = "with_unit_tests=False"
    generators = "cmake"
    exports_sources = "src/*", "!src/src/boost/*", "CMakeLists.txt", "external_boost.patch", "with_unit_tests.patch", "create_relative_uri_without_sheme.patch"
    no_copy_source = True
    build_policy = "missing"

    def configure(self):
        # Only C++11
        if self.settings.compiler.get_safe("libcxx") == "libstdc++":
            raise Exception("This package is only compatible with libstdc++11")

    def build_requirements(self):
        self.build_requires("boost/[>=1.60.0]@odant/stable")

    def source(self):
        tools.patch(patch_file="external_boost.patch")
        tools.patch(patch_file="with_unit_tests.patch")
        tools.patch(patch_file="create_relative_uri_without_sheme.patch")

    def build(self):
        build_type = "RelWithDebInfo" if self.settings.build_type == "Release" else "Debug"
        cmake = CMake(self, build_type=build_type)
        cmake.verbose = True
        #
        if self.settings.os != "Windows":
            cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE:BOOL"] = "ON"
        cmake.definitions["BUILD_SHARED_LIBS:BOOL"] = "OFF"
        #
        cmake.definitions["Uri_BUILD_TESTS:BOOL"] = "ON" if self.options.with_unit_tests else "OFF"
        if self.options.with_unit_tests:
            cmake.definitions["gtest_force_shared_crt:BOOL"] = "ON"
        cmake.definitions["Uri_BUILD_DOCS:BOOL"] = "OFF"
        cmake.definitions["Uri_USE_STATIC_CRT:BOOL"] = "OFF"
        #
        cmake.configure()
        cmake.build()
        if self.options.with_unit_tests:
            if self.settings.os == "Windows":
                self.run("ctest --output-on-failure --build-config %s" % self.settings.build_type)
            else:
                self.run("ctest --output-on-failure")

    def package(self):
        self.copy("*.hpp", dst="include", src="src/include", keep_path=True)
        self.copy("libnetwork-uri.a", dst="lib", src="lib", keep_path=False)
        self.copy("network-uri.lib", dst="lib", src="lib", keep_path=False)
        self.copy("network-uri.pdb", dst="bin", src="lib", keep_path=False)

    def package_id(self):
        self.info.options.with_unit_tests = "any"

    def package_info(self):
        self.cpp_info.libs = ["network-uri"]
