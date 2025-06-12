* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.StackNode.DragLeave.html

**Experimental** : this API is experimental and might be changed or removed in the future.
#  [StackNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.StackNode.html).DragLeave
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
public bool DragLeave([UIElements.DragLeaveEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragLeaveEvent.html) evt, IEnumerable<ISelectable> selection, [Experimental.GraphView.IDropTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.IDropTarget.html) leftTarget, [Experimental.GraphView.ISelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ISelection.html) dragSource); 
### Parameters
Parameter | Description  
---|---  
evt | The event.  
selection | The selected elements.  
leftTarget | The drop target.  
dragSource | The drag source.  
### Returns
**bool** Returns event propagation. 
### Description
This method is automatically called when a drag leave event occurs.
* * *
