from requests_html import HTMLSession
import argparse, time, os

parser = argparse.ArgumentParser(description='Fetch html.')
parser.add_argument('urls', type=str, nargs='+')
parser.add_argument('--metadata',action='store_true')

args = parser.parse_args()
print(args.urls)
if args.metadata:
    for u in args.urls:
        if os.path.exists(u + ".html"):
            y = time.localtime(os.stat(u + ".html").st_mtime)  
            ftime = time.strftime("%Y-%m-%d %H:%M:%S",y)
            with open(u + ".html") as f:
                content = f.read()
                links = content.count("<a ")
                imgs = content.count("<img ")
                print("site: " + u)
                print("num_links: " + str(links))
                print("images: " + str(imgs))
                print("last_fetch: " + ftime)
        else:
            print("Never fetch " + u)
else:
    for u in args.urls:
        # try:
            session = HTMLSession()
            r = session.get("https://" + u)
            with open(u + ".html", "w") as f:
                f.write(r.html.html)
        # except:
        #     print("Failed to fetch " + u)
# print(r.html.html)

# with open()