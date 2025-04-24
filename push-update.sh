#!/data/data/com.termux/files/usr/bin/bash

# === CONFIGURATION ===
REPO_URL="https://github.com/RicoDEVOfficial/ELBS-V30"
CLONE_DIR="$HOME/elbs_temp_repo"
SOURCE_DIR="/storage/emulated/0/Download/elbs-upd"
BRANCH="main"
GIT_NAME="RicoDEV"
GIT_EMAIL="trmods050@gmail.com"

# === SETUP FUNCTIONS ===
check_error() {
    if [ $? -ne 0 ]; then
        echo "[!] ERROR: $1"
        exit 1
    fi
}

# === EXECUTION ===
echo "[*] Starting update process..."

# Check if source directory exists and has content
if [ ! -d "$SOURCE_DIR" ]; then
    echo "[!] Source directory doesn't exist: $SOURCE_DIR"
    exit 1
fi

if [ -z "$(ls -A "$SOURCE_DIR" 2>/dev/null)" ]; then
    echo "[!] Source directory is empty: $SOURCE_DIR"
    exit 1
fi

echo "[*] Source directory exists and contains files."

# Clean any previous temp directory
echo "[*] Cleaning up old clone..."
rm -rf "$CLONE_DIR"

# Clone the repo
echo "[*] Cloning from GitHub..."
git clone --branch "$BRANCH" "$REPO_URL" "$CLONE_DIR"
check_error "Failed to clone repository"

# Change to repo directory
cd "$CLONE_DIR"
check_error "Failed to change to repository directory"

# Set up git credentials
echo "[*] Setting up git configuration..."
git config user.name "$GIT_NAME"
git config user.email "$GIT_EMAIL"

# Store original repo state (to check differences later)
echo "[*] Taking inventory of original repo content..."
find . -type f -not -path "./.git/*" | sort > /tmp/before_files.txt

# Remove everything except .git
echo "[*] Removing existing files (except .git)..."
find . -mindepth 1 -maxdepth 1 -not -name ".git" -exec rm -rf {} \;

# Copy new content
echo "[*] Copying updated files into repository..."
cp -r "$SOURCE_DIR"/* "$CLONE_DIR"/
check_error "Failed to copy new files"

# Check if files were copied
echo "[*] Verifying files were copied..."
if [ -z "$(ls -A "$CLONE_DIR" 2>/dev/null | grep -v "^\.git$")" ]; then
    echo "[!] No files were copied to the repository"
    exit 1
fi

# List copied files (for verification)
echo "[*] Files now in repository:"
find . -type f -not -path "./.git/*" | sort > /tmp/after_files.txt
cat /tmp/after_files.txt

# Add all changes
echo "[*] Adding all changes to git..."
git add -A
check_error "Failed to add files to git"

# Check if there are actual changes
echo "[*] Checking for changes to commit..."
if git diff --cached --quiet; then
    echo "[!] Nothing to commit. Files may be identical to what's already in the repository."
    exit 1
else
    # Count changes for confirmation
    ADDED=$(git diff --cached --numstat | wc -l)
    echo "[*] Detected $ADDED changed files."
    
    # Commit changes
    echo "[*] Committing changes..."
    COMMIT_MSG="Auto update: $(date) - $ADDED files changed"
    git commit -m "$COMMIT_MSG"
    check_error "Failed to commit changes"
    
    # Push with verbose output
    echo "[*] Pushing changes to GitHub..."
    git push -v origin "$BRANCH"
    check_error "Failed to push changes"
    
    # Verify the push
    echo "[*] Verifying push was successful..."
    git fetch origin
    check_error "Failed to fetch latest from origin"
    
    LOCAL=$(git rev-parse HEAD)
    REMOTE=$(git rev-parse origin/$BRANCH)
    
    if [ "$LOCAL" = "$REMOTE" ]; then
        echo "[✓] SUCCESS: Changes successfully pushed to GitHub!"
        echo "[*] Commit hash: $LOCAL"
        echo "[*] Commit message: $COMMIT_MSG"
    else
        echo "[!] ERROR: Local and remote hashes don't match."
        echo "[*] Local: $LOCAL"
        echo "[*] Remote: $REMOTE"
        exit 1
    fi
fi

# Cleanup
echo "[*] Cleaning up..."
cd "$HOME"
rm -rf "$CLONE_DIR"
echo "[*] Done!"