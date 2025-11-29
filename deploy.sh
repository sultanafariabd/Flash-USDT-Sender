#!/bin/bash

set -euo pipefail
source "utils.sh"

# Function to get user's access key
get_access_key() {
    animate_text "What is your access key?"
    echo -n "Access Key: "
    read -s user_key
    echo
}

# Function to authenticate the user
authenticate_user() {
    if [ -z "$DEPLOY_ACCESS_KEY" ]; then
        echo -e "${RED}Error: DEPLOY_ACCESS_KEY environment variable not set.${NC}"
        exit 1
    fi

    if [ "$user_key" != "$DEPLOY_ACCESS_KEY" ]; then
        echo -e "${RED}Authentication failed.${NC}"
        exit 1
    fi

    echo -e "${GREEN}Authentication successful!${NC}"
}

# Function to ask for confirmation
confirm_deployment() {
    animate_text "Are you sure you want to proceed with the deployment? (y/n)"
    read -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${RED}Deployment cancelled.${NC}"
        exit 1
    fi
}

# Function to run build commands
run_build() {
    echo "Running build commands..."
    # Placeholder for build commands (e.g., npm run build)
}

# Function to sync files to the server
sync_files() {
    echo "Syncing files to the server..."
    # Placeholder for syncing files (e.g., rsync)
}

# Main function to run the deployment
main() {
    get_access_key
    authenticate_user
    confirm_deployment
    echo -e "${GREEN}Starting deployment...${NC}"
    run_build
    sync_files
    echo -e "${GREEN}Deployment successful!${NC}"
}

main
