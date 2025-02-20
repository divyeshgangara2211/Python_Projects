import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            data = json.load(file)
            if isinstance( data ,list ):
                return data
            else:
                return[]
    except(FileNotFoundError , json.JSONDecodeError):
        return []
        
# def load_data():
#     try:
#         with open('youtube.txt','r') as file:
#             return json.load(file)
#             # test = json.load(file)
#             # print(test)
#             # print(type(test))
#             # return test 
#     except FileNotFoundError:
#         #return ["22222"]
#         return []

def Save_Data(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file,indent = 4)  # indent =4 for better readability
        


def list_all_videos(videos):
    print("\n")
    print("*" * 50)

    if videos:
        print("List of all videos are below: \n")
        for index,video in enumerate(videos,start = 1):
            print(f"{index}] :- Name = {video['name']} & Time = {video['time']} minutes")
    else:
        print(" \n No Videos Found.")  

    # print("\n")
    print("*" * 50)


def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time(In minute): ")
    videos.append( { 'name': name , 'time': time } )    # [ {name:"",time:""} , {} , {} ]  aaa formate ma krvu che!!
    Save_Data(videos)
    print(" \n Your video was Added Sucessfullyy !!")

def update_video(videos):

    if videos:
        list_all_videos(videos)
        index = int(input("  Enter the video number to update: "))
        if 1 <= index <= len(videos):
            new_name = input("Enter the new video name: ")
            new_time = input("Enter the new video time: ")
        
            videos[index -1] = { 'name' : new_name , 'time' : new_time}
            Save_Data(videos)
            print(" \n  Video Updated Sucessfullyy !!")
        else:
            print(" \n Invalid video index selected.")

    else :
        return print(" \n No Videos Found.")  

   
def delete_video(videos):

    if videos:

        list_all_videos(videos)
        index = int(input("Enter the new video number to delete: "))
     
        if 1 <= index <= len(videos):
            del videos[index - 1]
            Save_Data(videos)
            print(" \n Video Deleted Sucessfully !!")
        else:
            print(" \n Invalid video index seleted. ")

    else :
        return print(" \n No Videos Found.")  




def main():
    videos = load_data()
    while True:
        print("\n Youtube Video Manager App | choose an option \n")
        print("1. List all Youtube videos")
        print("2. Add a Youtube video")
        print("3. Update a Youtube video details")
        print("4. Delete a Youtube video")
        print("5. Exit the app")
        print("\n")
        
        choise = input("Enter Your Choise :  ")  #notice we take input as string not convert in int
        #  print(videos)

        match choise:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case'4':
                delete_video(videos)
            case'5':
                print(" \n Sucessfulyy exited the app \n")
                break
            case _:
                print(" \n Invalid Choise")


if __name__ == "__main__":
    main()               

        

