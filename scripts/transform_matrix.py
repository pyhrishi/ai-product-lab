import sys

filepath = '/Users/pyhrishi/Desktop/100 AI Projects/PROJECT_MATRIX_FULL.md'

with open(filepath, 'r') as f:
    lines = f.readlines()

new_lines = []

for line in lines:
    if line.startswith('| # | Name'):
        # Header update
        new_lines.append("| # | Name | Tier | Category | Pattern | Depth | Type | Build | Core Problem | Why AI | Stack | Complexity | Target Signal | Content Pieces | Narrative |\n")
        continue
    
    if line.startswith('|') and not line.startswith('| # | Name'):
        parts = line.strip().split('|')
        if len(parts) >= 16:
            # Re-mapping to a more concise format to avoid extreme width
            p_id = parts[1].strip()
            name = parts[2].strip()
            category = parts[3].strip()
            depth = parts[4].strip()
            key_system = parts[9].strip()
            stack = parts[10].strip()
            complexity = parts[11].strip()
            signal = parts[12].strip()
            narrative = parts[16].strip()
            
            # Logic for new columns
            tier = "1" if depth == "Deep" else ("2" if depth == "Shallow" else "3")
            pattern = "RAG" if "RAG" in key_system else ("Agent" if "Agent" in key_system else ("Eval loop" if "Eval" in key_system else ("Memory" if "Memory" in key_system else "Workflow")))
            content = "Tweet/Thread/Case Study" if tier == "1" else "Tweet/Thread"
            
            # Formulate concise row (15 columns)
            # | # | Name | Tier | Category | Pattern | Depth | Type | Build | Core Problem | Why AI | Stack | Complexity | Target Signal | Content Pieces | Narrative |
            new_row = [
                "", # start
                p_id,
                name,
                tier,
                category,
                pattern,
                depth,
                parts[5].strip(), # type
                parts[6].strip(), # build
                parts[7].strip(), # problem
                parts[8].strip(), # why ai
                stack,
                complexity,
                signal,
                content,
                narrative,
                "" # end
            ]
            new_lines.append("|".join(new_row) + "\n")
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open(filepath, 'w') as f:
    f.writelines(new_lines)
print("Successfully transformed PROJECT_MATRIX_FULL.md")
