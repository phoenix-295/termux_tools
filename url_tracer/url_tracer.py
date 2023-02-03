import requests
def main():
    url = input("Enter url: ")
    payload = {"url": url}
    r = requests.post("https://deref.link/deref", data=payload)
    result = r.json()
    print("Start url: ", result["start_url"])
    print("Final url: ", result["final_url"])
    print("Route log: ", result["route_log"])

if __name__ == "__main__":
    main()