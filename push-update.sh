#!/data/data/com.termux/files/usr/bin/bash

# === CONFIGURATION ===
REPO_URL="https://github.com/RicoDEVOfficial/ELBS-V30"
CLONE_DIR="$HOME/elbs_temp_repo"
SOURCE_DIR="/storage/emulated/0/Download/elbs-upd"
BRANCH="main"
GIT_NAME="RicoDEV"
GIT_EMAIL="trmods050@gmail.com"

echo "[*] Cleaning up old clone..."
rm -rf "$CLONE_DIR"

echo "[*] Cloning from GitHub..."
git clone --branch "$BRANCH" "$REPO_URL" "$CLONE_DIR" || {
    echo "[!] Failed to clone repo"
    exit 1
}

cd "$CLONE_DIR" || {
    echo "[!] Failed to cd into repo"
    exit 1
}

echo "[*] Removing everything except .git..."
shopt -s extglob
rm -rf !(.git)

echo "[*] Copying updated files into clone..."
cp -r "$SOURCE_DIR"/* "$CLONE_DIR"/

# Confirm files copied
echo "[*] Files now in repo directory:"
ls -al "$CLONE_DIR"

echo "[*] Git config..."
git config user.name "$GIT_NAME"
git config user.email "$GIT_EMAIL"

echo "[*] Adding all changes to git..."
git add -A

echo "[*] Checking for changes to commit..."
if git diff --cached --quiet; then
    echo "[!] Nothing to commit. Are the files identical?"
    exit 1
else
    echo "[*] Committing..."
    git commit -m "Auto update: $(date)"
    echo "[*] Pushing..."
    git push origin "$BRANCH" && echo "[✓] Pushed!"
fi