* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.html

# Hierarchy
class in Unity.Hierarchy
/
Implemented in:[UnityEngine.HierarchyCoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.HierarchyCoreModule.html)
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
Represents a tree-like container of nodes. 
### Properties
Property | Description  
---|---  
[Count](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.Count.html) |  The total number of nodes.   
[IsCreated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.IsCreated.html) |  Whether or not this object is valid and uses memory.   
[Root](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.Root.html) |  The root node.   
[UpdateNeeded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.UpdateNeeded.html) |  Whether the hierarchy requires an update.   
[Updating](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.Updating.html) |  Whether the hierarchy is currently updating.   
### Constructors
Constructor | Description  
---|---  
[Hierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy-ctor.html) |  Constructs a new Hierarchy.   
### Public Methods
Method | Description  
---|---  
[Add](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.Add.html) |  Adds a new node that has a specified parent node to the hierarchy.   
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.Clear.html) |  Removes all nodes from the hierarchy.   
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.Dispose.html) |  Dispose this object to release its memory.   
[DoesChildrenNeedsSorting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.DoesChildrenNeedsSorting.html) |  Gets whether the child nodes of a hierarchy node need to be sorted.   
[EnumerateChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.EnumerateChildren.html) |  Gets the child nodes of a hierarchy node.   
[EnumerateNodeTypeHandlersBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.EnumerateNodeTypeHandlersBase.html) |  Enumerates all the node type handlers base that this hierarchy uses.   
[Exists](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.Exists.html) |  Determines whether a node exists or not.   
[GetChild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.GetChild.html) |  Gets the child node at the specified index of a hierarchy node.   
[GetChildIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.GetChildIndex.html) |  Gets the index of a child node in the parent's children list.   
[GetChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.GetChildren.html) |  Gets the child nodes of a hierarchy node.   
[GetChildrenCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.GetChildrenCount.html) |  Gets the number of child nodes that a hierarchy node has.   
[GetChildrenCountRecursive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.GetChildrenCountRecursive.html) |  Gets the number of child nodes that a hierarchy node has, including children of children.   
[GetDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.GetDepth.html) |  Determines the depth of a node.   
[GetName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.GetName.html) |  Gets the name of a hierarchy node.   
[GetNextSibling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.GetNextSibling.html) |  Gets the next sibling of a node.   
[GetNodeType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.GetNodeType.html) |  Gets the type of the specified hierarchy node.   
[GetNodeTypeHandlerBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.GetNodeTypeHandlerBase.html) |  Gets a hierarchy node type handler instance from this hierarchy.   
[GetOrCreateNodeTypeHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.GetOrCreateNodeTypeHandler.html) |  Get or create a hierarchy node type handler instance for this hierarchy.   
[GetOrCreatePropertyString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.GetOrCreatePropertyString.html) |  Creates a string property with a specified name.   
[GetOrCreatePropertyUnmanaged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.GetOrCreatePropertyUnmanaged.html) |  Creates an unmanaged property with a specified name.   
[GetParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.GetParent.html) |  Gets the parent of a hierarchy node.   
[GetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.GetPath.html) |  Gets the path of a hierarchy node.   
[GetSortIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.GetSortIndex.html) |  Gets the sort index of a hierarchy node. Default is 0.   
[Remove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.Remove.html) |  Removes a node from the hierarchy.   
[RemoveChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.RemoveChildren.html) |  Recursively removes all children of a node.   
[Reserve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.Reserve.html) |  Ensures that the hierarchy has enough memory reserved for storing the specified number of nodes.   
[ReserveChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.ReserveChildren.html) |  Ensures that the hierarchy node has enough memory reserved for storing the specified number of children nodes.   
[SetName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.SetName.html) |  Sets the name of a hierarchy node.   
[SetParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.SetParent.html) |  Sets the parent of a hierarchy node.   
[SetSortIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.SetSortIndex.html) |  Sets the sort index of a hierarchy node.   
[SortChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.SortChildren.html) |  Sorts the child nodes of a hierarchy node according to their sort index.   
[Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.Update.html) |  Updates the hierarchy and requests that every registered hierarchy node type handler integrates their changes into the hierarchy.   
[UpdateIncremental](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.UpdateIncremental.html) |  Updates the hierarchy incrementally.   
[UpdateIncrementalTimed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.UpdateIncrementalTimed.html) |  Incrementally updates the hierarchy until a time limit is reached.   
* * *
