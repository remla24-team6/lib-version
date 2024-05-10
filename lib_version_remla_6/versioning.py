from importlib_resources import files


class VersioningUtil:
    def get_version(self):
        """This library is version-aware. This method fetches the current version from the project metadata and returns it.
        Returns the version of this library.
        """ 
        version = files('resources').joinpath('version.txt').read_text()
        return version
    
    
if __name__ == "__main__":
    util = VersioningUtil()
    
    print(util.get_version())