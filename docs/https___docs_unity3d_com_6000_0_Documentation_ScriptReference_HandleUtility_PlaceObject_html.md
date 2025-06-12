* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PlaceObject.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).PlaceObject
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
public static bool PlaceObject([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) guiPosition, out [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, out [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) normal); 
### Parameters
Parameter | Description  
---|---  
guiPosition | The GUI position in the [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html). You can pass Event.current.mousePosition to this parameter in most cases.  
position | Returns the nearest intersected point to a ray cast from the mouse position into the scene.  
normal | Returns the normal of the nearest intersected point to a ray cast from the mouse position into the scene.  
### Returns
**bool** Returns true if the raycast intersected something in the scene; otherwise, false. 
### Description
Casts a ray against the loaded scenes and returns the nearest intersected point on a collider.
Use this method to match the behavior of drag and drop in the [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html).  
  
[PlaceObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PlaceObject.html) also queries any delegates registered to [placeObjectCustomPasses](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility-placeObjectCustomPasses.html) when determining the nearest point.
* * *
