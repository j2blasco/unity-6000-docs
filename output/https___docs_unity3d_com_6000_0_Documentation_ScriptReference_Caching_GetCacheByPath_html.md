* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetCacheByPath.html

#  [Caching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html).GetCacheByPath
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
public static [Cache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) GetCacheByPath(string cachePath); 
### Parameters
Parameter | Description  
---|---  
cachePath | The cache path.  
### Returns
**Cache** A reference to the Cache with the given path. 
### Description
Returns the Cache that has the given cache path.
```
using System.IO;
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void GetCacheByPathExample()
    {
        Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)("Cache1");
        Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)("Cache2");
        Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)("Cache3");  
  
        Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)("Cache1"); //Placed in cache list at position 1
        Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)("Cache2"); //Placed in cache list at position 2
        Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)("Cache3"); //Placed in cache list at position 3  
  
        Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) c1 = Caching.GetCacheByPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetCacheByPath.html)("Cache1");
        Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) c2 = Caching.GetCacheByPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetCacheByPath.html)("Cache2");
        Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) c3 = Caching.GetCacheByPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetCacheByPath.html)("Cache3");
    }
}

```

* * *
