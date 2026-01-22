source "$BASE_DIR/core/config.sh"
source "$BASE_DIR/core/db_functions.sh"
# source "$BASE_DIR/.db/placeholders.db"
# Functions
require_command_db() {
  if [ ! -s "$COMMANDS_DB" ]; then
    echo -e "${RED}[!]${RESET} No commands saved yet."
    exit 0
  fi
}

run_command() {
  local TOOL="$1"
  local KEYWORD="$2"

  # Check if tool exist or not
  if [ -z "$TOOL" ]; then
    echo "Usage: allin1 run <tool> \"keyword\""
    exit 1
  fi

  # Check if commands database exist or not
  require_command_db

  # Find tool in database
  MATCH=$(grep -i "^$TOOL|.*$KEYWORD" "$COMMANDS_DB")

  # Check if tool found or not
  if [ -z "$MATCH" ]; then
    echo -e "${RED}[!]${RESET} Tool not found: $TOOL"
    exit 1
  fi

  # Separate from database
  IFS="|" read -r T D CMD <<<"$MATCH"

  # Tool informations
  echo -e "${YELLOW}[*]${RESET} Description: $D"
  echo -e "${YELLOW}[*]${RESET} Command: $CMD"

  # Initialize database if not exists
  if ! db_exists; then
    init_db
  fi

  # Extract all placeholders from commands
  placeholders=$(extract_placeholders "$CMD")

  if [ -n "$placeholders" ]; then
    echo -e "${YELLOW}[*]${RESET} Found placeholders: $placeholders"

    # Process each placeholders
    for placeholder in $placeholders; do
      echo ""
      echo -e "${YELLOW}===${RESET} Processing placeholder: {$placeholder} ${YELLOW}===${RESET}"

      saved_value=$(db_get "$placeholder")

      if [ -n "$saved_value" ]; then
        echo -e "${GREEN}[+]${RESET} From database: $saved_value"
        read -p "   Use this? [Y/n/new]: " choice

        case $choice in
        [Nn]*)
          echo "   Skipping {$placeholder}"
          continue
          ;;
        [Nn][Ee][Ww]*)
          read -p "   Enter new value: " value
          db_save "$placeholder" "$value"
          ;;
        *)
          value="$saved_value"
          ;;
        esac
      else
        # not exists
        read -p "   Enter value for {$placeholder}: " value
        read -p "   Save it for later? [Y/n]: " save

        if [[ ! $save =~ ^[Nn]$ ]]; then
          db_save "$placeholder" "$value"
        fi
      fi

      # Replace placeholders with value
      CMD="${CMD//\{$placeholder\}/$value}"
    done
    echo ""
    echo -e "${GREEN}[+]${RESET} Final command:"
    echo "    $CMD"
  else
    echo -e "${YELLOW}[*]${RESET} No placeholders found"
  fi

  # Execute Command
  printf "\n%b[!]%b Execute command? [Y/n]: " "$RED" "$RESET"
  read execute
  if [[ ! $execute =~ ^[Nn]$ ]]; then
    echo -e "${YELLOW}[*]${RESET} Executing...\n"
    bash -c "$CMD"
  else
    echo -e "${YELLOW}[*]${RESET} Command not executed"
  fi

}
