* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.ChangeSetDescription.html

#  [Provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.html).ChangeSetDescription
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
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) ChangeSetDescription([VersionControl.ChangeSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ChangeSet.html) changeset); 
### Parameters
Parameter | Description  
---|---  
changeset | Changeset to query description of.  
### Description
Given a changeset only containing the changeset ID, this will start a task for quering the description of the changeset.
The resulting description can be retrieved using the task's "text" property.
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.VersionControl;
using UnityEngine;  
  
public class EditorScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Version Control/Changeset Description")]
    static void ExampleChangeSetDescription()
    {
        AssetList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets = new AssetList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html)();
        ChangeSet[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ChangeSet.html) changeset = new ChangeSet[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ChangeSet.html)("Unknown Description", "1111");
        Task[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) t = Provider.ChangeSetDescription[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.ChangeSetDescription.html)(changeset);
        t.Wait();
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(t.text);
    }
}

```

The code above will check the description of the changeset with the ID of "1111" and output it to the console.
* * *
