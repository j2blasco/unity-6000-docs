* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Delete.html

#  [Provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.html).Delete
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
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) Delete(string assetProjectPath); 
## Declaration
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) Delete([VersionControl.AssetList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets); 
## Declaration
public static [VersionControl.Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) Delete([VersionControl.Asset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) asset); 
### Parameters
Parameter | Description  
---|---  
assetProjectPath | The path to the asset that is to be deleted.  
assets | List of assets to delete.  
asset | Asset to delete.  
### Description
Starts a task to delete an Asset or a list of Assets from the disk and from the version control system.
Once the task has completed the resultCode of the task will tell if the assets were successfully deleted.  
  
Note that after this operation is completed, Asset Database is not refreshed automatically. It can be updated by calling [AssetDatabase.Refresh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.Refresh.html).
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.VersionControl;
using UnityEngine;  
  
public class EditorScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Version Control/Delete")]
    public static void ExampleDelete()
    {
        AssetList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets = new AssetList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html)();
        assets.Add(Provider.GetAssetByPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.GetAssetByPath.html)("Assets/ExampleAsset.cs"));
        assets.Add(Provider.GetAssetByPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.GetAssetByPath.html)("Assets/ExampleAsset.cs.meta"));
        Task[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) t = Provider.Delete[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Delete.html)(assets);
        t.Wait();
    }
}

```

* * *
