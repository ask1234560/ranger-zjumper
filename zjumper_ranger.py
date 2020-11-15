import ranger.api
from ranger.api.commands import *
from os import getenv


class z(Command):
    """:z
    Uses .z file to set the current directory.
    """
    def execute(self):

        # location of .z file
        z_loc = getenv("HOME")+"/.z"
        with open(z_loc,"r") as fobj:
            flists = fobj.readlines()

        # user given directory
        req = self.args
        directories = []
        for i in flists:
            for j in req[1:]:
                if j.lower() in i.lower():
                    if j == req[-1]:
                        directories.append(i.split("|")[0])
                else:
                    break

        try:
            #  smallest(length) directory will be the directory required
            self.fm.execute_console("cd " + min(directories,key=lambda x: len(x)))
        except Exception as e:
            raise Exception("Directory not found")
