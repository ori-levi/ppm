from enum import Enum
from installers.basic_installer import BasicInstaller


class MsiInstaller(BasicInstaller):

    INSTALLER_ARGS = Enum()

    def install(self, manifest, verify=True):
        pass
