* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.ClearCachedVersion.html

#  [Caching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html).ClearCachedVersion
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
public static bool ClearCachedVersion(string assetBundleName, [Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) hash); 
### Parameters
Parameter | Description  
---|---  
assetBundleName | The AssetBundle name.  
hash | Version needs to be cleaned.  
### Returns
**bool** Returns true when cache clearing succeeded. Can return false if any cached bundle is in use. 
### Description
Removes the given version of the AssetBundle.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void ClearAssetBundleBundleFromCache(AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) bundleToClear, string manifestBundlePath)
    {
        AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) manifestBundle = AssetBundle.LoadFromFile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadFromFile.html)(manifestBundlePath);
        AssetBundleManifest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.html) manifest = manifestBundle.LoadAsset<AssetBundleManifest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.html)>("AssetBundleManifest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleManifest.html)");  
  
        //This will clear the cached version from all caches, not just the currentCacheForWriting
        Caching.ClearCachedVersion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.ClearCachedVersion.html)(bundleToClear.name, manifest.GetAssetBundleHash(bundleToClear.name));  
  
        //Unload the AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html)
        manifestBundle.Unload(true);
    }
}

```

* * *
