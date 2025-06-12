* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.ChangeSets.html

#  [Provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.html).ChangeSets
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
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) ChangeSets(); 
### Description
Gets a list of pending changesets owned by the current user.
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.VersionControl;
using UnityEngine;  
  
public class EditorScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Version Control/Changesets")]
    static void ExampleChangeSets()
    {
        Task[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) t = Provider.ChangeSets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.ChangeSets.html)();
        t.Wait();
        t.changeSets.ForEach(changeset => Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(changeset.id + " : " + changeset.description));
    }
}

```

The code above will output all of the currently active changesets to the console.
* * *
