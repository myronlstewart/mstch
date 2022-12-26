from conans import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps

class MstchConan(ConanFile):
    name = "mstch"
    version = "1.0.1"
    settings = "os", "compiler", "build_type", "arch"
    description = "mstch is a complete implementation of {{mustache}} templates using modern C++. It's compliant with specifications v1.1.3, including the lambda module"
    url = "https://github.com/no1msd/mstch"
    license = "MIT"
    author = "Daniel Sipka"
    no_copy_source = True

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def requirements(self):
        self.requires("boost/1.77.0")    # -> depend on boost 1.77.0

    def export_sources(self):
        self.copy("*.txt")
        self.copy("src/*")
        self.copy("include/*")
        self.copy("cmake/*")

    def generate(self):
        CMakeToolchain(self).generate()    # -> conantoolchain.cmake  (variables translated from conan settings)
        CMakeDeps(self).generate()         # -> creates FindBoost.cmake  (sets paths to Boost files in conan cache)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.hpp", dst="include", src="include")

    def package_info(self):
        self.cpp_info.includedirs = ["include"]      # List of header directories
        self.cpp_info.libdirs = ["lib"]              # List of directories to search for libraries
        self.cpp_info.libs = ["mstch"]               # List of libraries to link with