* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.CollectionPool_2.Get.html

#  [CollectionPool<T0,T1>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.CollectionPool_2.html).Get
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
public static TCollection Get(); 
### Returns
**TCollection** A pooled object or a new instance if the pool is empty. 
### Description
Get an instance from the pool. If the pool is empty then a new instance will be created.
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
* * *
## Declaration
public static PooledObject<TCollection> Get(out TCollection value); 
### Parameters
Parameter | Description  
---|---  
value | Out parameter that will contain a reference to an instance from the pool.  
### Returns
**PooledObject <TCollection>** A PooledObject that will return the instance back to the pool when its Dispose method is called. 
### Description
Returns a PooledObject that will automatically return the instance to the pool when it is disposed.
* * *
