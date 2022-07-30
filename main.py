import requests
from PIL import Image
import os
import shutil
from time import sleep

response = requests.get("https://fortnite-api.com/v2/cosmetics/br/new")
new = response.json()

print("GENERATE ALL NEW COSMETICS - (1)")
print("\nDELETE IMAGES FROM IMAGES FOLDER - (2)")
print("\nSEARCH COSMETICS BY SET NAME - (3)")


ask = input('>>> ')

if ask == "1":
    print(f"Getting {len(new['data']['items'])} cosmetic images...")
    status_code = response.status_code
    get_ver = response.json()['data']['build']
    if get_ver == get_ver:
        print("Latest Build Acquired!")
    else:
        print("Can't get the latest cosmetics!\n\nBuild is: "+get_ver+" (!!!) ")
    if status_code == 200:
        print("Retrieved.")

for i in new["data"]["items"]:
    if ask == "1":
        print("Loading Images From Cosmetic ID: "+i["id"])
        url = i["images"]["icon"]

        r = requests.get(url, allow_redirects=True)
        open(f'images/{i["id"]}.png', 'wb').write(r.content)
        iconImg = Image.open(f'images/{i["id"]}.png')
        sleep(0.1)  # dunno why
    elif ask == "2":
        print("DELETING IMAGES..")
        try:
            shutil.rmtree('images')
            os.makedirs('images')
            shutil.rmtree('setimages')
            os.makedirs('setimages')
        except:
            os.makedirs('images')
            os.makedirs('setimages')
        sleep(2)
        print("CLEARED IMAGES")
        exit()
    elif ask == "3":
        ask = input('(SET_NAME) >>> ')
        response = requests.get(
            f'https://fortnite-api.com/v2/cosmetics/br/search/all?set={ask}')
        sleep(1)
        status_code_num = response.json()['status']
        if status_code_num == 404:
            print("ITEM ERROR..")
            sleep(2)
            exit()
        new_cos = response.json()['data']

        print(f"SET GRABBED!\n\nGENERATING IMAGES FROM {ask}..")
        sleep(0.5)
        print(f"FOUND {len(new_cos)} COSMETICS....")

        for i in new_cos:
            print("GETTING IMAGES FOR COSMETIC ID: "+i["id"])
            url = i["images"]["icon"]

            r = requests.get(url, allow_redirects=True)
            open(f'setimages/{i["id"]}.png', 'wb').write(r.content)
            iconImg = Image.open(f'setimages/{i["id"]}.png')
            sleep(0.1)

close = input('EXIT : ')
if close == "":
    exit()
#status_code = r.status_code
# print(r.text)


# if status_code == 200:
#    print("Sucess!")
# else:
#    print("Something went wrong.") # uhh yeah............................................................................. anyways
