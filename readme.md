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


## A Quick How-To
### Setting up your first collaborative space

## Windows
1. Download and install [FreeFileSync](https://freefilesync.org/download.php)  
2. Download GreenSync from the [release page](https://github.com/lshachar/GreenSync/releases)
3. Extract the files to: `C:\GreenSync\ZZ GreenSync Operations\Setup\GreenSync\`
4. edit the file `greensync_config.yaml`
5. replace `username` with your own google username in ` base_remote: 'gdrive:\username@gmail.com\GreenSync'`
6. launch `make_greensync_operations.exe`
      
  <img width="658" height="236" alt="image" src="https://github.com/user-attachments/assets/c86d2a30-fefe-48bd-9f94-0804bc1b2de8" />

7. Note: A list of Sync operation files got created.   
  
  <img width="532" height="332" alt="image" src="https://github.com/user-attachments/assets/c5de0e5e-e53b-4e27-81c5-01e20ce13a24" />
  
8. Note: you can run the .exe or script file from a command prompt to see text output from the script
  
    
9. Create the folder: `c:\GreenSync\Testing ground`
10. copy a few temporary files into that folder, just for the sake of the example:

  <img width="625" height="142" alt="image" src="https://github.com/user-attachments/assets/93e09cbf-b507-4302-b81b-485ebca684cc" />

11. launch `"C:\GreenSync\ZZ GreenSync Operations\test\Testing ground - 2 Upload.ffs_gui"`
  
 ### One time only - to connect FreeFileSync with your google cridentials:
12. Click the cloud 

<img width="897" height="605" alt="image" src="https://github.com/user-attachments/assets/7600cd82-d490-4446-b5f8-b812710e9bdf" />

13. Click `Add Connection`

<img width="561" height="571" alt="image" src="https://github.com/user-attachments/assets/785b5008-434b-4303-93c4-7fa280d5323b" />

14. A browser window should appear. log into your google user account, and give FFS privileges to access your Google Account:

  <img width="814" height="371" alt="image" src="https://github.com/user-attachments/assets/a73fedca-fc1e-47a5-85d4-86a0798af9b9" />

15. (Click Ok to close This window once you've logged in through a web browser)

16. Click `Compare` - your two new files in `\Testing Ground` are ready to be uploaded to an identical folder in your Google drive storage.

<img width="905" height="256" alt="image" src="https://github.com/user-attachments/assets/9e47828c-426f-4ac3-b661-e45a22bb89fc" />

17. Click `Synchronize -> Start` to start the Synchronization process.
18. Congrats: You've now uploaded files to a remote server through GreenSync + FFS.
19.  **make sure you Close FreeFileSync.** once. This saves FFS configurations internally, so that you wouldn't have to connect to your google user account using the remote browser the next time.


## Downloading changes from the remote server
(Note: If you get the gist, you can skip steps 18-27. Uploading and Downloading works just about the same.)

20. Open Google drive in a web browsers
21. Drag some file from your computer into the `\Testing Ground` folder.
    <img width="873" height="671" alt="image" src="https://github.com/user-attachments/assets/dc745884-11ce-4169-980f-3a934c610a83" />
    <img width="803" height="540" alt="image" src="https://github.com/user-attachments/assets/711afaf4-6dff-40a9-af99-5f0b856c8e39" />
22. (The file `contents.html` was created on the remote storage)
23. Note: do not start a new Google Docs / Google Sheets / Google Slides in that folder, as these files are not regular files and you will learn how to deal with them later.
    [Custom foo description](The-problem-with-syncing-google-Doc-/-Google-Sheets-/-google-draw-files)

25. Back to your computer,
26. Now launch the files `"C:\GreenSync\ZZ GreenSync Operations\test\Testing ground - 1 Download.ffs_gui"`
27. Click Compare in FFS (or click `F5`)
28. The file `contents.html` is ready to be downloaded from the remote server to the local copy of the `Testing Ground` Project. You can Click Synchronize to download.

29. <img width="895" height="269" alt="image" src="https://github.com/user-attachments/assets/14117d72-12c0-4bfa-9b21-27a7edff2f37" />

30. Great! you now know how to do two-way synchronization files to that folder.
  Now here's the cool part:

## Only a single user has to create the sync operations (Steps 1-7.) you will now learn how to share your Sync Operations to all other users in your team!

30. Launch `"C:\GreenSync\ZZ GreenSync Operations\ZZ GreenSync Ops - 2 Upload.ffs_gui"`

<img width="1170" height="674" alt="image" src="https://github.com/user-attachments/assets/d4ae5483-8ddb-4936-bbf5-9ff2f5cb07ed" />

31. You should now be ready to upload (and share) all your GreenSync Operations to the remote serrver, and also the configurations and executables that you've used to create the Operations **in the first place** (again, in steps 1-7)
32. Upload your files (Click `Synchronize`)

### Adding another PC / Client / Collaborating partner is really easy.
33. locate this single file, which you just uploaded: `ZZ GreenSync Ops - 1 Download.ffs_gui`, either on your local folder or better - in google drive's storage.
34. Share that file with your collaborator.
35. Install FFS on that PC, too.
36. Launch the sync operation file (from step 31)
37. FFS will start. Now follow steps 10-13 to log that user in, with the same google drive cridenials as the first user.
38. **Note: It's possible for each user to access the shared base folder from their own google account (look for the multiple users configuration section in `greensync_config.yaml`) But let's leave that for later now. **
39. Download all Greensync's operations to that PC.
40. Now, this user can also access the operations of `Testing Ground` project, and thus sync that project.
41. Launch `Testing ground - 1 Download.ffs_gui` from the 2nd PC download the files that were uploaded in step 15 from the 1st PC.

<img width="1025" height="613" alt="image" src="https://github.com/user-attachments/assets/f66ce64b-322f-4961-8e65-c08e8aede52f" />

## When you feel comfortable with the basics

42. Note that you can drag and drop many Operations into one instance of FFS.
43. Use that as a shortlist of projects that you are currently working on and syncing files to/with.

<img width="314" height="387" alt="image" src="https://github.com/user-attachments/assets/ea9a3c1e-b040-4263-8db4-d353d0a05a72" />

44. Read the file [greensync_config.yaml](greensync_config.yaml). That's where you define new projects, project names, operations save paths, and multiple users access.

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
---
## The following information is currently being revised.
It's too confusing and it must be improved.
So read and tread carefuly.
דד

---

## Using FreeFileSync with your project operations
FreeFileSync is very easy to use.[See the manual here](https://freefilesync.org/manual.php) or [video tutorials here](https://freefilesync.org/tutorials.php)


* Note that running synchronization operations creates `sync.ffs_db` files on both the local and remote folders. They are important for correct FFS behaviour, such as: If a file gets deleted on one side, or a file gets created on the other side, In order for FFS to sync them in accordance to your selected operation (upload/download/undo changes) FFS must know what happened before the creation/deletion. That's basically what the databases are for. They are marked as hidden files, just let them be and try your best not to delete them by accident.
  

---

## 5 pictures are worth five thousand words

### Download:
1 `only local.doc` 	  - file exists on left (local) side only, marked "do nothing"  
2 `other files.txt`   - right side (remote) is newer - will be downloaded to local  
3 `remote video.mp4`  - file exists on right (remote) side only - will be downloaded  
4 `some files.txt`    - local file is newer, do nothing.  
<!--![FFS testing ground - 1 download.jpg](https://github.com/lshachar/GreenSync/blob/master/readme/FFS%20testing%20ground%20-%201%20download.jpg?raw=true)-->
<p align="center"><img src="/readme/FFS testing ground - 1 download.jpg" height="500" alt="GreenSync logo" /></p>
  
### Upload:
1 `only local.doc` 	  - copy new file to remote  
2 `other files.txt`   - server (remote) is newer, do nothing  
3 `remote video.mp4`  - exist on remote server only, do nothing  
4 `some files.txt`    - copy more recent file to remote server.  
<!--![FFS testing ground - 2 upload.jpg](https://github.com/lshachar/GreenSync/blob/master/readme/FFS%20testing%20ground%20-%202%20upload.jpg?raw=true)-->
<p align="center"><img src="/readme/FFS testing ground - 2 upload.jpg" height="500" alt="FFS testing ground - 2 upload" /></p>



### Sync:
Note: confusing when there are lots of changes both remote and local. it's advised to **upload** your work first, then **download** all other changes that are on the remote server. use Sync to **view** all current changes, not necessarily to sync them.  
  
1 `only local.doc` 	  - copy new file to remote  
2 `other files.txt`   - right side (remote) is newer - will be downloaded to local  
3 `remote video.mp4`  - file exists on right (remote) side only - will be downloaded  
4 `some files.txt`    - copy more recent file to remote server.  
<!--![FFS testing ground - 3 sync.jpg](https://github.com/lshachar/GreenSync/blob/master/readme/FFS%20testing%20ground%20-%203%20sync.jpg?raw=true)-->
<p align="center"><img src="/readme/FFS testing ground - 3 sync.jpg" height="500" alt="FFS testing ground - 3 sync" /></p>

### Undo local changes:
Note: Will change only local files, to revert all local changes, restoring to the same state as the remote server.  
1 `only local.doc` 	  - **deletes local file, since it's only saved locally**  
2 `other files.txt`   - right side (remote) is newer - will be downloaded to local  
3 `remote video.mp4`  - file exists on right (remote) side only - will be downloaded  
4 `some files.txt`    - **removes local changes in left side even though it's newer**
<!--![FFS testing ground - undo local.jpg](https://github.com/lshachar/GreenSync/blob/master/readme/FFS%20testing%20ground%20-%20undo%20local.jpg?raw=true)-->
<p align="center"><img src="/readme/FFS testing ground - undo local.jpg" height="500" alt="GreenSync logo" /></p>

### Force upload:
Note: This operation is disabled by default (in `greensync_config.yaml`), since it could be little risky: If used unwisely somebody could overwrite an entire project by accident, by uploading all their local changes. Also, it is possible to manually achieve this behaviour in FFS.
# (It's useful when tiding up the remote server.)

by clicking in the two marked areas, you change the synchronization behavior in the 2nd and 3rd file from do nothing - to upload (compare this to the sync screenshot).
Hence you don't really have to use the commented-out operation "Force upload", because you can manually override remote changes if you need to.

1 `only local.doc` 	  - upload. copy new file to remote.  
2 `other files.txt`   - **upload - Revert changes on the remote side**  
3 `remote video.mp4`  - **delete file on server side - Revert remote the same state as local**  
4 `some files.txt`    - upload, copy more recent file to remote server  
<!--![FFS testing ground - undo local.jpg](https://github.com/lshachar/GreenSync/blob/master/readme/FFS%20testing%20ground%20-%20undo%20local.jpg?raw=true)-->
<p align="center"><img src="/readme/FFS testing ground - undo local.jpg" height="500" alt="GreenSync logo" /></p>

---

## Multiple Google Drive users? 

* It's easiest to configure GreenSync with a single, shared cridential (Username and Password) that all your collaborators share. However this might not be safe, or comfortable enough for you.

---

## Advanced stuff that you shouldn't probably ever use: Changing more of FreeFileSync's configurations through greensync_template.xml

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
