$TREE = tree /f . | select-object -skip 2
$TREE[0] -match '[^\\]*$|^[A-Z](?=:\\$)'
$TREE[0] = $Matches.0
$DIRNAME = $TREE[0]
$FILENAME = "dirlist-$DIRNAME.txt"
foreach($ITEM in $TREE) {
	$CLEANITEM = $ITEM -replace '[\u2500-\u25FF]', ' '
	echo "$CLEANITEM" | out-file -append $FILENAME
}
