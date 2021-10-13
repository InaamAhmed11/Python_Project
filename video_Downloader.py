# from pytube import YouTube
#
# url = input("Please Enter The Url")
# my_video = YouTube(url)
# print(my_video.title)
# print(my_video.thumbnail_url)
# print("1) High Resolution \n2) low Resolution \n3) Audio")
# type1 = input("please Enter the number of the video type 1, 2, 3")
# if type1 == "1":
#     print("please wait for a few minutes")
#     my_video.streams.get_highest_resolution().download()
# elif type1 == "2":
#     print("please wait for a few minutes")
#     my_video.streams.get_lowest_resolution().download()
# elif type1 == "3":
#     print("please wait for a few minutes")
#     my_video.streams.filter(only_audio=True).first().download()
# else:
#     print("Invalid Input please check")
# print("file is downloaded successfully")




from pytube import YouTube

url = input('please enter the URl')
my_video = YouTube(url)
print(my_video.title)
print(my_video.thumbnail_url)
print("1) High Resolution \n2) Low Resolution \n3) Audio")
type1 = input("Please enter the number of the video like: 1, 2, 3")
if type1 == "1":
    print("please wait for a few minutes")
    my_video.streams.get_highest_resolution().download()
elif type1 == "2":
    print("please wait for a few minutes")
    my_video.streams.get_lowest_resolution().download()
elif type1 == "3":
    print("please wait for a few minutes")
    my_video.streams.get_audio_only().download()
else:
    print("Invalid input please check")
print("file is downloaded successfully")























