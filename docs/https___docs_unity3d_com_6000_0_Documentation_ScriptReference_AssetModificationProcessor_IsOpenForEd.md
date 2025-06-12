* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.IsOpenForEdit.html

#  [AssetModificationProcessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.html).IsOpenForEdit(string[],List<string>,StatusQueryOptions)
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
assetOrMetaFilePaths | Paths to Assets or their .meta files, relative to the project folder.  
outNotEditablePaths | Destination list of non-editable Asset paths.  
statusQueryOptions | Specifies how Unity should query the version control system. The default value is [StatusQueryOptions.UseCachedIfPossible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.UseCachedIfPossible.html).  
### Returns
**void** Returns `true` if all files are editable. 
### Description
This is called by Unity when inspecting assets to determine if an editor should be disabled.
Although this is called by Unity's own systems, you can also call it if you are implementing your own Editor tools such as a custom version control integration.  
  
Additional resources: [AssetDatabase.IsOpenForEdit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsOpenForEdit.html), [StatusQueryOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.html).
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
class CustomAssetModificationProcessor : UnityEditor.AssetModificationProcessor
{
    static bool IsOpenForEdit(string[] paths, List<string> outNotEditablePaths, StatusQueryOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.html) statusQueryOptions)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("IsOpenForEdit:");
        foreach (var path in paths)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(path);
        return true;
    }
}

```

* * *
### Parameters
Parameter | Description  
---|---  
assetOrMetaFilePath | Path to the asset file or its .meta file on disk, relative to project folder.  
message | Returns a reason for the asset not being open for edit.  
### Returns
**void** True if the asset is considered open for edit by the selected version control system. 
### Description
This is called by Unity when inspecting an asset to determine if an editor should be disabled.
Although this is called by Unity's own systems, you can also call it if you are implementing your own Editor tools such as a custom version control integration. Consider using method overload that accepts an array of file paths to improve version control system performance.
* * *
