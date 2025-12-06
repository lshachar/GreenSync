<p align="center"><img src="/readme/GreenSync.png" height="400" alt="GreenSync logo" /></p>
<h1 align="center">GreenSync - A Reliable Collaboration Tool For Shared Project Files!</h1>

GreenSync was born in the wake of the now-defunct GrabCAD Workbench, a once-popular cloud-based platform that allowed engineering teams to collaborate effortlessly on CAD projects. Since GrabCAD shut down in 2023 no comfortable replacement emerged, and the absence of a simple and reliable way to collaborate work on shared files affected my own life, So… that's how we got here.

GreenSync is a practical solution made from a couple of lightweight Python scripts, a clear setup guide, the excellent FreeFileSync (FFS) tool for file synchronization, and Google Drive as the remote storage server.

Setup is simple and designed to be shared across team members for a smooth, unified experience. a single person can configure GreenSync for an entire team, and everyone else can immediately collaborate using the same configurations.

GreenSync supports all the essential and intuitive operations needed for collaborative work: **Upload, Download, Undo Local Changes**—so you can update your project files quickly, confidently, and get back to work faster.
3

 [<img width="100" alt="Watch the video tutorials on YouTube" src="https://github.com/user-attachments/assets/61b3791e-214e-454b-8a06-6b17c4300d6a" >](https://www.youtube.com/playlist?list=PLB7_MxikWTNoCSxZbEPRPo8c0aFSEUMVV)   **Click to watch the video tutorials on YouTube**

---

* GreenSync will work with Cad files... **or any other type of file**. It should be useful for many collaborative projects where file synchronization is needed.
* FreeFileSync is available for Windows, macOS and Linux.
* GreenSync's python scripts are precompiled for the same operation systems, get them from the [release page](https://github.com/lshachar/GreenSync/releases) (or install Python and run the scripts directly)
* Remote syncing destinations options: Google drive, a local folder / network folder, or a folder on an FTP server.
* Multiple configuration files could be saved and used individually for different projects, users, and remote syncing destinations.
* Published under GNU GPLv3

## Important Note About Google Drive's sync speed using FreeFileSync

To achieve high-speed syncing with Google Drive, you’ll need the **Donation Edition** of FreeFileSync.

The free version of FFS allows only [a single file access operation at a time](https://freefilesync.org/manual.php?topic=performance), which creates a significant bottleneck in upload and download speeds.
You can start by using GreenSync together with FFS (FreeFileSync) free edition to test everything and confirm it fits your workflow. Once you’re happy with how well GreenSync works, upgrading to FFS Donation Edition unlocks full-speed synchronization and a much smoother experience.

* You can donate **any** amount you choose.
* The license is lifetime and valid for all your devices.
* The developer kindly asks users **not to share your Donation Edition with others.**

If you're working as part of a professional team, please purchase a **business license**—it’s very affordable and helps support an excellent piece of software.


## A Personal Note

I’ve invested many hours building GreenSync. I’m not a fast programmer-but I’m persistent—and it took me a long time to refine the tools and practices that make GreenSync fast, reliable, and genuinely pleasant to use.
If GreenSync helps you or your team, I’d be grateful if you would consider supporting my work with a small (or even better - a very large) [**donation**](https://paypal.me/lshachar).

Thank you.

---


## How to use
* There is one important configuration file: `greensync_config.yaml`
And one configuration file for some less common options: `greensync_template.xml` 
  
* There is one important python script: `make_greensync_operations.py` 
And one supporting python script: `make_projects_list_from_base_folder.py` - which is only useful when setting up a long list of projects.

You don't have to download python or edit scripts, get a precompiled version of the scripts from the [release page](https://github.com/lshachar/GreenSync/releases)
  

**Start** by editing `greensync_config.yaml`:
Under base_remote: `gdrive:\username@gmail.com\GreenSync` replace `username` with the relevant gmail username. You may rename the base folder `GreenSync` if needed.

* It's possible to sync to a remote location that's available on the local network / hard drive as well. just change the `base_remote` value accordingly


Under `projects`:
The 1st project in the list is specially reserved to store all of GreenSync's operations. (Default name: `ZZ GreenSync Ops`. It is prefixed with ZZ to appear last in the list of projects in FFS)

The next three projects in the default `greensync_config.yaml` file are just there as examples. (`Testing ground`,`Project A`, `Project B`. remove, rename, or add to them however you'd like.

under `Operations`:
You may want to uncomment the 5th operation "Force upload". or comment out the 3rd operation "sync", which I don't recommend using regularly - it's more of a comfortable way to see all project changes in one place.

* run `make_greensync_operations`

You may want to run the command from a command prompt (Windows) / terminal window (macOS / Linux) to catch the script's output messages.(run `make_greensync_operations -h` for further help about running the script with arguments)

a FreeFileSync's folder configuration definition is saved in an `.ffs_gui` files. it is quite human-readble .xml file.

The operations are created in `<local base folder> \ <1st project>` which defaults to `c:\GreenSync\ZZ GreenSync Ops\`

* launch FreeFileSync  
`Configuration` -> `Open...` OR `File` -> `Open`  
* Go to the 1st project folder on your local drive (default `c:\GreenSync\ZZ GreenSync Ops\`)  
Select all files in folder, click open.
  
This is what you should get:  
![FFS populated](https://github.com/lshachar/GreenSync/blob/master/readme/FFS%20populated.jpg?raw=true)

---

## Using FreeFileSync with your project operations
FreeFileSync is very easy to use.[See the manual here](https://freefilesync.org/manual.php) or [video tutorials here](https://freefilesync.org/tutorials.php)


My best word of advice is: don't worry about clicking on anything and generally trying things out in FreeFileSync. 
*Only thing you should be careful around*: after you click on the synchronize button on the top left (or F9), Don't click *Start* unless you're sure of yourself. clicking start is the only way to actually write files to disk.

* You may want to use the project "Testing Ground" as a place for trials and attempts, ie:  
Create the local folder `c:\GreenSync\Testing Ground\`, copy some files to it, use `Testing ground - 2 Upload.ffs_gui` to upload them to your remote destination, update some of those files directly on the remote destination, delete some files remotely and some locally, connect another computer and FFS to the same remote destination (etc...) - and see how FFS displays the changes its file view in each defined operation.

* Note: When either your local or remote project folders are new folders, you might need to synchronize once before all your changes will show up.  
  
* Note that running synchronization operations creates `sync.ffs_db` files on both local and remote folders. They are important for FFS for file-move operations (saving time, instead of deleting and redownloading, FFS will just move files wherever needed) and to keep track which side had deleted a file or created a new file. (just ignore these files.)

---

## 5 pictures are worth five thousand words

### Download:
1 `only local.doc` 	  - file exists on left (local) side only, marked "do nothing"  
2 `other files.txt`   - right side (remote) is newer - will be downloaded to local  
3 `remote video.mp4`  - file exists on right (remote) side only - will be downloaded  
4 `some files.txt`    - local file is newer, do nothing.  
![FFS testing ground - 1 download.jpg](https://github.com/lshachar/GreenSync/blob/master/readme/FFS%20testing%20ground%20-%201%20download.jpg?raw=true)
  
### Upload:
1 `only local.doc` 	  - copy new file to remote  
2 `other files.txt`   - server (remote) is newer, do nothing  
3 `remote video.mp4`  - exist on remote server only, do nothing  
4 `some files.txt`    - copy more recent file to remote server.  
![FFS testing ground - 2 upload.jpg](https://github.com/lshachar/GreenSync/blob/master/readme/FFS%20testing%20ground%20-%202%20upload.jpg?raw=true)

### Sync:
Note: confusing when there are lots of changes both remote and local. it's advised to **upload** your work first, then **download** all other changes that are on the remote server. use Sync to **view** all current changes, not necessarily to sync them.  
  
1 `only local.doc` 	  - copy new file to remote  
2 `other files.txt`   - right side (remote) is newer - will be downloaded to local  
3 `remote video.mp4`  - file exists on right (remote) side only - will be downloaded  
4 `some files.txt`    - copy more recent file to remote server.  
![FFS testing ground - 3 sync.jpg](https://github.com/lshachar/GreenSync/blob/master/readme/FFS%20testing%20ground%20-%203%20sync.jpg?raw=true)

### Undo local changes:
Note: Will change only local files, to revert all local changes, restoring to the same state as the remote server.  
1 `only local.doc` 	  - **deletes local file, since it's only saved locally**  
2 `other files.txt`   - right side (remote) is newer - will be downloaded to local  
3 `remote video.mp4`  - file exists on right (remote) side only - will be downloaded  
4 `some files.txt`    - **removes local changes in left side even though it's newer**  
![FFS testing ground - undo local.jpg](https://github.com/lshachar/GreenSync/blob/master/readme/FFS%20testing%20ground%20-%20undo%20local.jpg?raw=true)

### Force upload:
Note: This operation is disabled by default (in `greensync_config.yaml`), since it could be little risky: If used unwisely somebody could overwrite an entire project by accident, by uploading all their local changes. Also, it is possible to manually achieve this behaviour in FFS.
# (It's useful when tiding up the remote server.)

by clicking in the two marked areas, you change the synchronization behavior in the 2nd and 3rd file from do nothing - to upload (compare this to the sync screenshot).
Hence you don't really have to use the commented-out operation "Force upload", because you can manually override remote changes if you need to.

1 `only local.doc` 	  - upload. copy new file to remote.  
2 `other files.txt`   - **upload - Revert changes on the remote side**  
3 `remote video.mp4`  - **delete file on server side - Revert remote the same state as local**  
4 `some files.txt`    - upload, copy more recent file to remote server  
![FFS testing ground - undo local.jpg](https://github.com/lshachar/GreenSync/blob/master/readme/FFS%20testing%20ground%20-%20undo%20local.jpg?raw=true)


---

## Sharing your projects with other users
* **One time only**: from FFS click the configuration `ZZ GreenSync Ops - 2 Upload`, and upload the created .ffs_gui files to your remote server/folder. (This needs to be done once when the sync operations are updated, normally after the script make_greensync_operations is run with new settings, to update the remote side's sync operations, which are  shared and used by all users)

![FFS upload greensync ops.jpg](https://github.com/lshachar/GreenSync/blob/master/readme/FFS%20upload%20greensync%20ops.jpg?raw=true)


* copy and install FFS on to the new machine.  
* Copy the file `ZZ GreenSync Ops - 1 Download.ffs_gui` on to the new machine.  
  
*tip: if you're using google drive as the remote server, you might like to share a link to this google drive file by email.  

* Start FFS, load the copied configuration file, and download all the Operation files that are on the remote server.  
![FFS download greensync ops.jpg](https://github.com/lshachar/GreenSync/blob/master/readme/FFS%20download%20greensync%20ops.jpg?raw=true)

*Done!* You can now start working!

---

## Multiple Google Drive users? 

* It's easiest to use GreenSync with the same Google drive username for all of your users.
However, if you'd like to be able to see which user uploaded the current version of a file (viewed in google drive web interface) you may want to share your remote folder with seperate google users.  
Then you'd also need to create seperate synchronization operation files for each user.  
please run the script `make_greensync_operations -h` (with the argument `-h`) in order to learn about argument usage with the script. You will create and use several copies of `greensync_config.yaml` (and / or `greensync_template.xml`) to automate the creation of multiple project operation files, each defined for a seperate user.  

---

## Changing more of FreeFileSync's configurations through greensync_template.xml

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

* You can find out what each setting in `greensync_template.xml` does by the same process.

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
