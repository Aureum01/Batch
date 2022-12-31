import requests
from bs4 import BeautifulSoup
import nmap

def recon(url):
    # Make an HTTP request to the website
    r = requests.get(url)
    
    # Parse the HTML or XML document
    soup = BeautifulSoup(r.text, "html.parser")
    
    # Extract information from the document
    title = soup.title.string
    links = [a['href'] for a in soup.find_all('a', href=True)]
    
    # Print the results
    print("Title:", title)
    print("Links:", links)
    
    # Perform port scanning and vulnerability assessment
    nm = nmap.PortScanner()
    nm.scan(url, '1-1024')
    for host in nm.all_hosts():
        print("Host:", host)
        print("State:", nm[host].state())
        for proto in nm[host].all_protocols():
            print("Protocol:", proto)
            lport = nm[host][proto].keys()
            lport.sort()
            for port in lport:
                print("Port:", port)
                print("State:", nm[host][proto][port]['state'])

# Perform reconnaissance on the website "www.example.com"
recon("https://google-gruyere.appspot.com/part1")

# To use this batch file, you will need to save it with a .bat file extension and then run it in the Command Prompt by typing the name of the batch file and pressing Enter. The batch file will execute the Python script and display the results on the screen.
