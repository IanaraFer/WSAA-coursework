import os
from git import Repo, GitCommandError

# Define repository information
repository_path = r"C:\path\to\your\local\repository"  # Replace with the actual path to your local repository
file_to_edit = "file.txt"  # Replace with the file name
old_text = "Ianara"
new_text = "NEW_TEXT"  # Replace with the new text

print(f"Repository Path: {repository_path}")
print(f"File to Edit: {file_to_edit}")
print(f"Old Text: {old_text}, New Text: {new_text}")

try:
    # Initialize the repository
    repo = Repo(repository_path)

    if repo.bare:
        raise Exception("The repository path is invalid or empty.")

    # Construct the file path
    file_path = os.path.join(repository_path, file_to_edit)

    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        raise FileNotFoundError(f"The file '{file_to_edit}' does not exist in the repository.")

    # Read, modify, and save the file
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    updated_content = content.replace(old_text, new_text)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(updated_content)

    # Stage the changes
    repo.index.add([file_path])

    # Commit the changes
    commit_message = f"Replaced all instances of '{old_text}' with '{new_text}'"
    repo.index.commit(commit_message)

    # Push the changes
    try:
        origin = repo.remote(name="origin")
        print("Pushing changes to the remote repository...")
        push_result = origin.push()
        for result in push_result:
            if result.flags & result.ERROR:
                raise GitCommandError(f"Push failed: {result.summary}")
        print("Changes committed and pushed successfully.")
    except GitCommandError as e:
        print(f"Failed to push changes: {e}")
        print("Ensure you have the correct permissions and that the remote repository is accessible.")

except Exception as e:
    print(f"An error occurred: {e}")