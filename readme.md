<p align="center"><img src="/readme/GreenSync.png" height="400" alt="GreenSync logo" /></p>
<h1 align="center">GreenSync - A Reliable Collaboration Tool For Shared Project Files!</h1>

GreenSync was born in the wake of the now-defunct GrabCAD Workbench, a once-popular cloud-based platform that allowed engineering teams to collaborate effortlessly on CAD projects. Since GrabCAD shut down in 2023 no comfortable replacement emerged, and the absence of a simple and reliable way to collaborate work on shared files affected my own life, So… that's how we got here.

GreenSync is a practical solution made from a couple of lightweight Python scripts, a clear setup guide, the excellent FreeFileSync (FFS) tool for file synchronization, and Google Drive as the remote storage server.

Setup is simple and designed to be shared across team members for a smooth, unified experience. a single person can configure GreenSync for an entire team, and everyone else can immediately collaborate using the same configurations.

GreenSync supports all the essential and intuitive operations needed for collaborative work: **Upload, Download, Undo Local Changes**—so you can update your project files quickly, confidently, and get back to work faster.

Greensync was made in cooperation with robotics team [#4590 GreenBlitz](https://www.facebook.com/GreenBlitz4590/) from Israel. [<img width="150" alt="Greenblitz" src="https://github.com/user-attachments/assets/0fed0fb4-fe5b-46b6-9a1c-cc7dbfa214c5" >](https://www.facebook.com/GreenBlitz4590/)

---

* GreenSync will work with Cad files... **or any other type of file**. It should be useful for many collaborative projects where file synchronization is needed.
* FreeFileSync is available for Windows, macOS and Linux, 
* GreenSync's python scripts are precompiled for the same operation systems, get them from the [release page](https://github.com/lshachar/GreenSync/releases) (or install Python and run the scripts directly).
* If you're running Linux / macOS, you should change windows style backslashes `\` into forward slashes `/` in `greensync_config.yaml`.
* Remote syncing destinations options: Google drive, a local folder / network folder, or a folder on an FTP server.
* Multiple configuration files could be saved and used individually for different projects, users, and remote syncing destinations.
* Published under GNU GPLv3

---

[<img width="100" alt="Watch the video tutorials on YouTube" src="https://github.com/user-attachments/assets/61b3791e-214e-454b-8a06-6b17c4300d6a" >](https://www.youtube.com/playlist?list=PLB7_MxikWTNoCSxZbEPRPo8c0aFSEUMVV)   **Click to watch the video tutorials on YouTube**

---

## [A Quick How To Use GreenSync Guide](https://github.com/lshachar/GreenSync/blob/master/readme/How%20To%20Use%20GreenSync.md)
A step-by-step guide. Best to start here. In only a few minutes you'll have everything up and running.

---

## [The four default operations explained with images](https://github.com/lshachar/GreenSync/blob/master/readme/Default%20Operations.md)

One case example with only a few changed files. Explains how each possible operation affects how the files will be synchronized.

---

## Important Note About Google Drive's sync speed using FreeFileSync

To achieve high-speed syncing with Google Drive, you’ll need the **Donation Edition** of FreeFileSync.

The free version of FFS allows only [a single file access operation at a time](https://freefilesync.org/manual.php?topic=performance), which creates a significant bottleneck in upload and download speeds.
You can start by using GreenSync together with FFS (FreeFileSync) free edition to test everything and confirm it fits your workflow. Once you’re happy with how well GreenSync works, upgrading to FFS Donation Edition unlocks full-speed synchronization and a much smoother experience.

* You can donate **any** amount you choose.
* The license is lifetime and valid for all your devices.
* The developer kindly asks users **not to share your Donation Edition with others.**

If you're working as part of a professional team, please purchase a **business license**—it’s very affordable and helps support an excellent piece of software.


## A Personal Note

I’ve invested **many** hours building GreenSync. I’m not a fast programmer-but I’m persistent, and it took me a long time to refine the tools and practices that make GreenSync fast, reliable, and genuinely pleasant to use.
If GreenSync helps you or your team, I’d be grateful if you would consider supporting my work with a small (or even better - a very large 😅 ) [**donation**](https://paypal.me/lshachar).

**Thank you.** ❤️

---

## Why do I have a new sync.ffs_db file in my project folder?
running synchronization operations stores folder structure databases in `sync.ffs_db` files on both the local and remote folders. They are important for correct FFS behaviour, such as: it's a possiblity that a file got deleted on one side, but it's also a possiblity that a file got created on the other side! In order for FFS to sync them in accordance to your selected operation rule (upload/download/undo changes) FFS must know what was the last state of affairs before the current directory comparison. That's basically what the databases are for. They are good for you. let them be and try your best not to delete them by accident. They are marked as hidden files on your local system by FFS. (so you can hide these files in windows explorer easily)

FreeFileSync's [manual](https://freefilesync.org/manual.php) or [video tutorials here](https://freefilesync.org/tutorials.php)
  

---

## Access From Multiple Google User Accounts

* It's easiest to configure GreenSync with a single, shared cridential (Username and Password) that all your collaborators share. However this might not be safe or comfortable enough for your needs. Not to worry! GreenSync can easily be configured to support as many seperate google accounts as needed.

1. Read the `Users` section of `greensync_config.yaml`   
for each user, 3 lines must be defined in `greensync_config.yaml`:  
 `- name: '<personal name>'`  
   `base_local: '<path for local files>'`						(use `C:\GreenSync` for easy configuration)  
   `base_remote: '<path for remote files on google drive.>`  	(use `gdrive:\username@gmail.com\GreenSync` for easy configuration)  
   
2. Watch the [YouTube tutorial](https://youtu.be/EDvjGOFoVD0?si=XoTLtCxlmy97CcZU&t=264) (starting at 4:24), learn how each google user must add a link to the shared google drive project folder - to their own individual google drive, using the web graphical interface.

3. Once changes are saved in `greensync_config.yaml`, Run the script `make_greensync_operations` to create new synchronization Operations for all defined users.

It's very easy to set up once you've played and experimented with GreenSync a little bit.


---

## Advanced stuff that you probably would never use: Changing more of FreeFileSync's configurations through greensync_template.xml

Try this:
* in FFS, Select any operation from the list of configurations (open any file from `C:\GreenSync\ZZ GreenSync Operations`)
* Enter the syncrhonization settings menu by clicking F8 / clicking the blue gear -> synchronization
* Under Delete and overwrite, click Permanent
* Click OK
* Under configuration, click save as
* Give the file a temporary name.
* View the created file in a text editor, and view `greensync_template.xml` as well.
* In `greensync_template.xml` you will find at line 14:   `<DeletionPolicy>RecycleBin</DeletionPolicy>`
* In the temporary file you will find at the same line: `<DeletionPolicy>Permanent</DeletionPolicy>`
* If you'd like files to be permanently deleted, instead of sent to the recycle bin, edit the file `greensync_template.xml` and add change the deletionPolicy to Permanent.

* You can find out what each XML setting in `greensync_template.xml` does by the same process. and fine tune it to your needs.

---

## The problem with syncing Google Doc / Google Sheets / Google draw files
These files are never saved as binary files on your hard drive, even when syncing with the google drive ("drive for desktop") application. (With the application they are saved locally as shell links, that launches a web browser with the right URL when opened.)
FreeFileSync [does not support creating / following those shell links](https://freefilesync.org/forum/viewtopic.php?t=9370) (as the operation of creating those links won't be considered a sync operation!)

Furthermore, these google files aren't automatically saved with a file extension, so they cannot be ignored by default with FFS exclude filter.

![completed with errors google doc files.jpg](https://github.com/lshachar/GreenSync/blob/master/readme/completed%20with%20errors%20google%20doc%20files.jpg?raw=true)
This is the error you will encounter  
  
Luckily there are two very comfortable workarounds

### 1. exclude the "offensive" files from syncing:  
  
in FFS, right click the offensive file -> rename -> add an extension to the file:
< .gdoc / .gsheet / .gdraw > depending on the type of file you're renaming <document / sheet / drawing>  
(Not sure of the correct file type? open the file in google drive web browser and view the content.)
* these three file extensions are already in the exclude list of GreenSync, so FFS won't try syncing the renamed files again.
* Too much work manually renaming lots of files you don't know their correct extension? no sweat, just add the extension .gfile to them... it's also excluded by GreenSync, and none of these extensions mean anything to google drive. So all your files will still open normally on google drive web interface.
  
![rename with gsheet extension.jpg](https://github.com/lshachar/GreenSync/blob/master/readme/rename%20with%20gsheet%20extension.jpg?raw=true)
  
### 2 export the "offensive" files as regular (non google-drive) files:

Regular MS word / MS excel / MS powerpoint files are treated as normal files that FFS can download properly,
and also, you can still edit them online with google doc / sheet / draw.
  
Open an offensive file in google drive web browser, click File -> Download -> (Microsoft excel / Microsoft Word / Microsoft Powerpoint - depending on whichever file you opened)  
  
The exported file is downloaded to your computer. upload this file to the same google drive folder, then delete the original google drive version of that file.
