* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html

# EditorGUI
class in UnityEditor
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
These work pretty much like the normal GUI functions - and also have matching implementations in [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).
### Static Properties
Property | Description  
---|---  
[actionKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI-actionKey.html) | Is the platform-dependent "action" modifier key held down? (Read Only)  
[indentLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI-indentLevel.html) | The indent level of the field labels.  
[showMixedValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI-showMixedValue.html) | Makes the following controls give the appearance of editing multiple different values.  
### Static Methods
Method | Description  
---|---  
[BeginChangeCheck](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html) | Starts a new code block to check for GUI changes.  
[BeginDisabledGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginDisabledGroup.html) | Create a group of controls that can be disabled.  
[BeginFoldoutHeaderGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginFoldoutHeaderGroup.html) | Make a label with a foldout arrow to the left of it.  
[BeginProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginProperty.html) | Create a Property wrapper, useful for making regular GUI controls work with SerializedProperty.  
[BoundsField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BoundsField.html) | Makes Center and Extents field for entering a Bounds.  
[BoundsIntField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BoundsIntField.html) | Makes Position and Size field for entering a BoundsInt.  
[ColorField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ColorField.html) | Makes a field for selecting a Color.  
[CurveField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.CurveField.html) | Makes a field for editing an AnimationCurve.  
[DelayedDoubleField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DelayedDoubleField.html) | Makes a delayed text field for entering doubles.  
[DelayedFloatField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DelayedFloatField.html) | Makes a delayed text field for entering floats.  
[DelayedIntField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DelayedIntField.html) | Makes a delayed text field for entering integers.  
[DelayedTextField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DelayedTextField.html) | Makes a delayed text field.  
[DoubleField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DoubleField.html) | Makes a text field for entering doubles.  
[DrawPreviewTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DrawPreviewTexture.html) | Draws the texture within a rectangle.  
[DrawRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DrawRect.html) | Draws a filled rectangle of color at the specified position and size within the current editor window.  
[DrawTextureAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DrawTextureAlpha.html) | Draws the alpha channel of a texture within a rectangle.  
[DropdownButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DropdownButton.html) | Makes a button that reacts to mouse down, for displaying your own dropdown content.  
[DropShadowLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DropShadowLabel.html) | Draws a label with a drop shadow.  
[EndChangeCheck](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html) | Ends a code block and checks for any GUI changes.  
[EndDisabledGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndDisabledGroup.html) | Ends a disabled group started with BeginDisabledGroup.  
[EndFoldoutHeaderGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndFoldoutHeaderGroup.html) | Closes a group started with BeginFoldoutHeaderGroup. Additional resources: EditorGUILayout.BeginFoldoutHeaderGroup.  
[EndProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndProperty.html) | Ends a Property wrapper started with BeginProperty.  
[EnumFlagsField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EnumFlagsField.html) | Displays a menu with an option for every value of the enum type when clicked. An option for the value 0 with name "Nothing" and an option for the value ~0 (that is, all bits set) with the name "Everything" are always displayed at the top of the menu. The names for the values 0 and ~0 can be overriden by defining these values in the enum type.  
[EnumPopup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EnumPopup.html) | Makes an enum popup selection field.  
[FloatField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.FloatField.html) | Makes a text field for entering floats.  
[FocusTextInControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.FocusTextInControl.html) | Move keyboard focus to a named text field and begin editing of the content.  
[Foldout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Foldout.html) | Makes a label with a foldout arrow to the left of it.  
[GetPropertyHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.GetPropertyHeight.html) | Get the height needed for a PropertyField control.  
[GradientField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.GradientField.html) | Makes a field for editing a Gradient.  
[HandlePrefixLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.HandlePrefixLabel.html) | Makes a label for some control.  
[HelpBox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.HelpBox.html) | Makes a help box with a message to the user.  
[InspectorTitlebar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.InspectorTitlebar.html) | Makes an inspector-window-like titlebar.  
[IntField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.IntField.html) | Makes a text field for entering integers.  
[IntPopup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.IntPopup.html) | Makes an integer popup selection field.  
[IntSlider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.IntSlider.html) | Makes a slider the user can drag to change an integer value between a min and a max.  
[LabelField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html) | Makes a label field. (Useful for showing read-only info.)  
[LargeSplitButtonWithDropdownList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LargeSplitButtonWithDropdownList.html) | Creates a large button that contains a regular button section and an arrow to open a dropdown menu.  
[LayerField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LayerField.html) | Makes a layer selection field.  
[LinkButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LinkButton.html) | Make a clickable link label.  
[LogarithmicIntSlider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LogarithmicIntSlider.html) | Makes a text field for entering an integer on a logarithmic scale.  
[LongField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LongField.html) | Makes a text field for entering long integers.  
[MaskField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.MaskField.html) | Makes a field for masks.  
[MinMaxSlider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.MinMaxSlider.html) | Makes a special slider the user can use to specify a range between a min and a max.  
[MultiFloatField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.MultiFloatField.html) | Makes a multi-control with text fields for entering multiple floats in the same line.  
[MultiIntField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.MultiIntField.html) | Makes a multi-control with text fields for entering multiple integers in the same line.  
[MultiPropertyField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.MultiPropertyField.html) | Makes a multi-control with several property fields in the same line.  
[ObjectField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ObjectField.html) | Makes an object field. You can assign objects either by drag and drop objects or by selecting an object using the Object Picker.  
[PasswordField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PasswordField.html) | Makes a text field where the user can enter a password.  
[Popup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Popup.html) | Makes a generic popup selection field.  
[PrefixLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PrefixLabel.html) | Makes a label in front of some control.  
[ProgressBar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ProgressBar.html) | Makes a progress bar.  
[PropertyField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PropertyField.html) | Use this to make a field for a SerializedProperty in the Editor.  
[RectField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.RectField.html) | Makes an X, Y, W, and H field for entering a Rect.  
[RectIntField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.RectIntField.html) | Makes an X, Y, W, and H field for entering a RectInt.  
[RenderingLayerMaskField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.RenderingLayerMaskField.html) | Makes a rendering layer selection field.  
[SelectableLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.SelectableLabel.html) | Makes a selectable label field. (Useful for showing read-only info that can be copy-pasted.)  
[Slider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Slider.html) | Makes a slider the user can drag to change a value between a min and a max.  
[TagField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.TagField.html) | Makes a tag selection field.  
[TextArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.TextArea.html) | Makes a text area.  
[TextField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.TextField.html) | Makes a text field.  
[Toggle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Toggle.html) | Makes a toggle.  
[ToggleLeft](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ToggleLeft.html) | Makes a toggle field where the toggle is to the left and the label immediately to the right of it.  
[Vector2Field](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Vector2Field.html) | Makes an X and Y field for entering a Vector2.  
[Vector2IntField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Vector2IntField.html) | Makes an X and Y integer field for entering a Vector2Int.  
[Vector3Field](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Vector3Field.html) | Makes an X, Y, and Z field for entering a Vector3.  
[Vector3IntField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Vector3IntField.html) | Makes an X, Y, and Z integer field for entering a Vector3Int.  
[Vector4Field](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Vector4Field.html) | Makes an X, Y, Z, and W field for entering a Vector4.  
### Events
Event | Description  
---|---  
[hyperLinkClicked](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI-hyperLinkClicked.html) | Event used to react on clicks on a text hyperlink part.  
* * *
