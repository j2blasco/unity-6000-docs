* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.ClearAllCachedVersions.html

#  [Caching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html).ClearAllCachedVersions
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
public static bool ClearAllCachedVersions(string assetBundleName); 
### Parameters
Parameter | Description  
---|---  
assetBundleName | The AssetBundle name.  
### Returns
**bool** Returns true when cache clearing succeeded. 
### Description
Removes all the cached versions of the given AssetBundle from the cache.
Returns false if any cached bundle is in use.
```
using System.Collections;
using UnityEngine.Networking;
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    IEnumerator ClearAllCachedVersionsExample(string uri)
    {
        //Download the bundle
        UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) request = UnityWebRequestAssetBundle.GetAssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html)(uri);
        yield return request.SendWebRequest();
        AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) bundle = DownloadHandlerAssetBundle.GetContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.GetContent.html)(request);  
  
        //Given the name of an asset bundle, this will clear every cached version across all caches
        Caching.ClearAllCachedVersions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.ClearAllCachedVersions.html)(bundle.name);  
  
        //Unload the AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html)
        bundle.Unload(true);
    }
}

```

* * *
