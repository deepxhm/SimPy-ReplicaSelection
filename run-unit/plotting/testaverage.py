import numpy
def average(filenamestr):
	filenamestr = filenamestr.strip("\n")
	filenamestr = filenamestr.split(" ")
	strategyname = GetstrategyName(filenamestr) + ".txt"
	f = open("%s" %strategyname, "w")
	for i in range(len(filenamestr)):
		listset = []
		tempfile = open("%s" %filenamestr[i], "r")
		for oneline in tempfile.readlines():
			oneline = oneline.strip("\n")
			oneline = oneline.replace("\t", " ")
			oneline = oneline.split(" ")
			onelist = []
			for oneitem in oneline[1:]:
				onelist.append(float(oneitem))
			listset.append(onelist)
		tempfile.close()
		
		"""
		print "\t\t", "%s" %filenamestr[i]
		
		#print "strategy:", "\t", "ORA", "\t", "C3", "\t"

		print "average:", numpy.mean(listset, axis = 0)
		print "var:", numpy.var(listset, axis = 0)
		print "std:", numpy.std(listset, axis = 0)
		"""
		average = float(numpy.mean(listset, axis = 0))
		f = open("%s" %strategyname, "a")
		f.write(str(average))
		f.write("\t")
		print average
	f.close()
				
def GetstrategyName(filenamestr):
	f = f = open("%s" %filenamestr[0], "r")
	oneline = f.readline()
	oneline = oneline.strip("\n")
	oneline = oneline.replace("\t", " ")
	oneline = oneline.split(" ")
	oneitem = oneline[0].split("-")
	return oneitem[0]



def Aggregate(filenamestr):
	filenamestr = filenamestr.strip("\n")
	filenamestr = filenamestr.split(" ")
	Agg = open("figuredatafortest.txt", 'w')
	dictinter = {}
	dictinter['10'] = []
	dictinter['200'] = []
	dictinter['500'] = []
	for i in range(len(filenamestr)):
		#Agg = open("figuredata.txt", 'a')
		strategyname = filenamestr[i] + ".txt"
		tempfile = open("%s" %strategyname, 'r')
		item = tempfile.readline()
		item = item.strip('\n')
		item = item.split('\t')
		dictinter['10'].append(item[0])
		dictinter['200'].append(item[1])
		dictinter['500'].append(item[2])	
		#Agg.write(item)
		tempfile.close()

	Agg = open("figuredatafortest.txt", 'a')
	Agg.write("interpara" + "\t")
	for item in filenamestr:
		Agg.write(item + "\t")
	Agg.write("\n")

	for key in ['10', '200', '500']:
		Agg.write(key + "\t")
		for item in dictinter[key]:
			Agg.write(item + "\t")
		Agg.write("\n")
	Agg.close()  
#filenamestr = "RR RAND WRR WRRT PROB TC LOR LRT DS C3 InterC"
import testaverage
testaverage.average("inter10 inter200 inter500")

#usage







