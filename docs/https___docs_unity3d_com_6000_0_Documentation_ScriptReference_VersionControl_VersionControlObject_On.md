* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.OnDeactivate.html

#  [VersionControlObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html).OnDeactivate
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
public void OnDeactivate(); 
### Description
Called when your version control system is deactivated.
This happens when the user selects a different VCS from Version Control settings window, or if it gets deactivated from script, or when the Editor is closed.  
  
Unity calls this method to inform [VersionControlObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html) that it's no longer active and VCS operations such as checkout or submit should no longer be performed.
```
using UnityEditor.VersionControl;
using UnityEngine;  
  
[VersionControl("Custom")]
public class CustomVersionControlObject : VersionControlObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html)
{
    public override void OnActivate()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Custom VCS activated.");
    }  
  
    public override void OnDeactivate()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Custom VCS deactivated.");
    }
}

```

Additional resources: [VersionControlObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html).
* * *
