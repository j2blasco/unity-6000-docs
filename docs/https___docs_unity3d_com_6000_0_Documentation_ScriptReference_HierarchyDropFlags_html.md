* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HierarchyDropFlags.html

# HierarchyDropFlags
enumeration
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
Define how dragged objects should be dropped relative to already existing Hierarchy items.
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HierarchyDropFlags.None.html) | Insert dragged object in the Hierarchy. The default flag value is 0. The only case in which DropMode is 0 is when dragging outside items and parentForDraggedObjects is set. Then dropTargetInstanceID is 0 and the target is passed to the parentForDraggedObjects.  
[DropUpon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HierarchyDropFlags.DropUpon.html) | Drop a dragged object on the Hierarchy item the mouse is hovering over. The hovered-over item is the dropTargetInstanceID and the dropped object is inserted as a child of the target. This flag is also used when dragging and dropping objects from outside the Hierarchy and into and below the last item in the Hierarchy to add to the Scene. In this case, the dropTargetInstanceID is the Scene handle.  
[DropBetween](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HierarchyDropFlags.DropBetween.html) | Drop a dragged object between two Hierarchy sibling items the mouse is hovered over. The dropTargetInstanceID is the Hierarchy item above the hover point, the dropped object is inserted below the target.   
[DropAfterParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HierarchyDropFlags.DropAfterParent.html) | Drop a dragged object into the first child position after the parent of the Hierarchy item when the mouse is hovering between the parent and the first child. The dropTargetInstanceID is the first child under a parent and the dropped object is inserted between the parent and the first child. When using DropAfterParent, DropBetween and DropAbove are also used to provide information to locate the dropped object.  
[SearchActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HierarchyDropFlags.SearchActive.html) | This flag is set if the Hierarchy is showing search results. If a search is active, only DropUpon is allowed (no other actions can be performed on a partial list of items).  
[DropAbove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HierarchyDropFlags.DropAbove.html) | Drop a dragged object above the Hierarchy sibling item the mouse is hovered over. The dropTargetInstanceID is the Hierarchy item below the hover point and the dropped object is inserted above the target.  
* * *
