import requests


site = input("Site Listesinin Adını Girin: ")

with open(site,"r") as dosya:

    sites = dosya.readlines()

    for i in sites:

        i = i.strip()        
        try:
            r = requests.get(i)

            if(r.status_code==200):
                print(r.status_code,i)
                with open("List.txt","a") as file:
                    file.write(i)
                    file.write("\n")

            else:
                print(r.status_code,i)
                pass

        except:
            pass
