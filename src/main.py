from textnode import TextNode, TextType
import os
import shutil
import logging

logger = logging.getLogger(__name__)

def main():
    print(f"Hello world")
    print("copy static")
    copy_static

def copy_static():
    # copy all of static files to public
    # check if path exists, create public if it doesn't. delete public and re-create it if it does
    # copy all files and subdirectories to from static to public
    # log paths.
    public_path = os.path.abspath("./public/")
    path = os.path.exists(public_path)
    if not path:
        os.mkdir(public_path)
    else:
        shutil.rmtree(public_path)

    # list all files and loop through.
    static_path = os.path.abspath("./static/")
    static_dir = os.listdir(static_path)
    for line in static_dir:
        src = os.path.join(static_path,line)
        destination = os.path.join(public_path,line)
        is_file = os.path.isfile(src)
        if is_file:

            shutil.copy(src, destination)
        else:
            shutil.copytree(src, destination)

main()
