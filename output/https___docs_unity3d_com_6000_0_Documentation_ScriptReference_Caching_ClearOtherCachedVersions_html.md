* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.ClearOtherCachedVersions.html

#  [Caching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html).ClearOtherCachedVersions
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
public static bool ClearOtherCachedVersions(string assetBundleName, [Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) hash); 
### Parameters
Parameter | Description  
---|---  
assetBundleName | The AssetBundle name.  
hash | Version needs to be kept.  
### Returns
**bool** Returns true when cache clearing succeeded. 
### Description
Removes all the cached versions of the AssetBundle from the cache, except for the specified version.
Returns false if any cached bundle is in use.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void ClearOtherCachedVersionsExample(AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) bundleToSave, string manifestBundlePath)
    {
        AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) manifestBundle = AssetBundle.LoadFromFile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFile.html)(manifestBundlePath);
        AssetBundleManifest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.html) manifest = manifestBundle.LoadAsset<AssetBundleManifest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.html)>("AssetBundleManifest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.html)");  
  
        //This will clear all the cached version of this asset bundle except for this specific cached version
        bool success = Caching.ClearOtherCachedVersions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.ClearOtherCachedVersions.html)(bundleToSave.name, manifest.GetAssetBundleHash(bundleToSave.name));  
  
        if (!success)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Unable to clear the caches");
        }  
  
        //Unload the AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html)
        manifestBundle.Unload(true);
    }
}

```

* * *
