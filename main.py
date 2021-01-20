from bs4 import BeautifulSoup
import requests
import os

#This program will use mangakakalot to get manga from because I don't know how to use mangadex

#Get url to search
def urlReturn(searchQuery):
    searchQuery = searchQuery.replace(" ","_")
    url = f'https://mangakakalot.com/search/story/{searchQuery}'
    return url

