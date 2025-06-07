import os  # os functions
import check_camera
import capture_image
import train_image
import recognize


def title_bar():
    os.system('cls')
    print("\t***** Face Recognition Attendance System *****")


def mainMenu():
    title_bar()
    print()
    print(10 * "*", "WELCOME MENU", 10 * "*")
    print("[1] Check Camera")
    print("[2] Capture Faces")
    print("[3] Train Images")
    print("[4] Recognize & Attendance")
    print("[5] Quit")
    while True:
        try:
            choice = int(input("Enter Choice: "))
            if choice == 1:
                checkCamera()
                break
            elif choice == 2:
                CaptureFaces()
                break
            elif choice == 3:
                Trainimages()
                break
            elif choice == 4:
                recognizeFaces()
                break
            elif choice == 5:
                print("Thank You")
                break
            else:
                print("Invalid Choice. Enter 1-5")
                mainMenu()
        except ValueError:
            print("Invalid Choice. Enter 1-5\n Try Again")
    exit

# camera test function from check camera.py file


def checkCamera():
    check_camera.camer()
    # TODO: Unused variable, remove or use. # key = input("Enter any key to return main menu ")
    input("Enter any key to return main menu ")  # Keep the input call
    mainMenu()

# image function form capture image.py file


def CaptureFaces():
    capture_image.takeImages()
    # TODO: Unused variable, remove or use. # key = input("Enter any key to return main menu")
    input("Enter any key to return main menu")  # Keep the input call
    mainMenu()

# train images from train_images.py file


def Trainimages():
    train_image.TrainImages()
    # TODO: Unused variable, remove or use. # key = input("Enter any key to return main menu")
    input("Enter any key to return main menu")  # Keep the input call
    mainMenu()

# recognize_attendance from recognize.py file


def recognizeFaces():
    recognize.recognize_attendence()
    # TODO: Unused variable, remove or use. # key = input("Enter any key to return main menu")
    input("Enter any key to return main menu")  # Keep the input call
    mainMenu()


# main driver
mainMenu()
