import feedparser
import json

def download_rss_to_json(url, output_file):
    # Download the RSS feed
    feed = feedparser.parse(url)
    json_dict = dict()
    json_dict['entries'] = []
    json_dict['feed'] = dict()
    json_dict['feed'] = feed.feed.copy()
    
    # Convert the feed entries to JSON
    for entry in feed.entries:
        temp_dict = dict()
        temp_dict = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
            'published_parsed': entry.published_parsed,
            'summary': entry.summary,
            'summary_detail': entry.summary_detail.type,
            'author': entry.author,
            'image': entry.image.href,
            'id' : entry.id,
            'itunes_duration': entry.itunes_duration,
          # Add more fields as needed
        }

        for media in entry.media_content:
            if 'audio' in media['type'].lower():
                temp_dict['audio']=media['url']
            if 'video' in media['type'].lower():
                temp_dict['video']=media['url']
            if 'image' in media['type'].lower():
                temp_dict['image']=media['url']
        for key in entry.keys():
            if 'transcript' in key.lower():
                temp_dict['transcript_url']=entry[key]['url']
                temp_dict['transcript_type']=entry[key]['type']
            
            
        json_dict['entries'].append(temp_dict)

    # Write the JSON data to a file
    with open(output_file, 'w') as f:
        json.dump(json_dict, f, indent=2)

# Example usage
rss_url = 'https://omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/E5F91208-CC7E-4726-A312-AE280140AD11/D64F756D-6D5E-4FAE-B24F-AE280140AD36/podcast.rss'
output_file = 'output.json'
download_rss_to_json(rss_url, output_file)