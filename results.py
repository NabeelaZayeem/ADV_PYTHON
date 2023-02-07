import pandas as pd
import numpy as np
class Readcsv():

    def create_df(self,path):
        self.path=path
        self.df=pd.DataFrame(self.path)

    def total(self):
        df['Total']=self.df.iloc[:,[1,2,3,4,5,6]].sum(axis=1)
        print(df)

    def pass_fail(self):
        self.df['Result']=np.where((self.df['M1']>=35)& (self.df['M2']>=35) & (self.df['M3']>=35) & (df['M4']>=35) &(df['M5']>=35), "Pass","Fail" )
        print(self.df)
    def avg_df(self):
        self.df['avg']=np.where((self.df['Result'])=='Pass',round(self.df['Total']/5),0.0)
        return self.df
    def rank(self):
        self.df['Rank']=np.where((self.df['Result']=='Pass'),df['Total'].rank(ascending=False),'nA')
        print(self.df)



df = pd.read_csv("..//data/marks.csv")
rs=Readcsv()
rs.create_df(df)
rs.total()
rs.pass_fail()
print(rs.avg_df())
rs.rank()


