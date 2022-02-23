# co2

Quicky script to render measurements from a CO2 sensor onto a small OLED screen via an Raspberry Pi. Detailed writeup [here](https://koljapluemer.com/2021/11/26/ll-co2.html)

## Setup

Do not use `venv`, it only introduces problems. Do `sudo apt update` and `sudo apt upgrade -y` first. 
Always call pip indirectly, like `sudo -H python3 -m pip install $FOO`.

Follow the specific instructions for `luma` and `numpy`, if problems arise.

## Next Up

* Reassemble the setup
* Consider switching to Arduino
* Add temperature and moisture sensors?
