#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    计算算法准确率 && 召回率
"""
count_ns_chunk = 0
'''

def compute_chunk(list ) :
    flag = "false"
    for str in list :
        temps = line.split("\t")
        if temps[len(temps) - 2] == temps[len(temps) - 1] :
            flag = "true"
        else :
            flag = "false"
    return flag
    
'''

def compare(list_tag ,list_predict) :
    count_right = 0
    map_tag = {}
    map_predict = {}
    start = 0
    for i, j in enumerate(list_tag):
        # print i, j
        if j == "B_NS" :
            start = i
            map_tag[start] = i
        elif j == "I_NS" :
            map_tag[start] = i

    for i, j in enumerate(list_predict):
        # print i, j
        if j == "B_NS" :
            start = i
            map_predict[start] = i
        elif j == "I_NS" :
            map_predict[start] = i

    for key in map_tag :
        if map_predict.has_key(key) :
            if map_tag[key] == map_predict[key] :
                count_right += 1

    global count_ns_chunk
    count_ns_chunk += len(map_predict)


    return count_right

def main() :
    f = open("./data/sample_test_result.txt")
    lines = f.readlines()
    count_right_ns = 0
    count_right_o = 0
    count_error_ns = 0
    count_error_o = 0
    for line in lines:
        # print line
        line = line.strip('\n')
        temps = line.split("\t")
        tag = temps[len(temps) - 2]
        # print "tag: " + tag
        predict_tag = temps[len(temps) - 1]
        # print "predict:" + predict_tag
        # print tag +" "+predict_tag
        if tag == predict_tag:
            if "NS" in tag:
                count_right_ns += 1
            elif "O" in tag:
                count_right_o += 1
        else:
            print line
            if "NS" in tag:
                count_error_ns += 1
            elif "O" in tag:
                count_error_o += 1
    print "count_right_ns: %.2f" % count_right_ns
    print "count_right_o: %.2f" % count_right_o
    print "count_error_ns: %.2f" % count_error_ns
    print "count_error_o: %.2f" % count_error_o

    print "## 20000 sentences test result : (tag level) ##"
    precision = float(count_right_ns) / float((count_right_ns + count_error_ns))
    recall = float(count_right_ns) / float((count_right_ns + count_error_o))
    print "precision: %.2f" % (precision * 100) + "%"
    print "recall: %.2f" % (recall * 100) + "%"

    print "## 20000 sentences test result : (chunk level) ##"
    count_ns_right_chunk = 0

    list_tag = []
    list_predict = []
    for line in lines:

        line = line.strip('\n')
        if line != "":
            temps = line.split("\t")
            tag = temps[len(temps) - 2]
            predict_tag = temps[len(temps) - 1]
            list_tag.append(tag)
            list_predict.append(predict_tag)

        else:
            count_ns_right_chunk += compare(list_tag, list_predict)

            list_tag = []
            list_predict = []

    print "count_ns_chunk  : %d" % count_ns_chunk
    print "count_ns_right_chunk  : %d" % count_ns_right_chunk

    precision = float(count_ns_right_chunk) / float(count_ns_chunk)
    print "precision: %.2f" % (precision * 100) + "%"

    '''
    list = []
    flag = "false"
    count_ns_chunk = 0
    count_ns_right_chunk = 0
    up_sentence = ""
    current_sentence = ""
    for line in lines :

        line = line.strip('\n')
        if line != "" :
            current_sentence = line
            temps = line.split("\t")
            tag = temps[len(temps) - 2]
            predict_tag = temps[len(temps) - 1]
            if tag == "B_NS" :
                count_ns_chunk += 1

            if tag == "B_NS" and flag == "false":

                list.append(line)
                flag = "true"

            elif tag == "I_NS" and flag == "true":

                list.append(line)


            elif tag == "O" and flag == "true":

                flag = "false"


                if compute_chunk(list) == "true":
                    count_ns_right_chunk += 1

                list = []

            if up_sentence != "" :
                up_temps = up_sentence.split("\t")
                up_tag = up_temps[len(up_temps) - 2]
                up_predict_tag = up_temps[len(up_temps) - 1]
                if up_tag == "I_NS" and predict_tag == "I_NS" and tag != "I_NS" :
                    count_ns_right_chunk -= 1

            up_sentence = line


        else :
            flag = "false"
            temps = current_sentence.split("\t")
            tag = temps[len(temps) - 2]
            predict_tag = temps[len(temps) - 1]
            if tag == "I_NS" :
                #count_ns_chunk += 1

                if compute_chunk(list) == "true":
                    count_ns_right_chunk += 1

                list = []
                #print("new sentence")

    print "count_ns_chunk  : %d"%count_ns_chunk
    print "count_ns_right_chunk  : %d"%count_ns_right_chunk

    precision = float(count_ns_right_chunk) / float(count_ns_chunk)
    print "precision: %.2f" % (precision * 100 )+ "%"
    '''

    f.close()


if __name__ == '__main__':
    main()
