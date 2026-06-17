from textnode import TextNode, TextType
import os
import shutil
import logging





def main():
    print(f"main")
    copy_static()

def copy_static():
    # copy all of static files to public
    # check if path exists, create public if it doesn't. delete public and re-create it if it does
    # copy all files and subdirectories to from static to public
    # log paths.
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info("copy_static started")
    public_path = os.path.abspath("./public/")
    logging.info(f"public_path : {public_path}")
    path = os.path.exists(public_path)
    logging.info(f"public_path exists: {path}")
    if not path:
        logging.info("no path found, creating directory.")
        os.mkdir(public_path)
    else:
        logging.info("path found, deleting directory and recreating it.")
        shutil.rmtree(public_path)
        os.mkdir(public_path)


    # list all files and loop through.
    logging.info("list all files and loop through")
    static_path = os.path.abspath("./static/")
    logging.info(f"static_path: {static_path}")
    static_dir = os.listdir(static_path)
    for line in static_dir:
        src = os.path.join(static_path,line)
        destination = os.path.join(public_path,line)
        is_file = os.path.isfile(src)
        if is_file:

            shutil.copy(src, destination)
        else:
            shutil.copytree(src, destination)
def generate_page(from_path, template_path, dest_path):
    pass

main()
