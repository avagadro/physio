import string
import random
import enchant
d = enchant.Dict("en_US"); # LOADING ENGLISH DICTIONARY 
chars=string.ascii_lowercase;
size=4;
count=0;
strings = [[] for i in range(100)];
print ('Random 4 letter Strings are'); 
for y in range(0,100):
 value="".join(random.choice(chars) for _ in range(size)); # FUNCTIONS WHICH MAKES RANDOM LETTER WORDS 
 strings[y]=value; 
 print ('%s'%(strings[y]));
for x in range(0,100):
 if d.check(strings[x]): 
  term=count+1; 
  count=term; 
  print ('Word found in dictionary : %s' %(strings[x])); # TO CHECK IF ANY RANDOM GENERATED WORD EXISTED IN THE DICTIONARY AND PRINTING IT 
print ('Total correct words %d'%(count));
print ('Frequency of characters is:'); 
freq = [0]*26; 
for t in range(0,100): 
 term2=strings[t]; 
 for e in range(0,4): 
  char_value=ord(term2[e]); 
  term3=char_value-97; 
  count2=freq[term3]; 
  count3=count2+1; 
  freq[term3]=count3; 
print (freq[:]); # THE ABOVE CODE IS USED TO GET THE FREQUENCY OF THE CHARACTERS IN THE GENERATED RANDOM WORDS 
print ('PDF is:'); 
pdf = [0]*26; 
for u in range(0,26): 
 pdf[u]=freq[u]*0.0025; # THIS CODE IS USED TO CALCULATE THE PDF OF EVERY CHARACTER USING ITS FREQUENCY 
print (pdf[:]); 
hello=[0]*26; 
hello2=0; 
print ('CDF is:'); 
for q in range(0,26): 
 hello2=hello2+pdf[q]; 
 hello[q]=round(hello2,6); # THIS CODE IS USED TO GET THE CDF OF THE FOUND PDF IN THE ABOVE FUNCTION 
print (hello[:]);
weighted_arr=[0]*26; 
for x in range(0,26): 
 z=97+x; 
 weighted_arr[x]=(chr(z),freq[x]); 
count 
print ('THE WEIGHTED AVERAGE IS'); 
print (weighted_arr[:]);
stgs=[[] for i in range(10)]; 
print ('THE WEIGHTED AVERAGE NEW WORDS ARE'); 
population=[val for val,cnt in weighted_arr for x in range(cnt)] 
for x in range(0,10): 
 value="".join(random.choice(population) for _ in range(size)); 
 stgs[x]=value; 
 print ('%s'%(stgs[x]));
freq1=[0]*26; 
for i in range(0,10):    
 term=stgs[i];    
 for j in range(0,4):        
  charval=ord(term[j]);        
  freq1[charval-97]+=1; 
print ('THE WAITED AVERAGE FREQUENCY'); 
print (freq1[:]);