import pandas as pd
from matplotlib import pyplot as plt
def data_plot(file):
	df=pd.read_json(file)
	df1=df.groupby('user_id').sum()
	fig=plt.figure()
	ax=fig.add_subplot(1,1,1)
	ax.set_title("StudyData")
	ax.set_xlabel("User ID")
	ax.set_ylabel("Study Time")
	minutes=df1['minutes']
	ax.plot(minutes)
	plt.show()
	return ax

if __name__=='__main__':
	file='user_study.json'
	data_plot(file)
