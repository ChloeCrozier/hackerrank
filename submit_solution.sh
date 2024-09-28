if [ -z "$1" ]; then
  echo "Error: No commit message provided."
  echo "Usage: ./submit_solution.sh \"Your commit message here\""
  exit 1
fi

./update_readme.sh
git pull
git add .
git commit -m "$1"
git push
