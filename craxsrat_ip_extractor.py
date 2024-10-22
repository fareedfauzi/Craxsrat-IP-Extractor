import sys
import os
import subprocess
import tempfile
import base64
import glob
import hashlib

def check_jadx_installed():
    try:
        subprocess.run(['jadx', '-v'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print("Error: 'jadx' is not installed or not found in your PATH.")
        print("Please install jadx from https://github.com/skylot/jadx before running this script.")
        sys.exit(1)

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def extract_ips_from_apk(apk_path):
    md5_hash = calculate_md5(apk_path)
    print(f"Processing {apk_path}")
    
    print("[*] Decompiling APK...")
    with tempfile.TemporaryDirectory() as temp_dir:
        result = subprocess.run(['jadx', '--no-res', '-d', temp_dir, apk_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode != 0:
            return
        
        print("[*] Finding the C2 IP Address...")
        java_files = glob.glob(os.path.join(temp_dir, '**', '*.java'), recursive=True)
        for file_path in java_files:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    if 'public static String ClientHost' in line and '=' in line and '"' in line:
                        parts = line.split('=')
                        if len(parts) >= 2:
                            base64_string = parts[1].split('"')[1]
                            padded_string = base64_string + '=' * (-len(base64_string) % 4)
                            try:
                                decoded_ip = base64.b64decode(padded_string).decode('utf-8')
                                print(f"[{md5_hash}]: {decoded_ip}\n")
                            except:
                                continue

def main():
    check_jadx_installed()

    if len(sys.argv) != 2:
        print('Usage: python craxsrat_ip_extractor.py /path/to/apk/folder')
        sys.exit(1)
    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print('Invalid directory path')
        sys.exit(1)
    
    # Collect all files in the folder
    files = glob.glob(os.path.join(folder_path, '*'))

    for file_path in files:
        extract_ips_from_apk(file_path)

if __name__ == '__main__':
    main()
