* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ListViewController.html

# ListViewController
class in UnityEngine.UIElements
/
Inherits from:[UIElements.BaseListViewController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseListViewController.html)
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
List view controller. View controllers of this type are meant to take care of data virtualized by any [ListView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ListView.html) inheritor. 
### Properties
Property | Description  
---|---  
[listView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ListViewController-listView.html) |  View for this controller, cast as a ListView.   
### Inherited Members
### Properties
Property | Description  
---|---  
[baseListView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseListViewController-baseListView.html) |  View for this controller, cast as a BaseListView.   
[itemsSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController-itemsSource.html) |  The items source stored in a non-generic list.   
[view](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController-view.html) |  The view for this controller.   
### Public Methods
Method | Description  
---|---  
[AddItems](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseListViewController.AddItems.html) |  Adds a certain amount of items at the end of the collection.   
[ClearItems](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseListViewController.ClearItems.html) |  Removes all items from the source.   
[Move](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseListViewController.Move.html) |  Moves an item in the source.   
[NeedsDragHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseListViewController.NeedsDragHandle.html) |  Returns whether this item needs a drag handle or not with the Animated drag mode.   
[RemoveItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseListViewController.RemoveItem.html) |  Removes an item from the source, by index.   
[RemoveItems](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseListViewController.RemoveItems.html) |  Removes items from the source, by indices.   
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.Dispose.html) |  Called when this controller is not longer needed to provide a way to release resources.   
[GetIdForIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.GetIdForIndex.html) |  Returns the id for the specified index.   
[GetIndexForId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.GetIndexForId.html) |  Returns the index for the specified id.   
[GetItemForId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.GetItemForId.html) |  Returns the item with the specified ID.   
[GetItemForIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.GetItemForIndex.html) |  Returns the item with the specified index.   
[GetItemsCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.GetItemsCount.html) |  Returns the expected item count in the source.   
[SetView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.SetView.html) |  Sets the view for this controller.   
### Protected Methods
Method | Description  
---|---  
[RaiseItemsAdded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseListViewController.RaiseItemsAdded.html) |  Invokes the itemsAdded event.   
[RaiseItemsRemoved](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseListViewController.RaiseItemsRemoved.html) |  Invokes the itemsRemoved event.   
[RaiseOnSizeChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseListViewController.RaiseOnSizeChanged.html) |  Invokes the itemsSourceSizeChanged event.   
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
[itemsAdded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseListViewController-itemsAdded.html) |  Raised when an item is added to the CollectionViewController.itemsSource.   
[itemsRemoved](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseListViewController-itemsRemoved.html) |  Raised when an item is removed from the CollectionViewController.itemsSource.   
[itemsSourceSizeChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseListViewController-itemsSourceSizeChanged.html) |  Raised when the CollectionViewController.itemsSource size changes.   
[itemIndexChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController-itemIndexChanged.html) |  Raised when an item in the source changes index. The first argument is source index, second is destination index.   
[itemsSourceChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController-itemsSourceChanged.html) |  Raised when the itemsSource changes.   
* * *
