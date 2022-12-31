@echo off

echo Running nbtstat...
nbtstat -n >> C:\Users\%USERNAME%\Desktop\recon.txt

echo Running netstat...
netstat -nao >> C:\Users\%USERNAME%\Desktop\recon.txt

echo Running route...
route print >> C:\Users\%USERNAME%\Desktop\recon.txt

echo Done!
pause
