import sqlite3

con = sqlite3.connect("youtube_videos.db")

cursor = con.cursor()

cursor.execute(''' 
     CREATE TABLE IF NOT EXISTS videos(
               Id INTEGER PRIMARY KEY,
               Name TEXT NOT NULL,
               Time TEXT NOT NULL )
''')    #triple code ma lkhel nu formating as it is mle

# def list_all_videos():
#     print("\n")
#     print("*" * 50)
#     print("List of all videos are below: \n")
#     cursor.execute(" SELECT * FROM videos")
#     for row in cursor.fetchall():
#         print(row)
#         if len(videos) == 0 :
#             print("divyesh")
#             return []
#         else:
#             return print( f"{row[0]}] :- Name = {row[1]} & Time = {row[2]} ")
#             # print(row)
#             # print(type(row))
#     print("*" * 50)

def list_all_videos():
    print("\n")
    print("*"*50)
    cursor.execute("SELECT * FROM videos ")
    rows = cursor.fetchall()
 
    if len(rows) == 0:
        print("No Videos Found.")
    else:
        print("List of all videos are below: \n ")
        for row in rows:
            print(f"{row[0]}] :- Name = {row[1]} & Time = {row[2]} Minutes")
    print("*" * 50)


def add_videos():
    Name = input("Enter the video name : ")
    Time = input("Enter the video time (In Minutes): ")
    cursor.execute( "INSERT INTO videos (name , time ) VALUES (? , ?) " , ( Name , Time) ) 
    con.commit()
    print(" \n Your video was Added Sucessfullyy !!")

    
def update_videos():

    cursor.execute("SELECT * FROM videos ")
    rows = cursor.fetchall()
    
    # cursor.execute(" UPDATE videos SET(name , time) WHERE ID = ? " , ( New_name , New_time , Video_ID))
    
    if len(rows) == 0:
        print(" \n No Videos Found.")
    else:
        list_all_videos()

        Video_ID = int(input("Enter video ID which you want to update: "))
        New_name = input("Enter the video name : ")
        New_time = input("Enter the video time : ")
        cursor.execute(" UPDATE videos SET name = ? , time = ? WHERE ID = ? " , ( New_name , New_time , Video_ID))
        print(" \n  Video Updated Sucessfullyy !!")
    con.commit()
    

def delete_videos():

    cursor.execute("SELECT * FROM videos ")
    rows = cursor.fetchall()
    
    if len(rows) == 0:
        print(" \n No Videos Found.")
    else:
        list_all_videos()

        video_id = input("Enter video ID to delete: ")
        cursor.execute(" DELETE FROM videos WHERE id = ? " , ( video_id ,))  # ahi tuple j accept thay so single tuple lakhvani mathods "( video_id ,)"
        print(" \n Video Deleted Sucessfully !!")
    con.commit()

def main():
    while True:

        print(" \n Youtube Video Manager App With DB | Choose an Option \n ")
        print("1. List all Youtube videos")
        print("2. Add a Youtube video")
        print("3. Update a Youtube video details")
        print("4. Delete a Youtube video")
        print("5. Exit the app")
        print("\n")

        choise = input("Enter Your Choise: ")    #   Note take input as string 

        if choise == '1':
            list_all_videos()
        elif choise == '2':
            add_videos()                             
        elif choise == '3':
            update_videos()
        elif choise == '4':
            delete_videos()
        elif choise == '5':
            print(" \n Sucessfulyy exited the app \n")
            break
        else :
            print(" \n Invalid Choise")

    con.close()   # closed the connection because data currupt thata rokva mate (house kiping jevu )

if __name__ == "__main__":
    main()
