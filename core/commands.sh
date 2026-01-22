source "$BASE_DIR/core/config.sh"
source "$BASE_DIR/core/runner.sh"

save_commands() {
  TOOL="$1"
  DESC="$2"
  CMD="$3"

  if [ -z "$TOOL" ] || [ -z "$DESC" ] || [ -z "$CMD" ]; then
    echo "Usage: allin1 save <tool> \"desc\" \"command\""
    exit 1
  fi

  echo "$TOOL|$DESC|$CMD" >>"$COMMANDS_DB"
  echo -e "${GREEN}[+]${RESET} Command saved!"
}

list_commands() {
  require_command_db

  echo -e "${YELLOW}Saved Commands:${RESET}"
  while IFS='|' read -r TOOL DESC CMD; do
    echo "[$TOOL] $DESC"
  done <"$COMMANDS_DB"

  printf "\n${YELLOW}[?]${RESET} Do you want to delete a command? [Y/n] : "
  read delete

  case $delete in
  [Nn]*)
    printf "${YELLOW}Okay :)${RESET}"
    ;;
  *)
    printf "${YELLOW}[?]${RESET} Which command do you want to delete? <tool> : "
    read tool
    printf "${YELLOW}[?]${RESET} Which command do you want to delete? <keyword> : "
    read keyword

    if [ -z "$tool" ]; then
      echo -e "Enter a tool, e.g : nmap"
      continue
    elif [ -z "$keyword" ]; then
      echo -e "Enter a keyword, e.g : Basic scan"
      continue
    else
      sed -i "/${tool}\|${keyword}/d" $COMMANDS_DB
      printf "\n${RED}[-]${RESET} Command deleted succesfuly! "
    fi
    ;;
  esac
}

search_commands() {
  KEYWORD="$1"

  if [ -z "$KEYWORD" ]; then
    echo -e "${YELLOW}Usage${RESET}: allin1 search <keyword>"
    exit 1
  fi

  if [ ! -s "$COMMANDS_DB" ]; then
    echo -e "${RED}[!]${RESET} No commands saved yet"
    exit 0
  fi

  echo -e "${YELLOW}[*]${RESET} Search result for \"$KEYWORD\":"
  grep -i "$KEYWORD" "$COMMANDS_DB" | while IFS='|' read -r TOOL DESC CMD; do echo "[$TOOL] $DESC"; done
}
