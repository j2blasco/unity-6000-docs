* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPostprocessAllAssets.html

#  [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html).OnPostprocessAllAssets(string[] importedAssets, string[] deletedAssets, string[] movedAssets, string[] movedFromAssetPaths, bool didDomainReload)
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
importedAssets | Array of paths to imported assets.  
deletedAssets | Array of paths to deleted assets.  
movedAssets | Array of paths to moved assets.  
movedFromAssetPaths | Array of original paths for moved assets.  
didDomainReload | Boolean set to true if there has been a domain reload.  
### Description
This is called after importing of any number of assets is complete (when the Assets progress bar has reached the end).
This call may occur after a manual reimport, or when you move an asset or a folder of assets to a new location in the Project window. Every string array item contains a file path relative to the Assets folder, under the Project root. `importedAssets` contains paths of all assets used in the operation. Each consecutive index of `movedAssets` and `movedFromAssetPaths` refers to the same asset.  
  
If you perform a bulk operation on several individual assets instead of a folder containing those assets, this function will be called once per asset with each individual asset as the only item in the various arrays.  
  
OnPostProcessAllAssets is called when the asset database finishes importing assets. You can safely perform any asset database operations from within this callback, such as loading, importing, moving or deleting assets.  
  
OnPostProcessAllAssets should be used for initialization after a domain reload, if the initialization requires asset operations like loading of assets. `didDomainReload` parameter can be checked whether there has been a domain reload. All domain reloads will cause OnPostprocessAllAssets to be called.  
  
Note: If your code causes any new asset imports during this callback, OnPostProcessAllAssets will be called again once those new imports are complete.  
  
Note that this function must be declared as `static`, that is it will not be called correctly if it is declared as an instance function.  
  
The order specified by GetPostprocessOrder does not affect this function, instead the order can be controlled by defining dependencies using the following attributes: 
  * [RunAfterClassAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunAfterClassAttribute.html), [RunBeforeClassAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunBeforeClassAttribute.html)
  * [RunAfterAssemblyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunAfterAssemblyAttribute.html), [RunBeforeAssemblyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunBeforeAssemblyAttribute.html)
  * [RunAfterPackageAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunAfterPackageAttribute.html), [RunBeforePackageAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunBeforePackageAttribute.html)


Note: A version of this callback without the `didDomainReload` parameter is also available (**OnPostprocessAllAssets(string[] importedAssets, string[] deletedAssets, string[] movedAssets, string[] movedFromAssetPaths)**)
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class MyAllPostprocessor : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    static void OnPostprocessAllAssets(string[] importedAssets, string[] deletedAssets, string[] movedAssets, string[] movedFromAssetPaths, bool didDomainReload)
    {
        foreach (string str in importedAssets)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Reimported Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html): " + str);
        }
        foreach (string str in deletedAssets)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Deleted Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html): " + str);
        }  
  
        for (int i = 0; i < movedAssets.Length; i++)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Moved Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html): " + movedAssets[i] + " from: " + movedFromAssetPaths[i]);
        }  
  
        if (didDomainReload)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Domain has been reloaded");
        }
    }
}

```

* * *
