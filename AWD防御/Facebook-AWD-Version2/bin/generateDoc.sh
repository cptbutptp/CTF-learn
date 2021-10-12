#!/bin/sh

#The script must be call from the root of the app
apigen generate -s $PWD/src -s $PWD/vendor/pop-code -s $PWD/vendor/facebook -d $PWD/docs 
#apigen generate -s $(dirname $PWD)/facebook-awd-connect/src -s $PWD/src -s $PWD/vendor/pop-code -s $PWD/vendor/facebook -d $PWD/docs 