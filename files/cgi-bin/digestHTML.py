#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import sys
import datetime

time = datetime.datetime.today()

args = sys.argv

output_file = "creditsSheet.txt"
f_o = open(output_file, 'w')

#htmlにするため
#print("print \"Content-type: text/html; charset=utf-8\n\").encode('utf-8')
print("<html><meta charset=\"utf-8\"><body>")

#webからURLのクエリ
input_file ="htmlsource"
input_file = input_file  + str(time) + ".txt"
form = cgi.FieldStorage()
f_i = open(input_file, 'w')
f_i.write(form['pastedHTML'].value)
f_i = open(input_file)

line = f_i.readline()
credit = {"A+":0, "A":0, "B":0, "C":0, "F":0, "G":0, "H":0 }
group = {}
nonfinishedGroup = {}
currentGroup = "NONEGROUP"
GPA = 0
classNum = 0

#htmlを解釈して、履修した授業数を群ごとにカウント、スコアも計算
while line:
#	print line
	
	#授業の成績を調べる
	if line.find("operationboxf") != -1 :
		line = f_i.readline()
		#群(A群C群とかのあれ)をセット
		if line.find("群") != -1:
			currentGroup = line.strip().replace("<TD>","").replace("</TD>", "").replace("◎","")
			group[currentGroup] = 0
			nonfinishedGroup[currentGroup] = 0
			continue
		elif currentGroup != "NONEGROUP":
			line = f_i.readline()
			line = f_i.readline()
			line = f_i.readline()
			#授業の単位数	
			creditNum =int(line.strip().replace("<TD>","").replace("</TD>","").replace("<BR>", "0").replace("＊", "0"))
			line = f_i.readline()
			#成績評価
			grade = line.strip().replace("<TD>","").replace("</TD>","") 	
	#		print grade
			#単位数のカウント
			if grade != "＊" and grade != "<BR>": 
				group[currentGroup] += creditNum
			elif grade == "＊":
				nonfinishedGroup[currentGroup] += creditNum 
			line = f_i.readline()
			#授業のスコア
			score = int(line.strip().replace("<TD>","").replace("</TD>","").replace("<BR>", "0").replace("＊", "0"))
			GPA += score
		#	print classNum
			if grade in credit:
				credit[grade] += 1
			else:
				credit[grade] = 1
	line = f_i.readline()	

print "受講している授業名の、htmlからの抽出が終了しました。"

creditSum = 0
nonfinishedCreditSum = 0
print "---群別の単位数(カッコ内は履修はしているもののまだ成績が決定されていないもの)---"
for key in group.keys():
	print key + ": "+ str(group[key]) + " ("+str(nonfinishedGroup[key])+")"
	creditSum += group[key]
	nonfinishedCreditSum += nonfinishedGroup[key]
print "合計: " + str(creditSum) +" ("+ str(nonfinishedCreditSum) +")" +" 単位"

print ("\n---評価別の数(＊は未評価)---")
for key in credit.keys():
	if key != "<BR>":
		print key + " " + str(credit[key])
		classNum += credit[key]

print "\n---成績計算---"
print "scoreSum " + str(GPA)
print "class " + str(classNum)
print "finishedClass " +str(classNum -credit["＊"])
print "GPA " + str(float(GPA)/(classNum-credit["＊"]))


print ("</body></html>")
