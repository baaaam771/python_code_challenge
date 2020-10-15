import requests


urls = []


def test():
    Urls_box = input(
        "Welcome to IsItDown.py \nPlease write a URL or URLs you want to check. (seperated by comma)\n")

    Spilt_Urls = Urls_box.split(",")

    for url in Spilt_Urls:
        if "." not in url:
            print(f"{url} is not a VALID Url")
            return

    for url in Spilt_Urls:
        if 'https://' in url:
            url = url.strip()
            urls.append(url)
            # print("yes")
            # print(url)
        else:
            # print("no")
            url = url.strip()
            url = "https://"+url
            urls.append(url)
            # print(url)

    for url in urls:
        single_url = requests.get(url)

        if single_url.status_code == 200:
            print(f"{url} is up!")
        else:
            print(f"{url} is down!")

    # print(Spilt_Urls)
    # print(urls)

    check = input("Do you want to start over? y/n\n")

    if check == "y":
        # print("yes")
        # del urls
        test()
    else:
        print("bye")


test()
