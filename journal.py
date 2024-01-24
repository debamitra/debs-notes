import os
import subprocess
import datetime

def choose_folder():
    print("Choose a folder to save the journal entry:")
    print("1. Dump")
    print("2. Notes")
    print("3. Journal")
    choice = input("Enter your choice (1/2/3): ")

    folder_map = {'1': "dump", '2': "notes", '3': "journal"}
    return folder_map.get(choice, "dump")

def write_journal_entry(folder):
    now = datetime.datetime.now()
    filename = now.strftime("%Y-%m-%d_%H-%M-%S") + ".md"
    
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, filename)

    print("Write your entry in Markdown format. Type 'quit' on a new line to exit:")
    
    with open(file_path, "w") as file:
        while True:
            line = input()
            if line.lower() == "quit":
                break
            file.write(line + "\n")

    return file_path

def git_push(filepath):
    try:
        subprocess.run(["git", "add", filepath], check=True)
        commit_message = "Entry for " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Journal entry pushed to GitHub.")
    except subprocess.CalledProcessError as e:
        print("Failed to push entry to GitHub:", e)

def ask_to_push_to_git():
    choice = input("Do you want to push this entry to GitHub? (yes/no): ")
    return choice.lower() in ["yes", "y"]

def main():
    folder = choose_folder()
    filepath = write_journal_entry(folder)

    if ask_to_push_to_git():
        git_push(filepath)
    else:
        print("Entry saved locally.")

if __name__ == "__main__":
    main()
