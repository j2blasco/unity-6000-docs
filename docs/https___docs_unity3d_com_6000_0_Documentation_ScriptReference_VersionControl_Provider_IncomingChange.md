* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.IncomingChangeSetAssets.html

#  [Provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.html).IncomingChangeSetAssets
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
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) IncomingChangeSetAssets([VersionControl.ChangeSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ChangeSet.html) changeset); 
## Declaration
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) IncomingChangeSetAssets(string changesetID); 
### Parameters
Parameter | Description  
---|---  
changeset | Incoming changeset.  
changesetID | Incoming changesetid.  
### Description
Given an incoming changeset this will start a task to query the version control server for which assets are part of the changeset.
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.VersionControl;
using UnityEngine;  
  
public class EditorScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Version Control/ChangeSetAssets")]
    public static void ExampleChangeSetAssets()
    {
        Task[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) t1 = Provider.IncomingChangeSetAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.IncomingChangeSetAssets.html)("1111");
        t1.Wait();
        t1.assetList.ForEach(asset => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(asset.name + " " + asset.state.ToString()));
    }
}

```

The code above will return the names and version control states for the assets belonging to the "1111" incoming changeset.
* * *
