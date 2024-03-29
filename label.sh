#/bin/bash

image=$1
output=${image/images/pt}
echo $image to $output
labelme $image --output $output --labels court,ball,hit_player --flags occluded,hit,turn --nodata --autosave --labelflags "{.*: [occluded], hit_player:[forehand, backhand]}"