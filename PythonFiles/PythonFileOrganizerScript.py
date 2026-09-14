from pathlib import Path
import shutil
import time

# Step 1 mapping extensions to folder names
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".avif"],  # Added .avif
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm"],
    "Data": [".csv", ".json", ".xml"],
    "Apps": [".apk"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".mpeg"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".json", ".xml", ".yaml", ".ts", ".prisma"],  # Added .ts, .prisma
    "Config": [".cfg", ".ini", ".webmanifest"],
    "Subtitles": [".srt"],
    "Executables": [".exe", ".msi", ".app", ".deb", ".rpm"],
    "Others": []
}

# Step 2: The organizing function with error handling
def organize(folder_path, folders):
    if not folder_path.exists():
        print("Folder path doesn't exist")
        return
    
    moved_count = 0
    skipped_count = 0
    error_count = 0
    
    for file in folder_path.iterdir():
        if file.is_dir():
            continue
        
        moved = False
        for folder_name, extensions in folders.items():
            if file.suffix.lower() in extensions:
                target = folder_path / folder_name
                target.mkdir(exist_ok=True)
                
                try:
                    shutil.move(str(file), str(target / file.name))
                    print(f"Moved {file.name} to folder {folder_name}")
                    moved = True
                    moved_count += 1
                except PermissionError:
                    print(f"⚠️ SKIPPED: {file.name} - File is in use by another program")
                    error_count += 1
                    moved = True  # Mark as handled so it doesn't show as "No matching folder"
                except Exception as e:
                    print(f"❌ ERROR moving {file.name}: {e}")
                    error_count += 1
                    moved = True
                break
        
        if not moved:
            print(f"Skipped {file.name} (No matching folder)")
            skipped_count += 1
    
    # Summary
    print("\n" + "="*50)
    print("📊 ORGANIZATION SUMMARY")
    print("="*50)
    print(f"✅ Files successfully moved: {moved_count}")
    print(f"⚠️ Files skipped (in use): {error_count}")
    print(f"📝 Files with no matching folder: {skipped_count}")
    print("="*50)

# Confirm before running
print("⚠️ This will organize ALL files in your Downloads folder!")
print("Make sure to CLOSE all open files (Word, Excel, PDFs, etc.)")
print("Files that are open will be skipped.")
print()
response = input("Continue? (yes/no): ")

if response.lower() in ['yes', 'y']:
    folder_path = Path("C:/Users/Administrator/Downloads")
    organize(folder_path, folders)
    print("\n✅ Done!")
else:
    print("❌ Cancelled by user")