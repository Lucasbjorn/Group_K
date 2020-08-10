""" author @sprihaak
created 11:35 8/9"""

#these numbers don't make sense... it's not (#)(1000)/487.5
atp_depriv= 5000/487.500
control=2000/487.500
ek_neg40= 1000/487.500
ena_30= 2000/487.500
gk_5= 1000/487.500
gna_point2=5000/487.500
gnatkfast_gnapkslow= 2000/487.500

print(atp_depriv)
print(control)
print(ek_neg40)
# only calculating these values and will use them to figure out the other ones.
import matplotlib.pyplot as plt

data= {'2.05':2, '4.10':3,'10.26':2}
firing_rate= data.keys()
number= data.values()
plt.bar(firing_rate, number, color ='mediumaquamarine', width = 0.4) 
  
plt.xlabel("Firing Rates (AP/s)") 
plt.ylabel("No. of simulations") 
plt.title("Number of simulations with certain firing rates") 
plt.show() 