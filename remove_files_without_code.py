"""
Script to remove documentation files that don't contain code blocks.
Files without triple backticks (```) will be removed from the docs folder.
"""

import os
import sys
from pathlib import Path


def has_code_blocks(file_path):
    """Check if a file contains code blocks (triple backticks)."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            return '```' in content
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return True  # Keep files we can't read to be safe


def remove_files_without_code(docs_folder="docs"):
    """Remove all files in docs folder that don't contain code blocks."""
    docs_path = Path(docs_folder)
    
    if not docs_path.exists():
        print(f"Error: Docs folder not found at: {docs_path.absolute()}")
        return
    
    if not docs_path.is_dir():
        print(f"Error: {docs_path.absolute()} is not a directory")
        return
    
    # Get all files in the docs folder and subfolders
    all_files = list(docs_path.rglob("*"))
    files = [f for f in all_files if f.is_file()]
    
    if not files:
        print("No files found in docs folder")
        return
    
    print(f"Scanning {len(files)} files in docs folder...")
    
    removed_count = 0
    kept_count = 0
    
    for file_path in files:
        try:
            if has_code_blocks(file_path):
                print(f"KEEP: {file_path.name} (contains code blocks)")
                kept_count += 1
            else:
                print(f"REMOVE: {file_path.name} (no code blocks found)")
                file_path.unlink()  # Remove the file
                removed_count += 1
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            kept_count += 1  # Count as kept since we couldn't remove it
    
    print(f"\nSummary:")
    print(f"- Files removed: {removed_count}")
    print(f"- Files kept: {kept_count}")
    print(f"- Total processed: {removed_count + kept_count}")


if __name__ == "__main__":
    # You can pass a different docs folder path as a command line argument
    docs_folder = sys.argv[1] if len(sys.argv) > 1 else "docs"
    
    print("Unity Docs Cleanup Script")
    print("=" * 30)
    print(f"Target folder: {Path(docs_folder).absolute()}")
    
    # Ask for confirmation
    response = input("\nThis will permanently delete files without code blocks. Continue? (y/N): ")
    if response.lower() in ['y', 'yes']:
        remove_files_without_code(docs_folder)
        print("\nCleanup completed!")
    else:
        print("Operation cancelled.")
