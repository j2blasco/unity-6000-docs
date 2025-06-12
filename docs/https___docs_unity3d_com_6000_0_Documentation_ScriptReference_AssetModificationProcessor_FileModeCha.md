* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.FileModeChanged.html

#  [AssetModificationProcessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.html).FileModeChanged(string[],FileMode)
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
### Description
Unity calls this method when file mode has been changed for one or more files.
Array of strings specifies changed files. [FileMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.FileMode.html) specifies new file mode. This method must be static if implemented.
```
using UnityEngine;
using UnityEditor.VersionControl;  
  
class CustomAssetModificationProcessor : UnityEditor.AssetModificationProcessor
{
    static void FileModeChanged(string[] paths, FileMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.FileMode.html) mode)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{nameof(FileModeChanged)} ({mode}):");
        foreach (var path in paths)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(path);
    }
}

```

* * *
