* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TreeViewController.html

# TreeViewController
class in UnityEngine.UIElements
/
Inherits from:[UIElements.BaseTreeViewController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.html)
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
Tree view controller. View controllers of this type are meant to take care of data virtualized by any [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TreeView.html) inheritor. 
### Properties
Property | Description  
---|---  
[treeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TreeViewController-treeView.html) |  View for this controller, cast as a TreeView.   
### Inherited Members
### Properties
Property | Description  
---|---  
[baseTreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController-baseTreeView.html) |  View for this controller, cast as a BaseTreeView.   
[itemsSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController-itemsSource.html) |  Items for this tree. Contains items that are expanded in the tree.   
[view](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController-view.html) |  The view for this controller.   
### Public Methods
Method | Description  
---|---  
[CanChangeExpandedState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.CanChangeExpandedState.html) |  Determines whether the item with the specified ID can be expanded or collapsed.   
[CollapseAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.CollapseAll.html) |  Collapses all items in the tree and refreshes the view.   
[CollapseItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.CollapseItem.html) |  Collapses the item with the specified ID, hiding its children. Allows to collapse the whole hierarchy under that item.   
[CollapseItemByIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.CollapseItemByIndex.html) |  Collapses the item with the specified index, hiding its children. Allows to collapse the whole hierarchy under that item.   
[Exists](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.Exists.html) |  Checks if an ID exists within this tree.   
[ExpandAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.ExpandAll.html) |  Expands all items in the tree and refreshes the view.   
[ExpandItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.ExpandItem.html) |  Expands the item with the specified ID, making its children visible. Allows to expand the whole hierarchy under that item.   
[ExpandItemByIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.ExpandItemByIndex.html) |  Expands the item with the specified index, making his children visible. Allows to expand the whole hierarchy under that item.   
[GetAllItemIds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.GetAllItemIds.html) |  Returns all item IDs that can be found in the tree, optionally specifying root IDs from where to start.   
[GetChildIndexForId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.GetChildIndexForId.html) |  Gets the child index under the parent of the item with the specified ID.   
[GetChildrenIds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.GetChildrenIds.html) |  Get all children of a specific ID in the tree.   
[GetChildrenIdsByIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.GetChildrenIdsByIndex.html) |  Gets the children IDs of the item with the specified index.   
[GetIdForIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.GetIdForIndex.html) |  Returns the ID for a specified index in the visible items source.   
[GetIndentationDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.GetIndentationDepth.html) |  Returns the depth of the element at that ID.   
[GetIndentationDepthByIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.GetIndentationDepthByIndex.html) |  Return the depth of the element at that index.   
[GetIndexForId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.GetIndexForId.html) |  Returns the index in the source of the item, by ID.   
[GetParentId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.GetParentId.html) |  Returns the parent ID of an item, by ID.   
[GetRootItemIds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.GetRootItemIds.html) |  Returns the root items of the tree, by IDs.   
[GetTreeItemsCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.GetTreeItemsCount.html) |  Get the number of items in the whole tree.   
[HasChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.HasChildren.html) |  Return whether the item with the specified ID has one or more child.   
[HasChildrenByIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.HasChildrenByIndex.html) |  Return whether the item with the specified index has one or more child.   
[IsExpanded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.IsExpanded.html) |  Return whether the item with the specified ID is expanded in the tree.   
[IsExpandedByIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.IsExpandedByIndex.html) |  Return whether the item with the specified index is expanded in the tree.   
[Move](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.Move.html) |  Moves an item by ID, to a new parent and child index.   
[TryRemoveItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.TryRemoveItem.html) |  Removes an item by id.   
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.Dispose.html) |  Called when this controller is not longer needed to provide a way to release resources.   
[GetItemForId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.GetItemForId.html) |  Returns the item with the specified ID.   
[GetItemForIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.GetItemForIndex.html) |  Returns the item with the specified index.   
[GetItemsCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.GetItemsCount.html) |  Returns the expected item count in the source.   
[SetView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.SetView.html) |  Sets the view for this controller.   
### Protected Methods
Method | Description  
---|---  
[BindItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.BindItem.html) |  Binds a row to an item index.   
[DestroyItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.DestroyItem.html) |  Destroys a VisualElement when the view is rebuilt or cleared.   
[MakeItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.MakeItem.html) |  Creates a VisualElement to use in the virtualization of the collection view.   
[PrepareView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.PrepareView.html) |  Initialization step once the view is set.   
[RaiseItemIndexChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.RaiseItemIndexChanged.html) |  Invokes the itemIndexChanged event.   
[RaiseItemsSourceChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.RaiseItemsSourceChanged.html) |  Invokes the itemsSourceChanged event.   
[SetItemsSourceWithoutNotify](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.SetItemsSourceWithoutNotify.html) |  Set the itemsSource without raising the itemsSourceChanged event.   
[UnbindItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.UnbindItem.html) |  Unbinds a row to an item index.   
### Events
Event | Description  
---|---  
[itemIndexChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController-itemIndexChanged.html) |  Raised when an item in the source changes index. The first argument is source index, second is destination index.   
[itemsSourceChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController-itemsSourceChanged.html) |  Raised when the itemsSource changes.   
* * *
