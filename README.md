# Réentrainement de YOLO

- Cloner le repo : `git clone https://github.com/ofacklam/darknet`
- Executer le script de téléchargement du dataset : 
```
cd darknet/training
./get_coco_dataset.sh
```
- Compiler l'executable `darknet` avec :
```
cd ..
make
```
Si probleme de compilation, mettre a jour le path avec : `export PATH="/usr/local/cuda/bin:/usr/local/cuda/nvvm/bin:$PATH"`
- Lancer le réentrainement avec
```
./darknet detector train cfg/new_coco.data cfg/yolov3-tiny_custom.cfg <path/to/last/backup>
```
A priori le `<path/to/last/backup>` sera de la forme `training/backup/yolov3-tiny_custom.backup`. Pour commencer un nouveau réentrainement, on peut se contenter d'utiliser `training/yolov3-tiny.conv.15`


![Darknet Logo](http://pjreddie.com/media/files/darknet-black-small.png)

# Darknet #
Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.

For more information see the [Darknet project website](http://pjreddie.com/darknet).

For questions or issues please use the [Google Group](https://groups.google.com/forum/#!forum/darknet).
