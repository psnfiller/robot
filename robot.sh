while true; do
curl 'http://robot:5000/motor?l=30&r=30'
sleep 1
curl 'http://robot:5000/motor?l=-30&r=-30'
sleep 1
done

