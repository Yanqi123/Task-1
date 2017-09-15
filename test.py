#!/usr/bin/env python

import json

print ("Hello world")


with open("/Users/yanqixu/Downloads/v2_iter_350000.log","r") as load_f:
 load_dict=json.load(load_f)
#print(load_dict["Image-tupu-2016-09-01-21-20-3374.jpg"])
#print (load_dict["Image-tupu-2016-09-01-21-20-3374.jpg"]["Top-1 Index"])

p1=input("P1:")
p2=input("P2:")

a=0
b=0

for name in load_dict:
# print (load_dict[name]["Confidence"][0])
 if load_dict[name]["Top-1 Index"] == p1:
  a=a+1
 
 if (load_dict[name]["Top-1 Index"] == p1) and (load_dict[name]["Confidence"][p1] > p2):
  b=b+1
  

print(a)
print(b)
