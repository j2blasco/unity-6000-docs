* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.ClearCache.html

#  [Caching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html).ClearCache
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
public static bool ClearCache(); 
## Declaration
public static bool ClearCache(int expiration); 
### Parameters
Parameter | Description  
---|---  
expiration | The number of seconds that AssetBundles may remain unused in the cache.  
### Returns
**bool** True when cache clearing succeeded, false if cache was in use. 
### Description
Removes all AssetBundle content that has been cached by the current application.
This method is not available to WebPlayer applications that use the shared cache.  
  
Additional resources: [Downloading Asset Bundles](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityWebRequest-DownloadingAssetBundle.html).
```
using System.IO;
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void ClearCacheExample()
    {
        Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)("Cache1");
        Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)("Cache2");
        Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)("Cache3");  
  
        Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)("Cache1"); //Placed in cache list at position 1
        Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)("Cache2"); //Placed in cache list at position 2
        Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)("Cache3"); //Placed in cache list at position 3  
  
        //Clears all of the caches
        bool success = Caching.ClearCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.ClearCache.html)();  
  
        if (!success)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Unable to clear cache");
        }
    }
}

```

Web player is not supported from 5.4.0 and beyond.
* * *
