import os

def rename_files(mypath):
    files = []
    for x in os.walk(mypath):
        print x
        files.extend(x[2])
        break
    print 'Files: ', files

    for this_file in files:
        if str(this_file).lower().find(".mp3") != -1:
            fname = str(this_file)[:str(this_file).rfind(".")]
            res = ''
            for ch in fname:
                if ch.find(' ') == 0 or ch.isalpha():
                    res = res + str(ch)
            res = res.lower()
            remove_str_list = [
                "wwwmpmadcom",  "downloadmingse", "kbps", "songsmpcom", "freshmazainfo", "downloadmingse",
                "songsmpcom", "mympsongcom", "wwwdjmazacom", "songsmpcom", "songspkain", "wwwmpmadcom",
                "songspksongspkscom", "vipmusicin", "pagalworldcom", "wwwsudwapcom"
            ]
            for strr in remove_str_list:
                res = res.replace(strr, "")
            print res

            res = res.title()
            res = res.strip()
            # print res
            os.rename(mypath + this_file, mypath+res+'.mp3')

mypath = 'D:\harsh data\mp3'+os.sep
rename_files(mypath)
