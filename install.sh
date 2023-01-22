#!/bin/bash

echo "DONT DO THIS UNLESS JAKE IS THERE!!!"
echo ""
echo "hello user (immaculata)"
echo "this is the install script for mac os "
echo "this script will install all the dependencies for JJ (jokey jerry)"
echo "this script will also install the required python packages"
echo ""
echo "list of dependencies:"
echo "python3"
echo "python3-pip"
echo ""
echo "list of python packages:"
echo "discord"
echo "rich"
echo "datetime"
echo "random"
echo ""
echo "would you like to install these dependencies and packages? (Y/n)"
read -r answer


if [ "$answer" == "Y" ] || [ "$answer" == "y" ] || [ "$answer" == "yes" ] || [ "$answer" == "Yes" ] || [ "$answer" == "YES" ];
then
    echo "installing dependencies"
    brew install python3
    brew install python3-pip
    echo "installing python packages"
    pip3 install discord
    pip3 install rich
    pip3 install datetime
    echo "done"
    echo "you can now run the start.sh script"
    echo "if you need help then tell jake!!"
else
    echo "well then"
    echo "you can install the dependencies and packages manually"
    echo "or you can run the start.sh script but that will throw errors"
    echo "goodbye"
    exit
fi