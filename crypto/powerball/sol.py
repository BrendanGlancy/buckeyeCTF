import requests

url = "https://powerball.chall.pwnoh.io/"

def main():
    # get the javascript output from the website
    r = requests.get(url)
    # get the console output from the website
    console = r.text.split("console.log(")[1].split(");")[0]
    print(console)

if __name__ == "__main__":
    main()
