* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.GetActivePlugin.html

#  [Provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.html).GetActivePlugin
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
## Declaration
public static [VersionControl.Plugin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Plugin.html) GetActivePlugin(); 
### Description
Gets the current, user selected verson control [Plugin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Plugin.html).
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.VersionControl;
using UnityEngine;  
  
public class EditorScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Version Control/GetActivePlugin")]
    public static void ExampleGetActivePlugin()
    {
        Plugin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Plugin.html) plugin;
        plugin = Provider.GetActivePlugin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.GetActivePlugin.html)();
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(plugin.name);
    }
}

```

The code above fetches the name of the currently used version control system.
* * *
