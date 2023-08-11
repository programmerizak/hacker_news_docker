from django.core.management.base import BaseCommand, CommandError
from datetime import timedelta, time, datetime
from django.utils import timezone
from django.utils.timezone import make_aware
import requests,datetime


from items.models import Item



BASE_API_URL = "https://hacker-news.firebaseio.com/v0"

# Get the item detail using the ID
def get_item(item_id):
    item = requests.get(f"{BASE_API_URL}/item/{item_id}.json")
    return item.json()

# Get items
def get_stories(story_type, count=3):
    story_items = requests.get(f"{BASE_API_URL}/{story_type}.json")
    top_story_ids = story_items.json()[:count]
    
    stories = []
    for story_id in top_story_ids:
        stories.append(get_item(story_id))
    
    return stories



def store_latest_items(story_type, count=3):
    
    stories = get_stories(story_type, count)
    
    for story in stories:
        api_item_id = story.get('id', '')  # Get the API item ID
        item, created = Item.objects.get_or_create(api_item_id=api_item_id, defaults={
            'title': story.get('title', ''),
            'url': story.get('url', ''),
            'text': story.get('text', ''),
            'api_item_id': story.get('id', ''),
            'score': story.get('score', 0),
            'item_creator': story.get('by', ''),
            'date_created': timezone.make_aware(datetime.datetime.fromtimestamp(story.get('time')), 
                    timezone.get_current_timezone()),
            'item_type': story_type,
            'is_api_post':True,
        })
        
        if not created:
            # Update the existing item
            item.title = story.get('title', '')
            item.url = story.get('url', '')
            item.text = story.get('text', '')
            item.score = story.get('score', 0)
            item.item_type = story_type
            item.save()


        kids_ids = story.get('kids', [])  # Get the kids' IDs list
        
        # Create and save the "kid" items in the model
        for kid_id in kids_ids:
            kid_story = get_item(kid_id)  # Retrieve the kid item details from the API
            
            kid_item, _ = Item.objects.get_or_create(api_item_id=kid_id, defaults={
                'title': kid_story.get('title', ''),
                'item_creator': kid_story.get('by', ''),
                'date_created': timezone.make_aware(datetime.datetime.fromtimestamp(kid_story.get('time')), 
                    timezone.get_current_timezone()),
                'text': kid_story.get('text', ''),
                'api_item_id': kid_story.get('id', ''),
                'is_api_post':True,
                'item_type': 'comment',  # Set the item_type for kid items
                'parent_item': item,  # Establish the ForeignKey relationship
                
            })
            
            # Update the existing "kid" item if necessary
            if not kid_item == created:
                kid_item.title = kid_story.get('title', '')
                kid_item.item_creator = kid_story.get('by', '')
                kid_item.text = kid_story.get('text', '')
                kid_item.api_item_id = kid_story.get('id', '')
                kid_item.date_created = timezone.make_aware(datetime.datetime.fromtimestamp(kid_story.get('time')), 
                    timezone.get_current_timezone())
                kid_item.item_type = 'comment'  # Set the item_type for kid items
                kid_item.parent_item = item  # Establish the ForeignKey relationship
                # Update other attributes as needed
                kid_item.save()     



class Command(BaseCommand):
    help = "Make request to Hacker News API and Update our models"

    def handle(self, *args, **options):
        store_latest_items("topstories", 100)  # Top stories
        store_latest_items("askstories", 100)  # Ask stories
        store_latest_items("showstories", 100) # Show stories
        store_latest_items("jobstories", 100)  # Job stories
        self.stdout.write("Items were updated successfully ")
