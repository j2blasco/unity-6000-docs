* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-dataPath.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).dataPath
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
dataPath; 
### Description
Contains the path to the game data folder on the target device (Read Only).
The value depends on which platform you are running on:  
  
**Unity Editor:** <_path to project folder_ >/Assets  
  
**Mac player:** <_path to player app bundle_ >/Contents  
  
**iOS player:** <_path to player app bundle_ >/<_AppName.app_ >/Data (this folder is read only, use [Application.persistentDataPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-persistentDataPath.html) to save data).  
  
**Win/Linux player:** <_path to executablename_Data folder_ > (note that most Linux installations will be case-sensitive!)  
  
**WebGL:** The absolute url to the player data file folder (without the actual data file name)  
  
**Android:** Normally it points directly to the APK. If you are running a split binary build, it points to the [OBB](https://docs.unity3d.com/6000.0/Documentation/Manual/android-OBBsupport.html) instead.  
  
**UWP Apps:** The absolute path to the player data folder (this folder is read only, use [Application.persistentDataPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-persistentDataPath.html) to save data)  
  
Note that the string returned on a PC will use a forward slash as a folder separator.  
  
For any unlisted platform, run the example script on the target platform to find the dataPath location in the debug log.
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
//This script outputs the Application[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html)’s path to the Console
//Run this on the target device to find the application data path for the platform
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    string m_Path;  
  
    void Start()
    {
        //Get the path of the Game data folder
        m_Path = Application.dataPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-dataPath.html);  
  
        //Output the Game data path to the console
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("dataPath : " + m_Path);
    }
}

```

* * *
