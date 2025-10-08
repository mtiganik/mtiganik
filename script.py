import datetime
import time
import subprocess

README_PATH = "README.md"
INPUT_PATH = "input.txt"

def ReadTodayCount():
    today_str = datetime.date.today().strftime("%d.%m.%Y")  
    #today_str = datetime.date.today()
    with open(INPUT_PATH, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2 and parts[0] == today_str:
                try:
                    return int(parts[1])
                except ValueError:
                    return 0
    return 0

def toggle_semicolon_in_readme():
    with open(README_PATH, "r") as f:
        lines = f.readlines()

    if not lines:
        return False

    # Toggle colon in the first line
    first_line = lines[0].rstrip("\n")
    if first_line.endswith(":"):
        first_line = first_line[:-1]  # remove colon
    else:
        first_line += ":"

    lines[0] = first_line + "\n"

    with open(README_PATH, "w") as f:
        f.writelines(lines)

    return True

def git_commit_push(commit_message):
    subprocess.run(["git", "add", README_PATH], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push"], check=True)

def main():
    num_commits = ReadTodayCount()
    print(f"Commits scheduled for today: {num_commits}")

    if num_commits <= 0:
        num_commits = 1

    for i in range(num_commits):
        changed = toggle_semicolon_in_readme()
        if changed:
            commit_message = f"Daily commit {i+1}/{num_commits} - {datetime.date.today()}"
            git_commit_push(commit_message)
            time.sleep(5)  # short delay between commits
        else:
            print("No change made to README.md.")

if __name__ == "__main__":
    main()
