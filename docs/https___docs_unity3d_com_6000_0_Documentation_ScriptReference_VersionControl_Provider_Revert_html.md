* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Revert.html

#  [Provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.html).Revert
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
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) Revert([VersionControl.AssetList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets, [VersionControl.RevertMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.RevertMode.html) mode); 
## Declaration
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) Revert([VersionControl.Asset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) asset, [VersionControl.RevertMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.RevertMode.html) mode); 
### Parameters
Parameter | Description  
---|---  
assets | The list of assets to be reverted.  
asset | The asset to be reverted.  
mode | How to revert the assets.  
### Description
Reverts the specified assets by undoing any changes done since the last time you synced.
The last sync time is usually when [Provider.GetLatest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.GetLatest.html) was last issued but may differ if an external version control client is used at the same time.  
  
Note that after this operation is completed, Asset Database is not refreshed automatically. It can be updated by calling [AssetDatabase.Refresh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.Refresh.html).
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.VersionControl;
using UnityEngine;  
  
public class EditorScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Version Control/Revert")]
    public static void ExampleRevert()
    {
        AssetList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets = new AssetList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html)();
        assets.Add(Provider.GetAssetByPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.GetAssetByPath.html)("Assets/ExampleAsset.cs"));
        Task[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) t = Provider.Revert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Revert.html)(assets, RevertMode.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.RevertMode.Normal.html));
        t.Wait();
    }
}

```

[Provider.Revert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Revert.html) can be used with two different revert modes - normal and unchanged. The normal revert mode reverts all of the local changes made while the unchanged mode only reverts files that haven't been modified yet.
* * *
