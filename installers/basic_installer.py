import os
import urllib

from hurry.filesize import size, alternative
from abc import ABCMeta, abstractmethod


class BasicInstaller(object):
    __metaclass__ = ABCMeta
    
    def __init__(self, manifest):
        """
        :param manifest: The package manifest.
        :type manifest: manifest.__Manifest
        """
        super(BasicInstaller, self).__init__()
        self._manifest = manifest
        self.__dir = None
        self.__app_directory = None
        self.__cache_directory = None

    def install(self, verify=True):
        """
        This is the core function that actually install the package.
        :param verify: verify the installation on not [default: True]
        :type verify: bool
        :return: return if installed correctly or not,
                 if verify is False return always True.
        :rtype: bool
        """
        print "Installing '{}' ({}).".format(self._manifest.name,
                                             self._manifest.version)
        self.download_file()
        self.check_hash()
        self._install()

        if self._manifest.get('add_to_path', False):
            self.add_to_path()

        return self._verify() if verify else True

    def __lazy_path_load(self, path, attribute):
        attribute = '_BasicInstaller{}'.format(attribute)
        if not getattr(self, attribute):
            setattr(self, attribute, path)
            if not os.path.exists(path):
                os.mkdir(path)

    @property
    def dir(self):
        path = os.path.join(os.path.expanduser('~'), 'ppm')
        self.__lazy_path_load(path, '__dir')
        return self.__dir

    @property
    def app_directory(self):
        path = os.path.join(self.dir, self._manifest.name)
        self.__lazy_path_load(path, '__app_directory')
        return self.__app_directory

    @property
    def cache_directory(self):
        path = os.path.join(self.dir, 'cache')
        self.__lazy_path_load(path, '__cache_directory')
        return self.__cache_directory

    @property
    def cache_app_file(self):
        return os.path.join(self.cache_directory,
                            '{}#{}'.format(self._manifest.name,
                                           self.download_file_name))

    @property
    def download_file_name(self):
        head, tail = os.path.split(self._manifest.url)
        return tail

    @abstractmethod
    def _install(self):
        pass

    @abstractmethod
    def _verify(self):
        pass

    def download_file(self):
        print 'Downloading', self._manifest.name, '...'
        urllib.urlretrieve(self._manifest.url, self.cache_app_file,
                           self.__report_download)
        print

    def __report_download(self, count, block_size, total_size):
        percent = int(count * block_size * 100 / total_size)
        equal = int(percent * 0.7)
        print "\r{file_name} ({size}) [{equal}>{space}] {percent}%".format(
            percent=percent,
            equal='=' * equal,
            space=' ' * (70 - equal),
            size=size(total_size, alternative),
            file_name=self.download_file_name
        ),

    def add_to_path(self):
        raise NotImplemented()
