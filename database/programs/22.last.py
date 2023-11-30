D={'PYTHON':198,'DBMS':167,'DSA':289,'CSA':278,'ARTIFICIAL INTELLIGENCE':190}
print(D)
keymax=max(zip(D.values(),D.keys()))[1]
print(keymax)
keymax=min(zip(D.values(),D.keys()))[1]
print(keymax)
print("The original dictionary is : " + str(D))
res = 0
for val in D.values():
    res += val
res = res / len(D)
print("The AVERAGE IS : " + str(res))