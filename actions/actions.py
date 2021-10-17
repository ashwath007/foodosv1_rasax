import requests
import json
import os
import sqlite3

import datetime as dt 
from typing import Any, Text, Dict, List,Optional

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import UserUttered, FollowupAction, BotUttered

NODE_SERVER = "http://localhost:8000/rasaapi"


# class ActionHelloWorld(Action):
    
#     def name(self) -> Text:
#         return "action_show_time"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text=f"{dt.datetime.now()}")

#         return []


class ActionGetFood(Action):
    
    def name(self) -> Text:
        return "action_getfood"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            is_user = requests.post(NODE_SERVER+"/user/exist", json = {'chatId':tracker.sender_id })
            # is_user = requests.post(NODE_SERVER+"/user/exist", json = {'chatId':'918072002769@c.us'})
            # print(is_user.text)
            is_user = is_user.json()
            # print(is_user)
            # print(is_user['user_data']['profile_completed'] == True)
            if(is_user['is_exist'] == True):
                # dispatcher.utter_message(text="Hi "+is_user['user_data']['name'])
                dispatcher.utter_message(text=is_user['user_data']['name']+" you can order form here - "+" \n \n http://localhost:3000/menu/bot/:botId/need/menu/user/{}".format(is_user['user_data']['_id']))

                # print(is_user)
                # print(is_user['user_data'])
                # print(is_user['user_data']['name'])
                # print(is_user['user_data']['profile_completed'] == 'True')
                # if(is_user['user_data']['profile_completed'] == True):
                #     dispatcher.utter_message(text="Your can order form here - "+"http://localhost:3000/menu/bot/:botId/need/menu/user/" + is_user['user_data']['_id'])
                # elif(is_user['user_data']['profile_completed'] == 'False'):
                    # here triger intent to ask user location to comple profile
            else:
                print("*Here")
                # response = requests.post("http://localhost:5005/webhooks/rest/webhook",
                #                          json={"name": "formgenerate"}, headers={"Content-Type": "application/json"})
                # return [UserUttered("/profile_form_generate", {
                #      "intent": {"confidence": 1, "name": "profile_form_generate"}, 
                #      "entities": []
                #     })]                         
                # print(response.text)
                mesg = "We hope you are new to our platform, Just a quick walkthrough \n \n Type ```signup``` or ```login or sign in``` to create an account, and \n \n Type ```Profile``` to view your profile"
                dispatcher.utter_message(text=mesg)
                
                # UserUttered("/asks_for_person_search_with_provided_name",intent={'name': 'asks_for_person_search_with_provided_name', 'confidence': 1.0}),
                    # response = requests.post("http://localhost:5005/conversations/{tracker.sender_id}/trigger_intent",
                    #                      json={"name": "profile"}, headers={"Content-Type": "application/json"})
                    # print(response)


            return []


class ShowMenu(Action):
    
    def name(self) -> Text:
        return "action_show_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # entities = tracker.latest_message['entities']


        # print("User Id : {}".format(tracker.sender_id))
        
        
        message = "Please order here - LINK"
        dispatcher.utter_message(text=message)

        return []


class ShowQuickMenu(Action):
    
    def name(self) -> Text:
        return "action_quick_show_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # entities = tracker.latest_message['entities']
        # print(entities[0]['value'])
        # print(entities)
        print("User Id : {}".format(tracker.sender_id))
        
        
        message = "Quick Menu"
        dispatcher.utter_message(text=message)

        return []




class UserProfileForm(FormValidationAction):
    
    def name(self) -> Text:
        return "action_user_profile_form"
    
    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
    
        print("User Profile Form")
        name = tracker.get_slot("user_name")
        age = tracker.get_slot("user_age")
        sex = tracker.get_slot("user_sex")
        print(name)
        print(tracker.sender_id)
        print(age,sex)
        r = requests.post(NODE_SERVER+'/user/create/profile',
        json = {'userId':tracker.sender_id, 'name':name, 'age':age, 'sex':sex})
        
        print("Response: {}".format(r.text))
        # conn = sqlite3.connect('user.db')
        dispatcher.utter_message(text="Can you share your Loaction in Watsapp?")
        return []

class AlreadyaUser(Action):
    def name(self) -> Text:
        return "action_already_user"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            is_user = requests.post(NODE_SERVER+"/user/exist", json = {'chatId':tracker.sender_id })
            # is_user = requests.post(NODE_SERVER+"/user/exist", json = {'chatId':'918072002769@c.us'})
            # print(is_user.text)
            is_user = is_user.json()
            # print(is_user)
            # print(is_user['user_data']['profile_completed'] == True)
            if(is_user['is_exist'] == True):
                # dispatcher.utter_message(text="Hi "+is_user['user_data']['name'])
                dispatcher.utter_message(text=is_user['user_data']['name']+" you can order form here - "+" \n \n http://localhost:3000/menu/bot/:botId/need/menu/user/{}".format(is_user['user_data']['_id']))

                # print(is_user)
                # print(is_user['user_data'])
                # print(is_user['user_data']['name'])
                # print(is_user['user_data']['profile_completed'] == 'True')
                # if(is_user['user_data']['profile_completed'] == True):
                #     dispatcher.utter_message(text="Your can order form here - "+"http://localhost:3000/menu/bot/:botId/need/menu/user/" + is_user['user_data']['_id'])
                # elif(is_user['user_data']['profile_completed'] == 'False'):
                    # here triger intent to ask user location to comple profile
            else:
                print("*Here")
                # response = requests.post("http://localhost:5005/webhooks/rest/webhook",
                #                          json={"name": "formgenerate"}, headers={"Content-Type": "application/json"})
                # return [UserUttered("/profile_form_generate", {
                #      "intent": {"confidence": 1, "name": "profile_form_generate"}, 
                #      "entities": []
                #     })]                         
                # print(response.text)
                mesg = "We hope you are new to our platform, Just a quick walkthrough \n \n Type ```signup``` or ```login or sign in``` to create an account, and \n \n Type ```Profile``` to view your profile"
                dispatcher.utter_message(text=mesg)
                
                # UserUttered("/asks_for_person_search_with_provided_name",intent={'name': 'asks_for_person_search_with_provided_name', 'confidence': 1.0}),
                    # response = requests.post("http://localhost:5005/conversations/{tracker.sender_id}/trigger_intent",
                    #                      json={"name": "profile"}, headers={"Content-Type": "application/json"})
                    # print(response)


            return []



# Order business Login Here

class ShowUserOrders(Action):
    def name(self) -> Text:
        return "show_order_in_chat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


            user_details = requests.post(NODE_SERVER+'/user/getalldata',json = {'chatId':tracker.sender_id})
            # user_details = requests.post(NODE_SERVER+'/user/getalldata',json = {'chatId':'918072002769@c.us'})
            user_details = user_details.json()
            # print(user_details['user_data']['_id'])
            r = requests.post(NODE_SERVER+'/user/create/showOrder',json = {'userId':user_details['user_data']['_id']})
            # r = requests.post(NODE_SERVER+'/user/create/showOrder',json = {'chatId':'918072002769@c.us'})
            r = r.json()
            # print("Orders {}".format(r))
            # print(r['order_data']['productData'])
            print(len(r['order_data']['productData'][0]))
            
            order_bill = " 👉 Item {} \n🍲Food Name: {}\n🧂Qty: {}\n💵Price : {} \n "
            order_bill_list = []
            for i in range(len(r['order_data']['productData'][0])):
                order_bill_list.append(order_bill.format(str(i),r['order_data']['productData'][0][i]['product']['name'],str(r['order_data']['productData'][0][i]['qty'][0]),str(r['order_data']['productData'][0][i]['product']['price'])))
                print(order_bill_list)
            order_details_here = " \t\t 🧢 Your Order - {}, Here we go ✔️ \n \n".format(r['order_data']['orderId'])
            total_price = " \n \n-------------------- \n 💸 Total Price: ₹{} \n 💰 Delivery Charge: ₹50 \n --------------------".format(r['order_data']['totalPrice'])
            order_bill_list.append(total_price)
            order_bill_list.insert(0,order_details_here)
            order_bill_list.append(" \n \n 😺 Shall we confirm the above order 😁? \n")
            order_bill = "".join(order_bill_list)
            print(order_bill)
            dispatcher.utter_message(text=order_bill)
            # Here we need to handle more than 2 orders
            return []


# Asking Payment method here

class ActionGetUserDeliveryOrders(Action):

    def name(self) -> Text:
        return "action_payment_options"

    def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            entities = tracker.latest_message['entities']
            print(entities[0]['value'])
            if(entities[0]['value'] == 'Cash' or entities[0]['value'] == 'cash'):
                dispatcher.utter_message(text="🛵 Please tell your delivery location🚏, Share it though WhatApp location 📍")
            if(entities[0]['value'] == 'Card' or entities[0]['value'] == 'card'):
                user_details = requests.post(NODE_SERVER+'/user/getalldata',json = {'chatId':tracker.sender_id})
                user_details = user_details.json()
                r = requests.post(NODE_SERVER+'/user/create/showOrder',json = {'userId':user_details['user_data']['_id']})
                r = r.json()
                total_price = "\n \n _Can you send  💸 *Total Price: ₹{}*_ ".format(r['order_data']['totalPrice'])
                dispatcher.utter_message(text=total_price)
                # print("Orders {}".format(r))
                # print(r['order_data']['productData'])
            print(entities)
            print("User Id : {}".format(tracker.sender_id))
            
            # message = "Please select from the hotels to order briyani following menu - https://www.swiggy.com/restaurants"
            # dispatcher.utter_message(text=message)

            return []


# class ActionDummy(Action):
    
#     def name(self) -> Text:
#         return "action_payment_options"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         entities = tracker.latest_message['entities']
#         # print(entities[0]['value'])
#         print(entities)
#         print("User Id : {}".format(tracker.sender_id))
        
#         message = "Please select from the hotels to order briyani following menu - https://www.swiggy.com/restaurants"
#         dispatcher.utter_message(text=message)

#         return []



class ActionAboutFoodos(Action):
    
    def name(self) -> Text:
        return "action_about_foodos"
    
    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        FollowupAction(name="utter_what_you_can_help_with_order")
        BotUttered(text = "okok, so briyani venumaa, illa roti, naan with butter gravy ?? any plan, offer iruku pa")

        dispatcher.utter_message(text="Hi Im Sara, I can help you with day-to-day services like food, grocery delivery and I can handle transport too. I can be your assistant too. \n \n  briyani sudaa🔥 iruku, u want ???, illa 🍗 grill?? 🍖 ")
        return []