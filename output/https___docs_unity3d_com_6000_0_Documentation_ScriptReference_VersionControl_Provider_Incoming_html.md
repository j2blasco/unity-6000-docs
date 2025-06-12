* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Incoming.html

#  [Provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.html).Incoming
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
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) Incoming(); 
### Description
Starts a task that queries the version control server for incoming changes.
The task returns the incoming changesets which then can be accessed through the task's [Task.changeSets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task-changeSets.html) property once it has been completed.
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.VersionControl;
using UnityEngine;  
  
public class EditorScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Version Control/Incoming")]
    public static void ExampleIncoming()
    {
        ChangeSets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ChangeSets.html) exampleChangesets = new ChangeSets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ChangeSets.html)();
        ChangeSet[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ChangeSet.html) exampleChangeset = new ChangeSet[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ChangeSet.html)();
        Task[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) t1 = Provider.Incoming[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Incoming.html)();
        t1.Wait();
        exampleChangesets = t1.changeSets;
        exampleChangeset = exampleChangesets[0];
        Task[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) t2 = Provider.IncomingChangeSetAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.IncomingChangeSetAssets.html)(exampleChangeset);
        t2.Wait();
        t2.assetList.ForEach(asset => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(asset.name + " " + asset.state.ToString()));
    }
}

```

The code above fetches the incoming changesets using [Provider.Incoming](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Incoming.html) and parses it to [Provider.IncomingChangeSetAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.IncomingChangeSetAssets.html) in order to output the incoming asset file names and their status.
* * *
