* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.HandleDragAndDropArgs.html

# HandleDragAndDropArgs
struct in UnityEngine.UIElements
/
Implemented in:[UnityEngine.UIElementsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UIElementsModule.html)
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
Information about a drag-and-drop operation in progress. See [BaseVerticalCollectionView.dragAndDropUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-dragAndDropUpdate.html) and [BaseVerticalCollectionView.handleDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-handleDrop.html). 
### Properties
Property | Description  
---|---  
[childIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.HandleDragAndDropArgs-childIndex.html) |  The child index under the parentId that the drag-and-drop operation targets. Used only for trees.   
[dragAndDropData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.HandleDragAndDropArgs-dragAndDropData.html) |  Data stored for the drag-and-drop operation.   
[dropPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.HandleDragAndDropArgs-dropPosition.html) |  The type of drop position.   
[insertAtIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.HandleDragAndDropArgs-insertAtIndex.html) |  The index at which the drop operation wants to happen.   
[parentId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.HandleDragAndDropArgs-parentId.html) |  The new parent targeted by the drag-and-drop operation. Used only for trees.   
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.HandleDragAndDropArgs-position.html) |  The world position of the pointer.   
[target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.HandleDragAndDropArgs-target.html) |  The target of the drop. There is only a target when hovering over an item. DropPosition.OverItem  
* * *
