* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlManager-versionControlDescriptors.html

#  [VersionControlManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlManager.html).versionControlDescriptors
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
versionControlDescriptors; 
### Description
An array containing all available version control systems.
Each [VersionControlDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlDescriptor.html) contains a unique VCS name. You can pass the VCS name to [SetVersionControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlManager.SetVersionControl.html) to activate that VCS.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.VersionControl;
using UnityEngine;  
  
static class Example
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Print Available VCS")]
    static void PrintAvailableVCS()
    {
        var message = "Available version control systems:";
        foreach (var descriptor in VersionControlManager.versionControlDescriptors[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlManager-versionControlDescriptors.html))
            message += " " + descriptor.displayName;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(message);
    }
}

```

Additional resources: [VersionControlManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlManager.html), [VersionControlObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html), [VersionControlDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlDescriptor.html).
* * *
