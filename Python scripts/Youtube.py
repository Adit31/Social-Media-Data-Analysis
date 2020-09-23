from googleapiclient.discovery import build
import pandas as pd

youTubeApiKey='A***aSyBtE***************A7eAIOjE'
youtube=build('youtube','v3',developerKey=youTubeApiKey)
channelId='UC_gUM8rL-Lrg6O3adPW9K1g'

statdata=youtube.channels().list(part='statistics',id=channelId).execute()

contentdata=youtube.channels().list(id=channelId,part='contentDetails').execute()
playlist_id = contentdata['items'][0]['contentDetails']['relatedPlaylists']['uploads']
videos = [ ]
next_page_token = None
while 1:
    res = youtube.playlistItems().list(playlistId=playlist_id,
                                               part='snippet',
                                               maxResults=50,
                                               pageToken=next_page_token).execute()
    videos += res['items']
    next_page_token = res.get('nextPageToken')
    if next_page_token is None:
        break

video_ids = list(map(lambda x:x['snippet']['resourceId']['videoId'], videos))
stats = []
for i in range(0, len(video_ids), 40):
    res = (youtube).videos().list(id=','.join(video_ids[i:i+40]),part='statistics').execute()
    stats += res['items']

title=[ ]
liked=[ ]
disliked=[ ]
views=[ ]
url=[ ]
comment=[ ]

for i in range(len(videos)):
      title.append((videos[i])['snippet']['title'])
      url.append("https://www.youtube.com/watch?v="+(videos[i])['snippet']['resourceId']['videoId'])
      liked.append(int((stats[i])['statistics']['likeCount']))
      disliked.append(int((stats[i])['statistics']['dislikeCount']))
      views.append(int((stats[i])['statistics']['viewCount']))
      if 'commentCount' not in (stats[i])["statistics"]:
                    comment.append(0)
      else:
          comment.append(int((stats[i])['statistics']['commentCount']))

data={'title':title,'url':url,'liked':liked,'disliked':disliked,'views':views,'comment':comment}
df=pd.DataFrame(data)

df.to_csv('C:\\Users\\aditg\\Desktop\\youtube_data.csv', header = False, mode = 'a')