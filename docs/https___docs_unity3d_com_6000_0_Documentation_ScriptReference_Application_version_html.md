* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-version.html

#  [Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html).version
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
version; 
### Description
Returns application version number (Read Only).
This function returns the current version of the application. This is read-only. To set the version number in Unity, go to **Edit** >**Project Settings** >**Player**.  
  
This is the same as [PlayerSettings.bundleVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-bundleVersion.html).
```
using UnityEngine;  
  
public class ApplicationVersionExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        //This will print whatever is in Edit>Project Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.Settings.html)>Player>Version (by default 0.1)
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Application[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html) Version : " + Application.version[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-version.html));
    }
}

```

* * *
