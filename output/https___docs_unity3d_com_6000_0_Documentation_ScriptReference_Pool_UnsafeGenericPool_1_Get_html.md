* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.UnsafeGenericPool_1.Get.html

#  [UnsafeGenericPool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.UnsafeGenericPool_1.html).Get
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
public static T Get(); 
### Returns
**T** A pooled object or a new instance if the pool is empty. 
### Description
Get an instance from the pool. If the pool is empty then a new instance will be created.
* * *
## Declaration
public static PooledObject<T> Get(out T value); 
### Parameters
Parameter | Description  
---|---  
value | Out parameter that will contain a reference to an instance from the pool.  
### Returns
**PooledObject <T>** A PooledObject that will return the instance back to the pool when its Dispose method is called. 
### Description
Returns a PooledObject that will automatically return the instance to the pool when it is disposed.
* * *
