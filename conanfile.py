from conans import ConanFile
import os

class DtcConan(ConanFile):
    name = "dtc_installer"
    version = "1.5.0"
    license = "GPLv2"
    url = "https://git.kernel.org/pub/scm/utils/dtc/dtc.git"
    description = "Device Tree Compiler (dtc) toolchain for working with device tree source and binary files."
    settings = "os", "compiler", "build_type", "arch"
    scm = {
        "type": "git",
        "url": "git://git.kernel.org/pub/scm/utils/dtc/dtc.git",
        "revision": "v1.5.0"
    }

    def build(self):
        self.run("make install NO_PYTHON=1 PREFIX='{}'".format(self.package_folder))

    def package_info(self):
        # make built applications usable by appending the bin directory to PATH
        self.env_info.PATH = [os.path.join(self.package_folder, "bin")]
        self.env_info.LD_LIBRARY_PATH = [os.path.join(self.package_folder, "lib")]
