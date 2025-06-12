* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.FindNearestVertex.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).FindNearestVertex
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
public static bool FindNearestVertex([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) guiPoint, out [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) vertex); 
## Declaration
public static bool FindNearestVertex([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) guiPoint, Transform[] objectsToSearch, out [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) vertex); 
## Declaration
public static bool FindNearestVertex([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) guiPoint, Transform[] objectsToSearch, Transform[] objectsToIgnore, out [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) vertex); 
## Declaration
public static bool FindNearestVertex([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) guiPoint, out [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) vertex, out [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject); 
## Declaration
public static bool FindNearestVertex([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) guiPoint, Transform[] objectsToSearch, out [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) vertex, out [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject); 
## Declaration
public static bool FindNearestVertex([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) guiPoint, Transform[] objectsToSearch, Transform[] objectsToIgnore, out [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) vertex, out [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject); 
### Parameters
Parameter | Description  
---|---  
guiPoint | A point in GUI space.  
vertex | The nearest vertex position to [guiPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility-guiPoint.html), or a default value if no vertex is within the minimum picking distance.  
objectsToSearch | An array of [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) to consider when picking the nearest vertex. If null, all active objects in open scenes are considered.  
objectsToIgnore | An array of [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) to exclude from consideration when picking nearest vertex.  
gameObject | The [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that contains the nearest vertex found by this function. Null if no vertex was found.  
### Returns
**bool** Returns true if a vertex within 50 pixels of the guiPoint was found, false if no vertex found within the minimum picking radius. 
### Description
Returns the nearest vertex to a guiPoint within a maximum radius of 50 pixels.
* * *
