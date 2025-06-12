* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.html

# AccessibilityHierarchy
class in UnityEngine.Accessibility
/
Implemented in:[UnityEngine.AccessibilityModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AccessibilityModule.html)
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
Represents the hierarchy data model that the screen reader uses for reading and navigating the UI. 
A hierarchy must be set to active through [AssistiveSupport.activeHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AssistiveSupport-activeHierarchy.html) when the screen reader is on for the screen reader to function. If a hierarchy is not set active, the screen reader cannot read and navigate through the UI. Once an active hierarchy is set, if the hierarchy is modified, the screen reader must be notified by calling AssistiveSupport.NotificationDispatcher.SendLayoutChanged or AssistiveSupport.NotificationDispatcher.SendScreenChanged (depending if the changes are only at the layout level, or a more considerable screen change). Modifications in the hierarchy consist of calls to: 
  * [AccessibilityHierarchy.AddNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.AddNode.html)
  * [AccessibilityHierarchy.Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.Clear.html)
  * [AccessibilityHierarchy.InsertNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.InsertNode.html)
  * [AccessibilityHierarchy.MoveNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.MoveNode.html)
  * [AccessibilityHierarchy.RemoveNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.RemoveNode.html)
  * Modifications to node [AccessibilityNode.frame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityNode-frame.html) values.


### Properties
Property | Description  
---|---  
[rootNodes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy-rootNodes.html) |  The root nodes of the hierarchy.   
### Constructors
Constructor | Description  
---|---  
[AccessibilityHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy-ctor.html) |  Initializes and returns an instance of an AccessibilityHierarchy.   
### Public Methods
Method | Description  
---|---  
[AddNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.AddNode.html) |  Creates and adds a new node with the given label in this hierarchy under the given parent node. If no parent is provided, the new node is added as a root in the hierarchy.   
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.Clear.html) |  Resets the hierarchy to an empty state, removing all the nodes and removing focus.   
[ContainsNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.ContainsNode.html) |  Returns whether a given node exists in the hierarchy.   
[GetLowestCommonAncestor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.GetLowestCommonAncestor.html) |  Retrieves the lowest common ancestor of two nodes in the hierarchy. The lowest common ancestor is the node that is the common node that both nodes share in their path to the root node of their branch in the hierarchy.   
[InsertNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.InsertNode.html) |  Creates and inserts a new node with the given label at the given index in this hierarchy under the given parent node. If no parent is provided, the new node is inserted at the given index as a root in the hierarchy.   
[MoveNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.MoveNode.html) |  Moves the node elsewhere in the hierarchy, which causes the given node to be parented by a different node in the hierarchy. An optional index can be supplied for specifying the position within the list of children the moved node should take (zero-based). If no index is supplied, the node is added as the last child of the new parent by default. Root nodes can be moved elsewhere in the hierarchy, therefore ceasing to be a root. Non-root nodes can be moved to become a root node by providing null as the new parent node.Warning: The moving operation is costly as many checks have to be executed to guarantee the integrity of the hierarchy. Therefore this operation should not be done excessively as it may affect performance.  
[RefreshNodeFrames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.RefreshNodeFrames.html) |  Refreshes all the node frames (i.e. the screen elements' positions) for the hierarchy.   
[RemoveNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.RemoveNode.html) |  Removes the node from the hierarchy. Can also optionally remove nodes under the given node depending on the value of the removeChildren parameter.   
[TryGetNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.TryGetNode.html) |  Tries to get the node in this hierarchy that has the given ID.   
[TryGetNodeAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilityHierarchy.TryGetNodeAt.html) |  Tries to retrieve the node at the given position on the screen.   
* * *
