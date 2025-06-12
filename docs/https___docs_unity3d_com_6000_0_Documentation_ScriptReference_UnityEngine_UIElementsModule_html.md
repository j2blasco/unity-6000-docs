* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UIElementsModule.html

# UnityEngine.UIElementsModule
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
The UIElements module implements the UIElements retained mode UI framework.
### Classes
Class | Description  
---|---  
[AbstractProgressBar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.AbstractProgressBar.html) |  Abstract base class for the ProgressBar.   
[AlignmentUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.AlignmentUtils.html) |  Static class containing utility methods for aligning visual elements.   
[AttachToPanelEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.AttachToPanelEvent.html) |  Event sent after an element is added to an element that is a descendant of a panel.   
[BackgroundPropertyHelper](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BackgroundPropertyHelper.html) |  Helper to convert between background properties and ScaleMode.   
[BaseBoolField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseBoolField.html) |  A BaseBoolField is a clickable element that represents a boolean value.   
[BaseCompositeField<T0,T1,T2>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseCompositeField_3.html) |  This is the base class for the composite fields.   
[BaseField<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.html) |  Abstract base class for controls.A BaseField is a base class for field elements like TextField and IntegerField. To align a BaseField element automatically with other fields in an Inspector window, use the .unity-base-field__aligned USS class. This style class is designed for use with Inspector elements like PropertyField, which has the style class by default. However, if you manually add a child BaseField element to a PropertyField, you must add the style class manually.When the style class is present, the field automatically calculates the label width to align with other fields in the Inspector window. If there are IMGUI fields present, UI Toolkit fields are aligned with them for consistency and compatibility.  
[BaseFieldMouseDragger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseFieldMouseDragger.html) |  Provides the base class for field mouse draggers.   
[BaseListView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseListView.html) |  Base class for a list view, a vertically scrollable area that links to, and displays, a list of items.   
[BaseListViewController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseListViewController.html) |  Base collection list view controller. View controllers of this type are meant to take care of data virtualized by any BaseListView inheritor.   
[BasePopupField<T0,T1>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BasePopupField_2.html) |  This is the base class for all the popup field elements. TValue and TChoice can be different, see MaskField, or the same, see PopupField   
[BaseSlider<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseSlider_1.html) |  This is a base class for the Slider fields.   
[BaseTreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.html) |  Base class for a tree view, a vertically scrollable area that links to, and displays, a list of items organized in a tree.   
[BaseTreeViewController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.html) |  Base collection tree view controller. View controllers of this type are meant to take care of data virtualized by any BaseTreeView inheritor.   
[BaseVerticalCollectionView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView.html) |  Base class for controls that display virtualized vertical content inside a scroll view.   
[BindableElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindableElement.html) |  Element that can be bound to a property. For more information, refer to UXML element BindableElement.   
[Binding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Binding.html) |  Base class for defining a binding.   
[BlurEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BlurEvent.html) |  Event sent immediately after an element has lost focus. This event trickles down and does not bubbles up.   
[BoundsField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BoundsField.html) |  A Bounds editor field. For more information, refer to UXML element BoundsField.   
[BoundsIntField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BoundsIntField.html) |  A BoundsInt field. For more information, refer to UXML element BoundsIntField.   
[Box](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Box.html) |  Styled visual element to match the IMGUI Box Style. For more information, refer to UXML element Box.   
[Button](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) |  This is a clickable button.   
[CallbackEventHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.html) |  Interface for classes capable of having callbacks to handle events.   
[ChangeEvent<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ChangeEvent_1.html) |  Sends an event when a value in a field changes.   
[Clickable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable.html) |  Manipulator that tracks Mouse events on an element and callbacks when the elements is clicked.   
[ClickEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ClickEvent.html) |  This event is sent when the left mouse button is clicked.   
[CollectionViewController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionViewController.html) |  Base collection view controller. View controllers are meant to take care of data virtualized by any BaseVerticalCollectionView inheritor.   
[Column](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Column.html) |  Represents a column in multi-column views such as multi-column list view or multi-column tree view. Provides the properties to define how user interacts with a column in a multi-column view, how its data and the data of each cell in this column are represented.   
[Columns](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Columns.html) |  Represents a collection of columns.   
[CommandEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CommandEventBase_1.html) |  Base class for command events.   
[ContextClickEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ContextClickEvent.html) |  The event sent when clicking the right mouse button.   
[ContextualMenuManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ContextualMenuManager.html) |  Use this class to display a contextual menu.   
[ContextualMenuManipulator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ContextualMenuManipulator.html) |  Manipulator that displays a contextual menu when the user clicks the right mouse button or presses the menu key on the keyboard.   
[ContextualMenuPopulateEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ContextualMenuPopulateEvent.html) |  The event sent when a contextual menu requires menu items. The event trickles down and bubbles up.   
[ConverterGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroup.html) |  A type to hold information about a conversion registry used locally on bindings.   
[ConverterGroups](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroups.html) |  Provides a set of static methods to register and use converter groups and registers a set of global converters. ConverterGroup. DataBinding.   
[CustomBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CustomBinding.html) |  Base class for general purpose binding extensibility.   
[CustomStyleResolvedEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CustomStyleResolvedEvent.html) |  Event sent after the custom style properties of a VisualElement have been resolved.   
[DataBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding.html) |  Binding type that enables data synchronization between a property of a data source and a property of a VisualElement.   
[DefaultMultiColumnTreeViewController<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DefaultMultiColumnTreeViewController_1.html) |  Default implementation of a MultiColumnTreeViewController.   
[DefaultTreeViewController<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DefaultTreeViewController_1.html) |  Default implementation of a TreeViewController.   
[DetachFromPanelEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DetachFromPanelEvent.html) |  Event sent just before an element is detached from its parent, if the parent is the descendant of a panel.   
[DoubleField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DoubleField.html) |  Makes a text field for entering doubles.   
[DragAndDropData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragAndDropData.html) |  Data stored during drag-and-drop operations, enabling information to be carried throughout the process.   
[DragAndDropEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragAndDropEventBase_1.html) |  Base class for drag and drop events.   
[DragEnterEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragEnterEvent.html) |  Use the DragEnterEvent class to manage events that occur when dragging enters an element or one of its descendants. The DragEnterEvent does not trickle down and does not bubble up.   
[DragExitedEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragExitedEvent.html) |  The event sent to a dragged element when the drag and drop process ends.   
[DragLeaveEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragLeaveEvent.html) |  Use the DragLeaveEvent class to manage events sent when dragging leaves an element or one of its descendants. The DragLeaveEvent does not trickle down and does not bubble up.   
[DragPerformEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragPerformEvent.html) |  The event sent to an element when another element is dragged and dropped on the element.   
[DragUpdatedEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragUpdatedEvent.html) |  The event sent when the element being dragged enters a possible drop target.   
[DropdownField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownField.html) |  A control that allows the user to pick a choice from a list of options. For more information, refer to UXML element DropdownField.   
[DropdownMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenu.html) |  Represents a dropdown menu.   
[DropdownMenuAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuAction.html) |  Represents a menu action item.   
[DropdownMenuEventInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuEventInfo.html) |  Provides information about the event that caused the dropdown menu to display.   
[DropdownMenuItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuItem.html) |  Represents an item in a dropdown menu.   
[DropdownMenuSeparator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownMenuSeparator.html) |  Provides a separator menu item.   
[DynamicAtlasSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasSettings.html) |  Contains the settings used by the dynamic atlas system.   
[Easing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Experimental.Easing.html) |  A collection of easing curves to be used with ValueAnimations.   
[EnumField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EnumField.html) |  Makes a dropdown for switching between enum values. For more information, refer to UXML element EnumField.   
[EventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase.html) |  The base class for all UIElements events. The class implements IDisposable to ensure proper release of the event from the pool and of any unmanaged resources, when necessary.   
[EventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase_1.html) |  Generic base class for events, implementing event pooling and automatic registration to the event type system.   
[EventDispatcher](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventDispatcher.html) |  Dispatches events to a IPanel.   
[EventInterestAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventInterestAttribute.html) |  Optional attribute on overrides of CallbackEventHandler.HandleEventBubbleUp and CallbackEventHandler.HandleEventTrickleDown. Use this attribute to specify all the event types used by the method override. The event dispatcher can then safely skip events not needed for this method if they are identified internally as valid candidates for performance optimizations.   
[ExecuteCommandEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ExecuteCommandEvent.html) |  This event is sent by the Editor when an element in the panel should execute a command.   
[FieldMouseDragger<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FieldMouseDragger_1.html) |  Provides dragging on a visual element to change a value field.   
[FloatField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FloatField.html) |  Makes a text field for entering a float. For more information, refer to UXML element FloatField.   
[Focusable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable.html) |  Base class for objects that can get the focus.   
[FocusChangeDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FocusChangeDirection.html) |  Base class for defining in which direction the focus moves in a focus ring.   
[FocusController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FocusController.html) |  Class in charge of managing the focus inside a Panel.   
[FocusEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FocusEvent.html) |  Event sent immediately after an element has gained focus. This event trickles down and does not bubbles up.   
[FocusEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FocusEventBase_1.html) |  Base class for focus related events.   
[FocusInEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FocusInEvent.html) |  Event sent immediately before an element gains focus. This event trickles down and bubbles up.   
[FocusOutEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FocusOutEvent.html) |  Event sent immediately before an element loses focus. This event trickles down and bubbles up.   
[Foldout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Foldout.html) |  A Foldout control is a collapsible section of a user interface. When toggled, it expands or collapses, which hides or reveals the elements it contains.   
[GenericDropdownMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GenericDropdownMenu.html) |  GenericDropdownMenu allows you to display contextual menus with default textual options or any VisualElement.   
[GeometryChangedEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GeometryChangedEvent.html) |  This event is sent after layout calculations, when the position or the dimension of an element changes.   
[GroupBox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GroupBox.html) |  This is an enclosing container for a group of IGroupBoxOption. All group options within this container will interact together to allow a single selection, using the DefaultGroupManager. Default options are RadioButton, but users can provide other implementations. If no IGroupBox is found in the hierarchy, the default container will be the panel.   
[Hash128Field](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Hash128Field.html) |  Makes a field for editing an Hash128. For more information, refer to UXML element Hash128Field.   
[HelpBox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.HelpBox.html) |  Makes a help box with a message to the user. For more information, refer to UXML element HelpBox.   
[IBindingExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IBindingExtensions.html) |  Extensions methods to provide additional IBindable functionality.   
[Image](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Image.html) |  A VisualElement representing a source texture.   
[IMGUIContainer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMGUIContainer.html) |  Element that draws IMGUI content. For more information, refer to UXML element IMGUIContainer.   
[IMGUIEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMGUIEvent.html) |  Class used to send a IMGUI event that has no equivalent UIElements event.   
[ImmediateModeElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ImmediateModeElement.html) |  VisualElement that can implement custom immediate mode rendering.   
[INotifyValueChangedExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.INotifyValueChangedExtensions.html) |  INotifyValueChangedExtensions is a set of extension methods useful for objects implementing INotifyValueChanged_1.   
[InputEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InputEvent.html) |  Sends an event when text from a TextField changes.   
[IntegerField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IntegerField.html) |  Makes a text field for entering an integer. For more information, refer to UXML element LongField.   
[KeyboardEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.KeyboardEventBase_1.html) |  This is the base class for keyboard events.   
[KeyboardNavigationManipulator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.KeyboardNavigationManipulator.html) |  Provides a default implementation for translating input device specific events to higher level navigation operations as commonly possible with a keyboard.   
[KeyDownEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.KeyDownEvent.html) |  This event is sent when a key is pressed.   
[KeyUpEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.KeyUpEvent.html) |  This event is sent when a pressed key is released.   
[Label](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) |  Provides an Element displaying text. For more information, refer to UXML element Label.   
[ListView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ListView.html) |  A ListView is a vertically scrollable area that links to, and displays, a list of items.   
[ListViewController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ListViewController.html) |  List view controller. View controllers of this type are meant to take care of data virtualized by any ListView inheritor.   
[LongField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LongField.html) |  Makes a text field for entering long integers. For more information, refer to UXML element LongField.   
[Manipulator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Manipulator.html) |  Base class for all Manipulator implementations. For more information, refer to Manipulators in User Manual.   
[MeshGenerationContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshGenerationContext.html) |  Provides methods for generating a visual element's visual content during the VisualElement.generateVisualContent callback.   
[MeshWriteData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshWriteData.html) |  Represents the vertex and index data allocated for drawing the content of a VisualElement.   
[MinMaxSlider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MinMaxSlider.html) |  A min/max slider containing a representation of a range. For more information, refer to UXML element MinMaxSlider.   
[MouseCaptureController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseCaptureController.html) |  Class that manages capturing mouse events.   
[MouseCaptureEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseCaptureEvent.html) |  Event sent after a handler starts capturing the mouse.   
[MouseCaptureEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseCaptureEventBase_1.html) |  Event sent when the handler capturing the mouse changes.   
[MouseCaptureOutEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseCaptureOutEvent.html) |  Event sent before a handler stops capturing the mouse.   
[MouseDownEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseDownEvent.html) |  This event is sent when a mouse button is pressed.   
[MouseEnterEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseEnterEvent.html) |  Event sent when the mouse pointer enters an element or one of its descendent elements. The event trickles down but does not bubble up.   
[MouseEnterWindowEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseEnterWindowEvent.html) |  Event sent when the mouse pointer enters a window. The event bubbles up but does not trickle down.   
[MouseEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseEventBase_1.html) |  The base class for mouse events.   
[MouseLeaveEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseLeaveEvent.html) |  Event sent when the mouse pointer exits an element and all its descendent elements. The event trickles down but does not bubble up.   
[MouseLeaveWindowEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseLeaveWindowEvent.html) |  Event sent when the mouse pointer exits a window. The event bubbles up but does not trickle down.   
[MouseManipulator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseManipulator.html) |  MouseManipulators have a list of activation filters.   
[MouseMoveEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseMoveEvent.html) |  This event is sent when the mouse moves.   
[MouseOutEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseOutEvent.html) |  Event sent when the mouse pointer exits an element. The event trickles down and bubbles up.   
[MouseOverEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseOverEvent.html) |  Event sent when the mouse pointer enters an element. The event trickles down and bubbles up.   
[MouseUpEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseUpEvent.html) |  This event is sent when a mouse button is released.   
[MultiColumnController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnController.html) |  The default controller for a multi column view. Takes care of adding the MultiColumnCollectionHeader and reacting to the various callbacks.   
[MultiColumnListView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnListView.html) |  A list view with multi column support. For more information, refer to MultiColumnListView.   
[MultiColumnListViewController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnListViewController.html) |  Multi-column list view controller. View controllers of this type are meant to take care of data virtualized by any MultiColumnListView inheritor.   
[MultiColumnTreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnTreeView.html) |  A tree view with multi column support. For more information, refer to MultiColumnTreeView.   
[MultiColumnTreeViewController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MultiColumnTreeViewController.html) |  Multi-column tree view controller. View controllers of this type are meant to take care of data virtualized by any MultiColumnTreeView inheritor.   
[NavigationCancelEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationCancelEvent.html) |  Event sent when the user presses the cancel button.   
[NavigationEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationEventBase_1.html) |  Navigation events abstract base class. By default, navigation events trickle down and bubble up. Disabled elements won't receive these events.   
[NavigationMoveEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationMoveEvent.html) |  Event typically sent when the user presses the D-pad, moves a joystick or presses the arrow keys.   
[NavigationSubmitEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationSubmitEvent.html) |  Event sent when the user presses the submit button.   
[Painter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Painter2D.html) |  Object to draw 2D vector graphics.   
[PanelChangedEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PanelChangedEventBase_1.html) |  Abstract base class for events notifying of a panel change.   
[PanelSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PanelSettings.html) |  Defines a Panel Settings asset that instantiates a panel at runtime. The panel makes it possible for Unity to display UXML-file based UI in the Game view.   
[PanelTextSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PanelTextSettings.html) |  Represents text rendering settings for a specific UI panel. PanelSettings.textSettings  
[PointerCancelEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerCancelEvent.html) |  This event is sent when pointer interaction is cancelled.   
[PointerCaptureEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerCaptureEvent.html) |  Event sent when a pointer is captured by a VisualElement.   
[PointerCaptureEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerCaptureEventBase_1.html) |  Base class for pointer capture events and mouse capture events.   
[PointerCaptureHelper](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerCaptureHelper.html) |  A static class to capture and release pointers.   
[PointerCaptureOutEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerCaptureOutEvent.html) |  Event sent when a VisualElement releases a pointer.   
[PointerDownEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerDownEvent.html) |  Sends when a pointer is pressed inside a visual element.   
[PointerDownLinkTagEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Experimental.PointerDownLinkTagEvent.html) |  This event is sent when a pointer is pressed on a Link tag.   
[PointerEnterEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEnterEvent.html) |  This event is sent when a pointer enters a VisualElement or one of its descendants. The event does not trickle down and does not bubble up.   
[PointerEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1.html) |  Base class for all pointer-related events.   
[PointerId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerId.html) |  A static class that holds pointer ID values.   
[PointerLeaveEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerLeaveEvent.html) |  This event is sent when a pointer exits an element and all of its descendants. The event does not trickle down and does not bubble up.   
[PointerManipulator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerManipulator.html) |  PointerManipulators have a list of activation filters.   
[PointerMoveEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerMoveEvent.html) |  This event is sent when a pointer changes state.   
[PointerMoveLinkTagEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Experimental.PointerMoveLinkTagEvent.html) |  This event is sent when a pointer changes state on a link tag.   
[PointerOutEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerOutEvent.html) |  This event is sent when a pointer exits an element. The event trickles down and bubbles up.   
[PointerOutLinkTagEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Experimental.PointerOutLinkTagEvent.html) |  This event is sent when a pointer exits a link tag.   
[PointerOverEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerOverEvent.html) |  This event is sent when a pointer enters an element. The event trickles down and bubbles up.   
[PointerOverLinkTagEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Experimental.PointerOverLinkTagEvent.html) |  This event is sent when a pointer enters a link tag.   
[PointerType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerType.html) |  A static class that holds pointer type values.   
[PointerUpEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerUpEvent.html) |  This event is sent when a pointer's last pressed button is released.   
[PointerUpLinkTagEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Experimental.PointerUpLinkTagEvent.html) |  This event is sent when a pointer's last pressed button is released on a link tag.   
[PopupField<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PopupField_1.html) |  Generic popup selection field.   
[PopupWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PopupWindow.html) |  Styled visual text element. This element doesn't have any functionality. It's just a container with a border and a title, rather than a window or popup. For more information, refer to UXML element PopupWindow.   
[ProgressBar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ProgressBar.html) |  A control that displays the progress between a lower and upper bound value. For more information, refer to UXML element ProgressBar.   
[RadioButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RadioButton.html) |  A control that allows users to select a single option inside a RadioButtonGroup. For more information, refer to UXML element RadioButton.   
[RadioButtonGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RadioButtonGroup.html) |  A control that allows single selection out of a logical group of RadioButton elements. Selecting one will deselect the others. For more information, refer to UXML element RadioButtonGroup.   
[RectField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RectField.html) |  A Rect field. For more information, refer to UXML element RectField.   
[RectIntField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RectIntField.html) |  A RectInt field. For more information, refer to UXML element RectIntField.   
[RegisterUxmlCacheAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RegisterUxmlCacheAttribute.html) |  Attribute allowing the UXML registry to more efficiently retrieve the UXML description data.   
[RepeatButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RepeatButton.html) |  A button that executes an action repeatedly while it is pressed. For more information, refer to UXML element RepeatButton.   
[RuntimePanelUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RuntimePanelUtils.html) |  A collection of static methods that provide simple World, Screen, and Panel coordinate transformations.   
[Scroller](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scroller.html) |  A vertical or horizontal scrollbar. For more information, refer to UXML element Scroller.   
[ScrollView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollView.html) |  Displays its contents inside a scrollable frame. For more information, see ScrollView.   
[Slider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) |  A slider containing floating point values.   
[SliderInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SliderInt.html) |  A slider containing Integer discrete values. For more information, refer to UXML element SliderInt.   
[SortColumnDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SortColumnDescription.html) |  This represents a description on what column to sort and in which order.   
[SortColumnDescriptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SortColumnDescriptions.html) |  This represents a collection or SortColumnDescriptions in multi SortColumnDescription views.   
[StyleSheet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleSheet.html) |  Style sheets are applied to visual elements in order to control the layout and visual appearance of the user interface.   
[Tab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Tab.html) |  Creates a tab to organize content on different screens.   
[TabView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TabView.html) |  Creates a tab view that groups a one or more Tab elements.   
[TemplateContainer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TemplateContainer.html) |  Represents the root VisualElement of UXML file.   
[TextElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextElement.html) |  Use this as the super class if you are declaring a custom VisualElement that displays text. For example, Button or Label use this as their base class. For more information, refer to UXML element TextElement.   
[TextField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextField.html) |  A TextField accepts and displays text input. For more information, refer to UXML element TextField.   
[TextInputBaseField<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1.html) |  Abstract base class used for all text-based fields.   
[TextValueField<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextValueField_1.html) |  Base class for text fields.   
[ThemeStyleSheet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ThemeStyleSheet.html) |  Represents a style sheet that's assembled from other style sheets.   
[Toggle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) |  A Toggle is a clickable element that represents a boolean value.   
[ToggleButtonGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroup.html) |  A control that allows single or multiple selection out of a logical group of Button elements.   
[ToggleButtonGroupStatePropertiesAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupStatePropertiesAttribute.html) |  Defines how a serialized ToggleButtonGroupState will be initialized in the inspector.   
[TooltipEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TooltipEvent.html) |  Event sent to find the first VisualElement that displays a tooltip.   
[TransitionCancelEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TransitionCancelEvent.html) |  Event sent when a transition is canceled.   
[TransitionEndEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TransitionEndEvent.html) |  Event sent at the completion of the transition. In the case where a transition is removed before completion then the event will not fire.   
[TransitionEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TransitionEventBase_1.html) |  Transition events abstract base class.   
[TransitionRunEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TransitionRunEvent.html) |  Event sent when a transition is created (i.e. added to the set of running transitions).   
[TransitionStartEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TransitionStartEvent.html) |  Event sent when a transition's delay phase ends.   
[TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TreeView.html) |  A TreeView is a vertically scrollable area that links to, and displays, a list of items organized in a tree.   
[TreeViewController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TreeViewController.html) |  Tree view controller. View controllers of this type are meant to take care of data virtualized by any TreeView inheritor.   
[TreeViewExpansionChangedArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TreeViewExpansionChangedArgs.html) |  A data structure for the tree view item expansion event.   
[TwoPaneSplitView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TwoPaneSplitView.html) |  A SplitView that contains two resizable panes. One pane is fixed-size while the other pane has flex-grow style set to 1 to take all remaining space. The border between the panes is draggable to resize both panes. Both horizontal and vertical modes are supported. Requires exactly two child elements to operate.   
[TypedUxmlAttributeDescription<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TypedUxmlAttributeDescription_1.html) |  Base class for all the UXML specific attributes.   
[UIDocument](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UIDocument.html) |  Defines a Component that connects VisualElements to GameObjects. This makes it possible to render UI defined in UXML documents in the Game view.   
[UIRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UIRenderer.html) |  A renderer Component that should be added next to a UIDocument Component to allow world-space rendering. This Component is added automatically by the UIDocument when the PanelSettings asset is configured in world-space.   
[UIToolkitInputConfiguration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UIToolkitInputConfiguration.html) |  Global configuration options for UI Toolkit input.   
[UnsignedIntegerField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UnsignedIntegerField.html) |  Makes a text field for entering an unsigned integer. For more information, refer to UXML element UnsignedIntegerField.   
[UnsignedLongField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UnsignedLongField.html) |  Makes a text field for entering unsigned long integers. For more information, refer to UXML element UnsignedLongField.   
[UQuery](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQuery.html) |  UQuery is a set of extension methods allowing you to select individual or collection of visualElements inside a complex hierarchy. See UQuery manual page for further information.   
[UQueryExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryExtensions.html) |  UQuery is a set of extension methods allowing you to select individual or collection of visualElements inside a complex hierarchy. For more information, refer to Find visual elements with UQuery.   
[UxmlAssetAttributeDescription<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlAssetAttributeDescription_1.html) |  Describes a UXML Object attribute referencing an asset in the project. In UXML, this is referenced as a string URI.   
[UxmlAttributeAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlAttributeAttribute.html) |  Declares that a field or property is associated with a UXML attribute.   
[UxmlAttributeDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlAttributeDescription.html) |  Base class for describing an XML attribute.   
[UxmlBoolAttributeDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlBoolAttributeDescription.html) |  Describes a UXML bool attribute.   
[UxmlChildElementDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlChildElementDescription.html) |  Describe an allowed child element for an element.   
[UxmlColorAttributeDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlColorAttributeDescription.html) |  Describes a UXML attribute representing a Color as a string.   
[UxmlDescriptionCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlDescriptionCache.html) |  Contains pre-processed information about UXML attribute descriptions to avoid relying on reflection.   
[UxmlDoubleAttributeDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlDoubleAttributeDescription.html) |  Describes a UXML double attribute.   
[UxmlElementAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlElementAttribute.html) |  Declares a custom control.   
[UxmlEnumAttributeDescription<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlEnumAttributeDescription_1.html) |  Describes a UXML attribute representing an enum as a string.   
[UxmlEnumeration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlEnumeration.html) |  Restricts the value of an attribute to be taken from a list of values.   
[UxmlFloatAttributeDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlFloatAttributeDescription.html) |  Describes a UXML float attribute.   
[UxmlHash128AttributeDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlHash128AttributeDescription.html) |  Describes a UXML Hash128 attribute.   
[UxmlIgnoreAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlIgnoreAttribute.html) |  Used for fields that are serialized but do not come from UXML data, such as UxmlSerializedData.uxmlAssetId.   
[UxmlIntAttributeDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlIntAttributeDescription.html) |  Describes a UXML int attribute.   
[UxmlLongAttributeDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlLongAttributeDescription.html) |  Describes a UXML long attribute.   
[UxmlObjectAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlObjectAttribute.html) |  Declares that a class can be instantiated from UXML and contain UXML attributes.   
[UxmlObjectReferenceAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlObjectReferenceAttribute.html) |  Declares that a field or property is associated with nested UXML objects.   
[UxmlSerializedData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlSerializedData.html) |  Generates an instance of the declaring element when the UxmlElementAttribute is used in a custom control.   
[UxmlSerializedDataUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlSerializedDataUtility.html) |  This is used by the code generator when a custom control is using the UxmlElementAttribute.   
[UxmlStringAttributeDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlStringAttributeDescription.html) |  Describes a UXML string attribute.   
[UxmlTypeAttributeDescription<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlTypeAttributeDescription_1.html) |  Describes an XML System.Type attribute.   
[UxmlTypeReferenceAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlTypeReferenceAttribute.html) |  Provides information about the expected type when applied to a Type field or property that has the UxmlAttributeAttribute attribute.   
[UxmlTypeRestriction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlTypeRestriction.html) |  Base class to restricts the value of an attribute.   
[UxmlUnsignedIntAttributeDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlUnsignedIntAttributeDescription.html) |  Describes a UXML uint attribute.   
[UxmlUnsignedLongAttributeDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlUnsignedLongAttributeDescription.html) |  Describes a UXML ulong attribute.   
[UxmlValueBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlValueBounds.html) |  Restricts the value of an attribute to be within the specified bounds.   
[UxmlValueMatches](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlValueMatches.html) |  Restricts the value of an attribute to match a regular expression.   
[ValidateCommandEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ValidateCommandEvent.html) |  This event is sent by the Editor while it determines whether the command will be handled by an element in the panel.   
[ValueAnimation<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Experimental.ValueAnimation_1.html) |  Implementation object for transition animations.   
[Vector2Field](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vector2Field.html) |  A Vector2 field. For more information, refer to UXML element Vector2Field.   
[Vector2IntField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vector2IntField.html) |  A Vector2Int field. For more information, refer to UXML element Vector2IntField.   
[Vector3Field](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vector3Field.html) |  A Vector3 field. For more information, refer to UXML element Vector3Field.   
[Vector3IntField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vector3IntField.html) |  A Vector3Int field. For more information, refer to UXML element Vector3IntField.   
[Vector4Field](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vector4Field.html) |  A Vector4 field. For more information, refer to UXML element Vector4Field.   
[VectorImage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VectorImage.html) |  An asset that represents a vector image.   
[VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) |  Base class for objects that are part of the UIElements visual tree.   
[VisualElementExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElementExtensions.html) |  VisualElementExtensions is a set of extension methods useful for VisualElement.   
[VisualElementFocusChangeDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElementFocusChangeDirection.html) |  Define focus change directions for the VisualElementFocusRing.   
[VisualElementFocusRing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElementFocusRing.html) |  Implementation of a linear focus ring. Elements are sorted according to their focusIndex.   
[VisualTreeAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualTreeAsset.html) |  An instance of this class holds a tree of VisualElementAsset's, created from a UXML file. Each node in the file corresponds to a VisualElementAsset. You can clone a VisualTreeAsset to create a tree of VisualElement's. Note: You can't generate a VisualTreeAsset from raw UXML at runtime.   
[WheelEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.WheelEvent.html) |  This event is sent when the mouse wheel moves.   
### Structs
Struct | Description  
---|---  
[Angle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Angle.html) |  Represents an angle value.   
[Background](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Background.html) |  Describes a VisualElement background.   
[BackgroundPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BackgroundPosition.html) |  Script interface for VisualElement background-position style property IStyle.BackgroundPosition.   
[BackgroundRepeat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BackgroundRepeat.html) |  Script interface for VisualElement background-repeat style property IStyle.backgroundRepeat.   
[BackgroundSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BackgroundSize.html) |  Script interface for VisualElement background-size style property IStyle.BackgroundSize.   
[BindablePropertyChangedEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindablePropertyChangedEventArgs.html) |  Provides information about the property that has changed.   
[BindingActivationContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingActivationContext.html) |  Contains information passed to binding instances during registration and deregistration.   
[BindingContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingContext.html) |  Context object containing the necessary information to resolve a binding.   
[BindingId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingId.html) |  Defines a binding property that serves as an identifier for the binding system.   
[BindingInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingInfo.html) |  Provides information about a binding.   
[BindingResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingResult.html) |  Provides information about the binding update.   
[CanStartDragArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CanStartDragArgs.html) |  Information about a drag-and-drop operation that is about to start. See BaseVerticalCollectionView.canStartDrag.   
[CreationContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CreationContext.html) |  This structure holds information used during UXML template instantiation.   
[Cursor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Cursor.html) |  Script interface for VisualElement cursor style property IStyle.cursor.   
[CustomStyleProperty<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CustomStyleProperty_1.html) |  Define a custom style property for an element to be retrieved with CustomStyleResolvedEvent.   
[DataSourceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataSourceContext.html) |  Contains information about the data source and data source path of a binding.   
[DataSourceContextChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataSourceContextChanged.html) |  Contains information passed to binding instances when the resolved data source context has changed.   
[EasingFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EasingFunction.html) |  Determines how intermediate values are calculated for a transition.   
[EventDispatcherGate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventDispatcherGate.html) |  Gates control when the dispatcher processes events.   
[FontDefinition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FontDefinition.html) |  Describes a VisualElement font.   
[HandleDragAndDropArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.HandleDragAndDropArgs.html) |  Information about a drag-and-drop operation in progress. See BaseVerticalCollectionView.dragAndDropUpdate and BaseVerticalCollectionView.handleDrop.   
[Length](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Length.html) |  Represents a distance value.   
[ManipulatorActivationFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ManipulatorActivationFilter.html) |  Defines conditions for manipulators to respond to specific events.   
[MeshGenerationNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MeshGenerationNode.html) |  Contains a part of the draw sequence of a VisualElement. You can use it in a job to add nested draw calls.   
[Rotate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) |  Provides rotation information for visual elements that rotates around the TransformOrigin. Positive values represent clockwise rotation.   
[Scale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html) |  Represents the scale applied as element transformations. The center point that doesn't move when the scaling is applied is the TransformOrigin.   
[SetupDragAndDropArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SetupDragAndDropArgs.html) |  Information about a drag-and-drop operation that just started. You can use it to store generic data for the rest of the drag. See BaseVerticalCollectionView.setupDragAndDrop.   
[StartDragArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StartDragArgs.html) |  Provides entry points to initialize the new drag-and-drop operation.   
[StyleBackground](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleBackground.html) |  Style value that can be either a Background or a StyleKeyword.   
[StyleBackgroundPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleBackgroundPosition.html) |  Represents a style value that can be either a BackgroundPosition or a StyleKeyword.   
[StyleBackgroundRepeat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleBackgroundRepeat.html) |  Represents a style value that can be either a BackgroundRepeat or a StyleKeyword.   
[StyleBackgroundSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleBackgroundSize.html) |  Represents a style value that can be either a BackgroundSize or a StyleKeyword.   
[StyleColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleColor.html) |  Style value that can be either a Color or a StyleKeyword.   
[StyleCursor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleCursor.html) |  Style value that can be either a Cursor or a StyleKeyword.   
[StyleEnum<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleEnum_1.html) |  Style value that can be either an enum or a StyleKeyword.   
[StyleFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleFloat.html) |  Style value that can be either a float or a StyleKeyword.   
[StyleFont](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleFont.html) |  Style value that can be either a Font or a StyleKeyword.   
[StyleFontDefinition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleFontDefinition.html) |  Style value that can be either a FontDefinition or a StyleKeyword.   
[StyleInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleInt.html) |  Style value that can be either an integer or a StyleKeyword.   
[StyleLength](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleLength.html) |  Style value that can be either a Length or a StyleKeyword.   
[StyleList<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleList_1.html) |  Style value that can be either a list or a StyleKeyword.   
[StylePropertyName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StylePropertyName.html) |  Defines the name of a style property.   
[StylePropertyNameCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StylePropertyNameCollection.html) |  Collection of StylePropertyName.   
[StyleRotate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleRotate.html) |  Represents a style value that can be either a Rotate or a StyleKeyword.   
[StyleScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleScale.html) |  Style value that can be either a Scale or a StyleKeyword.   
[StyleTextShadow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleTextShadow.html) |  Style value that can be either a TextShadow or a StyleKeyword.   
[StyleTransformOrigin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleTransformOrigin.html) |  Represents a style value that can be either a TransformOrigin or a StyleKeyword.   
[StyleTranslate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleTranslate.html) |  Style value that can be either a Translate or a StyleKeyword.   
[StyleValues](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Experimental.StyleValues.html) |  Container object used to animate multiple style values at once.   
[TempMeshAllocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TempMeshAllocator.html) |  Used in jobs to allocate UI Toolkit temporary meshes.   
[TextShadow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextShadow.html) |  Script interface for VisualElement text-shadow style property IStyle.textShadow.   
[TimerState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TimerState.html) |  Contains timing information of scheduler events.   
[TimeValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TimeValue.html) |  Represents a time value.   
[ToggleButtonGroupState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToggleButtonGroupState.html) |  The structure that keeps track of the Button states inside a ToggleButtonGroup.   
[TransformOrigin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TransformOrigin.html) |  Represents the point of origin where the transformations (Scale, Translate, and Rotate) are applied.   
[Translate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Translate.html) |  Represents a translation of the object. Percentage values in X and Y are relative to the width and height of the visual element where the style value is applied.   
[TreeViewItemData<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TreeViewItemData_1.html) |  Item structure provided to a TreeView using the default implementation. For more information on usage, refer to TreeView and Create list and tree views.   
[UQueryBuilder<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.html) |  Utility Object that constructs a set of selection rules to be run on a root visual element.   
[UQueryState<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryState_1.html) |  Query object containing all the selection rules. The object can be saved and rerun later without re-allocating memory.   
[UxmlAttributeNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlAttributeNames.html) |  Holds the description data of a UXML attribute.   
[Vertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vertex.html) |  Represents a vertex of geometry for drawing content of VisualElement.   
[VisualElementStyleSheetSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElementStyleSheetSet.html) |  This structure manipulates the set of StyleSheet objects attached to the owner VisualElement.   
### Enumerations
Enumeration | Description  
---|---  
[Align](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Align.html) |  Defines the alignment behavior along an axis.   
[AlternatingRowBackground](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.AlternatingRowBackground.html) |  Options to display alternating background colors for collection view rows.   
[AngleUnit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.AngleUnit.html) |  Unit of measurement used to express the value of an Angle.   
[ArcDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ArcDirection.html) |  Direction to use when defining an arc (see Painter2D.Arc).   
[BackgroundPositionKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BackgroundPositionKeyword.html) |  Defines the position of the background.   
[BackgroundSizeType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BackgroundSizeType.html) |  Defines the size of the background.   
[BindingLogLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingLogLevel.html) |  Options to change the log level for warnings that occur during the update of data bindings.   
[BindingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingMode.html) |  Binding mode to control how a binding is updated.   
[BindingSourceSelectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingSourceSelectionMode.html) |  Option to change the data source assignation when using Data Binding in collection views.   
[BindingStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingStatus.html) |  Status to report the result of a binding update.   
[BindingUpdateTrigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingUpdateTrigger.html) |  Option to tell a binding when to update.   
[CollectionVirtualizationMethod](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CollectionVirtualizationMethod.html) |  Options to change the virtualization method used by the collection view to display its content.   
[ColumnSortingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ColumnSortingMode.html) |  Defines the sorting mode of a MultiColumnListView or MultiColumnTreeView.   
[ContextType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ContextType.html) |  Describes in which context a VisualElement hierarchy is being ran.   
[DeltaSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DeltaSpeed.html) |  Speed at which the value changes for a given input device delta.   
[DisplayStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DisplayStyle.html) |  Defines how an element is displayed in the layout.   
[DragAndDropPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragAndDropPosition.html) |  Position where the drop operation occurs.   
[DragVisualMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DragVisualMode.html) |  The status of a drag-and-drop operation.   
[DynamicAtlasFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasFilters.html) |  Options to enable or disable filters for the dynamic atlas.   
[EasingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EasingMode.html) |  Represents a mathematical function that describes the rate at which a numerical value changes.   
[EditorTextRenderingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EditorTextRenderingMode.html) |  Defines how the editor rendering the text by default   
[EventInterestOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventInterestOptions.html) |  Options used as arguments for EventInterestAttribute when the affected method treats events in a general, non type-specific manner.   
[FillRule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FillRule.html) |  The fill rule to use when filling shapes with Painter2D.Fill.   
[FlexDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FlexDirection.html) |  Defines the main-axis of the flex layout.   
[HelpBoxMessageType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.HelpBoxMessageType.html) |  User message types.   
[Justify](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Justify.html) |  Defines the alignment along the main axis, how is extra space distributed.   
[KeyboardNavigationOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.KeyboardNavigationOperation.html) |  Represents an operation that the user is trying to accomplish through a specific input mechanism.   
[LanguageDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LanguageDirection.html) |  Indicates the directionality of the element's text.   
[LengthUnit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LengthUnit.html) |  Describes how to interpret a Length value.   
[LineCap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LineCap.html) |  Cap types for the beginning and end of paths (see Painter2D.lineCap).   
[LineJoin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LineJoin.html) |  Join types connecting two sub-paths (see Painter2D.lineJoin).   
[ListViewReorderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ListViewReorderMode.html) |  Options to change the drag-and-drop mode for items in the ListView.   
[MouseButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseButton.html) |  Describes a MouseButton.   
[Overflow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Overflow.html) |  Defines what should happened if content overflows an element bounds.   
[OverflowClipBox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.OverflowClipBox.html) |  Boxes against which the VisualElement content is clipped.   
[PanelScaleMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PanelScaleMode.html) |  Options that specify how elements in the panel scale when the screen size changes. See PanelSettings.scaleMode.   
[PanelScreenMatchMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PanelScreenMatchMode.html) |  Options that specify how to scale the panel area when the aspect ratio of the current screen resolution does not match the reference resolution. See PanelSettings.screenMatchMode.   
[PenButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PenButton.html) |  Describes a PenButton. Based on W3 conventions: https://www.w3.org/TR/pointerevents2/#the-buttons-property.   
[PickingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PickingMode.html) |  Describes the picking behavior.   
[Position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) |  Defines how the position values are interpreted by the layout engine.   
[PropagationPhase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PropagationPhase.html) |  The propagation phases of an event.   
[Repeat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Repeat.html) |  Defines how the background is repeated.   
[ScrollerVisibility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollerVisibility.html) |  Options for controlling the visibility of scroll bars in the ScrollView.   
[ScrollViewMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollViewMode.html) |  Configurations of the ScrollView to influence the layout of its contents and how scrollbars appear. ScrollView.mode  
[SelectionType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SelectionType.html) |  Controls how many items can be selected at once.   
[SliceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SliceType.html) |  The slice type determines whether the center of the image is scaled or tiled.   
[SliderDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SliderDirection.html) |  This is the direction of the Slider and SliderInt.   
[SortDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SortDirection.html) |  The sort direction.   
[StyleKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StyleKeyword.html) |  Keyword that can be used on any style value types.   
[TextOverflow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextOverflow.html) |  Specifies how the text Element treats hidden overflow content.   
[TextOverflowPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextOverflowPosition.html) |  Specifies which part of the text the Element replaces with an ellipsis when textOverflow is set to TextOverflow.Ellipsis.   
[TimeUnit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TimeUnit.html) |  Describes how to interpret a TimeValue.   
[TransformOriginOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TransformOriginOffset.html) |  Specifies the alignment keywords for TransformOrigin.   
[TrickleDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TrickleDown.html) |  Use this enum to specify during which phases the event handler is executed.   
[TwoPaneSplitViewOrientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TwoPaneSplitViewOrientation.html) |  Determines the orientation of the two resizable panes.   
[UIToolkitInputBackendOption](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UIToolkitInputBackendOption.html) |  Input backend options for UI Toolkit events at runtime.   
[UsageHints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UsageHints.html) |  Offers a set of options that describe the intended usage patterns of a VisualElement. These options serve as guidance for optimizations. You can set multiple usage hints on an element. For example, if both position and color change, you can set both DynamicTransform and DynamicColor. Note: Set the usage hints at edit time or before you add the VisualElement to a panel. In the case of transition, when it starts, the system might automatically add missing relevant usage hints to avoid regenerating geometry in every frame. However, this causes a one-frame performance penalty because the rendering data for the VisualElement and its descendants is regenerated.   
[VersionChangeType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VersionChangeType.html) |  Value used to signify some changes in the VisualElement   
[Visibility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Visibility.html) |  Style value that specifies whether or not a VisualElement is visible.   
[WhiteSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.WhiteSpace.html) |  Controls how white space and line breaks within an element's text are handled.   
[Wrap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Wrap.html) |  By default, items will all try to fit onto one line. You can change that and allow the items to wrap as needed with this property.   
* * *
