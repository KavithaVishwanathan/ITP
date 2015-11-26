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
