# Craxsrat-IP-Extractor
Python script to extract C2 IP from CraxsRAT's client APK

## Requirements
- **Python 3.x**: Ensure Python 3.x is installed on your system.
- **JADX command line**: The script relies on JADX to decompile APK files. You need to download and install JADX from its [GitHub repository](https://github.com/skylot/jadx). Make sure it's added to your system's PATH.

## Usage
```bash
$ git clone https://github.com/fareedfauzi/craxsrat-ip-extractor.git
$ cd craxsrat-ip-extractor
$ python3 craxsrat_ip_extractor.py /path/to/apk/folder
```

- I've placed 3 samples in the `apks` folder for testing.

## Expected output
```
remnux@siftworkstation: ~/work
$ python3 craxsrat_ip_extractor.py apks/
Processing apks/test2.apk
[*] Decompiling APK...
[*] Finding the C2 IP Address...
[79e19ea25071787899ca633812570dfc]: 202.55.133.59

Processing apks/test1.apk
[*] Decompiling APK...
[*] Finding the C2 IP Address...
[7da41e25ccdfa60ef992a9c4846e6a6b]: 192.168.5.143

Processing apks/test3.apk
[*] Decompiling APK...
[*] Finding the C2 IP Address...
[1ddc5fcd0042926c149971122f0cecbe]: seyo111.hopto.org
```
