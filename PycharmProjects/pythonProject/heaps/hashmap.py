class map:
    def __init__(self,size):
        self.size=size
        self.ht=self.createbucket()
    def createbucket(self):
        return [[] for _ in range(self.size)]

    def set_val(self,key,val):
        hkey=hash(key)%self.size
        bucket=self.ht[hkey]

        flag = True
        for i,r in enumerate(bucket):
            r_key,r_val=r
            if r_key==key:
                flag=True
                break
        if flag:
            bucket[i]=(key,val)
        else:
            bucket.append((key,val))