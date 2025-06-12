* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-systemVersion.html

#  [Device](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device.html).systemVersion
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
systemVersion; 
### Description
iOS version.
iOS version as a string. E.g. "7.0" or "8.1".
```
using UnityEngine;
using UnityEngine.iOS;  
  
public class SystemVersionExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    bool allowFeature = true;  
  
    void Start()
    {
        // Get the iOS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.iOS.html) version of the device this is running on
        string systemVersion = Device.systemVersion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device-systemVersion.html);  
  
        // Separate the version string to major and minor version numbers
        string[] separatedVersion = systemVersion.Split('.');  
  
        // Parse the major version number to an integer that can be used for comparison
        int majorVersion = int.Parse(separatedVersion[0]);  
  
        // Check if major version number of the device this is running on is below iOS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.iOS.html) 12
        if (majorVersion < 12)
        {
            // Log a message and disable the version-specific features.
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Sorry, this amazing feature requires iOS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.iOS.html) 12 and above to work. Please update your iOS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.iOS.html) version.");
            allowFeature = false;
        }
    }
}

```

* * *
