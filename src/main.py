import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page

dir_path_static = "/Users/daniellappe/workspace/github.com/DandyLion22/staticsitegenerator/static"
dir_path_public = "/Users/daniellappe/workspace/github.com/DandyLion22/staticsitegenerator/public"
dir_path_content = "/Users/daniellappe/workspace/github.com/DandyLion22/staticsitegenerator/content"
template_path = "/Users/daniellappe/workspace/github.com/DandyLion22/staticsitegenerator/src/template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )


main()


