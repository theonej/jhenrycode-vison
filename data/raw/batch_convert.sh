echo $PWD
export OUTPUT_PATH=../../../train/${TYPE}/${CLASS}
echo ${OUTPUT_PATH}
ls ${OUTPUT_PATH}

ls *.mp4 | xargs -i -n1 ffmpeg -i {} -vf fps=25 "${OUTPUT_PATH}/%06d.png"