#!/bin/bash
echo -n "Do you want to install me? [y/n]: "
read -r answer
if [[ "${answer,,}" -eq "y" ]]; then
    echo "Installed the package successfully!"
else
    echo "Cancelled installing the package!"
fi 