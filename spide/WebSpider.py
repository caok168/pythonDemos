
import re
import os
import requests
from threading import Thread


# get person list
def get_person_list(person_list_file):
    person_list = []
    with open(person_list_file, 'r', encoding = 'utf-8') as f:
        for person_name in f.readlines():
            person_list.append(person_name.strip())
    return person_list


# get url of person's picture
def get_pic_url(page_url, person):
    url_dict = {}
    page = 0
    for i in range(1000):    # number of page url
        page += 1
        r = requests.get(page_url)

        # get url of the picture
        pic_url = re.findall('"objURL":"(.+?)",', r.text, re.S)
        if pic_url:
            for url1 in pic_url:
                if url1 in url_dict.keys():
                    url_dict[url1] += 1
                else:
                    url_dict[url1] = 1
        else:
            print("%s的第%d个下载页面URL获取到的图片下载url为空" % (person, page))

        # get next page URL of the person
        reg = r'href="(.+?)" class="n">ä¸ä¸é¡µ</a>'
        re_obj = re.compile(reg)
        url_part = re_obj.findall(r.text)
        if not url_part:
            print("%s的图片url获取完毕！" % person)
            break
        page_url = r"http://image.baidu.com" + url_part[0]

    return list(url_dict.keys())


# save url of the picture
def save_url(url_file_path, person, url_list):
    if os.path.exists(url_file_path):
        os.remove(url_file_path)
    with open(url_file_path, 'w') as f:
        for i in range(len(url_list)):
            f.write(person + "_%06d"%(i + 1) + ' ' + url_list[i] + '\n')


# download picture
def download_pic(pic_url_file, pic_path, person):
    pic_num = 0
    with open(pic_url_file, 'r') as f:
        for line in f.readlines():
            pic_num += 1
            print("正在下载%s的第%d张图片..." % (person, pic_num))
            line = line.strip()
            cont_list = line.split()
            try:
                pic = requests.get(cont_list[1], timeout = 10)
            except Exception as e:
                print(e)
                continue

            # save picture
            pic_name = pic_path + '/' + cont_list[0] + ".jpg"
            with open(pic_name, 'wb') as f:
                f.write(pic.content)

    print("%s的图片下载结束！" % person)


def main():
    # get person name
    person_path = "/home/ck/images/"
    person_name_file = person_path + r"person_list.txt"
    person_list = get_person_list(person_name_file)
    person_num = 0

    t_list = []
    for person in person_list:
        person_num += 1
        pic_path = person_path + person
        url_file = pic_path + '/' + person + "_url.txt"
        if not os.path.exists(pic_path):
            os.mkdir(pic_path)

        # get the first page url of the person
        url_first = "http://image.baidu.com" + \
                    "/search/flip?tn=baiduimage&ie=utf-8&word="
        url_second = "&ct=201326592&v=flip"
        url = url_first + person + url_second

        # get url and save
        pic_url_list = get_pic_url(url, person)
        save_url(url_file, person, pic_url_list)

        # download picture
        t = Thread(target=download_pic, args=(url_file, pic_path, person))
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()


if __name__ == '__main__':
    main()
