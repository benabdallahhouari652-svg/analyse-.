import os
import zipfile

EXCLUDE_DIRS = {
    'node_modules',
    'dist',
    '.git',
    '.aistudio',
    '__pycache__',
    'coverage',
    'build',
    '.temp'
}

EXCLUDE_FILES = {
    'create-project-zip.py',
    '.DS_Store',
    'analyse-dz-project.zip'
}

def make_zip(source_dir, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            # Prune excluded directories
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')]
            
            for file in files:
                if file in EXCLUDE_FILES or file.endswith('.pyc') or file.endswith('.log'):
                    continue
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, source_dir)
                zipf.write(full_path, rel_path)

if __name__ == '__main__':
    out = os.path.join('/public', 'analyse-dz-project.zip')
    make_zip('/', out)
    print("Created ZIP at:", out, "Size:", os.path.getsize(out), "bytes")
