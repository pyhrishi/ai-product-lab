import os
import sys
import argparse

def scaffold_project(name, tier, pattern):
    # Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(base_dir, 'templates', 'PRD_TEMPLATE.md')
    target_dir = os.path.join(base_dir, 'projects', f'tier-{tier}', name)
    target_file = os.path.join(target_dir, 'README.md')

    # Create directory
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Created directory: {target_dir}")
    else:
        print(f"Directory already exists: {target_dir}")
        return

    # Read template
    with open(template_path, 'r') as f:
        content = f.read()

    # Replace placeholders
    content = content.replace('* Name:', f'* Name: {name}')
    content = content.replace('* Tier: (1 / 2 / 3)', f'* Tier: {tier}')
    content = content.replace('* Pattern: (RAG / Agent / Eval loop / etc.)', f'* Pattern: {pattern}')

    # Write new README
    with open(target_file, 'w') as f:
        f.write(content)
    
    print(f"Successfully scaffolded project: {name} in Tier {tier}")
    print(f"File created: {target_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scaffold a new AI Product Lab project.")
    parser.add_argument("name", help="Name of the project (e.g., my-new-agent)")
    parser.add_argument("tier", type=int, choices=[1, 2, 3], help="Tier of the project (1, 2, or 3)")
    parser.add_argument("pattern", help="AI pattern (e.g., RAG, Agent, Eval loop)")

    args = parser.parse_args()
    scaffold_project(args.name, args.tier, args.pattern)
