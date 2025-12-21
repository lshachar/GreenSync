# The Four Main Operations Explained

In this example I will show a single project folder which has some local and some remote files. The files are never changed all throughout this example; the only thing that's changed is the currently selected operation by the user. (under the `Configuration` tab on the left side)

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
Note: confusing when there are lots of changes both remote and local. it's advised to **upload** your work first, then **download** all other changes that are on the remote server. I recommend to only use **Sync** to **view** all current changes, not necessarily to sync them.
  
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
Note: Compare the next image to the `Upload` Operation:
by clicking in the two marked areas (Just to the right of the icon), you change the synchronization behavior for the 2nd and 3rd file from do nothing - to force-upload, overwriting these files on the remote side.

1 `only local.doc` 	  - upload. copy new file to remote.  
2 `other files.txt`   - **upload - Revert changes on the remote side**  
3 `remote video.mp4`  - **delete file on server side - Revert remote the same state as local**  
4 `some files.txt`    - upload, copy more recent file to remote server  
<!--![FFS testing ground - 2 upload - force.jpg](https://github.com/lshachar/GreenSync/blob/master/readme/FFS%20testing%20ground%20-%202%20upload%20-%20force.jpg?raw=true)-->
<p align="center"><img src="/readme/FFS%20testing%20ground%20-%202%20upload%20-%20force.jpg" height="500" alt="GreenSync logo" /></p>

Note: It's possible to enable `Force Upload` as it's own seperate operation. (Uncomment the last section in `greensync_config.yaml`), However it's disabled by default since it could be little risky: If used unwisely somebody could overwrite an entire project by accident, by uploading all their local changes. So I think it's usually best if users mark the files that they want to force upload manually.