
def replicate(times, number):
    if times=0:
        return [number]
    else times>0:
        replicate(times, number)
        times-1
        
