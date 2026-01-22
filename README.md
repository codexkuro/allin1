# allin1

allin1 is a personal cybersecurity command management & automation CLI tool.
It helps you store, search, and execute frequently used security-related commands efficiently.

Built for cybersecurity learners, students, and practitioners who are tired of retyping the same commands.

## Features
- Save commands to a local database
- Run commands by keyword
- Avoid command collision
- Simple and lightweight CLI interface

## Installation
```bash
git clone https://github.com/codexkuro/allin1.git
cd allin1
chmod +x allin1
sudo ln -s $(pwd)/allin1 /usr/local/bin/allin1
```

## Usage
```bash
allin1 list
allin1 search nmap
allin1 save nmap "Basic nmap scan" "nmap -sC -sV target"
allin1 run nmap scan
```
## Version
v0.1 – Initial Release

## Author
Built by Akbar (@akbrsmh)

## Disclaimer
This tool is intended for educational and personal workflow purposes.
