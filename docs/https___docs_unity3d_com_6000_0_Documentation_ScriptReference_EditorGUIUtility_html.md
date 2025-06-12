* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html

# EditorGUIUtility
class in UnityEditor
/
Inherits from:[GUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.html)
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
Miscellaneous helper stuff for [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).
### Static Properties
Property | Description  
---|---  
[currentViewWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-currentViewWidth.html) | The width of the GUI area for the current EditorWindow or other view. This Property should only be accessed within an OnGUI call.  
[editingTextField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-editingTextField.html) | Is a text field currently editing text?  
[fieldWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-fieldWidth.html) | The minimum width in pixels reserved for the fields of Editor GUI controls.  
[hierarchyMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-hierarchyMode.html) | Is the Editor GUI in hierarchy mode?  
[isProSkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-isProSkin.html) | Is the user currently using the pro skin? (Read Only)  
[labelWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-labelWidth.html) | The width in pixels reserved for labels of Editor GUI controls.  
[pixelsPerPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-pixelsPerPoint.html) | The scale of GUI points relative to screen pixels for the current viewThis value is the number of screen pixels per point of interface space. For instance, 2.0 on retina displays. Note that the value may differ from one view to the next if the views are on monitors with different UI scales.  
[singleLineHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-singleLineHeight.html) | Get the height used for a single Editor control such as a one-line EditorGUI.TextField or EditorGUI.Popup.  
[standardVerticalSpacing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-standardVerticalSpacing.html) | Get the height used by default for vertical spacing between controls.  
[systemCopyBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-systemCopyBuffer.html) | The system copy buffer.  
[textFieldHasSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-textFieldHasSelection.html) | True if a text field currently has focused and the text in it is selected.  
[whiteTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-whiteTexture.html) | Get a white texture.  
[wideMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-wideMode.html) | Is the Editor GUI currently in wide mode?  
### Static Methods
Method | Description  
---|---  
[AddCursorRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.AddCursorRect.html) | Add a custom mouse pointer to a control.  
[CommandEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.CommandEvent.html) | Creates an event that can be sent to another window.  
[DrawColorSwatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.DrawColorSwatch.html) | Draw a color swatch.  
[DrawCurveSwatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.DrawCurveSwatch.html) | Draw a curve swatch.  
[DrawRegionSwatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.DrawRegionSwatch.html) | Draw swatch with a filled region between two SerializedProperty curves.  
[FindTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.FindTexture.html) | Get a texture from its source filename.  
[GetBuiltinSkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.GetBuiltinSkin.html) | Get one of the built-in GUI skins, which can be the game view, inspector or Scene view skin as chosen by the parameter.  
[GetFlowLayoutedRects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.GetFlowLayoutedRects.html) | Layout list of string items left to right, top to bottom in the given area.  
[GetIconForObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.GetIconForObject.html) | Gets the custom icon associated with an object. Only GameObjects and MonoScripts have associated custom icons.  
[GetIconSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.GetIconSize.html) | Get the size that has been set using SetIconSize.  
[GetMainWindowPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.GetMainWindowPosition.html) | Returns position of Unity Editor's main window.  
[GetObjectPickerControlID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.GetObjectPickerControlID.html) | The controlID of the currently showing object picker.  
[GetObjectPickerObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.GetObjectPickerObject.html) | The object currently selected in the object picker.  
[HasObjectThumbnail](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.HasObjectThumbnail.html) | Does a given class have per-object thumbnails?  
[IconContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.IconContent.html) | Fetch the GUIContent from the Unity builtin resources with the given name.  
[IsDisplayReferencedByCameras](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.IsDisplayReferencedByCameras.html) | Check if any enabled camera can render to a particular display.  
[Load](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.Load.html) | Load a built-in resource.  
[LoadRequired](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.LoadRequired.html) | Load a required built-in resource.  
[LookLikeControls](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.LookLikeControls.html) | Make all EditorGUI look like regular controls.  
[ObjectContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.ObjectContent.html) | Return a GUIContent object with the name and icon of an Object.  
[PingObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.PingObject.html) | Ping an object in the Scene like clicking it in an inspector.  
[PixelsToPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.PixelsToPoints.html) | Convert from pixel space to point space.  
[PointsToPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.PointsToPixels.html) | Convert from point space to pixel space.  
[QueueGameViewInputEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.QueueGameViewInputEvent.html) | Send an input event into the game.  
[SetIconForObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.SetIconForObject.html) | Sets a custom icon to associate with a GameObject or MonoScript. The custom icon is displayed in the Scene view and the Inspector.  
[SetIconSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.SetIconSize.html) | Set icons rendered as part of GUIContent to be rendered at a specific size.  
[SetMainWindowPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.SetMainWindowPosition.html) | Sets position of Unity Editor's main window.  
[ShowObjectPicker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.ShowObjectPicker.html) | Show the object picker from code.  
[TrIconContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.TrIconContent.html) | Gets the GUIContent from Unity built-in resources with the given information or creates a GUIContent for a GUI element.The icon is loaded with a localized tooltip. Typically, the icon from `Assets/Editor Default Resources/Icons` is fetched using the icon name. Only the name of the icon, without the .png extension is needed.  
[TrTextContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.TrTextContent.html) | Gets the GUIContent from the Unity built-in resources with the given key or creates a GUIContent for a GUI element.The text and the tooltip are localized and loaded with an icon.Typically, the icon from `Assets/Editor Default Resources/Icons` is fetched using the icon name. Only the name of the icon, without the .png extension is needed.  
[TrTextContentWithIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.TrTextContentWithIcon.html) | Gets the GUIContent from Unity built-in resources with the given information or creates a GUIContent for a GUI element.The text and the tooltip are localized and loaded with an icon.Typically, the icon from `Assets/Editor Default Resources/Icons` is fetched using the icon name. Only the name of the icon, without the .png extension is needed.If a message type is specified instead of an icon or an icon name, the GUIContent.image is the icon associated with that message type.  
### Inherited Members
### Static Properties
Property | Description  
---|---  
[hasModalWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-hasModalWindow.html) | A global property, which is true if a ModalWindow is being displayed, false otherwise.  
[hotControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-hotControl.html) | The controlID of the current hot control.  
[keyboardControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-keyboardControl.html) | The controlID of the control that has keyboard focus.  
[systemCopyBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility-systemCopyBuffer.html) | Get access to the system-wide clipboard.  
### Static Methods
Method | Description  
---|---  
[AlignRectToDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.AlignRectToDevice.html) | Align a local space rectangle to the pixel grid.  
[ExitGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.ExitGUI.html) | Puts the GUI in a state that will prevent all subsequent immediate mode GUI functions from evaluating for the remainder of the GUI loop by throwing an ExitGUIException.  
[GetControlID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GetControlID.html) | Get a unique ID for a control.  
[GetStateObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GetStateObject.html) | Get a state object from a controlID.  
[GUIToScreenPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GUIToScreenPoint.html) | Convert a point from GUI position to screen space.  
[GUIToScreenRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.GUIToScreenRect.html) | Convert a rect from GUI position to screen space.  
[QueryStateObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.QueryStateObject.html) | Get an existing state object from a controlID.  
[RotateAroundPivot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.RotateAroundPivot.html) | Helper function to rotate the GUI around a point.  
[ScaleAroundPivot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.ScaleAroundPivot.html) | Helper function to scale the GUI around a point.  
[ScreenToGUIPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.ScreenToGUIPoint.html) | Convert a point from screen space to GUI position.  
[ScreenToGUIRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIUtility.ScreenToGUIRect.html) | Convert a rect from screen space to GUI position.  
* * *
