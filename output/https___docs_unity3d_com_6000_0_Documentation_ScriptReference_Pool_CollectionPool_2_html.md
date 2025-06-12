* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.CollectionPool_2.html

# CollectionPool<T0,T1>
class in UnityEngine.Pool
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
A Collection such as List, HashSet, Dictionary etc can be pooled and reused by using a CollectionPool.
Note the CollectionPool is not thread-safe. Additional resources: [DictionaryPool<T0,T1>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.DictionaryPool_2.html), [HashSetPool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.HashSetPool_1.html), [ListPool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.ListPool_1.html).
```
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Pool;  
  
// This example shows how both version of Get could be used to simplify a line of points.
public class Simplify2DLine
{
    public List<Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)> SimplifyLine(Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)[] points)
    {
        // This version will only be returned to the pool if we call Release on it.
        var simplifiedPoints = CollectionPool<List<Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)>, Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)>.Get();  
  
        // Copy the points into a temp list so we can pass them into the Simplify method
        // When the pooled object leaves the scope it will be Disposed and returned to the pool automatically.
        // This version is ideal for working with temporary lists.
        using (CollectionPool<List<Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)>, Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)>.Get(out List<Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)> tempList))
        {
            for (int i = 0; i < points.Length; ++i)
            {
                tempList.Add(points[i]);
            }  
  
            LineUtility.Simplify[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineUtility.Simplify.html)(tempList, 1.5f, simplifiedPoints);
        }
        return simplifiedPoints;
    }
}

```

### Static Methods
Method | Description  
---|---  
[Get](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.CollectionPool_2.Get.html) | Get an instance from the pool. If the pool is empty then a new instance will be created.  
[Release](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.CollectionPool_2.Release.html) | Returns the instance back to the pool.  
* * *
