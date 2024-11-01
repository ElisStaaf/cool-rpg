if [ -x /usr/bin/make ]; then
    sudo make install
elif [ -x /usr/bin/docker ]; then
    docker build rpg
else
    chmod +x rpg.py
    mv rpg.py /usr/bin/rpg
