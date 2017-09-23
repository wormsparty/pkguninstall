#!/usr/bin/env python3

import os
import sys
import argparse
import subprocess
import tkinter

# To uninstall, we need to be root.
#if not os.geteuid() == 0:
 #   print("This script must be run as root")
  #  sys.exit(1)

# First create the window
window = tkinter.Tk()

# Let's construct the list which will contain all packages we can uninstall
list = tkinter.Listbox(window)

# Let's list the packages
pkgutil = subprocess.Popen(('pkgutil', '--pkgs'), stdout=subprocess.PIPE)
output = subprocess.check_output(('grep', '-v', '^com.apple.'), stdin=pkgutil.stdout)

# We now fill the list
i = 1

for o in output.splitlines():
    list.insert(i, o)
    i += 1

list.pack()

window.mainloop()

'''
# List the packages to uninstall according to the script arguments.
# Note that we do not make any restrictions here and can
# remove Apple packages if asked to!
for package in args.packages:
    try:
        output = subprocess.check_output(['pkgutil', '--pkgs=' + package])
        packages.append(output)
    except subprocess.CalledProcessError:
        print('No matching package found for: ' + package)


def remove_file(f):
    if os.path.exists(f) and not os.path.isdir(f):
        os.remove(f)

    try:
        os.removedirs(os.path.dirname(f))
    except OSError:
        pass


def uninstall_package(pkg):
    info = subprocess.check_output(['pkgutil', '--pkg-info', pkg])
    location = info.splitlines()[3][10:]

    if not location.startswith('/'):
        location = '/' + location

    # We only to remove duplicated slashes when showing the files to the user
    # The filesystem doesn't care
    if location.endswith('/'):
        location = location[:-1]

    print("I'll be removing the following files:\n")

    files = subprocess.check_output(['pkgutil', '--files', pkg]).splitlines()

    for f in files:
        print(location + '/' + f)

    sys.stdout.write("\nProceed? This cannot be undone. (y/N) ")
    yesno = input().lower()

    if not yesno == 'y':
        return

    for f in files:
        remove_file(location + '/' + f)

    subprocess.check_output(['pkgutil', '--forget', pkg])


for package in packages:
    for p in package.splitlines():
        sys.stdout.write("Uninstall " + p + " ? (y/N) ")
        choice = raw_input().lower()

        if choice == 'y':
            uninstall_package(p)
            
'''