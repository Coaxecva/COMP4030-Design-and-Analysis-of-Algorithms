Brandon Hopper
def isValidSent(s, d):
	i = 0
	j = 0
	while(i!= len(s)):
	
		if(s[i:j] in d):
			i=j
			
		if(j>=len(s)):
			i = i +1
			j=i
		j = j + 1
	
	if(i==j-1):
		return True
		
	else:
		return False

d = ["apple,best,it,of,the,times,was"];
print(isValidSent("itwasthebestoftimes", d))
