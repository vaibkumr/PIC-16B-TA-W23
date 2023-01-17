x=1
while [ $x -le 5 ]
do
  echo "Hi $x times"
  x=$(( $x + 1 ))
done