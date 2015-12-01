##General Functions
#to get the text blah blah
def GettingBetweenTags(line, beginTag, endTag):
    if beginTag not in line:
        startPos = 0
    else:
        startPos = line.index(beginTag)
    if endTag not in line:
        endPos = len(line)
    else:
        endPos = line.index(endTag)
    return line[startPos+1:endPos]

def RemoveTags(line):
    while (">" in line):
        startpos = line.index("<")
        endpos = line.index(">")
        subline = line[startpos:endpos+1]
        line = line.replace(subline,"")
    return line


#to get the pageName 
def FindPageName(text):
    for line in text:
        # Break up the line
        print "#1" + line
        if "<title>" in line:
            pgName = GettingBetweenTags(line)
            print pgName



##To get text type contents from a html file
#to get the required sectios to pull text content            
def SplitTextByTags(filePath, search_begin_str, search_end_str):
    
    txtfile = open(filePath,"r")
    contentlist = []
    content = ""
    flag = 0
    for line in txtfile:
        if(search_begin_str in line) or (flag == 1):
            content = content + line.strip()
            if not(search_end_str in line):
                flag = 1
            else:
                flag = 0
                contentlist.append(content.strip())
                content = ""
    return contentlist

#to post to the TextContent table
def GetTextContent():
    contentlist = SplitTextByTags("Data/brg001-200.txt", """color="#FF0000">Car ""","</p>")
    for line in contentlist:
        pgline = line
        while (">" in pgline):
            pgline = GettingBetweenTags(pgline,">","</")
        contentline = RemoveTags(line)
        print pgline + " " + contentline


##To get image source files from a html file
#to get the image file from 
def GetImgFile(line):
    imgFile = []
    while '<img src="' in line:
        startpos = line.find('<img src="')
        endpos = line.find('"',startpos+10)
        subline = line[startpos:endpos]
        imgFile.append(subline.replace('<img src="',""))
        line = line.replace(subline,"")
    return imgFile

#to get the required sectios to pull text content  
def SplitImageContent(filePath, search_begin_str, search_image_str, search_end_str):
    txtfile = open(filePath,"r")
    contentlist = []
    content = ""
    sameContextFlag = 0
    booleanimg = False
    
    line = txtfile.readlines()
    
    for i in xrange(len(line)):
        if(search_begin_str in line[i]) or (sameContextFlag == 1):
            content = content + line[i].strip()
            if search_image_str in line[i]:
                booleanimg = True
            if i < len(line)-1:
                if (search_end_str in line[i+1]):
                    sameContextFlag = 0
                    if booleanimg == True:
                        contentlist.append(content.strip())
                    content = ""
            sameContextFlag = 1
    return contentlist

def GetImageContent():
    contentlist = SplitImageContent("Data/brg001-200.txt", """color="#FF0000">Car """,'<img src="',"""color="#FF0000">Car """)
    for line in contentlist:
        pgline = line
        while (">" in pgline):
            pgline = GettingBetweenTags(pgline,">","</")
            
        imgLine = GetImgFile(line)
        print pgline
        print imgLine
        
#mySQL Database connection and Execution
import MySQLdb
def DatabaseCommand(command):
    db = MySQLdb.connect("198.71.225.53","itp2015","*pwd*", "ITP_2015")
    cur = db.cursor()
    cur.execute (command)
    cur.close
