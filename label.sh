#/bin/bash

image=$1
output=${image/images/pt}
echo $image to $output
labelme $image --output $output --labels court,pole,ball,hit_player --flags court_occluded --nodata --autosave --labelflags "{court:[top_left, top_right, service_left, service_middle, service_right, middle_left, middle_middle, middle_right], pole:[left, right],, hit_player:[forehand, backhand]}"