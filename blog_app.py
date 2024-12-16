from jinja2 import Environment, FileSystemLoader
import os

# Paths
TEMPLATES_DIR = 'templates'

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

# List of pages to generate
pages = [
    {"templates": "index.html", "output": "index.html", "context": {"title": "Home"}},
    {"templates": "about.html", "output": "about.html", "context": {"title": "About Me"}},
]

for page in pages:
    template = env.get_template(page["templates"])
    output = template.render(page["context"])
    
    output_path = os.path.join(os.getcwd(), page["output"])
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)
        print(f"Generated static file: {output_path}")
