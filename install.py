import platform


def __windows_installer(manifest_path):
    """
    Get windows installer.
    :param manifest_path: path to the app manifest file.
    :type manifest_path: str
    :return: installer object to install the app.
    :rtype installers.basic_installer.BasicInstaller
    """
    raise NotImplementedError()


def __mac_os_installer(manifest_path):
    """
    Get macOS installer.
    :param manifest_path: path to the app manifest file.
    :type manifest_path: str
    :return: installer object to install the app.
    :rtype installers.basic_installer.BasicInstaller
    """
    raise NotImplementedError()


def __linux_installer(manifest_path):
    """
    Get linux installer.
    :param manifest_path: path to the app manifest file.
    :type manifest_path: str
    :return: installer object to install the app.
    :rtype installers.basic_installer.BasicInstaller
    """
    raise NotImplementedError()


PLATFORMS = {
    'Windows': __windows_installer,
    'Darwin': __mac_os_installer,
    'Linux': __linux_installer
}


def get_installer(manifest_path):
    """
    Get installer according to your operation system.
    :param manifest_path: path to the app manifest file.
    :type manifest_path: str
    :return: installer object to install the app.
    :rtype installers.basic_installer.BasicInstaller
    """
    platform_ = platform.system()
    installer = PLATFORMS[platform_]
    return installer(manifest_path)
