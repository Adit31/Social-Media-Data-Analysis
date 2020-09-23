import facebook
import json

token = 'EAAlrMhVkHZBkBABZAnHF0oZCsL*********************************1AfZC9k8rZADXtFX6LEW7P4x9mz0GMZAvR4CNNaw8tD90By1f4f0g*******************************************************5blNXTrHUxCxXFKJ8ZD'

graph = facebook.GraphAPI(token)

#profile = graph.get_object('me',fields='first_name,location,link,email')
#events = graph.request('/search?q=news&type=event&limit=100')
#graph.request("search", {'q' : 'social web', 'type' : 'page'})

user_id = '2068790616585272' # the id of the Facebook user
name = graph.get_object(user_id)["name"]
print (name)

