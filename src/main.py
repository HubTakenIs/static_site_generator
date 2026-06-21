from block_markdown import markdown_to_html_node
from textnode import TextNode, TextType
import os
import shutil
import logging
import sys





def main():
    print(f"main")
    base_url = ""
    if len(sys.argv) == 1 :
        base_url = "/"
    else:
        base_url = sys.argv[1]

    print(f"BASE URL: {base_url}")
    copy_static("./docs/")
    from_path = os.path.abspath("content")
    template_path = os.path.abspath("template.html")
    destination = os.path.abspath("docs")
    generate_pages_recursive(from_path, template_path, destination, base_url)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_url):
    content_list = os.listdir(dir_path_content)
    for content in content_list:
        from_path = os.path.join(dir_path_content, content)
        is_file = os.path.isfile(from_path)
        if is_file:
            destination = os.path.join(dest_dir_path, content.replace(".md", ".html"))
            generate_page(from_path, template_path, destination,base_url)
        else:
            # check if directory in destination.
            exists = os.path.isdir(
                os.path.join(
                    dest_dir_path, content
                )
            )
            destination = os.path.join(dest_dir_path, content)
            if exists:
                generate_pages_recursive(from_path, template_path, destination,base_url)
            else:
                os.mkdir(destination)
                generate_pages_recursive(from_path, template_path, destination,base_url)

def copy_static(other_path=None):
    # copy all of static files to public
    # check if path exists, create public if it doesn't. delete public and re-create it if it does
    # copy all files and subdirectories to from static to public
    # log paths.
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info("copy_static started")
    public_path = os.path.abspath("./public/")
    if other_path:
        public_path = os.path.abspath(other_path)
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

def generate_page(from_path, template_path, dest_path, base_url):
    # print message
    print(f"Generating page from {from_path}, to {dest_path} using {template_path}")
    # read file at from_path
    f = open(from_path)
    from_path_file = f.read()
    f.close()
    # read template at template_path
    f = open(template_path)
    template_file = f.read()
    f.close()
    # convert markdown to html
    html_content = markdown_to_html_node(from_path_file).to_html()
    # extract title
    title = extract_title(from_path_file)
    # replace title and content in template
    template_file = template_file.replace("{{ Title }}", title)
    template_file = template_file.replace("{{ Content }}", html_content)
    print(f"\n\n BASE URL INSIDE GENERATE PAGE \n\n {base_url}\n\n")
    template_file = template_file.replace('href="/',f'href="{base_url}')
    template_file = template_file.replace('src="/',f'src="{base_url}')
    # write new html page at dest_path
    f = open(dest_path,"w")
    f.write(template_file)
    f.close()

def extract_title(markdown):
    text = ""
    if markdown.startswith("# "):
        text = markdown.replace("# ", "").split("\n\n",1)[0]
    if not text:
        raise Exception("No Title")
    return text

if __name__ == "__main__":
    main()
