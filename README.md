# mPower
Control mPower Pro Units
Has been tested succesfully on mFi v2.1.8

Python Code to connect to mPower unit and either turn on, or off, a a port


#Usage

Run 'python setup.py install' to import the modules

OR

run "python mpower.py x y z'

Where x would be the host ip, y is the port # to change, and z is 'up' or 'down'.  

#Example

>python mpower.py 127.0.0.1 2 up

Change the status of 2 on host 127.0.0.1 to up

