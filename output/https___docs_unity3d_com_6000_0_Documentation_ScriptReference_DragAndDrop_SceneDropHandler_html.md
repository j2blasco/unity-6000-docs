* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.SceneDropHandler.html

#  [DragAndDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.html).SceneDropHandler
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
public delegate [DragAndDropVisualMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.html) SceneDropHandler([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) dropUpon, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) worldPosition, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) viewportPosition, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) parentForDraggedObjects, bool perform); 
### Parameters
Parameter | Description  
---|---  
dropUpon | Dragged Game Object that is being dropped into the Scene view.  
worldPosition | Position in the world.  
viewportPosition | Position in the viewport.  
parentForDraggedObjects | Parent transform of the dragged object.  
perform | True if the event is of type EventType.DragPerform.  
### Description
Handler for the Scene.
* * *
