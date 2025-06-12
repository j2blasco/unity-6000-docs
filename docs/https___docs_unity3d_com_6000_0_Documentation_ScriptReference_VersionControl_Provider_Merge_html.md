* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Merge.html

#  [Provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.html).Merge
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
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) Merge([VersionControl.AssetList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets); 
### Parameters
Parameter | Description  
---|---  
assets | The list of conflicting assets to be merged.  
### Description
Initiates a merge task to handle the merging of conflicting Assets. This invokes a merge tool, which you can set in the External Tools section of the Preferences window, on the conflicting Assets. When the merge task finishes, the [AssetList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) only contains the Assets that the tool could merge.
To correctly resolve the resulting [AssetList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) states (and replace the files with the correct, merged version), you must call a subsequent [Provider.Resolve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Resolve.html) task with a [ResolveMethod.UseMerged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ResolveMethod.UseMerged.html) ResolveMethod.
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.VersionControl;
using UnityEngine;  
  
public class EditorScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Version Control/Merge")]
    public static void ExampleMerge()
    {
        AssetList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets = new AssetList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html)();
        assets.Add(Provider.GetAssetByPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.GetAssetByPath.html)("Assets/ExampleAsset.cs"));
        Task[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) t1 = Provider.Merge[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Merge.html)(assets);
        t1.Wait();
        Task[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) t2 = Provider.Resolve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Resolve.html)(assets, ResolveMethod.UseMerged[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ResolveMethod.UseMerged.html));
        t2.Wait();
    }
}

```

* * *
