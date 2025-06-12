* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.html

**Experimental** : this API is experimental and might be changed or removed in the future.
# GraphView
class in UnityEditor.Experimental.GraphView
/
Inherits from:[UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)
Leave feedback
  

Implements interfaces:[ISelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ISelection.html)
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
Main GraphView class.
### Properties
Property | Description  
---|---  
[canPasteSerializedData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-canPasteSerializedData.html) | Ask whether or not the serialized data can be pasted.  
[contentViewContainer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-contentViewContainer.html) | Main content container.  
[deleteSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-deleteSelection.html) | Delete selection callback.  
[edges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-edges.html) | All edges in the graph.  
[elementResized](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-elementResized.html) | Element resized callback.  
[elementsAddedToGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-elementsAddedToGroup.html) | Callback for when GraphElements are added to the group.  
[elementsInsertedToStackNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-elementsInsertedToStackNode.html) | Callback for when GraphElements are inserted into a StackNode.  
[elementsRemovedFromGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-elementsRemovedFromGroup.html) | Callback for when GraphElements are removed from the group.  
[elementsRemovedFromStackNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-elementsRemovedFromStackNode.html) | Callback for when GraphElements are removed from a StackNode.  
[graphElements](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-graphElements.html) | All GraphElements in the graph.  
[graphViewChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-graphViewChanged.html) | Callback for when certain changes have occured in the graph. See GraphViewChange.  
[groupTitleChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-groupTitleChanged.html) | Callback for when a group title is changed.  
[isReframable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-isReframable.html) | Whether or not the selection is reframable.  
[maxScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-maxScale.html) | Max zoom level.  
[minScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-minScale.html) | Min zoom level.  
[nodeCreationRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-nodeCreationRequest.html) | Callback for when the user requests to display the node creation window.  
[nodes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-nodes.html) | All nodes currently in the graph.  
[placematContainer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-placematContainer.html) | The PlacematContainer used by the GraphView.  
[ports](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-ports.html) | All ports currently in the graph.  
[referenceScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-referenceScale.html) | Reference zoom level.  
[scale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-scale.html) | Current graph zoom level.  
[scaleStep](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-scaleStep.html) | Zoom step. See ContentZoomer.scaleStep for details.  
[selection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-selection.html) | All currently selected elements in the graph.  
[serializeGraphElements](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-serializeGraphElements.html) | Callback for serializing graph elements for copy/paste and other actions.  
[supportsWindowedBlackboard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-supportsWindowedBlackboard.html) | Set to true when this GraphView supports windowed Blackboards. Set to false otherwise.  
[unserializeAndPaste](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-unserializeAndPaste.html) | Callback for unserializing graph elements and adding them to the graph.  
[viewport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-viewport.html) | The graph's viewport. This is currently just itself.  
[viewTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-viewTransform.html) | Graph's view transform.  
[viewTransformChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-viewTransformChanged.html) | View transform changed callback.  
[zoomerMaxElementCountWithPixelCacheRegen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView-zoomerMaxElementCountWithPixelCacheRegen.html) | Number of elements in the graph above which the zoom manipulator will turn off pixel cache regeneration on each tick to avoid performance drops.  
### Public Methods
Method | Description  
---|---  
[AddElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.AddElement.html) | Add new GraphElement. Should use this instead of Add() for adding GraphElements.  
[AddLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.AddLayer.html) | Adds a new layer to the GraphView.  
[AddToSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.AddToSelection.html) | Add element to selection.  
[BuildContextualMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.BuildContextualMenu.html) | Add menu items to the contextual menu.  
[CalculateRectToFitAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.CalculateRectToFitAll.html) | Calculate the rectangle size and position to fit all elements in graph.  
[ClearSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.ClearSelection.html) | Clear selection.  
[DeleteElements](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.DeleteElements.html) | Remove elements from the graph view.  
[DeleteSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.DeleteSelection.html) | Delete selected elements.  
[FrameAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.FrameAll.html) | Focus view all elements in the graph.  
[FrameNext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.FrameNext.html) | Focus view on the next element after the one currently selected.  
[FrameOrigin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.FrameOrigin.html) | Focus view on the graph's origin.  
[FramePrev](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.FramePrev.html) | Focus view on the previous element before the one currently selected.  
[FrameSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.FrameSelection.html) | Focus view on currently selected elements.  
[GetBlackboard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.GetBlackboard.html) | Gets the blackboard associated with this GraphView.  
[GetCompatiblePorts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.GetCompatiblePorts.html) | Get all ports compatible with given port.  
[GetEdgeByGuid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.GetEdgeByGuid.html) | Get edge by its GUID.  
[GetElementByGuid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.GetElementByGuid.html) | Get any element with a given GUID.  
[GetNodeByGuid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.GetNodeByGuid.html) | Get node with a given GUID.  
[GetPortByGuid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.GetPortByGuid.html) | Get port by its GUID.  
[GetPortCenterOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.GetPortCenterOverride.html) | Gets another location for a specific port and checks if the port has an overridden position.  
[ReleaseBlackboard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.ReleaseBlackboard.html) | Releases an associated blackboard from this GraphView.  
[RemoveElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.RemoveElement.html) | Remove element from the graph.  
[RemoveFromSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.RemoveFromSelection.html) | Remove element from selection.  
[SetupZoom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.SetupZoom.html) | Setup zoom properties.  
[UpdateViewTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.UpdateViewTransform.html) | Update the viewport transform.  
### Protected Methods
Method | Description  
---|---  
[CanPasteSerializedData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.CanPasteSerializedData.html) | Default method for checking if serialized data can be pasted.  
[CreatePlacematContainer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.CreatePlacematContainer.html) | Override this method, in a derived class, to create a custom PlacematContainer.  
[DeleteSelectionOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.DeleteSelectionOperation.html) | Default method for deleting selection.  
[SerializeGraphElements](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.SerializeGraphElements.html) | Default method for serializing graph elements.  
[UnserializeAndPasteOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.UnserializeAndPasteOperation.html) | Default method for unserializing elements and pasting.  
[ValidateTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.ValidateTransform.html) | Validate the view transform.  
### Static Methods
Method | Description  
---|---  
[CalculateFrameTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.CalculateFrameTransform.html) | Calculate the view transform based on zoom level and the size of the window or parent.  
[CollectElements](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.CollectElements.html) | Retrieves the set of elements that match a specified condition. The matching elements are selected from an enumerable of graph elements.  
### Delegates
Delegate | Description  
---|---  
[CanPasteSerializedDataDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.CanPasteSerializedDataDelegate.html) | Delegate for checking if serialized data can be pasted.  
[DeleteSelectionDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.DeleteSelectionDelegate.html) | Delegate for deleting selection.  
[ElementResized](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.ElementResized.html) | Element resized delegate.  
[GraphViewChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.GraphViewChanged.html) | Delegate used to indicate a change in GraphView usualy done by a Manipulator.  
[SerializeGraphElementsDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.SerializeGraphElementsDelegate.html) | Delegate for serializing graph elements.  
[UnserializeAndPasteDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.UnserializeAndPasteDelegate.html) | Delegate for unserializing and pasting elements.  
[ViewTransformChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.ViewTransformChanged.html) | View transform changed (zoom) delegate.  
### Inherited Members
### Static Properties
Property | Description  
---|---  
[disabledUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-disabledUssClassName.html) |  USS class name of local disabled elements.   
### Properties
Property | Description  
---|---  
[canGrabFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable-canGrabFocus.html) |  Return true if the element can be focused.   
[delegatesFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable-delegatesFocus.html) |  Whether the element should delegate the focus to its children.   
[focusable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable-focusable.html) |  True if the element can be focused.   
[focusController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable-focusController.html) |  Return the focus controller for this element.   
[tabIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable-tabIndex.html) |  An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.   
[childCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-childCount.html) |  Number of child elements in this object's contentContainer.   
[contentContainer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-contentContainer.html) |  Child elements are added to it, usually this is the same as the element itself.   
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
[HandleEventBubbleUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.HandleEventBubbleUp.html) |  Executes logic on this element during the BubbleUp phase, immediately before this element's BubbleUp callbacks. Calling StopPropagation will prevent further invocations of this method along the propagation path.   
[HandleEventTrickleDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.HandleEventTrickleDown.html) |  Executes logic on this element during the TrickleDown phase, immediately after this element's TrickleDown callbacks. Calling StopPropagation will prevent further invocations of this method along the propagation path.   
[NotifyPropertyChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.NotifyPropertyChanged.html) |  Informs the data binding system that a property of a control has changed.   
* * *
