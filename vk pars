from tkinter import *
from turtle import width
import requests
from tkinter import messagebox

token = '1df1a4141df1a4141df1a414201d8864e611df11df1a4147c9f29385b778c0b84c75347' 
verssion = 5.131 
count = 100

def get_url():  
    url = urll.get()
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

def get_comment_post(post_id, id): 
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

    count_comments = data['response']['count']
    if count_comments: 
        comments = data['response']['items'] 
        for comment in comments:
            comment = comment['text']
            coment_listbox.insert(END, f"Сам комментарий: {comment}")


def get_posts(): 
    response = get_url() 
    try:
        data = response.json()
    except:
        messagebox.showinfo("GUI Python", 'errror')
        
    if 'response' in data:
        if data['response']['count'] == 0: 
            messagebox.showinfo("GUI Python", 'нету постов или заблокирована стена')
             
        else: 
            posts = data['response']['items']     
        return posts 
    else:
        Error = data['error']['error_msg']
        messagebox.showinfo("GUI Python", Error)


def main(): 
    posts = get_posts() 
    counter = 0 
    for post in posts: 
        id = post['owner_id'] 
        if 'attachments' not in post or 'copy_history' in post or 'video' in post['attachments'][0]['type'] \
            or 'audio' in post['attachments'][0]['type'] or 'link' in post['attachments'][0]['type'] \
                or 'post_id' not in post['attachments'][0]['photo']:
            post_id = post['id'] 
        else:
            post_id = post['attachments'][0]['photo']['post_id'] 
        comments_count = post['comments']['count'] 
        counter = counter + 1 
        if comments_count > 0: 
            coment_listbox.insert(END, f"\n Номер поста: {counter} \n количество комментариве {comments_count}")
            get_comment_post(post_id, id)   
        else: 
           coment_listbox.insert(END, f"\n нету комментариев в посте {counter} \n") 


def delete():
    coment_listbox.delete(0, END)

root = Tk()
root.title('Берет коменты вк')
root.geometry('500x300')

urll = StringVar()

url_label = Label(text='Ввидите domain или id vk')
url_label.grid(row=0, column=0, padx=5, pady=5)

url_entry = Entry(textvariable=urll, width=65)
url_entry.grid(row=1,column=0, padx=5, pady=5)

btn = Button(text="Выполнить", command=main)
btn.grid(row=1, column=1)

scrollbar = Scrollbar(root)
scrollbar.grid(row=3, column=0)

coment_listbox = Listbox(xscrollcommand=scrollbar.set)
coment_listbox.grid(row=2, column=0, columnspan=2, sticky=W+E, padx=5, pady=5)
scrollbar.config(command=coment_listbox.yview)

delete_button = Button(text="Удалить", command=delete).grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
