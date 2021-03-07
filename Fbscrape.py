# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 22:49:30 2020

@author: becky
"""


import requests
import json
import sys
import time
from importlib import reload
'''
reloading sys for utf8 encoding is for Python 2.7
This line should be removed for Python 3
In Python 3, we need to specify encoding when open a file
f = open("file.csv", encoding='utf-8')
'''
reload(sys)
sys.setdefaultencoding('utf8')

class FacebookScraper:
    '''
    FacebookScraper class to scrape facebook info
    '''

    def __init__(self, token):
        self.token = token

    @staticmethod
    def convert_to_epochtime(date_string):
        '''Enter date_string in 2000-01-01 format and convert to epochtime'''
        try:
            epoch = int(time.mktime(time.strptime(date_string, '%Y-%m-%d')))
            return epoch
        except ValueError:
            print('Invalid string format. Make sure to use %Y-%m-%d')
            quit()

    def get_feed_data(self, target_page, offset, fields, json_path, date_string):
        """
        This method will get the feed data
        """
        url = "https://graph.facebook.com/v2.10/{}/feed".format(target_page)
        param = dict()
        param["access_token"] = self.token
        param["limit"] = "100"
        param["offset"] = offset
        param["fields"] = fields
        param["since"] = self.convert_to_epochtime(date_string)

        r = requests.get(url, param)
        data = json.loads(r.text)
        f = open(json_path, "w")
        f.write(json.dumps(data, indent=4))
        print("json file has been generated")

        f.close()

        return data
   
    def create_table(self, list_rows, file_path, page_name, table_name):
        '''This method will create a table according to header and table name'''

        if table_name == "feed" :
            header = ["page_name", "id", "type", "created_time", "message", "name",\
            "description", "actions_link", "actions_name", "share_count",\
            "comment_count", "like_count"]
        elif table_name == "likes":
            header = ["page_name", "post_id", "user_id", "name"]
        elif table_name == "comments":
            header = ["page_name", "post_id", "created_time", "message",\
             "user_id", "name", "message_id"]
        else:
            print("Specified table name is not valid.")
            quit()

        file = open(file_path, 'w')
        file.write(','.join(header) + '\n')
        for i in list_rows:
            file.write('"' + page_name + '",')
            for j in range(len(i)):
                row_string = ''
                if j < len(i) -1 :
                    row_string += '"' + str(i[j]).replace('"', '').replace('\n', '') + '"' + ','
                else:
                    row_string += '"' + str(i[j]).replace('"', '').replace('\n', '') + '"' + '\n'
                file.write(row_string)
        file.close()
        print("Generated {} table csv File for {}".format(table_name, page_name))

    def convert_feed_data(self, response_json_list):
        '''This method takes response json data and convert to csv'''
        list_all = []
        for response_json in response_json_list:
            data = response_json["data"]

            for i in range(len(data)):
                list_row = []
                row = data[i]
                id = row["id"]
                try:
                    type = row["type"]
                except KeyError:
                    type = ""
                try:
                    created_time = row["created_time"]
                except KeyError:
                    created_time = ""
                try:
                    message = row["message"]
                except KeyError:
                    message = ""
                try:
                    name = row["name"]
                except KeyError:
                    name = ""
                try:
                    description = row["description"]
                except KeyError:
                    description = ""
                try:
                    actions_link = row["actions"][0]["link"]
                except KeyError:
                    actions_link = ""
                try:
                    actions_name = row["actions"][0]["name"]
                except KeyError:
                    actions_name = ""
                try:
                    share_count = row["shares"]["count"]
                except KeyError:
                    share_count = ""
                try:
                    comment_count = row["comments"]["summary"]["total_count"]
                except KeyError:
                    comment_count = ""
                try:
                    like_count = row["likes"]["summary"]["total_count"]
                except KeyError:
                    like_count = ""
               
                list_row.extend((id, type, created_time, message, name, \
                description, actions_link, actions_name, share_count, comment_count, like_count))
                list_all.append(list_row)
       
        return list_all
   
    def convert_likes_data(self, response_json_list):
        '''This will get the list of people who liked post,
        which can be joined to the feed table by post_id. '''
        list_all = []
        for response_json in response_json_list:
            data = response_json["data"]
            # like_list = []
            for i in range(len(data)):
                likes_count = 0
                row = data[i]
                post_id = row["id"]
                try:
                   like_count = row["likes"]["summary"]["total_count"]
                except KeyError:
                    like_count = 0
                if like_count > 0:
                    likes = row["likes"]["data"]
                    for like in likes:
                        row_list = []
                        user_id = like["id"]
                        name = like["name"]
                        row_list.extend((post_id, user_id, name))
                        list_all.append(row_list)
                # Check if the next link exists
                try:
                    next_link = row["likes"]["paging"]["next"]
                except KeyError:
                    next_link = None
                    continue

                if next_link is not None:
                    r = requests.get(next_link.replace("limit=25", "limit=100"))
                    likes_data = json.loads(r.text)
                    while True:
                        for i in range(len(likes_data["data"])):
                            row_list = []
                            row = likes_data["data"][i]
                            user_id = row["id"]
                            name = row["name"].encode("latin1", "ignore")
                            row_list.extend((post_id, user_id, name))
                            list_all.append(row_list)
                        try:
                            next = likes_data["paging"]["next"]
                            r = requests.get(next.replace("limit=25", "limit=100"))
                            likes_data = json.loads(r.text)
                        except KeyError:
                            print("Likes for the post {} completed".format(post_id))
                            break
        return list_all

    def convert_comments_data(self, response_json_list):
        '''This will get the list of people who commented on the post,
        which can be joined to the feed table by post_id. '''
        list_all = []
        for response_json in response_json_list:
            data = response_json["data"]
            # like_list = []
            for i in range(len(data)):
                likes_count = 0
                row = data[i]
                post_id = row["id"]
                try:
                   comment_count = row["comments"]["summary"]["total_count"]
                except KeyError:
                    comment_count = 0
                if comment_count > 0:
                    comments = row["comments"]["data"]
                    for comment in comments:
                        row_list = []
                        created_time = comment["created_time"]
                        message = comment["message"].encode('latin1', 'ignore')
                        user_id = comment["from"]["id"]
                        name = comment["from"]["name"].encode('latin1', 'ignore')
                        message_id = comment["id"]
                        row_list.extend((post_id, created_time, message,\
                        user_id, name, message_id))
                        list_all.append(row_list)
               
                # Check if the next link exists
                try:
                    next_link = row["comments"]["paging"]["next"]
                except KeyError:
                    next_link = None
                    continue
               
                if next_link is not None:
                    r = requests.get(next_link.replace("limit=25", "limit=100"))
                    comments_data = json.loads(r.text)
                    while True:
                        for i in range(len(comments_data["data"])):
                            row_list = []
                            comment = comments_data["data"][i]
                            created_time = comment["created_time"]
                            message = comment["message"].encode('latin1', 'ignore')
                            user_id = comment["from"]["id"]
                            name = comment["from"]["name"].encode('latin1', 'ignore')
                            message_id = comment["id"]
                            row_list.extend((post_id, created_time, message,\
                            user_id, name, message_id))
                            list_all.append(row_list)
                        try:
                            next = comments_data["paging"]["next"]
                            r = requests.get(next.replace("limit=25", "limit=100"))
                            comments_data = json.loads(r.text)
                        except KeyError:
                            print("Comments for the post {} completed".format(post_id))
                            break
        return list_all

if __name__ == "__main__":

    token_input = sys.argv[1]
    target_page_input = sys.argv[2]
    json_path_input = sys.argv[3]
    csv_feed_path_input = sys.argv[4]
    csv_likes_path_input = sys.argv[5]
    csv_comments_path_input = sys.argv[6]
    date_since_input = sys.argv[7]
    # Input check
    print(token_input)
    print(target_page_input)
    field_input = 'id,created_time,name,message,comments.summary(true),\
    shares,type,published,link,likes.summary(true),actions,place,tags,\
    object_attachment,targeting,feed_targeting,scheduled_publish_time,\
    backdated_time,description'

    fb = FacebookScraper(token_input)

    offset = 0
    json_list = []
    while True:
        path = str(offset) + "_" + json_path_input
        try:
            data = fb.get_feed_data(target_page_input, str(offset), field_input, path, date_since_input)
            check = data['data']
            if (len(check) >= 100):
                json_list.append(data)
                offset += 100
            else:
                json_list.append(data)
                print("End of loop for obtaining more than 100 feed records.")
                break
        except KeyError:
            print("Error with get request.")
            quit()

    feed_table_list = fb.convert_feed_data(json_list)
    likes_table_list = fb.convert_likes_data(json_list)
    comments_table_list = fb.convert_comments_data(json_list)
    # Record check
    print(feed_table_list[0])
    print(likes_table_list[0])
    print(comments_table_list[0])

    fb.create_table(feed_table_list, csv_feed_path_input, target_page_input, "feed")
    fb.create_table(likes_table_list, csv_likes_path_input, target_page_input, "likes")
    fb.create_table(comments_table_list, csv_comments_path_input, target_page_input, "comments")