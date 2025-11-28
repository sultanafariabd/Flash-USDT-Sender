#!/bin/bash

# Define colors
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function for animated text
animate_text() {
    local text="$1"
    for (( i=0; i<${#text}; i++ )); do
        echo -n "${text:$i:1}"
        sleep 0.05
    done
    echo
}

# --- Access Key Prompt ---
animate_text "What is your access key?"
echo -n "Access Key: "
read -s user_key
echo

# Read access key from environment variable
if [ -z "$DEPLOY_ACCESS_KEY" ]; then
    echo -e "${RED}Error: DEPLOY_ACCESS_KEY environment variable not set.${NC}"
    exit 1
fi

if [ "$user_key" != "$DEPLOY_ACCESS_KEY" ]; then
    echo -e "${RED}Authentication failed.${NC}"
    exit 1
fi

echo -e "${GREEN}Authentication successful!${NC}"
# --- End of Access Key Prompt ---


# Start of the deployment script
echo -e "${GREEN}Starting deployment...${NC}"

# Placeholder for build commands
echo "Running build commands..."
# npm run build or similar

# Placeholder for syncing files to server
echo "Syncing files to the server..."
# rsync -avz dist/ user@host:/path/to/your/project/

echo -e "${GREEN}Deployment successful!${NC}"
