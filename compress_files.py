import gzip
import shutil
import os

def compress_file(input_file):
    with open(input_file, 'rb') as f_in:
        with gzip.open(input_file + '.gz', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

files_to_compress = [
    'index.html',
    'login.html',
    'contact-us.html',
    'product-list.html',
    'shop.html',
    'signup.html',
    'assets/css/all.min.css',
    'assets/css/animate.css',
    'assets/css/animate.min.css',
    'assets/css/bootstrap.min.css',
    'assets/css/style.css',
    'assets/css/style.min.css',
    'assets/js/bootstrap.min.js',
    'assets/js/javascript.js',
    'assets/js/javascript.min.js',
]

for file in files_to_compress:
    if os.path.exists(file):
        compress_file(file)
        # Optionally replace the original files
        os.remove(file)
        os.rename(file + '.gz', file)
    else:
        print(f"File not found: {file}")

print("Files compressed successfully")
