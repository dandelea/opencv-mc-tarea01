# opencv-mc-tarea01
Aplicación para la tarea 01 de MC (Matemática computacional) para el Máster de Ingeniería Informática de la Universidad de Sevilla.

##Instrucciones de instalación

* Actualizar las bases de datos de repositorios
 * sudo apt-get update
* Instalar herramientas para compilar OpenCV 3.0:
 * sudo apt-get install build-essential cmake git pkg-config
* Instalar herramientas para leer formatos de imagen:
 * sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev
* Instalar funcionalidades GUI de OpenCV 3.0:
 * sudo apt-get install libgtk2.0-dev
* Instalar paquetes para optimizar algunas funciones de OpenCV, como las operaciones con matrices:
 * sudo apt-get install libatlas-base-dev gfortran
* Instalar pip:
 * wget https://bootstrap.pypa.io/get-pip.py
 * sudo python3 get-pip.py
* Instalar herramientas de entornos virtuales de Python:
 * sudo pip3 install virtualenv virtualenvwrapper
* Configurar entorno virtual:
 * sudo nano ~/.bashrc
* Pegar las siguientes líneas de texto en el fichero:
 * export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
 * export WORKON_HOME=$HOME/.virtualenvs
 * source /usr/local/bin/virtualenvwrapper.sh
* Recargar el fichero de configuración:
 * source ~/.bashrc
* Instalar Python 3.4:
 * sudo apt-get install python3.4-dev
* Instalar numpy:
 * pip install numpy
* Descargar los repositorios de OpenCV:
 * cd ~
 * git clone https://github.com/Itseez/opencv.git
 * cd opencv
 * git checkout 3.0.0
 * cd ~
 * git clone https://github.com/Itseez/opencv_contrib.git
 * cd opencv_contrib
 * git checkout 3.0.0
* Construir OpenCV:
 * cd ~/opencv
 * mkdir build
 * cd build
 * cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_C_EXAMPLES=ON \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	-D BUILD_EXAMPLES=ON ..
 * <code>make -j4</code>
 * sudo make install
 * sudo ldconfig
* Copiar OpenCV a nuestro entorno virtual de trabajo:
 * cd ~/.virtualenvs/cv/lib/python3.4/site-packages/
 * ln -s /usr/local/lib/python3.4/site-packages/cv2.cpython-34m.so cv2.so
* Instalar Matplotlib para gráficas de histogramas:
 * cd ~
 * git clone https://github.com/matplotlib/matplotlib.git
 * cd matplotlib
 * python setup.py install

##Referencias
* Instalación de OpenCV
 * LÓPEZ QUINTERO, MANUEL IGNACIO. Install OpenCV on Ubuntu or Debian. http://milq.github.io/install-opencv-ubuntu-debian/ (Fecha de consulta: 16 de Febrero de 2016).
 * ROSEBROCK, ADRIAN: Install OpenCV 3.0 and Python 3.4+ on Ubuntu. http://www.pyimagesearch.com/2015/07/20/install-opencv-3-0-and-python-3-4-on-ubuntu/ (Fecha de consulta: 17 de Febrero de 2016).
* OpenCV y NodeJS
 * SitePoint.com. Build a Face Detection App Using Node.js and OpenCV. http://www.sitepoint.com/face-detection-nodejs-opencv/ (Fecha de consulta: 16 de Febrero de 2016).
 * JUN KIM, ESTHER. Real-time face detection using OpenCV, Node.js, and WebSockets. http://drejkim.com/blog/2014/12/02/real-time-face-detection-using-opencv-nodejs-and-websockets (Fecha de consulta: 16 de Febrero de 2016).
 * Github. Face detection Node OpenCV. https://github.com/drejkim/face-detection-node-opencv (Fecha de consulta: 16 de Febrero de 2016).
 * Github. Node-OpenCV. Docs http://peterbraden.github.io/node-opencv/ (Fecha de consulta: 16 de Febrero de 2016).
 * Github. Node-OpenCV. Repository. https://github.com/peterbraden/node-opencv (Fecha de consulta: 16 de Febrero de 2016).
* Documentación de OpenCV
 * OpenCV- Python tutorials. https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_tutorials.html (Fecha de consulta: 19 de Febrero de 2016).
 * OpenCV 3.0.0 documentación. http://docs.opencv.org/3.0.0/index.html (Fecha de consulta: 19 de Febrero de 2016).



## Desarrollado por:
* Daniel de los Reyes Leal
