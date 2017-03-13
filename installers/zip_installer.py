from zipfile import ZipFile
from installers.basic_installer import BasicInstaller


class ZipInstaller(BasicInstaller):
    def __init__(self, manifest):
        super(self.__class__, self).__init__(manifest)

    def _verify(self):
        pass

    def _install(self):
        with ZipFile(self.cache_app_file) as zf:
            zf.extractall(self.app_directory)

if __name__ == '__main__':
    import manifest
    m = manifest.manifest('scapy.json')
    z = ZipInstaller(m)
    print z.install()
