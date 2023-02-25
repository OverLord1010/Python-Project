def bbcode(lst):
    j = open("bbcode.txt", "w")
    j.write("blabla")
    j.write("\n")
    while len(lst)-3 >= 0:
        j.write("[tbl3]")
        j.write("\n")
        for i in range(3):
            j.write("[case][timg=")
            j.write(lst[0][0])
            j.write(",")
            j.write(lst[0][1])
            j.write("][/case]")
            j.write("\n")

            lst.pop(0)
        j.write("[/tbl3]")
        j.write("\n")
    if len(lst)-2 >= 0:
        j.write("[tbl2]")
        j.write("\n")
        for i in range (2):
            j.write("[case][timg=")
            j.write(lst[0][0])
            j.write(",")
            j.write(lst[0][1])
            j.write("][/case]")
            j.write("\n")

            lst.pop(0)
        j.write("[/tbl2]")
        j.write("\n")
    elif len(lst)-1 >= 0:
        j.write("[tbl1]")
        j.write("\n")
        j.write(lst[0][0])
        j.write(lst[0][1])

        lst.pop(0)
        j.write("\n")
        j.write("[/tbl1]")
    j.close()

def test():
    h = open("url.txt", "r")
    j = open("test.txt", "w")
    listip=[]
    for elt in h:
        a = elt.split("=")
        listip.append(a[0])
        j.write(a[0])
        j.write("\n")
    j.close()
    



'''tab=[["Vipere_Vol_1_2","url"],["Vipere_Vol_2_2","url2"],["Vipere_Vol_3_2","url3"],["Vipere_Vol_4_2","url2"]]
bbcode(tab)'''
test()
