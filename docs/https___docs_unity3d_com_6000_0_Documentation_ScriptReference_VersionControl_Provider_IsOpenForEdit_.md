* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.IsOpenForEdit.html

#  [Provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.html).IsOpenForEdit
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
public static bool IsOpenForEdit([VersionControl.Asset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) asset); 
### Parameters
Parameter | Description  
---|---  
asset | Asset to test.  
### Description
Returns true if an asset can be edited.
Version control systems like Perforce or Plastic SCM require that an asset be checked out before it can be edited. In such cases this task will test whether the asset is checked out and editable.
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.VersionControl;
using UnityEngine;  
  
public class EditorScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Version Control/IsOpenForEdit")]
    public static void ExampleIsOpenForEdit()
    {
        AssetList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets = new AssetList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html)();
        assets.Add(Provider.GetAssetByPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.GetAssetByPath.html)("Assets/ExampleAsset.cs"));
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("ExampleAsset.cs is editable?" + Provider.IsOpenForEdit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.IsOpenForEdit.html)(assets[0]));
    }
}

```

Some version control systems like Git support editing without checking out the asset, in this case the task will always return true.
* * *
