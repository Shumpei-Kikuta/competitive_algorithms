file=$1
num=$2

for ((i=1 ; i<$num+1 ; i++))
do
    poetry run python ${file} < tests/answer-${i}.txt
done
