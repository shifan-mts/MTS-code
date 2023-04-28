import pytube
link = str(input("paste the link"))
myvid = pytube.YouTube(link)
print(myvid.title)
streams = myvid.streams.get_highest_resolution()
streams.download("/home/shifan")