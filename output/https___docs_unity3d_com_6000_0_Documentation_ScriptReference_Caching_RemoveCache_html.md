* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.RemoveCache.html

#  [Caching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html).RemoveCache
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
public static bool RemoveCache([Cache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) cache); 
### Parameters
Parameter | Description  
---|---  
cache | The Cache to be removed.  
### Returns
**bool** Returns true if the Cache is removed. 
### Description
Removes the Cache from cache list.
```
using System.IO;
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void RemoveCacheExample()
    {
        Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)("Cache1");
        Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)("Cache2");
        Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)("Cache3");  
  
        Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) c1 = Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)("Cache1"); //Placed in cache list at position 1
        Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) c2 = Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)("Cache2"); //Placed in cache list at position 2
        Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) c3 = Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)("Cache3"); //Placed in cache list at position 3  
  
        bool successfullyRemovedCache = Caching.RemoveCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.RemoveCache.html)(c1);  
  
        if (!successfullyRemovedCache)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Unable to remove cache.");
        }  
  
        //Now, if the remove was successful, the Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) list looks like:
        //Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) 0: Default Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html)
        //Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) 1: Cache2
        //Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) 2: Cache3
    }
}

```

* * *
