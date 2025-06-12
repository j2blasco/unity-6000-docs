* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.Cast.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).Cast
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
public int Cast([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) direction, List<RaycastHit2D> results, float distance = Mathf.Infinity, bool ignoreSiblingColliders = true); 
### Parameters
Parameter | Description  
---|---  
direction | Vector representing the direction to cast the shape.  
results | List to receive results.  
distance | Maximum distance over which to cast the shape.  
ignoreSiblingColliders | Determines whether the cast should ignore Colliders attached to the same [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) (known as sibling Colliders).  
### Returns
**int** The number of results returned. 
### Description
Casts the Collider shape into the Scene starting at the Collider position ignoring the Collider itself.
This function will take the Collider shape and cast it into the Scene starting at the Collider position in the specified `direction` for an optional `distance` and return the results in the provided `results` list. The integer return value is the number of results written into the `results` list. The results list will be resized if it doesn't contain enough elements to report all the results. This prevents memory from being allocated for results when the `results` list does not need to be resized, and improves garbage collection performance when casts are performed frequently.  
  
Additionally, this also detects other Collider(s) at the Collider start position if they are overlapping. In this case, the cast shape will start inside the Collider and may not intersect the Collider surface. This means that the collision normal cannot be calculated, in which case the returned collision normal is set to the inverse of the `direction` vector being tested.
* * *
## Declaration
public int Cast([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) direction, [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, List<RaycastHit2D> results, float distance = Mathf.Infinity, bool ignoreSiblingColliders = true); 
### Parameters
Parameter | Description  
---|---  
direction | Vector representing the direction to cast the shape.  
contactFilter | Filter results defined by the contact filter.  
results | List to receive results.  
distance | Maximum distance over which to cast the shape.  
ignoreSiblingColliders | Determines whether the cast should ignore Colliders attached to the same [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) (known as sibling Colliders).  
### Returns
**int** The number of results returned. 
### Description
Casts the Collider shape into the Scene starting at the Collider position ignoring the Collider itself.
This function will take the Collider shape and cast it into the Scene starting at the Collider position in the specified `direction` for an optional `distance` and return the results in the provided `results` list. The integer return value is the number of results written into the `results` list. The results list will be resized if it doesn't contain enough elements to report all the results. This prevents memory from being allocated for results when the `results` list does not need to be resized, and improves garbage collection performance when casts are performed frequently.  
  
The `contactFilter` parameter can filter the returned results by the options in [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html).  
  
Additionally, this also detects other Collider(s) at the Collider start position if they are overlapping. In this case, the cast shape will start inside the Collider and may not intersect the Collider surface. This means that the collision normal cannot be calculated, in which case the returned collision normal is set to the inverse of the `direction` vector being tested.
* * *
## Declaration
public int Cast([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) direction, RaycastHit2D[] results, float distance = Mathf.Infinity, bool ignoreSiblingColliders = true); 
### Parameters
Parameter | Description  
---|---  
direction | Vector representing the direction to cast the shape.  
results | Array to receive results.  
distance | Maximum distance over which to cast the shape.  
ignoreSiblingColliders | Determines whether the cast should ignore Colliders attached to the same [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) (known as sibling Colliders).  
### Returns
**int** The number of results returned. 
### Description
Casts the Collider shape into the Scene starting at the Collider position ignoring the Collider itself.
This function will take the collider shape and cast it into the Scene starting at the collider position in the specified `direction` for an optional `distance` and return the results in the provided `results` array. The integer return value is the number of results written into the `results` array. The results array will not be resized if it doesn't contain enough elements to report all the results. The significance of this is that no memory is allocated for the results and so garbage collection performance is improved when casts are performed frequently.  
  
Additionally, this will also detect other Collider(s) at the collider start position if they are overlapping. In this case the cast shape will be starting inside the Collider and may not intersect the Collider surface. This means that the collision normal cannot be calculated in which case the collision normal returned is set to the inverse of the `direction` vector being tested.  
  
**Note:** Use of Collider2D.Cast() requires the use of [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html). If no [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) is declared [Cast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.Cast.html)() does not work. However a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) can be static and attached to the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html). This will make the [Cast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.Cast.html)() work as expected. Also, if the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) object has no [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) object then it can collide with objects which have both [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) and [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) objects.
* * *
## Declaration
public int Cast([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) direction, [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, RaycastHit2D[] results, float distance = Mathf.Infinity, bool ignoreSiblingColliders = true); 
### Parameters
Parameter | Description  
---|---  
direction | Vector representing the direction to cast the shape.  
contactFilter | Filter results defined by the contact filter.  
results | Array to receive results.  
distance | Maximum distance over which to cast the shape.  
ignoreSiblingColliders | Determines whether the cast should ignore Colliders attached to the same [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) (known as sibling Colliders).  
### Returns
**int** The number of results returned. 
### Description
Casts the Collider shape into the Scene starting at the Collider position ignoring the Collider itself.
This function will take the collider shape and cast it into the Scene starting at the collider position in the specified `direction` for an optional `distance` and return the results in the provided `results` array. The integer return value is the number of results written into the `results` array. The results array will not be resized if it doesn't contain enough elements to report all the results. The significance of this is that no memory is allocated for the results and so garbage collection performance is improved when casts are performed frequently.  
  
The `contactFilter` parameter can filter the returned results by the options in [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html).  
  
Additionally, this will also detect other Collider(s) at the collider start position if they are overlapping. In this case the cast shape will be starting inside the Collider and may not intersect the Collider surface. This means that the collision normal cannot be calculated in which case the collision normal returned is set to the inverse of the `direction` vector being tested.
* * *
## Declaration
public int Cast([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position, float angle, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) direction, List<RaycastHit2D> results, float distance = Mathf.Infinity, bool ignoreSiblingColliders = true); 
### Parameters
Parameter | Description  
---|---  
position | The position to start casting the Collider from.  
angle | The rotation of the Collider.  
direction | Vector representing the direction to cast the Collider.  
results | List to receive results.  
distance | Maximum distance over which to cast the Collider.  
ignoreSiblingColliders | Determines whether the cast should ignore other Colliders attached to the same [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) (known as sibling colliders).  
### Returns
**int** The number of results returned. 
### Description
Casts the Collider shape into the Scene starting at the specified position and rotation.
This function will take the Collider shape and cast it into the Scene starting at the specified `position` and `angle` for an optional `distance` and return the results in the provided `results` list.  
  
The integer return value is the number of results written into the `results` list. The results list will be resized if it doesn't contain enough elements to report all the results. This prevents memory from being allocated for results when the `results` list does not need to be resized, and improves garbage collection performance when casts are performed frequently.  
  
Additionally, this also detects other Collider(s) at the Collider start position if they are overlapping. In this case, the cast shape will start inside the Collider and may not intersect the Collider surface. This means that the collision normal cannot be calculated, in which case the returned collision normal is set to the inverse of the `direction` vector being tested.  
  
**NOTE** : The `position` and `angle` used here represent the position of the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is attached to. If the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is offset from the center of mass then the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) will be overlapped at the same offset. This can be confusing so it is recommened that only [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) that align with the center of mass are used. If not then you must take this into account. If the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is not attached to a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html), this call cannot be used and will result in a warning.
* * *
## Declaration
public int Cast([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position, float angle, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) direction, [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html) contactFilter, List<RaycastHit2D> results, float distance = Mathf.Infinity, bool ignoreSiblingColliders = true); 
### Parameters
Parameter | Description  
---|---  
position | The position to start casting the Collider from.  
angle | The rotation of the Collider.  
direction | Vector representing the direction to cast the Collider.  
contactFilter | Filter results defined by the contact filter.  
results | List to receive results.  
distance | Maximum distance over which to cast the Collider.  
ignoreSiblingColliders | Determines whether the cast should ignore other Colliders attached to the same [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) (known as sibling colliders).  
### Returns
**int** The number of results returned. 
### Description
Casts the Collider shape into the Scene starting at the specified position and rotation.
This function will take the Collider shape and cast it into the Scene starting at the specified `position` and `angle` for an optional `distance` and return the results in the provided `results` list.  
  
The `contactFilter` parameter can filter the returned results by the options in [ContactFilter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactFilter2D.html).  
  
The integer return value is the number of results written into the `results` list. The results list will be resized if it doesn't contain enough elements to report all the results. This prevents memory from being allocated for results when the `results` list does not need to be resized, and improves garbage collection performance when casts are performed frequently.  
  
Additionally, this also detects other Collider(s) at the Collider start position if they are overlapping. In this case, the cast shape will start inside the Collider and may not intersect the Collider surface. This means that the collision normal cannot be calculated, in which case the returned collision normal is set to the inverse of the `direction` vector being tested.  
  
**NOTE** : The `position` and `angle` used here represent the position of the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is attached to. If the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is offset from the center of mass then the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) will be overlapped at the same offset. This can be confusing so it is recommened that only [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) that align with the center of mass are used. If not then you must take this into account. If the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is not attached to a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html), this call cannot be used and will result in a warning.
* * *
