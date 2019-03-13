from conans import ConanFile
import os

class DtcConan(ConanFile):
    name = "dtc_installer"
    version = "1.5.0"
    license = "GPLv2"
    url = "https://git.kernel.org/pub/scm/utils/dtc/dtc.git"
    description = "Device Tree Compiler (dtc) toolchain for working with device tree source and binary files."
    settings = "os", "compiler", "arch"  # "build_type" makes no sense currently since we do not modify the CFLAGS
    scm = {
        "type": "git",
        "url": "git://git.kernel.org/pub/scm/utils/dtc/dtc.git",
        "revision": "v1.5.0"
    }

    def configure(self):
        # The device tree compiler and libfdt is purely written in C.
        del self.settings.compiler.libcxx

    def build(self):
        # Build the device tree compiler as well as libfdt. The currently used
        # install target builds and installs both, the static and the shared
        # libfdt library.
        self.run("make install NO_PYTHON=1 CC='{}' PREFIX='{}'".format(self.settings.compiler,
                                                                       self.package_folder))

    def package_info(self):
        self.cpp_info.libs = ["fdt"]

        # Make built applications usable by appending the bin directory to PATH.
        self.env_info.PATH = [os.path.join(self.package_folder, "bin")]
        self.env_info.LD_LIBRARY_PATH = [os.path.join(self.package_folder, "lib")]
