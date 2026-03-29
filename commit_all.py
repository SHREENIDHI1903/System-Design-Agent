import subprocess
import os

def run_command(command):
    print(f"Executing: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout.strip()

def main():
    # Get all untracked and modified files (respecting .gitignore)
    files = run_command("git ls-files --others --exclude-standard").split('\n')
    files = [f for f in files if f.strip()]

    print(f"Found {len(files)} files to commit.")

    for i, file_path in enumerate(files, 1):
        if not os.path.exists(file_path):
            continue
            
        print(f"[{i}/{len(files)}] Committing: {file_path}")
        
        # Add the single file
        run_command(f'git add "{file_path}"')
        
        # Commit with a descriptive message
        # Use simple basename for message to keep it clean
        basename = os.path.basename(file_path)
        commit_message = f"Add {file_path}"
        run_command(f'git commit -m "{commit_message}"')

    print("Individual commits completed.")

if __name__ == "__main__":
    main()
