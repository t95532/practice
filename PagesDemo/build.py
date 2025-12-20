import json
from pathlib import Path

# Paths
DATA_FILE = "data.json"
TEMPLATE_FILE = "templates/index.template.html"
DIST_DIR = Path("dist")
OUTPUT_FILE = DIST_DIR / "index.html"

DIST_DIR.mkdir(exist_ok=True)

# Load data
with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Load template
with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
    template = f.read()

# Build skills HTML
skills_html = ""
for category, skills in data["skills"].items():
    skills_html += f"<h3>{category}</h3><ul>"
    for skill in skills:
        skills_html += f"<li>{skill}</li>"
    skills_html += "</ul>"

# Build projects HTML
projects_html = "<ul>"
for project in data["projects"]:
    projects_html += f"<li><strong>{project['name']}</strong>: {project['description']}</li>"
projects_html += "</ul>"

# Replace placeholders
html = template
replacements = {
    "{{name}}": data["name"],
    "{{title}}": data["title"],
    "{{location}}": data["location"],
    "{{about}}": data["about"],
    "{{skills}}": skills_html,
    "{{projects}}": projects_html,
    "{{email}}": data["contact"]["email"],
    "{{linkedin}}": data["contact"]["linkedin"]
}

for key, value in replacements.items():
    html = html.replace(key, value)

# Write output
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Portfolio generated: dist/index.html")
