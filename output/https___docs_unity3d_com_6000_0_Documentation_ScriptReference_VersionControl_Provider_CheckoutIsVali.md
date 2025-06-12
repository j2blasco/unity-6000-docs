* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.CheckoutIsValid.html

#  [Provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.html).CheckoutIsValid
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
public static bool CheckoutIsValid([VersionControl.AssetList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets); 
## Declaration
public static bool CheckoutIsValid([VersionControl.Asset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) asset); 
## Declaration
public static bool CheckoutIsValid([VersionControl.AssetList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets, [VersionControl.CheckoutMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.CheckoutMode.html) mode); 
## Declaration
public static bool CheckoutIsValid([VersionControl.Asset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) asset, [VersionControl.CheckoutMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.CheckoutMode.html) mode); 
### Parameters
Parameter | Description  
---|---  
assets | List of assets.  
asset | Single asset.  
mode | Specify to check only asset files, meta files or both.  
### Description
Given an asset or a list of assets this function returns true if [Provider.Checkout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.Checkout.html) is a valid task to perform on at least one of the given assets.
The [CheckoutMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.CheckoutMode.html) option can be used to narrow down the asset list to a specific type. For example: to only check whether meta files can be checked out and to ignore their asset file states, the [CheckoutMode.Meta](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.CheckoutMode.Meta.html) must be used.
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.VersionControl;
using UnityEngine;  
  
public class EditorScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Version Control/CheckoutIsValid")]
    public static void ExampleCheckoutIsValid()
    {
        AssetList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) assets = new AssetList[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html)();
        assets.Add(Provider.GetAssetByPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.GetAssetByPath.html)("Assets/ExampleAsset.cs.meta"));
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(Provider.CheckoutIsValid[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.CheckoutIsValid.html)(assets, CheckoutMode.Meta[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.CheckoutMode.Meta.html)));
    }
}

```

The code above will check the "ExampleAsset.cs" meta file and return true to the console if It can be checked out.
* * *
