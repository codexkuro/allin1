#!/usr/bin/bash

# ========================
# App Info
# ========================
APP_NAME="allin1"
VERSION="v0.1"
DESCRIPTION="command memory tool for cybersecurity workflows"

# ========================
# Directory Structure
# ========================
CORE_DIR="$BASE_DIR/core"
DB_DIR="$BASE_DIR/db_sample"
DATA_DIR="$BASE_DIR/data"

# ========================
# Database Paths
# ========================
COMMANDS_DB="$DATA_DIR/commands.db"
PLACEHOLDERS_DB="$DATA_DIR/placeholders.db"

COMMANDS_SAMPLE_DB="$DB_DIR/commands.sample.db"
PLACEHOLDERS_SAMPLE_DB="$DB_DIR/placeholders.sample.db"

# ========================
# Colors
# ========================
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
CYAN="\033[36m"
BOLD_CYAN="\033[1;36m"
BOLD="\033[1m"
RESET="\033[0m"
