* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.SubmitIsValid.html

#  [Provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.html).SubmitIsValid
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
public static bool SubmitIsValid([VersionControl.ChangeSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ChangeSet.html) changeset, [VersionControl.AssetList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets); 
### Parameters
Parameter | Description  
---|---  
changeset | The changeset to submit.  
assets | The asset to submit.  
### Description
Returns true if submitting the assets is a valid operation.
Do note that the task will always return true if the changeset parameter is set to an existing changeset.
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.VersionControl;
using UnityEngine;  
  
public class EditorScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Version Control/SubmitIsValid")]
    public static void ExampleSubmitIsValid()
    {
        AssetList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets = new AssetList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html)();
        assets.Add(Provider.GetAssetByPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.GetAssetByPath.html)("Assets/ExampleAsset.cs"));
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Provider.SubmitIsValid[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.SubmitIsValid.html)(null, assets));
    }
}

```

* * *
