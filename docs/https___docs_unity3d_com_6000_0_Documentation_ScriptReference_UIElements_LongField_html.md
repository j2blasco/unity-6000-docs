* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LongField.html

# LongField
class in UnityEngine.UIElements
/
Inherits from:[UIElements.TextValueField_1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextValueField_1.html)
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
Makes a text field for entering long integers. For more information, refer to [UXML element LongField](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-uxml-element-LongField.html). 
### Static Properties
Property | Description  
---|---  
[inputUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LongField-inputUssClassName.html) |  USS class name of input elements in elements of this type.   
[labelUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LongField-labelUssClassName.html) |  USS class name of labels in elements of this type.   
[ussClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LongField-ussClassName.html) |  USS class name of elements of this type.   
### Constructors
Constructor | Description  
---|---  
[LongField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LongField-ctor.html) |  Constructor.   
### Public Methods
Method | Description  
---|---  
[ApplyInputDeviceDelta](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LongField.ApplyInputDeviceDelta.html) |  Applies the values of a 3D delta and a speed from an input device.   
### Protected Methods
Method | Description  
---|---  
[StringToValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LongField.StringToValue.html) |  Converts a string to a long integer.   
[ValueToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LongField.ValueToString.html) |  Converts the given long integer to a string.   
### Inherited Members
### Static Properties
Property | Description  
---|---  
[alignedFieldUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1-alignedFieldUssClassName.html) |  USS class name of elements that are aligned in a inspector element   
[labelDraggerVariantUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1-labelDraggerVariantUssClassName.html) |  USS class name of labels in elements of this type, when there is a dragger attached on them.   
[mixedValueLabelUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1-mixedValueLabelUssClassName.html) |  USS class name of elements that show mixed values   
[noLabelVariantUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1-noLabelVariantUssClassName.html) |  USS class name of elements of this type, when there is no label.   
[inputUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-inputUssClassName.html) |  USS class name of input elements in elements of this type.   
[labelUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-labelUssClassName.html) |  USS class name of labels in elements of this type.   
[multilineInputUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-multilineInputUssClassName.html) |  USS class name of multiline input elements in elements of this type.   
[placeholderUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-placeholderUssClassName.html) |  USS class name of input elements when placeholder text is shown   
[singleLineInputUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-singleLineInputUssClassName.html) |  USS class name of single line input elements in elements of this type.   
[textInputUssName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-textInputUssName.html) |  USS class name of input elements in elements of this type.   
[ussClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-ussClassName.html) |  USS class name of elements of this type.   
[disabledUssClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-disabledUssClassName.html) |  USS class name of local disabled elements.   
### Properties
Property | Description  
---|---  
[label](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1-label.html) |  The string representing the label that will appear beside the field. If the string is empty, the label element is removed from the hierarchy. If the string is not empty, the label element is added to the hierarchy.   
[labelElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1-labelElement.html) |  This is the Label object that appears beside the input for the field.   
[mixedValueLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1-mixedValueLabel.html) |  Read-only label used to give the appearance of editing multiple different values.   
[rawValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1-rawValue.html) |  The value of the element.   
[showMixedValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1-showMixedValue.html) |  When set to true, gives the field the appearance of editing multiple different values.   
[value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1-value.html) |  The value associated with the field.   
[binding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindableElement-binding.html) |  Binding object that will be updated.   
[bindingPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindableElement-bindingPath.html) |  Path of the target property to be bound.   
[canGrabFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable-canGrabFocus.html) |  Return true if the element can be focused.   
[delegatesFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable-delegatesFocus.html) |  Whether the element should delegate the focus to its children.   
[focusable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable-focusable.html) |  True if the element can be focused.   
[focusController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable-focusController.html) |  Return the focus controller for this element.   
[tabIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable-tabIndex.html) |  An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.   
[autoCorrection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-autoCorrection.html) |  Determines if the touch screen keyboard auto correction is turned on or off.   
[cursorIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-cursorIndex.html) |  This is the cursor index in the text presented.   
[cursorPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-cursorPosition.html) |  The position of the text cursor inside the element.   
[doubleClickSelectsWord](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-doubleClickSelectsWord.html) |  Controls whether double clicking selects the word under the mouse pointer or not.   
[emojiFallbackSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-emojiFallbackSupport.html) |  Specifies the order in which the system should look for Emoji characters when rendering text. If this setting is enabled, the global Emoji Fallback list will be searched first for characters defined as Emoji in the Unicode 14.0 standard.   
[hideMobileInput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-hideMobileInput.html) |  Hides or shows the mobile input field.   
[isDelayed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-isDelayed.html) |  If set to true, the value property isn't updated until either the user presses Enter or the text field loses focus.   
[isPasswordField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-isPasswordField.html) |  Returns true if the field is used to edit a password.   
[isReadOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-isReadOnly.html) |  Returns true if the field is read only.   
[keyboardType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-keyboardType.html) |  The type of mobile keyboard that will be used.   
[maskChar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-maskChar.html) |  The character used for masking in a password field.   
[maxLength](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-maxLength.html) |  Maximum number of characters for the field.   
[onIsReadOnlyChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-onIsReadOnlyChanged.html) |  Calls the methods in its invocation list when isReadOnly changes.   
[selectAllOnFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-selectAllOnFocus.html) |  Controls whether the element's content is selected upon receiving focus.   
[selectAllOnMouseUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-selectAllOnMouseUp.html) |  Controls whether the element's content is selected when you mouse up for the first time.   
[selectIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-selectIndex.html) |  This is the selection index in the text presented.   
[text](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-text.html) |  The value of the input field.   
[textEdition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-textEdition.html) |  Retrieves this Field's TextElement ITextEdition   
[textSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-textSelection.html) |  Retrieves this Field's TextElement ITextSelection   
[touchScreenKeyboard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-touchScreenKeyboard.html) |  The active touch keyboard being displayed.   
[tripleClickSelectsLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-tripleClickSelectsLine.html) |  Controls whether triple clicking selects the entire line under the mouse pointer or not.   
[verticalScrollerVisibility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-verticalScrollerVisibility.html) |  Option for controlling the visibility of the vertical scroll bar in the TextInputBaseField_1.   
[formatString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextValueField_1-formatString.html) |  The format string used to define how numeric values are displayed. The string follows standard .NET formatting conventions.   
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
[MeasureTextSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1.MeasureTextSize.html) |  Computes the size needed to display a text string based on element style values such as font, font-size, and word-wrap.   
[SelectAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1.SelectAll.html) |  Selects all the text contained in the field.   
[SelectNone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1.SelectNone.html) |  Remove selection   
[SelectRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1.SelectRange.html) |  Select text between cursorIndex and selectIndex.   
[ApplyInputDeviceDelta](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextValueField_1.ApplyInputDeviceDelta.html) |  Applies the values of a 3D delta and a speed from an input device.   
[SetValueWithoutNotify](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextValueField_1.SetValueWithoutNotify.html) |  Allow to set the value without being notified.   
[StartDragging](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextValueField_1.StartDragging.html) |  Indicates the user started the mouse dragging for text selection.   
[StopDragging](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextValueField_1.StopDragging.html) |  Indicates the user stopped the mouse dragging for text selection.   
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
[UpdateMixedValueContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1.UpdateMixedValueContent.html) |  Update the field's visual content depending on showMixedValue.   
[HandleEventBubbleUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.HandleEventBubbleUp.html) |  Executes logic on this element during the BubbleUp phase, immediately before this element's BubbleUp callbacks. Calling StopPropagation will prevent further invocations of this method along the propagation path.   
[HandleEventTrickleDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.HandleEventTrickleDown.html) |  Executes logic on this element during the TrickleDown phase, immediately after this element's TrickleDown callbacks. Calling StopPropagation will prevent further invocations of this method along the propagation path.   
[NotifyPropertyChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.NotifyPropertyChanged.html) |  Informs the data binding system that a property of a control has changed.   
[ValueToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1.ValueToString.html) |  Converts a value of the specified generic type from the subclass to a string representation.   
[AddLabelDragger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextValueField_1.AddLabelDragger.html) |  Method used to add a mouse dragger on the label for specific numeric fields.   
* * *
