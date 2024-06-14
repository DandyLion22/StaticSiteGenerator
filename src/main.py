import os
import shutil
from pathlib import Path
from textnode import TextNode
from utils import generate_page, extract_title


def main():
    # Create a dummy object and print it (leaving your original functionality intact)
    dummy_object = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(dummy_object)

    # Define source and destination paths
    source_dir = Path("/Users/daniellappe/workspace/github.com/DandyLion22/staticsitegenerator/static")
    destination_dir = Path("/Users/daniellappe/workspace/github.com/DandyLion22/staticsitegenerator/public")

    # Step 1: Delete the contents of the 'public' directory
    if destination_dir.exists() and destination_dir.is_dir():
        shutil.rmtree(destination_dir)
    
    # Create the 'public' directory fresh
    os.makedirs(destination_dir, exist_ok=True)

    # Step 2: Define your copy function
    def copy_recursive(src, dest):
        for item in os.listdir(src):
            source_path = os.path.join(src, item)
            destination_path = os.path.join(dest, item)
            if os.path.isdir(source_path):
                os.makedirs(destination_path, exist_ok=True)
                copy_recursive(source_path, destination_path)  # Recurrence
            else:
                shutil.copy2(source_path, destination_path)
                print(f"Copied {source_path} to {destination_path}")

    # Copy the contents of the 'static' directory to the 'public' directory
    copy_recursive(source_dir, destination_dir)

    # Define paths
    from_path = "/Users/daniellappe/workspace/github.com/DandyLion22/staticsitegenerator/content/index.md"
    template_path = "/Users/daniellappe/workspace/github.com/DandyLion22/staticsitegenerator/src/template.html"
    dest_path = "/Users/daniellappe/workspace/github.com/DandyLion22/staticsitegenerator/public/index.html"
    
    # Generate the HTML page
    generate_page(from_path, template_path, dest_path)
    
    print("Page generated successfully!")


if __name__ == "__main__":
    main()



