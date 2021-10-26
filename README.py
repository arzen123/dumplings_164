# dumplings_164
# vk parser comment
import requests 
 


def take_url(): 
    resource = 0 
    token = '1df1a4141df1a4141df1a414201d8864e611df11df1a4147c9f29385b778c0b84c75347' 
    verssion = 5.131 
    count = 100 
    url = input('domain or id - ') 
    if url.startswith("id"): 
        id = url.replace("id", "-")  
        response = requests.get('https://api.vk.com/method/wall.get?', 
                                params={ 
                                    'access_token': token, 
                                    'v': verssion, 
                                    'owner_id': id, 
                                    'count': count 
                                } 
                                ) 
    else: 
        domain = url 
        response = requests.get('https://api.vk.com/method/wall.get?', 
                                params={ 
                                    'access_token': token, 
                                    'v': verssion, 
                                    'domain': domain, 
                                    'count': count 
                                } 
                                ) 
        return response 
 
 
def take_posts(): 
    response = take_url() 
    posts = []
    try:
        data = response.json()
    except: 
        print('Странца закрыта для общего просмотра') 
        quit()
    
    count = data['response']['count'] 
    if count == 0: 
        print('нету постов или заблокирована стена') 
    else: 
        post = data['response']['items'] 
        posts.extend(post) 
    return posts 

 
def main(): 
    posts = take_posts() 
    count = 0 
    for comments_post in posts: 
        id = comments_post['owner_id'] 
        if 'attachments' not in comments_post:
            post_id = comments_post['id'] 
        elif 'copy_history' in comments_post:
            post_id = comments_post['id']
            print('It is copy post')    
        elif 'video' in comments_post['attachments'][0]['type']:
            post_id = comments_post['id']
            print('Post with video')
        elif 'audio' in comments_post['attachments'][0]['type']:
            post_id = comments_post['id']
            print('Post with audio')
        elif 'link' in comments_post['attachments'][0]['type']:
            post_id = comments_post['id']
            print('Post with link')
        elif 'post_id' not in comments_post['attachments'][0]['photo']:
            post_id = comments_post['id']
        else:
            post_id = comments_post['attachments'][0]['photo']['post_id'] 
        comments_post = comments_post['comments']['count'] 
        count = count + 1 
        if comments_post > 0: 
            print(f"\n Номер коменнтраия: {count} \n количество комментариве {comments_post}")
            take_comments_in_post(post_id, id)   
        else: 
            print(f"\n нету комментариев в посте {count} \n") 
    
    

def take_comments_in_post(post_id, id): 
    token = '1df1a4141df1a4141df1a414201d8864e611df11df1a4147c9f29385b778c0b84c75347' 
    verssion = 5.131 
    count = 100 
    response = requests.get('https://api.vk.com/method/wall.getComments?', 
                            params={ 
                                'access_token': token, 
                                'v': verssion, 
                                'count': count, 
                                'owner_id': id, 
                                'post_id': post_id 
                            } 
                            ) 
    
    data = response.json() 

    count = data['response']['count']
    if count != 0: 
        comments = data['response']['items'] 
        for comment in comments:
            comment = comment['text']
            print(f"Сам комментарий: {comment}")
    
 
if __name__ == "__main__": 
    main()
