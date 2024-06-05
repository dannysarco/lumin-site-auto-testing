import os
import subprocess
import difflib

# Define paths
CURRENT_FILE = 'luminsmart_homepage.html'
PREVIOUS_FILE = 'luminsmart_homepage_previous.html'
DIFF_FILE = 'luminsmart_homepage_diff.html'

# Step 1: Run the `extract-elements.py` script
subprocess.run(['python3', 'extract-elements.py'])

# Step 2: Check if previous file exists
if os.path.exists(CURRENT_FILE):
    # If previous file exists, rename it
    if os.path.exists(PREVIOUS_FILE):
        os.remove(PREVIOUS_FILE)
    os.rename(CURRENT_FILE, PREVIOUS_FILE)

# Run the `extract-elements.py` script again to generate the latest file
subprocess.run(['python3', 'extract-elements.py'])

# Step 3: Compare the new file with the previous file
if os.path.exists(PREVIOUS_FILE):
    with open(CURRENT_FILE, 'r') as current, open(PREVIOUS_FILE, 'r') as previous:
        current_lines = current.readlines()
        previous_lines = previous.readlines()

    # Use difflib to get the differences
    diff = difflib.HtmlDiff().make_file(previous_lines, current_lines, fromdesc='Previous', todesc='Current')

    # Step 4: Write the differences to a file
    with open(DIFF_FILE, 'w') as diff_file:
        diff_file.write(diff)

    print(f"Differences written to {DIFF_FILE}")
else:
    print("No previous file to compare with. Generated the initial HTML file.")