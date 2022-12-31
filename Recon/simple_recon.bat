@echo off

echo Running nslookup...
nslookup www.localhost5000.com >> C:\Users\%Username%\Desktop\recon.txt

echo Running ping...
ping www.localhost5000.com >> C:\Users\%Username%\Desktop\recon.txt

echo Running tracert...
tracert www.localhost5000.com >> C:\Users\%Username%\Desktop\recon.txt

echo Downloading recon.txt from server...
curl -o C:\Users\%Username%\Desktop\recon.txt http://www.localhost5000.com/recon.txt

echo Done!
pause
