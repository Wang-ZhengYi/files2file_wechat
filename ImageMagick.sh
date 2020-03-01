wget -c https://www.imagemagick.org/download/ImageMagick.tar.gz
tar -xzvf ImageMagick-7.0.8-15
cd ImageMagick-7.0.8-15
./configure
make && make install
vim /etc/profile
# export ImageMagick_HOME=/usr/local/ImageMagick
# export PATH=$PATH:$ImageMagick_HOME/bin