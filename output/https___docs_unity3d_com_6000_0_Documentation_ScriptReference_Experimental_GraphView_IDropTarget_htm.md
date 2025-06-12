* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.IDropTarget.html

**Experimental** : this API is experimental and might be changed or removed in the future.
# IDropTarget
interface in UnityEditor.Experimental.GraphView
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
Drop target interface.
### Public Methods
Method | Description  
---|---  
[CanAcceptDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.IDropTarget.CanAcceptDrop.html) | Indicates if the dragged source can be dropped on the target interface.  
[DragEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.IDropTarget.DragEnter.html) | This method is automatically called when the dragged source intersects the drop target.  
[DragExited](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.IDropTarget.DragExited.html) | This method is automatically called when dragging ends and the drag source is not over a valid drop target.  
[DragLeave](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.IDropTarget.DragLeave.html) | This method is automatically called when the dragged source no longer intersects the drop target.  
[DragPerform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.IDropTarget.DragPerform.html) | "This method is automatically called when a drag is performed."  
[DragUpdated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.IDropTarget.DragUpdated.html) | This method is automatically called when the drag source is updated.  
* * *
