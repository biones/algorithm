
def count_inversenumber(array):

    if len(array)<=1:
        return array,0

    if len(array)==2:
        if array[0]<=array[1]:
            return (array,0)
        else:
            return ([array[1],array[0]],1)

    m=int(len(array)/2)
    nl=count_inv(array[:m])
    nr=count_inv(array[m:])

    A=[]
    Lsorted,cl=count_inv(array[:m])
    Rsorted,cr=count_inv(array[m:])

    count=cl+cr
    il=0
    ir=0
    while True:
        vl=Lsorted[il]
        vr=Rsorted[ir]
        if vl<vr:
            A.append(vl)
            il+=1
        else:
            A.append(vr)
            count+=1
            ir+=1

        if il==len(Lsorted):
            A.extend(Rsorted[ir:])
            break

        if ir==len(Rsorted):
            A.extend(Lsorted[il:])
            break

    return A,count

def merge_sort(array):

    if len(array)<=1:
        return array
    if len(array)==2:
        return sorted(array)


    m=int(len(array)/2)

    A=[]
    Lsorted=merge_sort(array[:m])
    Rsorted=merge_sort(array[m:])
    il=0
    ir=0

    while True:
        vl=Lsorted[il]
        vr=Rsorted[ir]
        if vl<vr:
            A.append(vl)
            il+=1
        else:
            A.append(vr)
            ir+=1

        if il==len(Lsorted):
            A.extend(Rsorted[ir:])
            break

        if ir==len(Rsorted):
            A.extend(Lsorted[il:])
            break


    return A

d=[9,6,7,2,5,1,8,4,2]
