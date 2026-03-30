import os
import json
import re

def parse_markdown_table(filepath):
    """Parses the AI Project Matrix markdown table and returns a list of dictionaries."""
    projects = []
    
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        # Check for project rows (start with | and have enough segments)
        if line.startswith('|') and '|' in line[1:]:
            parts = [p.strip() for p in line.split('|')]
            # Exclude the title row: | # | Name | Tier | ...
            if parts[1] == '#' or parts[1] == '---':
                continue
            
            # parts layout (16 elements including start/end gaps)
            # ['', '1', 'name', 'tier', 'category', 'pattern', 'depth', 'type', 'build', 'problem', 'why_ai', 'stack', 'complexity', 'signal', 'content', 'narrative', '']
            if len(parts) >= 15:
                project = {
                    "id": parts[1],
                    "name": parts[2],
                    "tier": parts[3],
                    "category": parts[4],
                    "pattern": parts[5],
                    "depth": parts[6],
                    "type": parts[7],
                    "build": parts[8],
                    "problem": parts[9],
                    "why_ai": parts[10],
                    "stack": parts[11],
                    "complexity": parts[12],
                    "signal": parts[13],
                    "content": parts[14],
                    "narrative": parts[15]
                }
                projects.append(project)
    
    return projects

def export_to_json():
    # Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file = os.path.join(base_dir, 'projects', 'PROJECT_MATRIX.md')
    output_dir = os.path.join(base_dir, 'docs')
    output_file = os.path.join(output_dir, 'projects.json')
    
    # Ensure docs dir exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    # Parse and Export
    try:
        data = parse_markdown_table(input_file)
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Successfully exported {len(data)} projects to {output_file}")
    except Exception as e:
        print(f"Error during export: {e}")

if __name__ == "__main__":
    export_to_json()
