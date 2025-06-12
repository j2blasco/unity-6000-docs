* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ListView.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Structure UI](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-structure-ui.html)
  * [Visual elements reference](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ElementRef.html)
  * ListView


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-LongField.html)
LongField
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-MaskField.html)
MaskField
# ListView
A ListView is a vertically scrollable area that links to and displays a list of items.
**Note** : The horizontal and vertical Scroller elements are standard UI Toolkit Scrollers.
## Create a ListView
You can create a ListView with UI Builder, UXML, and C#. The following C# example creates a ListView:
```
var listView = new ListView();

```

## ListView versus ScrollView
You can use a [ScrollView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ScrollView.html)A UI Control which displays a large set of Controls in a viewable area that you can see by using a scrollbar. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ScrollView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScrollView) control to create the same functionalities as using a ListView. However, a ListView is more efficient than a ScrollView when you do the following:
  * Populate list items
  * Manage item height
  * Bind and unbind to objects
  * Instantiate the number of **visual elements** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) required to fill a page
  * Recycle visual elements to optimize memory handling


## Refresh the collection view
To refresh the collection view, in general, call the [`RefreshItems`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.RefreshItems.html) or [`RefreshItem`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.RefreshItem.html) method. However, in the following cases, call [`Rebuild`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.Rebuild.html) instead to refresh the collection view:
  * You change the type of the [data source](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-itemsSource.html), such as changing from a `List<float>` to a `List<Vector3>`.
  * You make changes to `makeItem` or `destroyItem`.


**Note** : If you call `Rebuild`, the collection view is completely rebuilt, which can be expensive. If you call `RefreshItems` or `RefreshItem`, the collection view is only refreshed, which is less expensive.
## Set item height
To change how item height is used to drive content, use the [VirtualizationMethod](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-virtualizationMethod.html):
  * `VirtualizationMethod.FixedHeight` sets all items to the same height.
  * `VirtualizationMethod.DynamicHeight` allows items to have varying heights.


## Control the scroll speed
The ListView has a built-in child ScrollView element that lets users scroll through the list. You can [control the speed of the scroll](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ScrollView.html#control-the-scroll-speed) by [overriding the `mouseWheelScrollSize`, `horizontalPageSize`, and `verticalPageSize` properties of the ScrollView with C#](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Controls.html#access-properties-of-a-controls-read-only-children).
## Make a list reorderable
By default, the ListView control is not reorderable. To make it reorderable, set the `reorderable` property to `true` in UI Builder, UXML, or C#.
```
listView.reorderable = true;

```

## Implement drag-and-drop operations for ListView
Drag-and-drop is a common feature in UI design. To implement the drag-and-drop operations, override the following methods:
  * To enable dragging items, override [`canStartDrag`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-canStartDrag.html).
  * To set which items are dragged, override [`setupDragAndDrop`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-setupDragAndDrop.html).
  * To get item status changes, override [`dragAndDropUpdate`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-dragAndDropUpdate.html). You can perform certain actions based on the drag position or other conditions.
  * To control the drag-and-drop behavior, override [`handleDrop`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-handleDrop.html).


During the drag-and-drop operation, you can enable the reordering of items by dragging. To enable, set the `reorderable` attribute to `true` in UI Builder, UXML, and C#.
Refer to [Create a drag-and-drop list and tree views between windows](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-drag-and-drop-list-treeview-between-windows.html) for an example.
## ListView FAQs
The following are some frequently asked questions about the ListView control.
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
**Can I have a horizontal ListView?**
The ListView control doesn’t support horizontal layout and virtualization. It’s recommended to use a ScrollView with `flex-direction: row` to layout elements horizontally. However, applying this to a ListView breaks virtualization.
## Examples
The following UXML example creates a ListView:
```
<UXML xmlns="UnityEngine.UIElements">
    <ListView class="the-uxml-listview" fixed-item-height="20" />
</UXML>

```

The following C# example illustrates some of the customizable functionalities of the ListView:
```
/// <sample>
// Create some list of data, here simply numbers in interval [1, 1000]
const int itemCount = 1000;
var items = new List<string>(itemCount);
for (var i = 0; i < itemCount; i++)
    items.Add(i.ToString());

// The "makeItem" function will be called as needed
// when the ListView needs more items to render
Func<VisualElement> makeItem = () => new Label();

// As the user scrolls through the list, the ListView object
// will recycle elements created by the "makeItem"
// and invoke the "bindItem" callback to associate
// the element with the matching data item (specified as an index in the list)
Action<VisualElement, int> bindItem = (e, i) => ((Label)e).text = items[i];

var listView = container.Q<ListView>();
listView.makeItem = makeItem;
listView.bindItem = bindItem;
listView.itemsSource = items;
listView.selectionType = SelectionType.Multiple;

// Callback invoked when the user double clicks an item
listView.itemsChosen += (selectedItems) =>
{
    Debug.Log("Items chosen: " + string.Join(", ", selectedItems));
};

// Callback invoked when the user changes the selection inside the ListView
listView.selectedIndicesChanged += (selectedIndices) =>
{
    Debug.Log("Index selected: " + string.Join(", ", selectedIndices));

    // Note: selectedIndices can also be used to get the selected items from the itemsSource directly or
    // by using listView.viewController.GetItemForIndex(index).
};
/// </sample>

```

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**. ​ For more examples, refer to the following:
  * [Create list and tree views](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-ListView-TreeView.html): Use ListView, TreeView, MultiColumnListView, and MultiColumnTreeView to create list and tree views.
  * [Create a complex list view](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-list-view-complex.html): Use ListView to create a custom Editor window with a list of characters.
  * [Bind to a list with ListView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-bind-to-list.html): Create a list of toggles and bind the list to an underlying list of `GameSwitch` objects.
  * [Create a drag-and-drop list and tree views between windows](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-create-drag-and-drop-list-treeview-between-windows.html): Use ListView, TreeView, and MultiColumnListView to create a drag-and-drop UI between windows.


## C# base class and namespace
**C# class** : [`ListView`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ListView.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : [`BaseListView`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseListView.html)
## Member UXML attributes
This element has the following member attributes:
**Name** | **Type** | **Description**  
---|---|---  
`item-template` | [`UIElements.VisualTreeAsset`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualTreeAsset.html) | A UXML template that constructs each recycled and rebound element within the list. This template is designed to replace the `makeItem` definition.  
  
You can use it along with `BaseListView.bindingSourceSelectionMode` and bindings to have a completely codeless workflow.  
## Inherited UXML attributes
This element inherits the following attributes from its base class:
**Name** | **Type** | **Description**  
---|---|---  
`allow-add` | `boolean` | This property allows the user to allow or block the addition of an item when clicking on the Add Button. It must return `true` or `false`.  
  
If the callback is not set to `false`, any Add operation will be allowed.  
`allow-remove` | `boolean` | This property allows the user to allow or block the removal of an item when clicking on the Remove Button. It must return `true` or `false`.  
  
If the property is not set to `false`, any Remove operation will be allowed.  
`binding-path` | `string` | Path of the target property to be bound.  
`binding-source-selection-mode` | [`UIElements.BindingSourceSelectionMode`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingSourceSelectionMode.html) | This property controls whether every element in the list will get its data source setup automatically to the correct item in the collection’s source.  
  
When set to `AutoAssign`, the bind callbacks don’t need to be specified, since bindings can be used to fill the elements.  
`fixed-item-height` | `float` | The height of a single item in the list, in pixels.  
  
This property must be set when using the `virtualizationMethod` is set to `FixedHeight`, for the collection view to function. If set when `virtualizationMethod` is `DynamicHeight`, it serves as the default height to help calculate the number of items necessary and the scrollable area, before items are laid out. It should be set to the minimum expected height of an item.  
`focusable` | `boolean` | True if the element can be focused.  
`header-title` | `string` | This property controls the text of the foldout header when using `showFoldoutHeader`.  
  
If the `makeHeader` callback is set, this property gets overridden and the title is not shown.  
`reorder-mode` | [`UIElements.ListViewReorderMode`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ListViewReorderMode.html) | This property controls the drag and drop mode for the list view.  
  
The default value is `Simple`. When this property is set to `Animated`, Unity adds drag handles in front of every item and the drag and drop manipulation pushes items with an animation when the reordering happens. Multiple item reordering is only supported with the `Simple` drag mode.  
`reorderable` | `boolean` | Gets or sets a value that indicates whether the user can drag list items to reorder them.  
  
The default value is `false` which allows the user to drag items to and from other views when you implement `canStartDrag`, `setupDragAndDrop`, `dragAndDropUpdate`, and `handleDrop`. Set this value to `true` to allow the user to reorder items in the list.  
`selection-type` | [`UIElements.SelectionType`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SelectionType.html) | Controls the selection type.  
  
The default value is `SelectionType.Single`. When you set the collection view to disable selections, any current selection is cleared.  
`show-add-remove-footer` | `boolean` | This property controls whether a footer will be added to the list view.  
  
The default value is `false`. When this property is set to `true`, Unity adds a footer under the scroll view. This footer contains two buttons: A “+” button. When clicked, it adds a single item at the end of the list view. A “-” button. When clicked, it removes all selected items, or the last item if none are selected. If the `makeFooter` callback is set, it will override this property.  
`show-alternating-row-backgrounds` | [`UIElements.AlternatingRowBackground`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.AlternatingRowBackground.html) | This property controls whether the background colors of collection view rows alternate. Takes a value from the `AlternatingRowBackground` enum.  
`show-border` | `boolean` | Enable this property to display a border around the collection view.  
  
If set to true, a border appears around the ScrollView that the collection view uses internally.  
`show-bound-collection-size` | `boolean` | This property controls whether the list view displays the collection size (number of items).  
  
The default value is `true`. When this property is set to to `true`, the ListView includes a TextField to control the array size.  
  
SA: `UnityEditor.UIElements.BindingExtensions.Bind`  
`show-foldout-header` | `boolean` | This property controls whether the list view displays a header, in the form of a foldout that can be expanded or collapsed.  
  
The default value is `false`. When this property is set to `true`, Unity adds a foldout in the hierarchy of the list view and moves the scroll view inside that newly created foldout. You can change the text of this foldout with `headerTitle` property on the ListView. If `showBoundCollectionSize` is set to `true`, the ListView includes a TextField to control the array size. If the `makeHeader` callback is set, no Foldout is shown.  
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
`ussClassName` | `.unity-list-view` | The USS class name for ListView elements.  
  
Unity adds this USS class to every instance of the ListView element. Any styling applied to this class affects every ListView located beside, or below the stylesheet in the visual tree.  
`itemUssClassName` | `.unity-list-view__item` | The USS class name of item elements in ListView elements.  
  
Unity adds this USS class to every item element the ListView contains. Any styling applied to this class affects every item element located beside, or below the stylesheet in the visual tree.  
`emptyLabelUssClassName` | `.unity-list-view__empty-label` | The USS class name for label displayed when ListView is empty.  
  
Unity adds this USS class to the label displayed if the ListView is empty. Any styling applied to this class affects every empty label located beside, or below the stylesheet in the visual tree.  
`reorderableUssClassName` | `.unity-list-view__reorderable` | The USS class name for reorderable animated ListView elements.  
  
Unity adds this USS class to every instance of the ListView element when `reorderMode` is set to `Animated`. Any styling applied to this class affects every ListView located beside, or below the stylesheet in the visual tree.  
`reorderableItemUssClassName` | `.unity-list-view__reorderable-item` | The USS class name for item elements in reorderable animated ListView.  
  
Unity adds this USS class to every element in the ListView when `reorderMode` is set to `Animated`. Any styling applied to this class affects every element located beside, or below the stylesheet in the visual tree.  
`reorderableItemContainerUssClassName` | `.unity-list-view__reorderable-item__container` | The USS class name for item container in reorderable animated ListView.  
  
Unity adds this USS class to every item container in the ListView when `reorderMode` is set to `Animated`. Any styling applied to this class affects every item container located beside, or below the stylesheet in the visual tree.  
`reorderableItemHandleUssClassName` | `.unity-list-view__reorderable-handle` | The USS class name for drag handle in reorderable animated ListView.  
  
Unity adds this USS class to drag handles in the ListView when `reorderMode` is set to `Animated`. Any styling applied to this class affects every drag handle located beside, or below the stylesheet in the visual tree.  
`reorderableItemHandleBarUssClassName` | `.unity-list-view__reorderable-handle-bar` | The USS class name for drag handle bar in reorderable animated ListView.  
  
Unity adds this USS class to every drag handle bar in the ListView when `reorderMode` is set to `Animated`. Any styling applied to this class affects every drag handle bar located beside, or below the stylesheet in the visual tree.  
`footerUssClassName` | `.unity-list-view__footer` | The USS class name for the footer of the ListView.  
  
Unity adds this USS class to the footer element in the ListView. Any styling applied to this class affects every ListView located beside, or below the stylesheet in the visual tree.  
`foldoutHeaderUssClassName` | `.unity-list-view__foldout-header` | The USS class name for the foldout header of the ListView.  
  
Unity adds this USS class to the foldout element in the ListView. Any styling applied to this class affects every foldout located beside, or below the stylesheet in the visual tree.  
`arraySizeFieldUssClassName` | `.unity-list-view__size-field` | The USS class name for the size field of the ListView when show bound collection size is enabled  
  
Unity adds this USS class to the size field element in the ListView when `showBoundCollectionSize` is set to `true`. Any styling applied to this class affects every size field located beside, or below the stylesheet in the visual tree.  
`arraySizeFieldWithHeaderUssClassName` | `.unity-list-view__size-field--with-header` | The USS class name for the size field of the ListView when foldout header is enabled.  
  
Unity adds this USS class to the size field element in the ListView when `showBoundCollectionSize` is set to `true`. Any styling applied to this class affects every size field located beside, or below the stylesheet in the visual tree.  
`arraySizeFieldWithFooterUssClassName` | `.unity-list-view__size-field--with-footer` | The USS class name for the size field of the ListView when the footer is enabled.  
  
Unity adds this USS class to the size field element in the ListView when `showBoundCollectionSize` is set to `true`. Any styling applied to this class affects every size field located beside, or below the stylesheet in the visual tree.  
`listViewWithHeaderUssClassName` | `.unity-list-view--with-header` | The USS class name for ListView when foldout header is enabled.  
  
Unity adds this USS class to ListView when `showFoldoutHeader` is set to `true`. Any styling applied to this class affects every list located beside, or below the stylesheet in the visual tree.  
`listViewWithFooterUssClassName` | `.unity-list-view--with-footer` | The USS class name for ListView when add/remove footer is enabled.  
  
Unity adds this USS class to ListView when `showAddRemoveFooter` is set to `true`. Any styling applied to this class affects every list located beside, or below the stylesheet in the visual tree.  
`scrollViewWithFooterUssClassName` | `.unity-list-view__scroll-view--with-footer` | The USS class name for scroll view when add/remove footer is enabled.  
  
Unity adds this USS class scroll view of `BaseListView`when `showAddRemoveFooter` is set to `true`. Any styling applied to this class affects every list located beside, or below the stylesheet in the visual tree.  
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
  * [MultiColumnListView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-MultiColumnListView.html)
  * [MultiColumnTreeView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-MultiColumnTreeView.html)
  * [ScrollView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-ScrollView.html)
  * [TreeView](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-TreeView.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-LongField.html)
LongField
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-MaskField.html)
MaskField
