* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html

#  [Caching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html).AddCache
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
public static [Cache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) AddCache(string cachePath); 
### Parameters
Parameter | Description  
---|---  
cachePath | Path to the cache folder.  
### Description
Add a cache with the given path.
This allows you to add a new cache to the cache list. A reference to a Cache will be returned.
```
using System.IO;
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void AddCacheAtPath(string path)
    {
        if (!Directory.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.Exists.html)(path))
            Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)(path);  
  
        Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) newCache = Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)(path);  
  
        //Make sure your new Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) is valid
        if (newCache.valid)
        {
            //If you wanted to set your newly created cache to the active cache
            Caching.currentCacheForWriting[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching-currentCacheForWriting.html) = newCache;
        }
    }
}

```

* * *
