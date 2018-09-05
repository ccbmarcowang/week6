import json
import pandas as pd
import sys
def analysis(file,user_id):
	times=0
	minutes=0
	df=pd.read_json(file)
	df1=df.groupby('user_id').count()
	df2=df.groupby('user_id').sum()
	try:
		times=df1['course'][user_id]
		minutes=df2['minutes'][user_id]
	except:
		times=0
		minutes=0
	return times,minutes
if __name__=='__main__':
	try:
		file=sys.argv[1]
		user_id=int(sys.argv[2])
		print(analysis(file,user_id))
	except:
		print('Parameter Error')
		exit()
	