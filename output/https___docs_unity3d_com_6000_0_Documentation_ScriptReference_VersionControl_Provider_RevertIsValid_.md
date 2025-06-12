* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.RevertIsValid.html

#  [Provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.html).RevertIsValid
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
public static bool RevertIsValid([VersionControl.AssetList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets, [VersionControl.RevertMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.RevertMode.html) mode); 
## Declaration
public static bool RevertIsValid([VersionControl.Asset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) asset, [VersionControl.RevertMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.RevertMode.html) mode); 
### Parameters
Parameter | Description  
---|---  
assets | List of assets to test.  
asset | Asset to test.  
mode | Revert mode to test for.  
### Description
Returns true if [Provider.Revert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Revert.html) is a valid task to perform on at least one of the given assets in the list.
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.VersionControl;
using UnityEngine;  
  
public class EditorScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Version Control/RevertIsValid")]
    public static void ExampleRevertIsValid()
    {
        AssetList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets = new AssetList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html)();
        assets.Add(Provider.GetAssetByPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.GetAssetByPath.html)("Assets/ExampleAsset.cs"));
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Provider.RevertIsValid[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.RevertIsValid.html)(assets, RevertMode.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.RevertMode.Normal.html)));
    }
}

```

Do note that, [RevertMode.Unchanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.RevertMode.Unchanged.html) will only test locally checked out and locked files. While the [RevertMode.Normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.RevertMode.Normal.html) will test locally checked out, locked, added and deleted files.
* * *
