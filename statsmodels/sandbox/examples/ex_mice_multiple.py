import pandas as pd
import statsmodels.api as sm
from statsmodels.sandbox.mice import mice
import os
#
#cur_dir = os.getcwd()
#fn = os.path.join(cur_dir,"missingdata.csv")
data = pd.read_csv("missingfull.csv")
data.columns = ['x1','x2','x3']
impdata = mice.ImputedData(data)
m1 = impdata.new_imputer("x2", scale_method="perturb_chi2", method="pmm")
m2 = impdata.new_imputer("x3", model_class=sm.Poisson, scale_method="perturb_chi2", method="pmm")
m3 = impdata.new_imputer("x1", model_class=sm.Logit, scale_method="perturb_chi2", method="pmm")
impcomb = mice.MICE("x1 ~ x2 + x3", sm.Logit,[m1,m2,m3])
impcomb.run()
p1 = impcomb.combine()
print p1.summary()
