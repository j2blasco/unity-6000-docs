* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.ChangeSetStatus.html

#  [Provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.html).ChangeSetStatus
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
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) ChangeSetStatus([VersionControl.ChangeSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ChangeSet.html) changeset); 
## Declaration
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) ChangeSetStatus(string changesetID); 
### Parameters
Parameter | Description  
---|---  
changeset | Changeset to query for assets.  
changesetID | ChangesetID to query for assets.  
### Description
Retrieves a list of assets belonging to a changeset.
This is intended to work only with outgoing changesets. Use [Provider.IncomingChangeSetAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.IncomingChangeSetAssets.html) if you would like to retrieve assets from incoming changesets.
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.VersionControl;
using UnityEngine;  
  
public class EditorScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("VersionControl/ChangeSetStatus")]
    static void ExampleChangeSetStatus()
    {
        Task[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) t = Provider.ChangeSetStatus[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.ChangeSetStatus.html)("1111");
        t.Wait();
        t.assetList.ForEach(asset => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(asset.name + " " + asset.state.ToString()));
    }
}

```

The code above will output a full list of the asset names as well as their version control states for the given changelist "1111".
* * *
