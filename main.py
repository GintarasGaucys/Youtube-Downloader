from pytube import YouTube

link = input("Link: ")
yt = YouTube(link)

print ('Title: ', yt.title)
answer1 = input ('Is this video correct? Y/N ')
#if (answer1.lower == 'n'):
    #exit()
answer2 = input ('MP3 only mode? Y/N ')
if (answer2.lower() == 'n'):
    video = yt.streams.get_highest_resolution()
    print('Downloading')
    video.download('Downloads')
    print('Download complete')
elif (answer2.lower() == 'y'):
    video = yt.streams.get_audio_only()
    print('Downloading')
    video.download('Downloads')
    print('Download complete')

