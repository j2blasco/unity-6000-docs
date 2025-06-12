* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TreeView.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * TreeView


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ToolbarToggle.html)
ToolbarToggle
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TwoPaneSplitView.html)
TwoPaneSplitView
# TreeView
Use TreeView to display hierarchical data in a tree-like structure. It’s a powerful and flexible control that’s commonly used to present data with parent-child relationships or nested structures.
If you need a simple list of items (not a hierarchical tree), consider using the [ListView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ListView.html) control.
## Create a TreeView
You can create a TreeView with UI Builder, UXML, and C#. The following C# example creates a TreeView:
```
var treeView = new TreeView();

```

## Refresh the collection view
To refresh the collection view, in general, call the [`RefreshItems`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.RefreshItems.html) or [`RefreshItem`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.RefreshItem.html) method. However, in the following cases, call [`Rebuild`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.Rebuild.html) instead to refresh the collection view:
  * You change the type of the [data source](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-itemsSource.html), such as changing from a `List<float>` to a `List<Vector3>`.
  * You make changes to `makeItem` or `destroyItem`.


**Note** : If you call `Rebuild`, the collection view is completely rebuilt, which can be expensive. If you call `RefreshItems` or `RefreshItem`, the collection view is only refreshed, which is less expensive.
## Bind the TreeView to data
You can bind the TreeView to a data source. The data source can be a list of objects or a list of strings. 
The following example binds a TreeView to a custom type.
```
treeView.makeItem = () => new VisualElement();

var item = new VisualElement();
treeView.bindItem = (item, i) =>
{
    var c = treeView.GetItemDataForIndex<MyCustomType>(i);
};

```

**Note** : In the previouse example, the [TreeView.bindItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TreeView-bindItem.html) receives the Index. You must use the Index (not the ID) with [`GetItemDataForIndex<T>`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.GetItemDataForIndex.html).
## Implement drag-and-drop operations for TreeView
Drag-and-drop is a common feature in UI design. To implement the drag-and-drop operations, override the following methods:
  * To enable dragging items, override [`canStartDrag`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-canStartDrag.html).
  * To set which items are dragged, override [`setupDragAndDrop`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-setupDragAndDrop.html).
  * To get item status changes, override [`dragAndDropUpdate`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-dragAndDropUpdate.html). You can perform certain actions based on the drag position or other conditions.
  * To control the drag-and-drop behavior, override [`handleDrop`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-handleDrop.html).


During the drag-and-drop operation, you can enable the reordering of items by dragging. To enable, set the `reorderable` attribute to `true` in UI Builder, UXML, and C#.
Refer to [Create a drag-and-drop list and tree views between windows](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-drag-and-drop-list-treeview-between-windows.html) for an example.
## Set up the hierarchy of the TreeView
To set up the hierarchy of the TreeView, declare `TreeViewItemData<T>` where `T` is the type of data for the tree, then set the source through the `SetRootItems` API. For example, assume you have the following UXML structure:
```
<UXML xmlns="UnityEngine.UIElements">
    <TreeView class="the-uxml-treeview" fixed-item-height="20" />
</UXML>

```

You can set up the hierarchy of the TreeView as follows:
```
/// <sample>
// Create some list of data, here simply numbers in a few foldouts
var items = new List<TreeViewItemData<string>>(10);
for (var i = 0; i < 10; i++)
{
    var itemIndex = i * 10 + i;

    var treeViewSubItemsData = new List<TreeViewItemData<string>>(10);
    for (var j = 0; j < 10; j++)
        treeViewSubItemsData.Add(new TreeViewItemData<string>(itemIndex + j + 1, $"Data {i+1}-{j+1}"));

    var treeViewItemData = new TreeViewItemData<string>(itemIndex, $"Data {i+1}", treeViewSubItemsData);
    items.Add(treeViewItemData);
};

// The "makeItem" function will be called as needed
// when the TreeView needs more items to render
Func<VisualElement> makeItem = () => new Label();

// As the user scrolls through the list, the TreeView object
// will recycle elements created by the "makeItem"
// and invoke the "bindItem" callback to associate
// the element with the matching data item (specified as an index in the list)
Action<VisualElement, int> bindItem = (e, i) =>
{
    var item = treeView.GetItemDataForIndex<string>(i);
    var id = treeView.GetIdForIndex(i);
    ((Label)e).text = $"ID {id} - {item}";
};

treeView.SetRootItems(items);
treeView.makeItem = makeItem;
treeView.bindItem = bindItem;
treeView.selectionType = SelectionType.Multiple;
treeView.Rebuild();

// Callback invoked when the user double clicks an item
treeView.itemsChosen += (selectedItems) =>
{
    Debug.Log("Items chosen: " + string.Join(", ", selectedItems));
};

// Callback invoked when the user changes the selection inside the TreeView
treeView.selectedIndicesChanged += (selectedIndices) =>
{
    var log = "IDs selected: ";
    foreach (var index in selectedIndices)
    {
        log += $"{treeView.GetIdForIndex(index)}, ";
    }
    Debug.Log(log.TrimEnd(',', ' '));
};
/// </sample>

```

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.
## TreeView FAQs
The following are some frequently asked questions about the TreeView control:
**Can I get the indices of the rows that are visible on the screen?**
There are no dedicated APIs for this. You can use the `bindItem` and `unbindItem` callbacks to track these indices.
**Can I get the list of rows that are visible in the view?**
There are no dedicated APIs for this. You can use [UQuery](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UQuery.html) to retrieve the elements of interest.
**Is it mandatory for any of the overridden functions of a view controller to call`base.Method`?**
Call this method only if you want to extend its default behavior.
**I’ve added a Toggle to my row. Why doesn’t the selection jump to that row when the user selects it?**
By default, the row is selected only if the mouse down event is not consumed by the row’s contents. In this case, your Toggle stops the event propagation. To fix this, register a [`PointerDownEvent`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerDownEvent.html) callback with [`TrickleDown`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TrickleDown.html) on the Toggle to call [`SetSelection`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.SetSelection.html).
**How do I receive a callback when a user changes their selection in the view?**
It is recommended to use the [`selectedIndicesChanged`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-selectedIndicesChanged.html) callback to retrieve data by index when needed. While you can also use [`selectionChanged`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-selectionChanged.html), be aware that it returns a list of objects, which can cause boxing allocations when used with value types.
**How do I convert from ID to index and vice versa?**
Use [`BaseTreeViewController.GetIndexForId`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.GetIndexForId.html) and [`BaseTreeViewController.GetIdForIndex`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.GetIdForIndex.html).
**Can I have a horizontal TreeView?**
The TreeView control doesn’t support horizontal layout and virtualization. It’s recommended to use a ScrollView with `flex-direction: row` to layout elements horizontally.
## Examples
  * [Create list and tree views](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ListView-TreeView.html): Use ListView, TreeView, MultiColumnListView, and MultiColumnTreeView to create list and tree views.
  * [Create a drag-and-drop list and tree views between windows](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-drag-and-drop-list-treeview-between-windows.html): Use ListView, TreeView, and MultiColumnListView to create a drag-and-drop UI between windows.


## C# base class and namespace
**C# class** : [`TreeView`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TreeView.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : [`BaseTreeView`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.html)
## Member UXML attributes
This element has the following member attributes:
**Name** | **Type** | **Description**  
---|---|---  
`item-template` | [`UIElements.VisualTreeAsset`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualTreeAsset.html) | A UXML template that constructs each recycled and rebound element within the tree. This template is designed to replace the `makeItem` definition.  
## Inherited UXML attributes
This element inherits the following attributes from its base class:
**Name** | **Type** | **Description**  
---|---|---  
`auto-expand` | `boolean` | When true, items are automatically expanded when added to the TreeView.  
`binding-path` | `string` | Path of the target property to be bound.  
`fixed-item-height` | `float` | The height of a single item in the list, in pixels.  
  
This property must be set when using the `virtualizationMethod` is set to `FixedHeight`, for the collection view to function. If set when `virtualizationMethod` is `DynamicHeight`, it serves as the default height to help calculate the number of items necessary and the scrollable area, before items are laid out. It should be set to the minimum expected height of an item.  
`focusable` | `boolean` | True if the element can be focused.  
`reorderable` | `boolean` | Gets or sets a value that indicates whether the user can drag list items to reorder them.  
  
The default value is `false` which allows the user to drag items to and from other views when you implement `canStartDrag`, `setupDragAndDrop`, `dragAndDropUpdate`, and `handleDrop`. Set this value to `true` to allow the user to reorder items in the list.  
`selection-type` | [`UIElements.SelectionType`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SelectionType.html) | Controls the selection type.  
  
The default value is `SelectionType.Single`. When you set the collection view to disable selections, any current selection is cleared.  
`show-alternating-row-backgrounds` | [`UIElements.AlternatingRowBackground`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.AlternatingRowBackground.html) | This property controls whether the background colors of collection view rows alternate. Takes a value from the `AlternatingRowBackground` enum.  
`show-border` | `boolean` | Enable this property to display a border around the collection view.  
  
If set to true, a border appears around the ScrollView that the collection view uses internally.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`virtualization-method` | [`UIElements.CollectionVirtualizationMethod`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionVirtualizationMethod.html) | The virtualization method to use for this collection when a scroll bar is visible. Takes a value from the `CollectionVirtualizationMethod` enum.  
  
The default value is `FixedHeight`. When using fixed height, specify the `fixedItemHeight` property. Fixed height is more performant but offers less flexibility on content. When using `DynamicHeight`, the collection will wait for the actual height to be computed. Dynamic height is more flexible but less performant.  
This element also inherits the following attributes from [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-VisualElement.html):
**Name** | **Type** | **Description**  
---|---|---  
`content-container` | `string` | Child elements are added to it, usually this is the same as the element itself.  
`data-source` | `Object` | Assigns a data source to this VisualElement which overrides any inherited data source. This data source is inherited by all children.  
`data-source-path` | `string` | Path from the data source to the value.  
`data-source-type` | `System.Type` | The possible type of data source assignable to this VisualElement.  
  
This information is only used by the UI Builder as a hint to provide some completion to the data source path field when the effective data source cannot be specified at design time.  
`language-direction` | [`UIElements.LanguageDirection`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LanguageDirection.html) | Indicates the directionality of the element’s text. The value will propagate to the element’s children.  
  
Setting the languageDirection to RTL adds basic support for right-to-left (RTL) by reversing the text and handling linebreaking and word wrapping appropriately. However, it does not provide comprehensive RTL support, as this would require text shaping, which includes the reordering of characters, and OpenType font feature support. Comprehensive RTL support is planned for future updates, which will involve additional APIs to handle language, script, and font feature specifications.  
  
To enhance the RTL functionality of this property, users can explore available third-party plugins in the Unity Asset Store and make use of `ITextElementExperimentalFeatures.renderedText`  
`name` | `string` | The name of this VisualElement.  
  
Use this property to write USS selectors that target a specific element. The standard practice is to give an element a unique name.  
`picking-mode` | [`UIElements.PickingMode`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PickingMode.html) | Determines if this element can be pick during mouseEvents or `IPanel.Pick` queries.  
`style` | `string` | Sets the `VisualElement` style values.  
`tooltip` | `string` | Text to display inside an information box after the user hovers the element for a small amount of time. This is only supported in the Editor UI.  
`usage-hints` | [`UIElements.UsageHints`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.html) | A combination of hint values that specify high-level intended usage patterns for the `VisualElement`. This property can only be set when the `VisualElement` is not yet part of a `Panel`. Once part of a `Panel`, this property becomes effectively read-only, and attempts to change it will throw an exception. The specification of proper `UsageHints` drives the system to make better decisions on how to process or accelerate certain operations based on the anticipated usage pattern. Note that those hints do not affect behavioral or visual results, but only affect the overall performance of the panel and the elements within. It’s advised to always consider specifying the proper `UsageHints`, but keep in mind that some `UsageHints` might be internally ignored under certain conditions (e.g. due to hardware limitations on the target platform).  
`view-data-key` | `string` | Used for view data persistence, such as tree expanded states, scroll position, or zoom level.  
  
This key is used to save and load the view data from the view data store. If you don’t set this key, the persistence is disabled for the associated `VisualElement`. For more information, refer to [View data persistence](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ViewData.html).  
## USS classes
The following table lists all the C# public property names and their related USS selector.
**C# property** | **USS selector** | **Description**  
---|---|---  
`ussClassName` | `.unity-tree-view` | The USS class name for TreeView elements.  
  
Unity adds this USS class to every instance of the TreeView element. Any styling applied to this class affects every TreeView located beside, or below the stylesheet in the visual tree.  
`itemUssClassName` | `.unity-tree-view__item` | The USS class name for TreeView item elements.  
  
Unity adds this USS class to every item element of the TreeView. Any styling applied to this class affects every item located beside, or below the stylesheet in the visual tree.  
`itemToggleUssClassName` | `.unity-tree-view__item-toggle` | The USS class name for TreeView item toggle elements.  
  
Unity adds this USS class to every item toggle element of the TreeView. Any styling applied to this class affects every item located beside, or below the stylesheet in the visual tree.  
`itemIndentsContainerUssClassName` | `.unity-tree-view__item-indents` | The USS class name for TreeView indent container elements.  
  
Unity adds this USS class to every indent container element of the TreeView. Any styling applied to this class affects every item located beside, or below the stylesheet in the visual tree.  
`itemIndentUssClassName` | `.unity-tree-view__item-indent` | The USS class name for TreeView indent element.  
  
Unity adds this USS class to every indent element of the TreeView. Any styling applied to this class affects every item located beside, or below the stylesheet in the visual tree.  
`itemContentContainerUssClassName` | `.unity-tree-view__item-content` | The USS class name for TreeView item container elements.  
  
Unity adds this USS class to every item container element of the TreeView. Any styling applied to this class affects every item located beside, or below the stylesheet in the visual tree.  
`ussClassName` | `.unity-collection-view` | The USS class name for BaseVerticalCollectionView elements.  
  
Unity adds this USS class to every instance of the BaseVerticalCollectionView element. Any styling applied to this class affects every BaseVerticalCollectionView located beside, or below the stylesheet in the visual tree.  
`borderUssClassName` | `.unity-collection-view--with-border` | The USS class name for BaseVerticalCollectionView elements with a border.  
  
Unity adds this USS class to an instance of the BaseVerticalCollectionView element if the instance’s `BaseVerticalCollectionView.showBorder` property is set to true. Any styling applied to this class affects every such BaseVerticalCollectionView located beside, or below the stylesheet in the visual tree.  
`itemUssClassName` | `.unity-collection-view__item` | The USS class name of item elements in BaseVerticalCollectionView elements.  
  
Unity adds this USS class to every item element the BaseVerticalCollectionView contains. Any styling applied to this class affects every item element located beside, or below the stylesheet in the visual tree.  
`dragHoverBarUssClassName` | `.unity-collection-view__drag-hover-bar` | The USS class name of the drag hover bar.  
  
Unity adds this USS class to the bar that appears when the user drags an item in the list. Any styling applied to this class affects every BaseVerticalCollectionView located beside, or below the stylesheet in the visual tree.  
`dragHoverMarkerUssClassName` | `.unity-collection-view__drag-hover-marker` | The USS class name of the drag hover circular marker used to indicate depth.  
  
Unity adds this USS class to the bar that appears when the user drags an item in the list. Any styling applied to this class affects every BaseVerticalCollectionView located beside, or below the stylesheet in the visual tree.  
`itemDragHoverUssClassName` | `.unity-collection-view__item--drag-hover` | The USS class name applied to an item element on drag hover.  
  
Unity adds this USS class to the item element when it’s being dragged. Any styling applied to this class affects every BaseVerticalCollectionView item located beside, or below the stylesheet in the visual tree.  
`itemSelectedVariantUssClassName` | `.unity-collection-view__item--selected` | The USS class name of selected item elements in the BaseVerticalCollectionView.  
  
Unity adds this USS class to every selected element in the BaseVerticalCollectionView. The `BaseVerticalCollectionView.selectionType` property decides if zero, one, or more elements can be selected. Any styling applied to this class affects every BaseVerticalCollectionView item located beside, or below the stylesheet in the visual tree.  
`itemAlternativeBackgroundUssClassName` | `.unity-collection-view__item--alternative-background` | The USS class name for odd rows in the BaseVerticalCollectionView.  
  
Unity adds this USS class to every odd-numbered item in the BaseVerticalCollectionView when the `BaseVerticalCollectionView.showAlternatingRowBackgrounds` property is set to `ContentOnly` or `All`. When the `showAlternatingRowBackgrounds` property is set to either of those values, odd-numbered items are displayed with a different background color than even-numbered items. This USS class is used to differentiate odd-numbered items from even-numbered items. When the `showAlternatingRowBackgrounds` property is set to `None`, the USS class is not added, and any styling or behavior that relies on it’s invalidated.  
`listScrollViewUssClassName` | `.unity-collection-view__scroll-view` | The USS class name of the scroll view in the BaseVerticalCollectionView.  
  
Unity adds this USS class to the BaseVerticalCollectionView’s scroll view. Any styling applied to this class affects every BaseVerticalCollectionView scroll view located beside, or below the stylesheet in the visual tree.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
You can also use the [Matching Selectors section in the Inspector or the UI Toolkit Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/UIB-testing-ui.html#matching-selectors) to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.
## Additional resources
  * [MultiColumnTreeView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-MultiColumnTreeView.html)
  * [MultiColumnListView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-MultiColumnListView.html)
  * [ScrollView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ScrollView.html)A UI Control which displays a large set of Controls in a viewable area that you can see by using a scrollbar. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ScrollView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScrollView)
  * [ListView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ListView.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ToolbarToggle.html)
ToolbarToggle
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TwoPaneSplitView.html)
TwoPaneSplitView
