* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.HierarchyDropHandler.html

#  [DragAndDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.html).HierarchyDropHandler
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
public delegate [DragAndDropVisualMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.html) HierarchyDropHandler(int dropTargetInstanceID, [HierarchyDropFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HierarchyDropFlags.html) dropMode, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) parentForDraggedObjects, bool perform); 
### Parameters
Parameter | Description  
---|---  
dropTargetInstanceID | ID of the Game Object in the Hierarchy window that is under the mouse cursor.  
parentForDraggedObjects | The parentForDraggedObjects is only set under special situations in Prefab Mode (most often it will be null). If this value is set the dropTargetInstanceID is 0. And the client code should use 'parentForDraggedObjects' as a forced parent of the drag.  
perform | True if the event is of type EventType.DragPerform.  
dropMode | Specify how the dragged object is to be dropped in the Hierarchy window.  
### Returns
**DragAndDropVisualMode** Returns [DragAndDropVisualMode.None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.None.html) if this handler is not able to process event. In that case a new handler will be called for processing. Any other [DragAndDropVisualMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.html) results will stop the handler chain. 
### Description
Handler for the Hierarchy.
* * *
