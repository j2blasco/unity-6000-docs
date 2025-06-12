* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.IObjectPool_1.html

# IObjectPool<T0>
interface in UnityEngine.Pool
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
Interface for ObjectPools.
Additional resources: [ObjectPool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.ObjectPool_1.html), [LinkedPool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.LinkedPool_1.html).
### Properties
Property | Description  
---|---  
[CountInactive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.IObjectPool_1.CountInactive.html) | The total amount of items currently in the pool.  
### Public Methods
Method | Description  
---|---  
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.IObjectPool_1.Clear.html) | Removes all pooled items. If the pool contains a destroy callback then it will be called for each item that is in the pool.  
[Get](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.IObjectPool_1.Get.html) | Get an instance from the pool. If the pool is empty then a new instance will be created.  
[Release](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.IObjectPool_1.Release.html) | Returns the instance back to the pool.  
* * *
