# A Quick How To Use GreenSync Guide - Setting up your first collaborative space

## Written for Windows (very similar on Linux / macOS)

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
23. Note: Drag some file from your computer - don't try to simply create a new Google Docs / Google Sheets / Google Slides file in that folder, as these files are not regular files, and you can [learn how to deal with them later.](https://github.com/lshachar/GreenSync/?tab=readme-ov-file#the-problem-with-syncing-google-doc--google-sheets--google-draw-files)
24. Back at your computer;
25. launch the file `"C:\GreenSync\ZZ GreenSync Operations\test\Testing ground - 1 Download.ffs_gui"`
26. Click Compare in FFS (or click `F5`)
27. The file `contents.html` is ready to be downloaded from the remote server to the local copy of the `Testing Ground` Project. You can Click Synchronize to download.

28. <img width="895" height="269" alt="image" src="https://github.com/user-attachments/assets/14117d72-12c0-4bfa-9b21-27a7edff2f37" />

29. Great! You now successfully synchronized files in both ways (upload and download) to the temporary `Testing ground` project.
  Now here's the cool part:

## Only a single user has to create the sync operations (Steps 1-7.) you will now learn how to share your Sync Operations to all other users in your team!

30. Launch `"C:\GreenSync\ZZ GreenSync Operations\ZZ GreenSync Ops - 2 Upload.ffs_gui"`

<img width="1170" height="674" alt="image" src="https://github.com/user-attachments/assets/d4ae5483-8ddb-4936-bbf5-9ff2f5cb07ed" />

31. You should now be ready to upload (and share) all your GreenSync Operations to the remote server, and also the configurations and executables that you've used to create the Operations **in the first place** (again, in steps 1-7)
32. Upload your files (Click `Synchronize`)

### Adding another PC / Client / Collaborating partner is very sraightforward.
33. locate this single file, which you just uploaded: `ZZ GreenSync Ops - 1 Download.ffs_gui`, either on your local folder or better - in google drive's storage.
34. Share that file to your collaborator.
35. Install FFS on the collaborator's PC.
36. Launch the operation file (from step 33)
37. FFS will start. Now follow steps 10-13 to log that user in, with the same google drive cridenials as the first user.
38. Note: It's possible for each user to access the remote shared folder from their own (seperate) google account, read about it [here](https://github.com/lshachar/GreenSync/tree/master?tab=readme-ov-file#access-from-multiple-google-user-accounts)
39. Download all Greensync's operations to that PC.
40. Now, this user can also access the operations of `Testing Ground` project, and thus sync that project.
41. Launch `Testing ground - 1 Download.ffs_gui` from the 2nd PC, and download the project files that were uploaded in step 15 from the 1st PC.

<img width="1025" height="613" alt="image" src="https://github.com/user-attachments/assets/f66ce64b-322f-4961-8e65-c08e8aede52f" />

## When you feel comfortable with the basics

42. Note that you can drag and drop many Operations (`.ffs_gui` files) into one instance of FFS.
43. Use that as an easy to use list of projects and operations that you are currently working on and syncing files to/with.

<img width="314" height="387" alt="image" src="https://github.com/user-attachments/assets/ea9a3c1e-b040-4263-8db4-d353d0a05a72" />

44. Read the file [../greensync_config.yaml](greensync_config.yaml). That's where you define new projects, project names, operations save paths, and multiple users access.
