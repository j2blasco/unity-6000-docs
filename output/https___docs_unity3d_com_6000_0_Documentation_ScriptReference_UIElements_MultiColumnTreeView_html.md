* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnTreeView.html

# MultiColumnTreeView
class in UnityEngine.UIElements
/
Inherits from:[UIElements.BaseTreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.html)
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
A tree view with multi column support. For more information, refer to [MultiColumnTreeView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-MultiColumnTreeView.html). 
### Properties
Property | Description  
---|---  
[columns](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnTreeView-columns.html) |  The collection of columns for the multi-column header.   
[sortColumnDescriptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnTreeView-sortColumnDescriptions.html) |  The collection of sorted columns by default.   
[sortedColumns](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnTreeView-sortedColumns.html) |  Contains information about which columns are currently being sorted.   
[sortingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnTreeView-sortingMode.html) |  Indicates how to sort columns. To enable sorting, set it to ColumnSortingMode.Default or ColumnSortingMode.Custom. The Default mode uses the sorting algorithm provided by MultiColumnController, acting on indices. You can also implement your own sorting with the Custom mode, by responding to the columnSortingChanged event.   
[viewController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnTreeView-viewController.html) |  The view controller for this view, cast as a MultiColumnTreeViewController.   
### Constructors
Constructor | Description  
---|---  
[MultiColumnTreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnTreeView-ctor.html) |  Initializes a MultiColumnTreeView with an empty header.   
### Public Methods
Method | Description  
---|---  
[SetViewController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnTreeView.SetViewController.html) |  Assigns the view controller for this view and registers all events required for it to function properly.   
### Events
Event | Description  
---|---  
[columnSortingChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnTreeView-columnSortingChanged.html) |  If a column is clicked to change sorting, this event is raised to allow users to sort the tree view items. For a default implementation, set sortingMode to ColumnSortingMode.Default.   
[headerContextMenuPopulateEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnTreeView-headerContextMenuPopulateEvent.html) |  If a column is right-clicked to show context menu options, this event is raised to allow users to change the available options.   
### Inherited Members
### Static Properties
Property | Description  
---|---  
[itemContentContainerUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView-itemContentContainerUssClassName.html) |  The USS class name for TreeView item container elements.   
[itemIndentUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView-itemIndentUssClassName.html) |  The USS class name for TreeView indent element.   
[itemToggleUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView-itemToggleUssClassName.html) |  The USS class name for TreeView item toggle elements.   
[itemUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView-itemUssClassName.html) |  The USS class name for TreeView item elements.   
[ussClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView-ussClassName.html) |  The USS class name for TreeView elements.   
[borderUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-borderUssClassName.html) |  The USS class name for BaseVerticalCollectionView elements with a border.   
[dragHoverBarUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-dragHoverBarUssClassName.html) |  The USS class name of the drag hover bar.   
[dragHoverMarkerUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-dragHoverMarkerUssClassName.html) |  The USS class name of the drag hover circular marker used to indicate depth.   
[itemAlternativeBackgroundUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-itemAlternativeBackgroundUssClassName.html) |  The USS class name for odd rows in the BaseVerticalCollectionView.   
[itemDragHoverUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-itemDragHoverUssClassName.html) |  The USS class name applied to an item element on drag hover.   
[itemSelectedVariantUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-itemSelectedVariantUssClassName.html) |  The USS class name of selected item elements in the BaseVerticalCollectionView.   
[listScrollViewUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-listScrollViewUssClassName.html) |  The USS class name of the scroll view in the BaseVerticalCollectionView.   
[disabledUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-disabledUssClassName.html) |  USS class name of local disabled elements.   
### Properties
Property | Description  
---|---  
[autoExpand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView-autoExpand.html) |  When true, items are automatically expanded when added to the TreeView.   
[itemsSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView-itemsSource.html) |  Access to the itemsSource. For a TreeView, the source contains the items wrappers.   
[viewController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView-viewController.html) |  The view controller for this view, cast as a BaseTreeViewController.   
[contentContainer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-contentContainer.html) |  Returns the content container for the BaseVerticalCollectionView. Because the BaseVerticalCollectionView control automatically manages its content, this always returns null.   
[fixedItemHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-fixedItemHeight.html) |  The height of a single item in the list, in pixels.   
[horizontalScrollingEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-horizontalScrollingEnabled.html) |  This property controls whether the collection view shows a horizontal scroll bar when its content does not fit in the visible area.   
[reorderable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-reorderable.html) |  Gets or sets a value that indicates whether the user can drag list items to reorder them.   
[selectedIds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-selectedIds.html) |  Returns the persistent IDs of selected items in the data source, regardless of whether they are collapsed or not. Always returns an enumerable, even if no item is selected, or a single item is selected.   
[selectedIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-selectedIndex.html) |  Returns or sets the selected item's index in the data source. If multiple items are selected, returns the first selected item's index. If multiple items are provided, sets them all as selected. If no item is selected, returns -1.   
[selectedIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-selectedIndices.html) |  Returns the indices of selected items in the data source. Always returns an enumerable, even if no item is selected, or a single item is selected.   
[selectedItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-selectedItem.html) |  Returns the selected item from the data source. If multiple items are selected, returns the first selected item.   
[selectedItems](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-selectedItems.html) |  Returns the selected items from the data source. Always returns an enumerable, even if no item is selected, or a single item is selected.   
[selectionType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-selectionType.html) |  Controls the selection type.   
[showAlternatingRowBackgrounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-showAlternatingRowBackgrounds.html) |  This property controls whether the background colors of collection view rows alternate. Takes a value from the AlternatingRowBackground enum.   
[showBorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-showBorder.html) |  Enable this property to display a border around the collection view.   
[virtualizationMethod](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-virtualizationMethod.html) |  The virtualization method to use for this collection when a scroll bar is visible. Takes a value from the CollectionVirtualizationMethod enum.   
[binding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindableElement-binding.html) |  Binding object that will be updated.   
[bindingPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindableElement-bindingPath.html) |  Path of the target property to be bound.   
[canGrabFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable-canGrabFocus.html) |  Return true if the element can be focused.   
[delegatesFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable-delegatesFocus.html) |  Whether the element should delegate the focus to its children.   
[focusable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable-focusable.html) |  True if the element can be focused.   
[focusController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable-focusController.html) |  Return the focus controller for this element.   
[tabIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable-tabIndex.html) |  An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.   
[childCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-childCount.html) |  Number of child elements in this object's contentContainer.   
[contentRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-contentRect.html) |  The rectangle of the content area of the element, in the local space of the element. (Read Only)   
[customStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-customStyle.html) |  The custom style properties accessor of a VisualElement (Read Only).   
[dataSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-dataSource.html) |  Assigns a data source to this VisualElement which overrides any inherited data source. This data source is inherited by all children.   
[dataSourcePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-dataSourcePath.html) |  Path from the data source to the value.   
[dataSourceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-dataSourceType.html) |  The possible type of data source assignable to this VisualElement. This information is only used by the UI Builder as a hint to provide some completion to the data source path field when the effective data source cannot be specified at design time.   
[disablePlayModeTint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-disablePlayModeTint.html) |  Play-mode tint is applied by default unless this is set to true. It's applied hierarchically to this VisualElement and to all its children that exist on an editor panel.   
[enabledInHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-enabledInHierarchy.html) |  Returns true if the VisualElement is enabled in its own hierarchy.   
[enabledSelf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-enabledSelf.html) |  Returns true if the VisualElement is enabled locally.   
[experimental](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-experimental.html) |  Returns the UIElements experimental interfaces.   
[generateVisualContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-generateVisualContent.html) |  Delegate function to generate the visual content of a visual element.   
[hierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-hierarchy.html) |  Access to this element physical hierarchy   
[languageDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-languageDirection.html) |  Indicates the directionality of the element's text. The value will propagate to the element's children.   
[layout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-layout.html) |  The position and size of the VisualElement relative to its parent, as computed by the layout system. (Read Only)   
[localBound](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-localBound.html) |  Returns a Rect representing the Axis-aligned Bounding Box (AABB) after applying the transform, but before applying the layout translation.   
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-name.html) |  The name of this VisualElement.   
[paddingRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-paddingRect.html) |  The rectangle of the padding area of the element, in the local space of the element.   
[panel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-panel.html) |  The panel onto which this VisualElement is attached.   
[parent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-parent.html) |  The parent of this VisualElement.   
[pickingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-pickingMode.html) |  Determines if this element can be pick during mouseEvents or IPanel.Pick queries.   
[resolvedStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-resolvedStyle.html) |  The final rendered style values of a visual element, as it's rendered in the current frame.(Read Only)   
[scaledPixelsPerPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-scaledPixelsPerPoint.html) |  Return the resulting scaling from the panel that considers the screen DPI and the customizable scaling factor, but not the transform scale of the element and its ancestors. See Panel.scaledPixelsPerPoint. This should only be called on elements that are part of a panel.   
[schedule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-schedule.html) |  Retrieves this VisualElement's IVisualElementScheduler   
[style](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-style.html) |  Sets the style values on a VisualElement.   
[styleSheets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-styleSheets.html) |  Returns a VisualElementStyleSheetSet that manipulates style sheets attached to this element.   
[this[int]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.Index_operator.html) |  Retrieves the child element at a specific index.   
[tooltip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-tooltip.html) |  Text to display inside an information box after the user hovers the element for a small amount of time. This is only supported in the Editor UI.   
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-transform.html) |  Returns a transform object for this VisualElement. ITransform  
[usageHints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-usageHints.html) |  A combination of hint values that specify high-level intended usage patterns for the VisualElement. This property can only be set when the VisualElement is not yet part of a Panel. Once part of a Panel, this property becomes effectively read-only, and attempts to change it will throw an exception. The specification of proper UsageHints drives the system to make better decisions on how to process or accelerate certain operations based on the anticipated usage pattern. Note that those hints do not affect behavioral or visual results, but only affect the overall performance of the panel and the elements within. It's advised to always consider specifying the proper UsageHints, but keep in mind that some UsageHints might be internally ignored under certain conditions (e.g. due to hardware limitations on the target platform).   
[userData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-userData.html) |  This property can be used to associate application-specific user data with this VisualElement.   
[viewDataKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-viewDataKey.html) |  Used for view data persistence, such as tree expanded states, scroll position, or zoom level.   
[visible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-visible.html) |  Indicates whether or not this element should be rendered.   
[visualTreeAssetSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-visualTreeAssetSource.html) |  Stores the asset reference, if the generated element is cloned from a VisualTreeAsset.   
[worldBound](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-worldBound.html) |  Returns a Rect representing the Axis-aligned Bounding Box (AABB) after applying the world transform.   
[worldTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-worldTransform.html) |  Returns a matrix that cumulates the following operations (in order): -Local Scaling -Local Rotation -Local Translation -Layout Translation -Parent worldTransform (recursive definition - consider identity when there is no parent)   
### Public Methods
Method | Description  
---|---  
[AddItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.AddItem.html) |  Adds an item to the existing tree.   
[AddToSelectionById](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.AddToSelectionById.html) |  Adds an item to the current selection by id.   
[CollapseAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.CollapseAll.html) |  Collapses all TreeView items, including children.   
[CollapseItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.CollapseItem.html) |  Collapses the specified TreeView item.   
[ExpandAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.ExpandAll.html) |  Expands all TreeView items, including children.   
[ExpandItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.ExpandItem.html) |  Expands the specified TreeView item.   
[ExpandRootItems](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.ExpandRootItems.html) |  Expands all root TreeView items.   
[GetChildrenIdsForIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.GetChildrenIdsForIndex.html) |  Gets children identifiers for the specified TreeView item.   
[GetIdForIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.GetIdForIndex.html) |  Gets the specified TreeView item's identifier.   
[GetItemDataForId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.GetItemDataForId.html) |  Gets data for the specified TreeView item id.   
[GetItemDataForIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.GetItemDataForIndex.html) |  Gets data for the specified TreeView item index.   
[GetParentIdForIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.GetParentIdForIndex.html) |  Gets the specified TreeView item's parent identifier.   
[GetRootIds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.GetRootIds.html) |  Gets the root item identifiers.   
[GetSelectedItems](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.GetSelectedItems.html) |  Gets tree data for the selected item indices.   
[GetTreeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.GetTreeCount.html) |  Gets the TreeView's total number of items.   
[IsExpanded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.IsExpanded.html) |  Returns true if the specified TreeView item is expanded, false otherwise.   
[RemoveFromSelectionById](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.RemoveFromSelectionById.html) |  Removes an item from the current selection by id.   
[SetRootItems](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.SetRootItems.html) |  Sets the root items to use with the default tree view controller.   
[SetSelectionById](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.SetSelectionById.html) |  Sets the currently selected item by id.   
[SetSelectionByIdWithoutNotify](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.SetSelectionByIdWithoutNotify.html) |  Sets a collection of selected items by id, without triggering a selection change callback.   
[TryRemoveItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.TryRemoveItem.html) |  Removes an item of the tree if it can find it.   
[AddToSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.AddToSelection.html) |  Adds an item to the collection of selected items.   
[ClearSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.ClearSelection.html) |  Deselects any selected items.   
[GetRootElementForId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.GetRootElementForId.html) |  Gets the root element of the specified collection view item.   
[GetRootElementForIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.GetRootElementForIndex.html) |  Gets the root element of the specified collection view item.   
[Rebuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.Rebuild.html) |  Clears the collection view, recreates all visible visual elements, and rebinds all items.   
[RefreshItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.RefreshItem.html) |  Rebinds a single item if it is currently visible in the collection view.   
[RefreshItems](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.RefreshItems.html) |  Rebinds all items currently visible.   
[RemoveFromSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.RemoveFromSelection.html) |  Removes an item from the collection of selected items.   
[ScrollTo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.ScrollTo.html) |  Scrolls to a specific VisualElement.   
[ScrollToItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.ScrollToItem.html) |  Scrolls to a specific item index and makes it visible.   
[ScrollToItemById](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.ScrollToItemById.html) |  Scrolls to a specific item id and makes it visible.   
[SetSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.SetSelection.html) |  Sets the currently selected item.   
[SetSelectionWithoutNotify](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.SetSelectionWithoutNotify.html) |  Sets a collection of selected items without triggering a selection change callback.   
[HasBubbleUpHandlers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.HasBubbleUpHandlers.html) |  Return true if event handlers for the event propagation BubbleUp phase have been attached to this object.   
[HasTrickleDownHandlers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.HasTrickleDownHandlers.html) |  Returns true if event handlers, for the event propagation TrickleDown phase, are attached to this object.   
[RegisterCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.RegisterCallback.html) |  Adds an event handler to the instance. If the event handler has already been registered for the same phase (either TrickleDown or BubbleUp) then this method has no effect.   
[RegisterCallbackOnce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.RegisterCallbackOnce.html) |  Adds an event handler to the instance. If the event handler has already been registered for the same phase (either TrickleDown or BubbleUp) then this method has no effect. The event handler is automatically unregistered after it has been invoked exactly once.   
[UnregisterCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.UnregisterCallback.html) |  Remove callback from the instance.   
[Blur](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable.Blur.html) |  Tell the element to release the focus.   
[Focus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable.Focus.html) |  Attempt to give the focus to this element.   
[Add](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.Add.html) |  Add an element to this element's contentContainer   
[AddToClassList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.AddToClassList.html) |  Adds a class to the class list of the element in order to assign styles from USS. Note the class name is case-sensitive.   
[BringToFront](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.BringToFront.html) |  Brings this element to the end of its parent children list. The element will be visually in front of any overlapping sibling elements.   
[Children](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.Children.html) |  Returns the elements from its contentContainer.   
[ClassListContains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.ClassListContains.html) |  Searches for a class in the class list of this element.   
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.Clear.html) |  Remove all child elements from this element's contentContainer   
[ClearBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.ClearBinding.html) |  Removes a binding from the element.   
[ClearBindings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.ClearBindings.html) |  Removes all bindings from the element.   
[ClearClassList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.ClearClassList.html) |  Removes all classes from the class list of this element. AddToClassList  
[Contains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.Contains.html) |  Checks if this element is an ancestor of the specified child element.   
[ContainsPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.ContainsPoint.html) |  Checks if the specified point intersects with this VisualElement's layout.   
[ElementAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.ElementAt.html) |  Retrieves the child element at a specific index.   
[EnableInClassList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.EnableInClassList.html) |  Enables or disables the class with the given name.   
[FindAncestorUserData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.FindAncestorUserData.html) |  Searches up the hierarchy of this VisualElement and retrieves stored userData, if any is found.   
[FindCommonAncestor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.FindCommonAncestor.html) |  Finds the lowest common ancestor between two VisualElements inside the VisualTree hierarchy.   
[GetBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.GetBinding.html) |  Gets the binding instance for the provided targeted property.   
[GetBindingInfos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.GetBindingInfos.html) |  Gets information on all the bindings of the current element.   
[GetClasses](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.GetClasses.html) |  Retrieve the classes for this element.   
[GetDataSourceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.GetDataSourceContext.html) |  Queries the dataSource and dataSourcePath of a binding object.   
[GetFirstAncestorOfType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.GetFirstAncestorOfType.html) |  Walks up the hierarchy, starting from this element's parent, and returns the first VisualElement of this type   
[GetFirstOfType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.GetFirstOfType.html) |  Walks up the hierarchy, starting from this element, and returns the first VisualElement of this type   
[GetHierarchicalDataSourceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.GetHierarchicalDataSourceContext.html) |  Queries the dataSource and dataSourcePath inherited from the hierarchy.   
[HasBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.HasBinding.html) |  Allows to know if a target property has a binding associated to it.   
[IndexOf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.IndexOf.html) |  Retrieves the child index of the specified VisualElement.   
[Insert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.Insert.html) |  Insert an element into this element's contentContainer   
[MarkDirtyRepaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.MarkDirtyRepaint.html) |  Triggers a repaint of the VisualElement on the next frame. This method is called internally when a change occurs that requires a repaint, such as when UIElements.BaseField_1.value is changed or the text in a Label. If you are implementing a custom control, you can call this method to trigger a repaint when a change occurs that requires a repaint such as when using generateVisualContent to render a mesh and the mesh data has now changed.   
[PlaceBehind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.PlaceBehind.html) |  Places this element right before the sibling element in their parent children list. If the element and the sibling position overlap, the element will be visually behind of its sibling.   
[PlaceInFront](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.PlaceInFront.html) |  Places this element right after the sibling element in their parent children list. If the element and the sibling position overlap, the element will be visually in front of its sibling.   
[Remove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.Remove.html) |  Removes this child from the contentContainerhierarchy.   
[RemoveAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.RemoveAt.html) |  Remove the child element located at this position from this element's contentContainer   
[RemoveFromClassList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.RemoveFromClassList.html) |  Removes a class from the class list of the element.   
[RemoveFromHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.RemoveFromHierarchy.html) |  Removes this element from its parent hierarchy.   
[SendEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.SendEvent.html) |  Sends an event to the event handler.   
[SendToBack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.SendToBack.html) |  Sends this element to the beginning of its parent children list. The element will be visually behind any overlapping sibling elements.   
[SetBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.SetBinding.html) |  Assigns a binding between a target and a source.   
[SetEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.SetEnabled.html) |  Changes the VisualElement enabled state. A disabled visual element does not receive most events.   
[Sort](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.Sort.html) |  Reorders child elements from this VisualElement contentContainer.   
[ToggleInClassList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.ToggleInClassList.html) |  Toggles between adding and removing the given class name from the class list.   
[TryGetBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.TryGetBinding.html) |  Gets the binding instance for the provided targeted property.   
[TryGetDataSourceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.TryGetDataSourceContext.html) |  Queries the dataSource and dataSourcePath of a binding object.   
[TryGetLastBindingToSourceResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.TryGetLastBindingToSourceResult.html) |  Returns the last BindingResult of a binding object from the UI to the data source.   
[TryGetLastBindingToUIResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.TryGetLastBindingToUIResult.html) |  Returns the last BindingResult of a binding object from the data source to the UI.   
### Protected Methods
Method | Description  
---|---  
[CreateViewController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.CreateViewController.html) |  Creates the view controller for this view. Override this method in inheritors to change the controller type.   
[HandleEventBubbleUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.HandleEventBubbleUp.html) |  Executes logic on this element during the BubbleUp phase, immediately before this element's BubbleUp callbacks. Calling StopPropagation will prevent further invocations of this method along the propagation path.   
[HandleEventTrickleDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.HandleEventTrickleDown.html) |  Executes logic on this element during the TrickleDown phase, immediately after this element's TrickleDown callbacks. Calling StopPropagation will prevent further invocations of this method along the propagation path.   
[NotifyPropertyChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.NotifyPropertyChanged.html) |  Informs the data binding system that a property of a control has changed.   
### Events
Event | Description  
---|---  
[itemExpandedChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView-itemExpandedChanged.html) |  Raised when an item is expanded or collapsed.   
[canStartDrag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-canStartDrag.html) |  Called when a drag operation wants to start in this collection view.   
[dragAndDropUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-dragAndDropUpdate.html) |  Called when a drag operation updates in this collection view.   
[handleDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-handleDrop.html) |  Called when a drag operation is released in this collection view.   
[itemIndexChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-itemIndexChanged.html) |  Called when an item is moved in the itemsSource.   
[itemsChosen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-itemsChosen.html) |  Callback triggered when the user acts on a selection of one or more items, for example by double-clicking or pressing Enter.   
[itemsSourceChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-itemsSourceChanged.html) |  Raised when the data source of a vertical collection view is assigned a new reference or new type.   
[onItemsChosen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-onItemsChosen.html) |  Obsolete. Use BaseVerticalCollectionView.itemsChosen instead.   
[onSelectedIndicesChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-onSelectedIndicesChange.html) |  Obsolete. Use BaseVerticalCollectionView.selectedIndicesChanged instead.   
[onSelectionChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-onSelectionChange.html) |  Obsolete. Use BaseVerticalCollectionView.selectionChanged instead.   
[selectedIndicesChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-selectedIndicesChanged.html) |  Callback triggered when the selection changes.   
[selectionChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-selectionChanged.html) |  Callback triggered when the selection changes.   
[setupDragAndDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-setupDragAndDrop.html) |  Called when a drag operation starts in this collection view.   
* * *
