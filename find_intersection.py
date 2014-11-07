import sys
freq_of_participation={}
def make_dic(filepath):
	f = open(filepath, 'r')
	answer = {}
	for line in f:
	    rank,team_name,institute,score= line.strip().split(' | ')
	    key = team_name.strip()+" | "+institute.strip()
	    if(score!='0'):
		    if key in freq_of_participation:
		    	freq_of_participation[key][0]+=1
		    	freq_of_participation[key].append(filepath+"("+rank+")")
		    else:
		    	freq_of_participation[key]=[1,filepath+"("+rank+")"]
	f.close()
	
make_dic("amr")
make_dic("kan")
make_dic("kgp")
c=int(sys.argv[1])
for i in freq_of_participation:
	if(freq_of_participation[i][0]==c):
		print i+" |",freq_of_participation[i]