import pandas as pd
import statsmodels.api as sm
from statsmodels.sandbox.mice import mice
import os

cur_dir = os.getcwd()
fn = os.path.join(cur_dir,"missingdata.csv")
data = pd.read_csv(fn)
data.columns = ['x1','x2','x3']
impdata = mice.ImputedData(data)
impdata.new_imputer("x2", scale_method="perturb_chi2", method="pmm")
impdata.new_imputer("x3", scale_method="perturb_chi2", method="pmm")
impdata.new_imputer("x1", model_class=sm.Logit, scale_method="perturb_chi2", method="pmm")
impcomb = mice.MICE("x1 ~ x2 + x3", sm.Logit, impdata)
implist = impcomb.run()
p1 = impcomb.combine()
print p1.summary()
