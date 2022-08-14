
# def get_database():
#     from pymongo import MongoClient
#     import pymongo

#     # Provide the mongodb atlas url to connect python to mongodb using pymongo
#     CONNECTION_STRING_MGA1 = "mongodb://antuan:antuan2021@103.237.147.53:27017/admin?retryWrites=true&w=majority"
#     # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
#     from pymongo import MongoClient
#     client = MongoClient(CONNECTION_STRING_MGA1)

    # Create the database for our example (we will use the same database throughout the tutorial
    # return client
    
# This is added so that many files can reuse the function get_database()
# from ImportContent import *
from deep_translator import GoogleTranslator
from google_search_customer import *
import requests
import time
import random
from title_fix import Article
from urllib.parse import urlparse
from pymongo import MongoClient
import time
from urllib.parse import urlparse
import re
from preprocessing_content import *
import random
from bs4 import BeautifulSoup
from create_top_content import *
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from pymongo import MongoClient
import time
import json
import traceback


# client1 = MongoClient(CONNECTION_STRING_MGA1)

def GetTopUrl(website,categoryid):
    all_url = requests.get("{}/wp-json/wp/v2/posts?categories={}".format(website,categoryid),allow_redirects=False,verify=False,timeout=50).content
    hh = json.loads(all_url)
    urllist = []
    for i in hh:
        m = {"link":i["link"],
            "name":i["title"]["rendered"]}
        urllist.append(m)

    return urllist
# Add Text to an image
header_text_vi = "<p><strong>Dưới đây là các thông tin và kiến thức về chủ đề {} hay nhất do chính tay đội ngũ {} chúng tôi biên soạn và tổng hợp:</strong></p>"
header_text_en = "<p><strong>Below are the best information and knowledge on the subject {} compiled and compiled by our own team {}:</strong></p>"

def replace_attr(soup, from_attr: str, to_attr: str):
  try:
    if from_attr in str(soup):
        soup[to_attr] = soup[from_attr]
        del soup[from_attr]

        return soup
    else:
        return soup
  except:
    return soup

lasttime=0
userAgents=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',  # This is another valid field
}

h = 0
def no_accent_vietnamese(s):
  s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
  s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
  s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
  s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
  s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
  s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
  s = re.sub(r'[ìíịỉĩ]', 'i', s)
  s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
  s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
  s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
  s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
  s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
  s = re.sub(r'[Đ]', 'D', s)
  s = re.sub(r'[đ]', 'd', s)
  return s
header_titles = ["Top {}"]
last_titles = ["mới nhất năm 2022"]
def createandimportcontent(campaign_detail):
  keywords = campaign_detail["keyword"]["Keyword"]
  summary_text_title =  ""
  number_search = random.randint(10,30)
  img1 = Image.open('hinh.jpg')
 
# Call draw Method to add 2D graphics in an image
  I1 = ImageDraw.Draw(img1)
  
  # Custom font style and font size
  myFont = ImageFont.truetype("arial.ttf", 60)
  # myFont = ImageFont.truetype("arial.ttf", 28)
  if campaign_detail["campaign"]["language"] == "vi":
    list_url  = [i for i in search(campaign_detail["keyword"]["Keyword"], tld="com.vn",start=0,lang="vi",num=number_search,stop=number_search,pause=1)]
  else:
    list_url  = [i for i in search(campaign_detail["keyword"]["Keyword"], tld="com",start=0,num=number_search,stop=number_search,pause=1)]

  hhhhh = []
  url_ref = []
  print(len(list_url))
  for link in list_url:
    try:
      params = {
          "websiteid":str(campaign_detail["web_info"]["_id"]),
          "link":link[0]
      }
      checkurl = requests.get(LINKURL + "apihidden/checkurldone",params=params)
      checkurldone=json.loads(checkurl.content.decode("utf-8"))
      if checkurldone:
          continue
      domain = urlparse(link[0]).netloc

      if domain in campaign_detail["web_info"]["Blacklist"]:
          continue
      config = Configuration()
      config.request_timeout = 10
      config.browser_user_agent = random.choice(userAgents)
      r = requests.get(link[0],verify=False,timeout=10,headers=headers).content
      r = r.decode("utf-8")
      soups = BeautifulSoup(r)
      img = soups.find_all("img")
      for i in img:
          try:
            liii = re.findall("lazy.*=\'.*\'",str(i))
            if len(liii)>0:
                for j in liii:
                    hhh= j.split(" ")[0].split("=")[-1]
                    if ".JPG" in hhh.upper() or ".PNG" in hhh.upper():
                        i["src"] = hhh
                        break
          except Exception as e:
              print(str(e))
      soups = str(soups)
      article = Article("",keep_article_html=True,config=config)
      
      
      article.download(soups)
      article.parse()
      if "404" in article.title or "resource cannot be found" in article.title or "Cloudflare" in article.title or "cloudflare" in article.title or "Please Wait…" in article.title:
        continue
      if len(article.text.split(" "))<100:
        print("ko thoa man")
        continue

      self_url = str(no_accent_vietnamese(article.title.replace("\r","")))+ ' ' + str(time.time()).split(".")[0]
      self_url = re.sub('[^A-Za-z0-9 ]+', '', self_url)
  
      summary_text_title = summary_text_title + article.title+", "
      self_url = self_url.replace(" ","-")
      params = {
        "websiteid":str(campaign_detail["web_info"]["_id"]),
        "link":link[0]
      }
      addurl = requests.post(LINKURL + "apihidden/addurldone",params=params)
      addurldone=json.loads(addurl.content.decode("utf-8"))

      if len(article.text.split(" "))>100:
        paper = BeautifulSoup(article.article_html)
        for elem in paper.find_all(['a']):
          elem.unwrap()
        article.article_html = str(paper)
        done = ImportContents(campaign_detail,article.article_html,campaign_detail["campaign"]["CategoryNoIndexId"],article.title,self_url,None)
        url_ref.append(self_url)
      else:
        url_ref.append("")
      hhhhh.append(article)
    except Exception as e:
      number_search =number_search-1
      print(traceback.format_exc())
  number_search = len(hhhhh)
  lists_url_ref = []
  try:
    lists_url_ref = GetTopUrl(campaign_detail["web_info"]["Website"],campaign_detail["campaign"]["CategoryId"])
  except:
    pass
  if campaign_detail["campaign"]["language"] == "vi":
    prop = [True,True,True,False,False]
    outbouding = random.choice(prop)
    
    content = header_text_vi.format(campaign_detail["keyword"]["Keyword"],campaign_detail["web_info"]["Website"].split(".")[0].replace("https://","").replace("http://","")) + CreateTopContent(hhhhh,list_url,url_ref,campaign_detail["campaign"]["language"],lists_url_ref)
    if outbouding:
      try:
        translated = GoogleTranslator(source='auto', target='en').translate(campaign_detail["keyword"]["Keyword"])
        list_url_ref  = [i for i in search(translated, tld="com",start=0,num=10,stop=10,pause=1)]
        number_ref = random.randint(1,10)
        text_ref = """"
        <div class="section references sourcesandcitations sticky" bis_skin_checked="1">
          <h2 class="section-heading">
          <div class="mw-ui-icon mw-ui-icon-element indicator" id="references_first" bis_skin_checked="1"></div>
          <span class="mw-headline" id="Tham_kh.E1.BA.A3o">Tham khảo</span>
          </h2>
          <div id="tham_kh.e1.ba.a3o" class="section_text" bis_skin_checked="1"><ol class="firstref references">
          {}
          </ol></div>
          <div class="sticky-sentinel sticky-sentinel-top" bis_skin_checked="1"></div></div>
        """
        text_ref_element = """
        <li>
        <a target="_blank" rel="nofollow noreferrer noopener" class="external-free" href="{}">{}</a>
        </li>
        """
        text_ref_elements = ""
        for link_ref in list_url_ref[:number_ref]:
          text_ref_elements = text_ref_elements +text_ref_element.format(link_ref[0],link_ref[0])
        
        text_ref = text_ref.format(text_ref_elements)
        content = content + text_ref
      except Exception as e:
        print(traceback.format_exc())
  else:
    content = header_text_en.format(campaign_detail["keyword"]["Keyword"],campaign_detail["web_info"]["Website"].split(".")[0].replace("https://","").replace("http://","")) + CreateTopContent(hhhhh,list_url,url_ref,campaign_detail["campaign"]["language"],lists_url_ref)
  if campaign_detail["campaign"]["language"] == "vi":
    title = random.choice(header_titles).format(number_search)+" " +keywords+" " + random.choice(last_titles)
  else:
    title = random.choice(header_titles).format(number_search)+" " +keywords+" " + "in 2022"
    

  I1.text((150, 460), title, font=myFont, fill =(255, 215, 0))
  # Display edited image
  # Save the edited image
  if number_search<3:
    return True
  self_url = str(no_accent_vietnamese(title.replace("\r","")))+ ' ' + str(time.time()).split(".")[0]
  self_url = self_url.replace(" ","-")
  self_url = self_url.replace("--","-")
  self_url = self_url.replace(".","")

  img1.save("toplistlogo/"+self_url+".jpg")
  localpath = "toplistlogo/"+self_url+".jpg"
  newID = None
  with open(localpath, mode='rb') as f:
      image = Image.open(io.BytesIO(f.read()))
      output = io.BytesIO()
      image.save(output,format='JPEG',optimize = True,quality = 30)
      image = output.getvalue()
      user = campaign_detail["web_info"]["UserWP"]
      password = campaign_detail["web_info"]["PasswordWP"]
      website = campaign_detail["web_info"]["Website"] + "/wp-json/wp/v2/media"
      credentials = user + ':' + password 
      pathfile =self_url+".jpg"
      token = base64.b64encode(credentials.encode())
      header = {'Authorization': 'Basic ' + token.decode('utf-8'),'Content-Type': 'image/jpg','Content-Disposition' : 'attachment; filename=%s'%pathfile,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
      with requests.post(website,
                      data=image,
                      headers = header) as response:
          # res1 =  response.text
          res =  json.loads(response.content.decode("utf-8"))
          newID= res.get('id')
          print(newID)
  done = ImportContents(campaign_detail,content,campaign_detail["campaign"]["CategoryId"],title,self_url,newID)
  return done