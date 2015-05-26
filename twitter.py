## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.
File:   tweetId: Long,  parentTweetId: Long

Find 10 tweets with most replies?

tweetId,parentTweetId
10 2
11 2
2  1
3  1
5  3


select parentTweetId,count(tweetId) from tweet group by parentTweetId order by count(tweetId) desc limit 10

a=data.frame([10,2],[11,2],[2,1])
b=data.frame()

a.columns=['tweetId','parentTweetId']
count=1

b=unique(a['parentTweetId']),0

sort(a[parentTweetId])

for i in range(len(parentTweetId)-1):
    if(parentTweetId[i]==parentTweetId[i+1]):
        ++count
        b[parentId==parentTweetId[i]][count]=count
     else: count=1
        #b[parentId==parentTweetId[i+1]][count]=1
sort(b[count])

parentTweetId,count
2 2
1 2
3 1  

nlogn+n2