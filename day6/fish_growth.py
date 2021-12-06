s=open("f").read()[::2]
r=range
f=[0 for i in r(9)]
for i in s:f[int(i)]+=1
for i in r(257):
	t=f[0] 
	for i in r(8):f[i]=f[i+1]
	f[6]+=t
	f[8]=t
c=0
for i in r(8):c+=f[i]
print(c)