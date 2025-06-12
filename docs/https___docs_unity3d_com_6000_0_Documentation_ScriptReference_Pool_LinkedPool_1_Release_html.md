* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.LinkedPool_1.Release.html

#  [LinkedPool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.LinkedPool_1.html).Release
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
public void Release(T item); 
### Parameters
Parameter | Description  
---|---  
item | The instance to return to the pool.  
### Description
Returns the instance back to the pool.
If the pool has collection checks enabled and the instance is already held by the pool then an exception will be thrown.
* * *
