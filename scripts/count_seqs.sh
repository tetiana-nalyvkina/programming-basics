file=$1
n=$(grep -c ">" "$file")
m=$(grep -v ">" "$file" | grep -ic "atg")
echo "file $file contains $n sequences, $m of which contain the start codon 'atg'"
