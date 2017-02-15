# coding:utf8
import os
writeStr = "---\ntitle: github目录\ndate: 2016-01-01\n---\n## blogMarkdownFile\n## 寻找实习单位,[个人简介](https://makeitpossible16.github.io/about/)\n## [myblog](https://www.makeitpossible16.github.io)\n"
with open("/home/ubuntu/workspace/blog/hexo_blog/blog/source/_posts/README.md",'w') as f:
    dirFiles = os.listdir("/home/ubuntu/workspace/blog/hexo_blog/blog/source/_posts")
    dirFiles.sort()
    for files in dirFiles:
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
