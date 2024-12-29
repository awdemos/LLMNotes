sudo apt remove dkms
sudo apt install linux-headers-6.1.0-26-arm64
sudo apt install dkms

sudo apt install build-essential dkms libncurses-dev bison flex libssl-dev libelf-dev

sudo apt install libgpiod-dev libyaml-cpp-dev libbluetooth-dev

sudo apt install openssl libssl-dev libulfius-dev liborcania-dev

wget https://github.com/meshtastic/firmware/releases/download/v2.5.7.f77c87d/meshtasticd_2.5.7.f77c87d_arm64.deb
mkdir meshtastic
cd meshtastic
sudo apt install ../meshtasticd_2.5.7.f77c87d_arm64.deb
sudo systemctl start meshtasticd
sudo systemctl status meshtasticd
