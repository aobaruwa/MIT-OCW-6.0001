# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Ahmed Baruwa
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    
    def __init__(self, guid, title, description, link, pubdate):
        '''Initializes a NewsStory object
        A newsStory object has four attributes:
            self.guid(string, A globally unique identifier for this news story.)
            self.title(string, The news story's headline.)
            self.description(string, A paragraph or so summarizing the news story.)
            self.link(string, A link to a website with the entire story.)
            self.pubdate(dateTime,Date the news was published)
            '''
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):        
        return self.guid
    
    def get_title(self):        
        return self.title
    
    def get_description(self):        
        return self.description
    
    def get_link(self):        
        return self.link
    
    def get_pubdate(self):        
        return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    
    def __init__(self, phrase):

        self.phrase = phrase


        
    def is_phrase_in(self, text):
        mine = ''
        flag = [True]
        
        glean = "" # string of "text" stripped off of punctuations 
        for char in text.lower():
            if char in string.punctuation:
                glean += ' '
            else:
                glean += char
        mine =  ' '.join(glean.split())
        
        dict_mine = {} # stores the position of each word of phrase found in text
        mine_values = [] # holds all the values of dict_mine
        sorted_dict = [] # sorted mine_values
        
        # store the position of each word of phrase found in text!
        for word in self.phrase.lower().split():
            if word in mine.split():
                dict_mine[word] = mine.split().index(word) 
               
        for number in sorted(dict_mine.values()):
            sorted_dict.append(number)  
        for number in dict_mine.values():
            mine_values.append(number)
            
        # make sure all the words in phrase follow each other in text
        for i in range(len(mine_values) - 1):    
            if (mine_values[i + 1] - mine_values[i]) > 1:            
                flag.append(False)
        # check if the positions of all the words in phrase follow each other 
        if len(dict_mine.keys()) == len(self.phrase.lower().split()):
            if sorted_dict == mine_values:
                flag.append(True)
            else:
                flag.append(False)             
    
        # check if each word in phrase is even in the text
        for word in self.phrase.lower().split():
            if word in mine.split():
                flag.append(True)
            else:
                flag.append(False)
      
        # return False if there is any False whatsoever the flag List
        if min(flag) ==  True :
            return(True)
        else:
            return(False)




# Problem 3
# TODO: TitleTrigger

class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
    
    def evaluate(self, story):
        
        return self.is_phrase_in(story.get_title())
        
 
    

# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
    
    def evaluate(self, story):
        
        return self.is_phrase_in(story.get_description())
        

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, time_string):
        self.time = datetime.strptime(time_string, "%d %b %Y %H:%M:%S")
        
        
# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(Trigger):
    def __init__(self, time_string):
        TimeTrigger.__init__(self, time_string)
        
    def evaluate(self, story):
        
        return story.get_pubdate().replace(tzinfo=pytz.timezone("EST")) < self.time.replace(tzinfo=pytz.timezone("EST"))
    
class AfterTrigger(Trigger):
    def __init__(self, time_string):
        TimeTrigger.__init__(self, time_string)
        
    def evaluate(self, story):
        
        return story.get_pubdate().replace(tzinfo=pytz.timezone("EST")) > self.time.replace(tzinfo=pytz.timezone("EST"))

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, Trig):
        self.Trig = Trig

    def evaluate(self, story):
        
        return not self.Trig.evaluate(story)


# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, Trig1, Trig2):
        self.Trig1 = Trig1
        self.Trig2 = Trig2

    def evaluate(self, story):
        
        return self.Trig1.evaluate(story) and self.Trig2.evaluate(story)

# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, Trig1, Trig2):
        self.Trig1 = Trig1
        self.Trig2 = Trig2

    def evaluate(self, story):
        
        return self.Trig1.evaluate(story) or self.Trig2.evaluate(story)

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    filtered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) == True:
                filtered_stories.append(story)
                
    return filtered_stories
#    return stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("Artificial Intelligence")
        t2 = DescriptionTrigger("Robotics")
        t3 = DescriptionTrigger("Mobile Robots")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

