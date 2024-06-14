import os
from block_markdown import markdown_to_html_node
from htmlnode import to_html



def extract_title(markdown):
    md_lines = markdown.split("\n")
    h1_count = 0
    title = None
    
    for line in md_lines:
        line = line.strip()  # Remove leading and trailing whitespace
        if line.startswith("# ") and not line.startswith("## "):
            if h1_count == 0:
                title = line[2:].strip()  # Store the first title found
                h1_count += 1
            else:
                raise Exception("Multiple H1 titles found in the markdown file.")
    
    if title is None:
        raise Exception("No H1 title found in the markdown file.")



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Open and read the markdown file
    with open(from_path, "r") as file:
        content_from_path = file.read()
    
    # Open and read the template file
    with open(template_path, "r") as template_file:
        content_template_path = template_file.read()
    
    # Convert the markdown content to HTML
    html_node = markdown_to_html_node(content_from_path)
    html_content = html_node.to_html()  # .to_html() assumes that `html_node` has this method
    
    # Extract the title from the markdown content
    title = extract_title(content_from_path)
    
    # Replace placeholders in the template
    final_content = content_template_path.replace("{{ Title }}", title)
    final_content = final_content.replace("{{ Content }}", html_content)
    
    # Ensure the destination directory exists
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Write the final HTML content to the destination path
    with open(dest_path, "w") as dest_file:
        dest_file.write(final_content)



