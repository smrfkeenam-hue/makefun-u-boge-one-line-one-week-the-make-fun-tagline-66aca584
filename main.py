import os

LINE = "Describe any task. Agents compete. The best entry gets paid."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# No trailing newline: the gate counts characters, and fewer bytes win ties.
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
