* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.OnWillSaveAssets.html

#  [AssetModificationProcessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.html).OnWillSaveAssets(string[])
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
This is called by Unity when it is about to write serialized assets or Scene files to disk.
If it is implemented, it allows you to override which files are written by returning an array containing a subset of the pathnames which have been passed by Unity. Note that this function is static.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using System.Collections;  
  
public class FileModificationWarning : AssetModificationProcessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.html)
{
    static string[] OnWillSaveAssets(string[] paths)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnWillSaveAssets");
        foreach (string path in paths)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(path);
        return paths;
    }
}

```

* * *
