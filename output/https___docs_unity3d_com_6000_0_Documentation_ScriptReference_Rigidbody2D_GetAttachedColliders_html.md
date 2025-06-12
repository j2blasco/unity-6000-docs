* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.GetAttachedColliders.html

#  [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).GetAttachedColliders
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
public int GetAttachedColliders(out Collider2D[] results, bool findTriggers = true); 
### Parameters
Parameter | Description  
---|---  
results | An array of [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) used to receive the results.  
findTriggers | Whether [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) that are triggers should be returned or not.  
### Returns
**int** Returns the number of [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) placed in the `results` array. 
### Description
Returns all [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) that are attached to this [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).
Calculates all [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) that are attached to this [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) and returns them in the `results` array.  
  
When retrieving colliders, you should ensure that the provided array is large enough to contain all the colliders you are interested in. Typically the array would be reused therefore it would be a size to return a reasonable quantity of colliders. This function also means that no allocations occur which means no work is produced for the garbage collector.  
  
Additional resources: [Rigidbody2D.attachedColliderCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-attachedColliderCount.html).
* * *
## Declaration
public int GetAttachedColliders(List<Collider2D> results, bool findTriggers = true); 
### Parameters
Parameter | Description  
---|---  
results | A list of [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) used to receive the results.  
findTriggers | Whether [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) that are triggers should be returned or not.  
### Returns
**int** Returns the number of [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) placed in the `results` list. 
### Description
Returns all [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) that are attached to this [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).
Calculates all [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) that are attached to this [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) and returns them in the `results` list.  
  
The integer return value is the number of results written into the `results` list. The results list will be resized if it doesn't contain enough elements to report all the results. This prevents memory from being allocated for results when the `results` list does not need to be resized, and improves garbage collection performance when the query is performed frequently.  
  
Additional resources: [Rigidbody2D.attachedColliderCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-attachedColliderCount.html).
* * *
