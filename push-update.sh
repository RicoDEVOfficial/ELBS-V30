#!/bin/bash

# Local repo path
REPO_PATH="$HOME/ELBS-V30"

# Update source
UPDATE_PATH="/storage/emulated/0/Download/elbs-upd"

# Check repo exists
if [ ! -d "$REPO_PATH" ]; then
    echo "Cloning ELBS-V30 since it's missing..."
    git clone https://github.com/RicoDEVOfficial/ELBS-V30.git "$REPO_PATH"
fi

# Move to repo
cd "$REPO_PATH" || exit

# Remove all except .git
echo "Cleaning old files (except .git)..."
find . -mindepth 1 -not -path "./.git*" -exec rm -rf {} +

# Copy new files
echo "Copying update from $UPDATE_PATH..."
cp -r "$UPDATE_PATH"/* .

# Stage, commit, and push
echo "Committing changes..."
git add .
git commit -m "big update"
git push

echo "Update pushed successfully."