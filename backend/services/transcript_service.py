from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    try:
        api = YouTubeTranscriptApi()

        transcript_list = api.list(video_id)

       
        try:
            transcript = transcript_list.find_manually_created_transcript(['en', 'hi'])
        except:
            transcript = transcript_list.find_generated_transcript(['en', 'hi'])

        data = transcript.fetch()

        return " ".join([t.text for t in data])

    except Exception as e:
        print("Transcript error:", e)
        return None