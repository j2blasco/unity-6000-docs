* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.html

# DragAndDrop
class in UnityEditor
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
### Description
Editor drag & drop operations.
### Static Properties
Property | Description  
---|---  
[activeControlID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop-activeControlID.html) | Get or set ID of currently active drag and drop control.  
[objectReferences](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop-objectReferences.html) | References to objects being dragged.  
[paths](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop-paths.html) | The file names being dragged.  
[visualMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop-visualMode.html) | The visual indication of the drag.  
### Static Methods
Method | Description  
---|---  
[AcceptDrag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.AcceptDrag.html) | Accept a drag operation.  
[AddDropHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.AddDropHandler.html) | Allow override of the default behavior for the corresponding window. Multiple handlers can be registered on the same window. If a handler returns DragAndDropVisualMode.None the system will check the next handler. Any other results (DragAndDropVisualMode.Rejected or others DragAndDropVisualMode) means this handler has processed the drop event and no other handler will be called. The last handler is the default Unity handler.  
[GetGenericData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.GetGenericData.html) | Get data associated with current drag and drop operation.  
[HasHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.HasHandler.html) | Check if the handler is already registered for the destination window ID.  
[PrepareStartDrag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.PrepareStartDrag.html) | Clears drag & drop data.  
[RemoveDropHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.RemoveDropHandler.html) | Unregister a specific Drop Handler from a Window Drop Target.  
[SetGenericData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.SetGenericData.html) | Set data associated with current drag and drop operation.  
[StartDrag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.StartDrag.html) | Start a drag operation.  
### Delegates
Delegate | Description  
---|---  
[HierarchyDropHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.HierarchyDropHandler.html) | Handler for the Hierarchy.  
[InspectorDropHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.InspectorDropHandler.html) | Handler for the Inspector.  
[ProjectBrowserDropHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.ProjectBrowserDropHandler.html) | Handler for the Project.  
[SceneDropHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.SceneDropHandler.html) | Handler for the Scene.  
* * *
