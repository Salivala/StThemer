"""" aldkjdlakwjd """
class ConfigManger:
    """ alkjdlakwjd """
    def __init__(self, filename=False):
        """ Assume the file has already been checked for validity """
        self.filename = filename

    def read_all(self):
        """ Read all data from a text file """
        content = ""
        for _i, line in enumerate(open(self.filename, 'r')):
            content += line


