import os
writeStr = "# [myblog](http://www.makeitpossible.net.cn)\n\n"
with open("/home/ubuntu/workspace/blog/hexo_blog/blog/source/_posts/README.md",'w') as f:
    for files in os.listdir("/home/ubuntu/workspace/blog/hexo_blog/blog/source/_posts"):
            # print files
            for file in files.split("\n"):
                if os.path.isfile("/home/ubuntu/workspace/blog/hexo_blog/blog/source/_posts/" + file):
                    if(file.split(".")[1] == "md"):
                        if (file.split(".")[0] == "README"):
                            continue
                        writeStr =writeStr + "### ["+ file.split('.')[0] +"](https://github.com/MakeItPossible16/blogMarkdownFile/blob/master/" + file +")\n"
    print writeStr
    f.write(writeStr)
f.close()
