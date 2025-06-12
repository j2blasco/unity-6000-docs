* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.Overlap.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).Overlap
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
public int Overlap([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position, float angle, List<Collider2D> results); 
### Parameters
Parameter | Description  
---|---  
position | The position to overlap the Collider at.  
angle | The angle to overlap the Collider at.  
results | The list to receive results.  
### Returns
**int** Returns the number of results placed in the `results` list. 
### Description
Get a list of all Colliders that overlap this Collider.
The integer return value is the number of Colliders that overlap this Collider with the specific Colliders stored in the supplied list. The results list will be resized if it doesn't contain enough elements to report all the results. This prevents memory from being allocated for results when the `results` list does not need to be resized, and improves garbage collection performance when the query is performed frequently.  
  
**NOTE** : The `position` and `angle` used here represent the position of the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is attached to. If the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is offset from the center of mass then the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) will be overlapped at the same offset. This can be confusing so it is recommened that only [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) that align with the center of mass are used. If not then you must take this into account. If the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is not attached to a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html), this call cannot be used and will result in a warning.  
  
Additional resources: [Physics2D.OverlapCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.OverlapCollider.html) and [Rigidbody2D.Overlap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.Overlap.html).
* * *
## Declaration
public int Overlap([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position, float angle, [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, List<Collider2D> results); 
### Parameters
Parameter | Description  
---|---  
position | The position to overlap the Collider at.  
angle | The angle to overlap the Collider at.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth. Note that normal angle is not used for overlap testing.  
results | The list to receive results.  
### Returns
**int** Returns the number of results placed in the `results` list. 
### Description
Get a list of all Colliders that overlap this Collider.
The integer return value is the number of Colliders that overlap this Collider with the specific Colliders stored in the supplied list. The results list will be resized if it doesn't contain enough elements to report all the results. This prevents memory from being allocated for results when the `results` list does not need to be resized, and improves garbage collection performance when the query is performed frequently.  
  
**NOTE** : The `position` and `angle` used here represent the position of the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is attached to. If the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is offset from the center of mass then the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) will be overlapped at the same offset. This can be confusing so it is recommened that only [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) that align with the center of mass are used. If not then you must take this into account. If the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is not attached to a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html), this call cannot be used and will result in a warning.  
  
Additional resources: [Physics2D.OverlapCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.OverlapCollider.html) and [Rigidbody2D.Overlap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.Overlap.html).
* * *
## Declaration
public int Overlap(List<Collider2D> results); 
### Parameters
Parameter | Description  
---|---  
results | The list to receive results.  
### Returns
**int** Returns the number of results placed in the `results` list. 
### Description
Get a list of all Colliders that overlap this Collider.
The integer return value is the number of Colliders that overlap this Collider with the specific Colliders stored in the supplied list. The results list will be resized if it doesn't contain enough elements to report all the results. This prevents memory from being allocated for results when the `results` list does not need to be resized, and improves garbage collection performance when the query is performed frequently.  
  
Additional resources: [Physics2D.OverlapCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.OverlapCollider.html) and [Rigidbody2D.Overlap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.Overlap.html).
* * *
## Declaration
public int Overlap([ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, List<Collider2D> results); 
### Parameters
Parameter | Description  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth. Note that normal angle is not used for overlap testing.  
results | The list to receive results.  
### Returns
**int** Returns the number of results placed in the `results` list. 
### Description
Get a list of all Colliders that overlap this Collider.
The integer return value is the number of Colliders that overlap this Collider with the specific Colliders stored in the supplied list. The results list will be resized if it doesn't contain enough elements to report all the results. This prevents memory from being allocated for results when the `results` list does not need to be resized, and improves garbage collection performance when the query is performed frequently.  
  
Additional resources: [Physics2D.OverlapCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.OverlapCollider.html) and [Rigidbody2D.Overlap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.Overlap.html).
* * *
## Declaration
public int Overlap([ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, Collider2D[] results); 
### Parameters
Parameter | Description  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth. Note that normal angle is not used for overlap testing.  
results | The array to receive results. The size of the array determines the maximum number of results that can be returned.  
### Returns
**int** Returns the number of results placed in the `results` array. 
### Description
Get a list of all colliders that overlap this collider.
The integer return value is the number of colliders that overlap this Collider and which could be stored in the supplied array given its length. The results array will not be resized if it doesn't contain enough elements to report all the results. The significance of this is that no memory is allocated for the results and so garbage collection performance is improved when the query is performed frequently.  
  
Additional resources: [Physics2D.OverlapCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.OverlapCollider.html) and [Rigidbody2D.Overlap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.Overlap.html).
* * *
