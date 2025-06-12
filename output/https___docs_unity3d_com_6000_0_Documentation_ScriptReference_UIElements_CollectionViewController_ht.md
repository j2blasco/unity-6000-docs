* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.html

# CollectionViewController
class in UnityEngine.UIElements
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
Base collection view controller. View controllers are meant to take care of data virtualized by any [BaseVerticalCollectionView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.html) inheritor. 
### Properties
Property | Description  
---|---  
[itemsSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController-itemsSource.html) |  The items source stored in a non-generic list.   
[view](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController-view.html) |  The view for this controller.   
### Public Methods
Method | Description  
---|---  
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
