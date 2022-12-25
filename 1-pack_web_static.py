#!/usr/bin/python3
# # Fabfile to generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


# """
#     Fabric script that generates a .tgz archive from the
#     contents of the web_static folder of the AirBnB Clone repo.
# """
# from os import makedirs
# from datetime import datetime
# from fabric.api import local


# def do_pack():
#     """ Function that generates the archive. """
#     timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#     file_path = "versions/web_static_{}.tgz".format(timestamp)

#     try:
#         makedirs("./versions", exist_ok=True)
#         local('tar -cvzf {} web_static'.format(file_path))
#         print('all went well')
#         return file_path

#     except:
#         # return None
#         print("Something else went wrong")

do_pack()