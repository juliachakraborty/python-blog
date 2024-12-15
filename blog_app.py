from jinja2 import Environment, FileSystemLoader
import os

# Paths
templatesS_DIR = 'templates'
OUTPUT_DIR = 'output'

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader(templatesS_DIR))

# List of pages to generate
pages = [
    {"templates": "index.html", "output": "index.html", "context": {"title": "Home"}},
    {"templates": "about.html", "output": "about.html", "context": {"title": "About Me"}},
]

# Generate HTML files
os.makedirs(OUTPUT_DIR, exist_ok=True)

for page in pages:
    template = env.get_template(page["templates"])
    output = template.render(page["context"])
    
    output_path = os.path.join(OUTPUT_DIR, page["output"])
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)
        print(f"Generated static file: {output_path}")
