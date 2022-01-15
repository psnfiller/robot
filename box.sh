x=0.9
while true; do
curl 'http://robot:5000/motor?l=30&r=30'
sleep 2
curl 'http://robot:5000/motor?l=30&r=-30'
sleep $x
done

