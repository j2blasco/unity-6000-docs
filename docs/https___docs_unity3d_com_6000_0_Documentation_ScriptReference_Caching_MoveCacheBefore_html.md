* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.MoveCacheBefore.html

#  [Caching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html).MoveCacheBefore
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
public static void MoveCacheBefore([Cache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) src, [Cache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) dst); 
### Parameters
Parameter | Description  
---|---  
src | The Cache to move.  
dst | The Cache which should come after the source Cache in the cache list.  
### Description
Moves the source Cache before the destination Cache in the cache list.
```
using System.IO;
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void MoveCacheBeforeExample()
    {
        Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)("Cache1");
        Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)("Cache2");
        Directory.CreateDirectory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.CreateDirectory.html)("Cache3");  
  
        Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) c1 = Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)("Cache1"); //Placed in cache list at position 1
        Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) c2 = Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)("Cache2"); //Placed in cache list at position 2
        Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) c3 = Caching.AddCache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.AddCache.html)("Cache3"); //Placed in cache list at position 3  
  
        Caching.MoveCacheBefore[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.MoveCacheBefore.html)(c2, c1);  
  
        //Now the Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) list looks like:
        //Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) 0: Default Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html)
        //Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) 1: Cache2
        //Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) 2: Cache1
        //Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) 3: Cache3
    }
}

```

* * *
