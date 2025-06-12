* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlAttribute-displayName.html

#  [VersionControlAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlAttribute.html).displayName
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
displayName; 
### Description
Version control system display name.
Can be localized. Used in UI.
```
using UnityEditor.VersionControl;
using UnityEngine;  
  
public class CustomVersionControlAttribute : VersionControlAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlAttribute.html)
{
    static string GetDisplayName()
    {
        return $"Custom ({Application.systemLanguage[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-systemLanguage.html)})";
    }  
  
    public CustomVersionControlAttribute()
        : base("Custom", GetDisplayName())
    {
    }
}  
  
[CustomVersionControl]
public class CustomVersionControlObject : VersionControlObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html)
{
}

```

Additional resources: [VersionControlAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlAttribute.html), [VersionControlObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html), [VersionControlManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlManager.html), [VersionControlDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlDescriptor.html).
* * *
