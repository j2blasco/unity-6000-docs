* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.MakeEditable.html

#  [AssetModificationProcessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.html).MakeEditable(string[],string,List<string>)
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
### Parameters
Parameter | Description  
---|---  
paths | Specifies an array of file paths relative to the project root.  
prompt | Dialog prompt to show to the user, if a version control operation needs to be done. If `null` (default), no prompt is shown.  
outNotEditablePaths | Output list of file paths that could not be made editable.  
### Returns
**void** Returns `true` if all files have been made editable. 
### Description
Unity calls this method when one or more files need to be opened for editing.
It must be static if implemented.  
  
Additional resources: [AssetDatabase.MakeEditable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MakeEditable.html).
```
using System.Collections.Generic;
using UnityEngine;  
  
class CustomAssetModificationProcessor : UnityEditor.AssetModificationProcessor
{
    static bool MakeEditable(string[] paths, string prompt, List<string> outNotEditablePaths)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("MakeEditable:");
        foreach (var path in paths)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(path);
        return true;
    }
}

```

* * *
