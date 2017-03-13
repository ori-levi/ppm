from abc import ABCMeta, abstractmethod


class BasicInstaller(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def install(self, manifest, verify=True):
        """
        This is the core function that actually install the package.
        :param manifest: The package manifest.
        :type manifest: dict
        :param verify: verify the installation on not [default: True]
        :type verify: bool
        :return:
        """
        pass
