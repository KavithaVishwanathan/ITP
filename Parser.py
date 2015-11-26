##General Functions

#to get the text
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
