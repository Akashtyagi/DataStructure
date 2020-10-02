# My Approach
class Solution:
	def intToRoman(self,nums):
		self.roman = {1:"I", 2:"II", 3: "III", 4:"IV", 5:"V", 6:"VI",
		7:"VII", 8:"VIII", 9:"IX", 10: "X", 50:"L", 100:"C", 500:"D",
		1000:"M"}
		result = ''

		l = len(str(nums))
		digits = []
		for i in range(l-1,-1,-1):
			digits.append( (int(nums/10**i) %10) *10**i)

		for d in digits:
			if d ==0:
				continue
			if d not in self.roman:
				val = self.nearestRoman(d)
				diff = d-val
				x = 1
				if abs(diff) in self.roman:
					val2 = self.roman[abs(diff)]
				else:
					val2 = self.nearestRoman(abs(diff))
					x = int(abs(diff)/val2)
					val2 = self.roman[val2]*x
				
				if diff>0:
					result = result+self.roman[val]+val2
				else:
					result = result + val2 + self.roman[val]
			else:
				val = d
				result = result+self.roman[val]
		return result

	def nearestRoman(self,d):
		min_ = 0
		max_ = float("inf")
		l = len(str(d))-1
		for r in self.roman:
			if r<d:
				min_ = r
			else:
				max_ = r
				break
		if max_-d > 10**l:
			val = min_ #Roman val to be used
		else:
			val = max_
		return val


def romanToInt(s: str) -> int:
    roman = { "I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000 }
    
    if len(s)<1:
        return 0
    l = len(s)-1
    count = 0
    add = 0
#        print("l ",l)
    next_val = None
    while count<=l:
        curr_val = roman[s[count]]
#            print(s[count],curr_val,add)
        if count+1<=l:
            next_val = roman[s[count+1]]
        if next_val and next_val>curr_val:
#                print('asdsda')
            add+= (next_val-curr_val)
            count+=2
        else:
            add+=curr_val
            count+=1
        next_val = None
#            print(count, add)
    return add


x = Solution()

asd = [500,100,50,300,157,63,842,874,255,395,629,643,934,1994,58]

for a in asd:
    r1 = x.intToRoman(a)
    r2 = romanToInt(r1)
    if r2==a:
        print(f"Passed: {r1} =={r2}, {a}")
    else:
        print(f"Failed: {r1} !={r2}, {a} ")


# =============================================================================
# # BEST APPROACH
# =============================================================================
    
values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
romans = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]    

def intToRoman(nums):
    answer = ''
    i = 0
    while nums:
         # Check if "nums" fully divisible by current index value and 
         # if it divisible it means that roman no. should be added to answer
        answer = answer + (nums//values[i])*romans[i]      
        
        # reduce Nums value if "mod" exists.
        nums = nums%values[i]
        i=i+1
    return answer
        

def romanToInt(s):
    roman = { "I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000 }
    answer = 0
    if len(s)<1:
        return 0
    for i in range(0,len(s)-1):
        if roman[s[i]]<roman[s[i+1]]:
            answer = answer-roman[s[i]]
        else:
            answer = answer+roman[s[i]]
    return answer+roman[s[-1]]

asd = [500,100,50,300,157,63,842,874,255,395,629,643,934,1994,58]

for a in asd:
    r1 = intToRoman(a)
    r2 = romanToInt(r1)
    if r2==a:
        print(f"Passed: {r1} =={r2}, {a}")
    else:
        print(f"Failed: {r1} !={r2}, {a} ")
        
    
