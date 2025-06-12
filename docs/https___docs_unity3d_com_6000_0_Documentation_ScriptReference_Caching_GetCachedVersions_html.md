* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetCachedVersions.html

#  [Caching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html).GetCachedVersions
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
public static void GetCachedVersions(string assetBundleName, List<Hash128> outCachedVersions); 
### Parameters
Parameter | Description  
---|---  
assetBundleName | The AssetBundle name.  
outCachedVersions | List of all the cached version.  
### Description
Returns all cached versions of the given AssetBundle.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    IEnumerator GetCachedVersionExample(string uri)
    {
        //Download the bundle
        UnityWebRequest[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html) request = UnityWebRequestAssetBundle.GetAssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html)(uri);
        yield return request.SendWebRequest();
        AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) bundle = DownloadHandlerAssetBundle.GetContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.DownloadHandlerAssetBundle.GetContent.html)(request);  
  
        //Get all the cached versions
        List<Hash128[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html)> listOfCachedVersions = new List<Hash128[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html)>();
        Caching.GetCachedVersions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetCachedVersions.html)(bundle.name, listOfCachedVersions);  
  
        //use listOfCachedVersions hashes to perform actions on Caches...  
  
        //Unload the AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html)
        bundle.Unload(true);
    }
}

```

* * *
