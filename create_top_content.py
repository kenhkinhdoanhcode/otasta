import random
import time
from urllib.parse import urlparse
def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)
    
print(random_date("1/1/2008 1:30 PM", "1/1/2009 4:50 AM", random.random()))

menuheader = """
    <div class="postContent">
    <nav style="display: inline-block;background: #eff5f9;border: 1px solid #9cd5f4;border-radius: 4px;/*! width: 52%; */padding: 1.5%;margin-bottom: 10px;font-size: 14px;" role="navigation" id="table_of_contents" class="table-of-contents">
    <p style="position: relative;display: block;overflow: hidden;text-align: center;cursor: pointer;font-weight: bold;margin-bottom: 0;color: #333;">Menu</p>
    <ul id="nav_ul">"""
menufor =     """<li><a href="#h2_{}">{}.{}</a></li>"""
menufooter = """
    </ul>
    </nav>
    </div>
"""
body_vn ="""
    <h2 id="h2_{}">{}. {} </h2>
    <div class="content_toplist">
    <p><strong>Tác giả: </strong> {} </p>
    <p><strong>Ngày đăng: </strong> {} </p>
    <p><strong>Đánh giá: </strong> {} ⭐ ( {} đánh giá) </p>
    <p><strong>Tóm tắt: </strong> <span class="content">{}</span> </p>
    <p><strong>Khớp với kết quả tìm kiếm: </strong> {}</p>
    <p><img alt="{}"no-referrer" src="{}"></p>
    </div>
"""
body_en ="""
    <h2 id="h2_{}">{}. {} </h2>
    <div class="content_toplist">
    <p><strong>Author: </strong> {} </p>
    <p><strong>Date Submitted: </strong> {} </p>
    <p><strong>Average star voting: </strong> {} ⭐ ( {} reviews) </p>
    <p><strong>Summary: </strong> <span class="content">{}</span> </p>
    <p><strong>Match with the search results: </strong> {}</p>
    <p><img alt="{}"no-referrer" src="{}"></p>
    </div>
"""
comment_en = """
<p><br></p>
<div class="comment">
<h4>Comments</h4>
<div class="ele_comment">

<div class="comment_content">
<p class="user_name" title="User" s="" name'="">MinhCherry</p>
<p title="User" s="" comment'="">Admin, I want to learn about {}, can you find out and write an article on that topic? thank you very much</p> <span style="color: gray;font-size: 14px;padding-left: 20px;" title="Time of comment" class="relativetime-clean"> - - Today - -</span>
</div>
<div class="reply_content">
<p class="user_reply">Admin</p>
<p>Hi, I wrote an article about {}, you can read <a href="{}">here</a> </p> <span style="color: gray;font-size: 14px;padding-left: 20px;" title="Time of comment" class="relativetime-clean">- - Today - -</span>
</div>
<div class="reply_content">
<p class="user_reply">MinhCherry</p>
<p>Thank you admin, I'm reading it right now </p> <span style="color: gray;font-size: 14px;padding-left: 20px;" title="Time of comment" class="relativetime-clean">- - Today - -</span>
</div>
</div> 
<div class="ele_comment">
<div class="comment_content">
<p class="user_name" title="User" s="" name'="">Jerkey Mery</p>
<p title="User" s="" comment'="">I read an article about {} yesterday but I forgot the link to the article. Admin, can you help me find the link for that post?</p> <span style="color: gray;font-size: 14px;padding-left: 20px;" title="Time of comment" class="relativetime-clean"> - - Today - -</span>
</div>
<div class="reply_content">
<p class="user_reply">Admin</p>
<p>Is the link you're looking for <a href="a.com">ok</a> ? </p> <span style="color: gray;font-size: 14px;padding-left: 20px;" title="Time of comment" class="relativetime-clean">- - Today - -</span>
</div>
<div class="reply_content">
<p class="user_reply">Jerkey Mery</p>
<p>Very useful post, thank you very much </p> <span style="color: gray;font-size: 14px;padding-left: 20px;" title="Time of comment" class="relativetime-clean">- - Today - -</span>
</div>
</div>
<div class="ele_comment">
<div class="comment_content">
<p class="user_name" title="User" s="" name'="">David Vankage</p>
<p title="User" s="" comment'="">It's been a long time since I read a good article like this, exactly what I was looking for</p> <span style="color: gray;font-size: 14px;padding-left: 20px;" title="Time of comment" class="relativetime-clean"> - - Today - -</span>
</div>
<div class="reply_content">
<p class="user_reply">Alan</p>
<p> I will vote 5 stars for this article </p> <span style="color: gray;font-size: 14px;padding-left: 20px;" title="Time of comment" class="relativetime-clean">- -Today - -</span>
</div>
</div>
<div class="ele_comment">
<div class="comment_content">
<p class="user_name" title="User" s="" name'="">David Trump<</p>
<p title="User" s="" comment'="">Quality article</p> <span style="color: gray;font-size: 14px;padding-left: 20px;" title="Time of comment" class="relativetime-clean"> - - Today - -</span>
</div>
</div>
<div class="ele_comment">
<div class="comment_content">
<p class="user_name" title="User" s="" name'="">Tom</p>
<p title="User" s="" comment'="">I will apply the knowledge learned from the article to my life</p> <span style="color: gray;font-size: 14px;padding-left: 20px;" title="Time of comment" class="relativetime-clean"> - - today - -</span>
</div>
</div>
<div class="ele_comment">
<form class="input_box" action="#" method="">
<div class="input">
<textarea id="editor" placeholder=" write comment..." name="comment_Text"></textarea>
</div>
<div class="send">
<input type="submit" value="Send">
</div>
</form>
</div>
</div>
"""
comment_vi = """
<div class="top-news relatedItems" bis_skin_checked="1">{}<ul class="list-items">{}</ul></div>
"""
element_comment = """
<li><a href="{}"> {} </a></li>
"""
import random
def CreateTopContent(articles,urls,url_ref,lang,lists_url_ref):
    
    menubody = ""
    body1  = "" 
    if lang  == "vi":
        body = body_vn
    else:
        body = body_en

    for index, article in enumerate(articles):
        date = random_date("1/1/2019 1:30 PM", "1/1/2022 1:30 PM", random.random())
        menubody =  menubody + """<li><a href="#h2_{}">{}.{}</a></li>""".format(index,index+1,article.title)
        if url_ref[index] == "":
            body1 = body1 + body.format(index,index+1,article.title,urlparse(urls[index][0]).netloc,date,random.randint(3,5),random.randint(10000,100000),article.meta_description,urls[index][1],article.title,article.top_image)

        else:
            body1 = body1 + body.format(index,index+1,article.title,urlparse(urls[index][0]).netloc,date,random.randint(3,5),random.randint(10000,100000),article.meta_description,urls[index][1]+".... <a href=/{}>read more</a>".format(url_ref[index]),article.title,article.top_image)
    # menu1 = menuheader +menubody + menufooter 
    # if len(lists_url_ref)>0 and lang  == "vi":
    #     link_ref1 =random.choice(lists_url_ref)
    #     link_ref2 =random.choice(lists_url_ref) 
    #     contents = body1 +comment_vi.format(" ".join(link_ref1["name"].split(" ")[2:-4]),link_ref1["name"],link_ref1["link"],link_ref2["name"],link_ref2["link"],link_ref2["name"])

    # elif len(lists_url_ref)>0:
    #     link_ref1 =random.choice(lists_url_ref)
    #     link_ref2 =random.choice(lists_url_ref) 
    #     contents = body1 +comment_en.format()
    #     contents = body1 +comment_en.format(" ".join(link_ref1["name"].split(" ")[2:-2]),link_ref1["name"],link_ref1["link"],link_ref2["name"],link_ref2["link"],link_ref2["name"])
    # else:
    related = ""
    contents = body1 
    if len(lists_url_ref)>0:
        for i in lists_url_ref:
            related = related + element_comment.format(i["link"],i["name"])
        if lang  == "vi":
            contents = contents +comment_vi.format("<p><strong>Có thể bạn quan tâm đến các bài viết cùng chủ đề sau:</strong></p>",related)
        else:
            contents = contents +comment_vi.format("<p><strong>You may be interested in the following articles on the same topic:</strong></p>",related)


    return contents

        

