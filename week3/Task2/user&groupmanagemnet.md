**User and Group Management with permissions**
user group & permission is necessary for system security so that the they get access to things they really need not more than that.

### **  Task Summary**

Created a new user accounts and configured permissions to manage access to system files and commands._

I add to user to the system user1 and user2 by using the commond:

sudo adduser user1
sudo adduser user2

groupadd NetworkManager
usermod -aG NetworkManager user1
usermod -aG NetworkManager user2

The Networkingfiles folder has the permission has the default permission i will change the group ownership to the the NetworkManager group to avoid anyone else interfere with the files.

Changed the group ownership to NetworkManager group.

chown :NetworkManager Networkingfiles

chmod 2770 Networkingfiles

This will set the permission for the owner & group  to read write and excute and for other there there is nothing.The sgid bit is set to inherit the group ownership when new files is creating.

Thus this ensure that in a shared directory the user within the same group has the permission to access the files and data but no other user or group interfere with the files.
