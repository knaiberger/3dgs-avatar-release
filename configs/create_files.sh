declare -a images=("image" "foreground")
declare -a distorted=("distorted" "undistorted")
declare -a methods=("first" "average" "multiple" "calibrated")

for image in "${images[@]}"
    do
        for distort in "${distorted[@]}"
        do
            for method in "${methods[@]}"
            do
            	python create_file.py $method $image $distort
            done
        done
    done
