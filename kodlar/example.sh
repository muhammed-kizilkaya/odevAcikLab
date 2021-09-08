echo "$USER"

echo "Benim adım"
if [[ "$(whoami)" != "any_name" ]]; then
  
  exit 1
fi
