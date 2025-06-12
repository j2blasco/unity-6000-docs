* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.CollectionPool_2.Release.html

#  [CollectionPool<T0,T1>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.CollectionPool_2.html).Release
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
public static void Release(TCollection toRelease); 
### Parameters
Parameter | Description  
---|---  
toRelease | The instance to return to the pool.  
### Description
Returns the instance back to the pool.
If the pool has collection checks enabled and the instance is already held by the pool then an exception will be thrown.
* * *
