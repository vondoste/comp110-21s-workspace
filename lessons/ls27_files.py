import os

def traverse(path: str) -> None:
    # Base Case
    if os.path.isfile(path):
        print(f"file: {path}")
    else:
        # Recursive Case
        # When path refers to a directory name
        print(f"dir: {path}")
        for child_path in os.listdir(path):
            traverse(os.path.join(path, child_path))


traverse("exercises")