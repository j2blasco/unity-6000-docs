* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetCacheAt.html

#  [Caching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html).GetCacheAt
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
public static [Cache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) GetCacheAt(int cacheIndex); 
### Parameters
Parameter | Description  
---|---  
cacheIndex | Index of the cache to get.  
### Returns
**Cache** A reference to the Cache at the index specified. 
### Description
Returns the Cache at the given position in the cache list.
```
using System.IO;
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void GetCacheAtExample()
    {
        Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)("Cache1");
        Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)("Cache2");
        Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)("Cache3");  
  
        Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)("Cache1"); //Placed in cache list at position 1
        Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)("Cache2"); //Placed in cache list at position 2
        Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)("Cache3"); //Placed in cache list at position 3  
  
        Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) c0 = Caching.GetCacheAt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetCacheAt.html)(0); //The default cache
        Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) c1 = Caching.GetCacheAt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetCacheAt.html)(1);
        Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) c2 = Caching.GetCacheAt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetCacheAt.html)(2);
        Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) c3 = Caching.GetCacheAt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.GetCacheAt.html)(3);  
  
        string path0 = c0.path; //The default cache
        string path1 = c1.path;
        string path2 = c2.path;
        string path3 = c3.path;
    }
}

```

* * *
