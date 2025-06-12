* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-IMGUI-migration.html

  * [UI systems](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
  * [UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIElements.html)
  * [Migration guides](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-migration-guides.html)
  * Migrate from Immediate Mode GUI (IMGUI) to UI Toolkit


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transitioning-From-UGUI.html)
Migrate from uGUI to UI Toolkit
[](https://docs.unity3d.com/6000.0/Documentation/Manual/com.unity.ugui.html)
Unity UI 
# Migrate from Immediate Mode GUI (IMGUI) to UI Toolkit
This guide is for developers experienced with [Immediate Mode GUI (IMGUI)](https://docs.unity3d.com/6000.0/Documentation/Manual/GUIScriptingGuide.html) to migrate to UI Toolkit. This guide focuses on the Editor UI, but its information can also apply to the runtime UI as well.
## Key differences
### Code-driven versus UI-driven
IMGUI is code-driven by calls to the `OnGUI` function in a C# script that implements it. UI Toolkit provides more options for Editor UI creation. With UI Toolkit, you define the behaviors in C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts). However, when defining UI elements and styles, in addition to C#, you can visually define UI controls in [UI Builder](https://docs.unity3d.com/6000.0/Documentation/Manual/UIBuilder.html) or write in [an XML-like text file (called UXML)](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UXML.html) directly. For more information, refer to [Get started with UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-simple-ui-toolkit-workflow.html).
### Immediate versus retained mode
With IMGUI, you describe the UI tree when the UI is repainted within the [`OnGUI()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnGUI.html) function. You must call this function when an event enters the UI or when you repaint the UI. There is no persistent information pertaining to the UI tree between different events. Whereas, you create **visual elements** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualelement) with UI Toolkit in a tree structure called [Visual Tree](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-VisualTree.html)An object graph, made of lightweight nodes, that holds all the elements in a window or panel. It defines every UI you build with the UI Toolkit.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Visualtree). Information in the Visual Trees is retained persistently.
### Constant versus state changes
IMGUI is based on the `OnGUI()` function that runs at least once every frame. You define the look and the behaviors of the UI for every possible frame. The body of `OnGUI()` might contain many conditions and different states.
UI Toolkit operates in an event-driven system. You define the look of the UI in its default state and define the behaviors of the UI in response to events. Any changes you make in UI Toolkit cause persistent changes to the state of your UI.
For example, the declaration of a button in IMGUI looks like the following:
```
if (GUILayout.Button("Click me!"))
{
    //Code runs here in frames where the user clicks the button.

    //Code makes changes to the UI for frames where the user has just clicked the button.
}
else
{
    //Code specifies what happens in all other frames.
}

```

The example above looks like the following in UI Toolkit:
```
UIDocument document = GetComponent<UIDocument>();

//Create button.
Button button = new Button();
button.text = "Click me!";

//Set up event handler.
button.RegisterCallback<ClickEvent>((ClickEvent evt) =>
{
    //Code runs here after button receives ClickEvent.
});

//Add button to UI.
document.rootVisualElement.Add(button);

```

For a completed example of how to create a custom Editor window with UI Toolkit, refer to [Get started with UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-simple-ui-toolkit-workflow.html).
## IMGUI support
Use the `IMGUIContainer` to place IMGUI code inside of a `VisualElement`. Everything you can do inside of `OnGUI()` is supported. 
You can arrange multiple `IMGUIContainer`s and lay them out by mixing `GUILayout` and UI Toolkit layouts. Note that it’s not possible to add `VisualElement` instances inside of an `IMGUIContainer`.
![IMGUIContainer example](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/UIElementsIMGUI.png) `IMGUIContainer` example
## From IMGUI to UI Toolkit conversion
The following table lists the equivalent functions between IMGUI and UI Toolkit:
**Action** | **IMGUI** | **UI Toolkit**  
---|---|---  
Create an [Editor Window](https://docs.unity3d.com/6000.0/Documentation/Manual/editor-EditorWindows.html) | [`EditorWindow.OnGUI()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnGUI.html) | [`EditorWindow.CreateGUI()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.CreateGUI.html)  
Create a [Property Drawer](https://docs.unity3d.com/6000.0/Documentation/Manual/editor-PropertyDrawers.html)A Unity feature that allows you to customize the look of certain controls in the Inspector window by using attributes on your scripts, or by controlling how a specific Serializable class should look [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/editor-PropertyDrawers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PropertyDrawer) or a Property Attribute | [`PropertyDrawer.OnGUI()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.OnGUI.html) | [`PropertyDrawer.CreatePropertyGUI()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.CreatePropertyGUI.html)  
Create a custom Editor for the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** | [`Editor.OnInspectorGUI()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInspectorGUI.html) | [`Editor.CreateInspectorGUI()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateInspectorGUI.html)  
The following table lists the equivalent methods, classes, and attributes between IMGUI and UI Toolkit:
**IMGUI** | **IMGUI namespaces** | **UI Toolkit**  
---|---|---  
[`AddCursorRect()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.AddCursorRect.html) | EditorGUIUtility | Set [`VisualElement.style.cursor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-cursor.html), or set a visual element’s cursor texture in the UI Builder or USS. For more detailed interactivity, use C# events.  
[`AreaScope`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.AreaScope.html) | GUILayout | Scopes are generally not needed in UI Toolkit. See `BeginArea()`.  
[`BeginArea()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginArea.html) | GUILayout | To define the area itself, create a visual element and set [`style.position`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-position.html) to [`Position.Absolute`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.Absolute.html). To create children for the area, create child visual elements under it.  
[`BeginBuildTargetSelectionGrouping()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginBuildTargetSelectionGrouping.html) | EditorGUILayout | No equivalent.  
[`BeginChangeCheck()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html) | EditorGUI | Register callbacks on each element in the change check range. If using a [`PropertyField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PropertyField.html) as a stand-in for a serialized field in a custom Inspector, use [`PropertyField.RegisterCallback<SerializedPropertyChangeEvent>()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.RegisterCallback.html) or [`PropertyField.RegisterValueChangeCallback()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PropertyField.RegisterValueChangeCallback.html). In all other cases, use [`VisualElement.RegisterCallback<ChangeEvent<T>>()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.RegisterCallback.html) or [`VisualElement.RegisterValueChangedCallback<T>()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.INotifyValueChangedExtensions.RegisterValueChangedCallback.html).  
[`BeginDisabledGroup()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginDisabledGroup.html) | EditorGUI | [`VisualElement.SetEnabled(false)`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.SetEnabled.html)  
[`BeginFoldoutHeaderGroup()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginFoldoutHeaderGroup.html) | EditorGUI, EditorGUILayout | See `Foldout()`.  
[`BeginGroup()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BeginGroup.html) | GUI | See `BeginArea()`.  
[`BeginHorizontal()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginHorizontal.html) | EditorGUILayout, GUILayout | See `BeginArea()`.  
[`BeginProperty()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginProperty.html) | EditorGUI | If you use `BeginProperty()`/`EndProperty()` to bind a simple control to a serialized property, you can do that in UI Toolkit by calling [`BindProperty()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.BindProperty.html), by setting [`bindingPath`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindableElement-bindingPath.html), or by setting the `binding-path` UXML attribute. If you use `BeginProperty()`/`EndProperty()` to make a single property out of complex custom UI, that is not supported well in UI Toolkit.  
[`BeginScrollView()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BeginScrollView.html) | EditorGUILayout, GUI, GUILayout | [`UnityEngine.UIElements.ScrollView`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollView.html)  
[`BeginToggleGroup()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginToggleGroup.html) | EditorGUILayout | No equivalent.  
[`BeginVertical()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginVertical.html) | EditorGUILayout, GUILayout | See `BeginArea()`.  
[`BoundsField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BoundsField.html) | EditorGUI, EditorGUILayout | [`BoundsField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BoundsField.html)  
[`BoundsIntField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BoundsIntField.html) | EditorGUI, EditorGUILayout | [`BoundsIntField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BoundsIntField.html)  
[`Box()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Box.html) | GUI, GUILayout | [`Box`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Box.html)  
[`BringWindowToBack()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BringWindowToBack.html) | GUI | See `Window()`.  
[`BringWindowToFront()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.BringWindowToFront.html) | GUI | See `Window()`.  
[`Button()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html) | GUI, GUILayout | [`Button`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)  
[`CanCacheInspectorGUI()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.CanCacheInspectorGUI.html) | EditorGUI | Not needed in retained mode.  
[`ChangeCheckScope`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ChangeCheckScope.html) | EditorGUI | Scopes are generally not needed in UI Toolkit. See `BeginChangeCheck()`.  
[`ColorField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ColorField.html) | EditorGUI, EditorGUILayout | [`ColorField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ColorField.html)  
[`CommandEvent()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.CommandEvent.html) | EditorGUIUtility | Generally not needed in retained mode. Use C# callbacks to handle events.  
[`CurveField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.CurveField.html) | EditorGUI, EditorGUILayout | [`CurveField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CurveField.html)  
[`DelayedDoubleField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DelayedDoubleField.html) | EditorGUI, EditorGUILayout |  [`DoubleField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DoubleField.html) with [`isDelayed`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-isDelayed.html) set to true.  
[`DelayedFloatField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DelayedFloatField.html) | EditorGUI, EditorGUILayout |  [`FloatField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FloatField.html) with [`isDelayed`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-isDelayed.html) set to true.  
[`DelayedIntField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DelayedIntField.html) | EditorGUI, EditorGUILayout |  [`IntegerField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IntegerField.html) with [`isDelayed`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-isDelayed.html) set to true.  
[`DelayedTextField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DelayedTextField.html) | EditorGUI, EditorGUILayout |  [`TextField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextField.html) with [`isDelayed`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-isDelayed.html) set to true.  
[`DisabledScope`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DisabledScope.html) | EditorGUI | Scopes are generally not needed in UI Toolkit. See `BeginDisabledGroup()`.  
[`DoubleField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DoubleField.html) | EditorGUI, EditorGUILayout | [`DoubleField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DoubleField.html)  
[`DragWindow()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DragWindow.html) | GUI | See `Window()`.  
[`DrawPreviewTexture()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DrawPreviewTexture.html) | EditorGUI | No equivalent.  
[`DrawRect()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DrawRect.html) | EditorGUI | Use [`VisualElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html). Set [`style.position`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-position.html) to [`Absolute`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.Absolute.html). Set [`style.top`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-top.html) and [`style.left`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-left.html) to define the position. Set [`style.width`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-width.html) and [`style.height`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-height.html) to define the size. Set [`style.backgroundColor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-backgroundColor.html) to set the color.  
[`DrawTexture()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DrawTexture.html) | GUI |  [`Image`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Image.html). Set [`tintColor`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Image-tintColor.html) in place of `color`. There is no equivalent for a false `alphaBlend`. There are no equivalents for `borderWidth`, `borderWidths`, `borderRadius`, or `borderRadiuses`.  
[`DrawTextureAlpha()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DrawTextureAlpha.html) | EditorGUI | No equivalent.  
[`DrawTextureWithTexCoords()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DrawTextureWithTexCoords.html) | GUI |  [`Image`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Image.html). Set [`uv`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Image-uv.html) in place of `texCoords`. There is no equivalent for a false `alphaBlend`.  
[`DropdownButton()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DropdownButton.html) | EditorGUI, EditorGUILayout | No exact equivalent. Use fully-fledged [`DropdownField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DropdownField.html)s instead of just a `DropdownButton()`.  
[`DropShadowLabel()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DropShadowLabel.html) | EditorGUI |  [`Label`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) with shadow values set in [`style.textShadow`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-textShadow.html).  
[`EditorToolbar()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EditorToolbar.html) | EditorGUILayout | Create a [`Toolbar`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toolbar.html) with one [`ToolbarButton`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToolbarButton.html) for each tool. For each `ToolbarButton`, register a callback when clicked to call either [`ToolManager.SetActiveTool()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.SetActiveTool.html) or [`ToolManager.RestorePreviousTool()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.RestorePreviousTool.html) to make that button activate the tool or deactivate it, respectively.  
[`EndArea()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndArea.html) | GUILayout | See `BeginArea()`.  
[`EndBuildTargetSelectionGrouping()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndBuildTargetSelectionGrouping.html) | EditorGUILayout | See `BeginBuildTargetSelectionGrouping()`.  
[`EndChangeCheck()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html) | EditorGUI | See `BeginChangeCheck()`.  
[`EndDisabledGroup()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndDisabledGroup.html) | EditorGUI | See `BeginDisabledGroup()`.  
[`EndFoldoutHeaderGroup()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndFoldoutHeaderGroup.html) | EditorGUI, EditorGUILayout | See `Foldout()`.  
[`EndGroup()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.EndGroup.html) | GUI | See `BeginArea()`.  
[`EndHorizontal()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndHorizontal.html) | EditorGUILayout, GUILayout | See `BeginArea()`.  
[`EndProperty()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndProperty.html) | EditorGUI | See `BeginProperty()`.  
[`EndScrollView()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.EndScrollView.html) | EditorGUILayout, GUI, GUILayout | See `BeginScrollView()`.  
[`EndToggleGroup()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndToggleGroup.html) | EditorGUILayout | See `BeginToggleGroup()`.  
[`EndVertical()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndVertical.html) | EditorGUILayout, GUILayout | See `BeginArea()`.  
[`EnumFlagsField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EnumFlagsField.html) | EditorGUI, EditorGUILayout | [`EnumFlagsField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EnumFlagsField.html)  
[`EnumPopup()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EnumPopup.html) | EditorGUI, EditorGUILayout | [`EnumField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EnumField.html)  
[`ExpandHeight()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html) | GUILayout | No equivalent.  
[`ExpandWidth()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html) | GUILayout | No equivalent.  
[`FlexibleSpace()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.FlexibleSpace.html) | GUILayout | See `Space()`.  
[`FloatField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.FloatField.html) | EditorGUI, EditorGUILayout | [`FloatField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FloatField.html)  
[`FocusControl()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.FocusControl.html) | GUI | [`VisualElement.Focus()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable.Focus.html)  
[`FocusTextInControl()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.FocusTextInControl.html) | EditorGUI | [`TextField.Focus()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable.Focus.html)  
[`FocusWindow()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.FocusWindow.html) | GUI | See `Window()`.  
[`Foldout()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Foldout.html) | EditorGUI, EditorGUILayout | [`Foldout`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Foldout.html)  
[`GetControlRect()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.GetControlRect.html) | EditorGUILayout | Only needed to convert from EditorGUILayout to EditorGUI. Not needed in UI Toolkit.  
[`GetNameOfFocusedControl()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.GetNameOfFocusedControl.html) | GUI | [`VisualElement.focusController.focusedElement`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FocusController-focusedElement.html)  
[`GetPropertyHeight()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.GetPropertyHeight.html) | EditorGUI | [`PropertyField.layout.height`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect-height.html)  
[`GradientField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.GradientField.html) | EditorGUI, EditorGUILayout | [`GradientField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GradientField.html)  
[`GroupScope`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.GroupScope.html) | GUI | Scopes are generally not needed in UI Toolkit. See `BeginArea()`.  
[`Height()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html) | GUILayout | [`VisualElement.style.height`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-height.html)  
[`HelpBox()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.HelpBox.html) | EditorGUI, EditorGUILayout | [`HelpBox`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.HelpBox.html)  
[`HorizontalScope`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.HorizontalScope.html) | EditorGUILayout, GUILayout | Scopes are generally not needed in UI Toolkit. See `BeginArea()`.  
[`HorizontalScrollbar()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalScrollbar.html) | GUI, GUILayout |  [`Scroller`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scroller.html) with [`direction`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scroller-direction.html) set to [`Horizontal`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SliderDirection.Horizontal.html).  
[`HorizontalSlider()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html) | GUI, GUILayout |  [`Slider`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) with [`direction`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseSlider_1-direction.html) set to [`Horizontal`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SliderDirection.Horizontal.html)  
[`InspectorTitlebar()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.InspectorTitlebar.html) | EditorGUI, EditorGUILayout | No equivalent.  
[`IntField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.IntField.html) | EditorGUI, EditorGUILayout | [`IntegerField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IntegerField.html)  
[`IntPopup()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.IntPopup.html) | EditorGUI, EditorGUILayout | No equivalent.  
[`IntSlider()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.IntSlider.html) | EditorGUI, EditorGUILayout | [`SliderInt`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SliderInt.html)  
[`Label()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html) | GUI, GUILayout | [`Label`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)  
[`LabelField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html) | EditorGUI, EditorGUILayout |  [`TextField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextField.html) with [`isReadOnly`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-isReadOnly.html) set to true.  
[`LayerField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LayerField.html) | EditorGUI, EditorGUILayout | [`LayerField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LayerField.html)  
[`LinkButton()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LinkButton.html) | EditorGUI, EditorGUILayout | No equivalent.  
[`Load()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.Load.html) | EditorGUIUtility | If using C#, you can use this function as is and assign its return value to the `VisualElement.style` property you want. If using USS, use function `resource()` with the same argument you would give to `Load()`.  
[`LongField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LongField.html) | EditorGUI, EditorGUILayout | [`LongField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LongField.html)  
[`MaskField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.MaskField.html) | EditorGUI, EditorGUILayout | [`MaskField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MaskField.html)  
[`MaxHeight()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html) | GUILayout | [`VisualElement.style.maxHeight`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-maxHeight.html)  
[`MaxWidth()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html) | GUILayout | [`VisualElement.style.maxWidth`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-maxWidth.html)  
[`MinHeight()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html) | GUILayout | [`VisualElement.style.minHeight`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-minHeight.html)  
[`MinMaxSlider()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.MinMaxSlider.html) | EditorGUI, EditorGUILayout | [`MinMaxSlider`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MinMaxSlider.html)  
[`MinWidth()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html) | GUILayout | [`VisualElement.style.minWidth`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-minWidth.html)  
[`ModalWindow()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.ModalWindow.html) | GUI | See `Window()`.  
[`[NonReorderable]` attribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NonReorderableAttribute.html) |  | Ensure that [`ListView.reorderable`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseVerticalCollectionView-reorderable.html) is false.  
[`ObjectField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ObjectField.html) | EditorGUI, EditorGUILayout | [`ObjectField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ObjectField.html)  
[`PasswordField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PasswordField.html) | EditorGUI, EditorGUILayout, GUI, GUILayout |  [`TextField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextField.html) with [`isPasswordField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextInputBaseField_1-isPasswordField.html) set to true  
[`PixelsToPoints()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.PixelsToPoints.html) | EditorGUIUtility | Valid for use with UI Toolkit.  
[`PointsToPixels()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.PointsToPixels.html) | EditorGUIUtility | Valid for use with UI Toolkit.  
[`Popup()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Popup.html) | EditorGUI, EditorGUILayout | [`PopupField<T0>`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PopupField_1.html)  
[`ProgressBar()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ProgressBar.html) | EditorGUI | [`ProgressBar`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ProgressBar.html)  
[`PropertyField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PropertyField.html) | EditorGUI, EditorGUILayout | [`PropertyField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PropertyField.html)  
[`PropertyScope`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PropertyScope.html) | EditorGUI | Scopes are generally not needed in UI Toolkit. See `BeginProperty()`.  
[`RectField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.RectField.html) | EditorGUI, EditorGUILayout | [`RectField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RectField.html)  
[`RectIntField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.RectIntField.html) | EditorGUI, EditorGUILayout | [`RectIntField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RectIntField.html)  
[`RepeatButton()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.RepeatButton.html) | GUI, GUILayout | [`RepeatButton`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RepeatButton.html)  
[`ScrollTo()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.ScrollTo.html) | GUI |  [`ScrollView.ScrollTo()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollView.ScrollTo.html) or [`ScrollView.scrollOffset`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollView-scrollOffset.html)  
[`ScrollViewScope`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ScrollViewScope.html) | EditorGUILayout, GUI, GUILayout | Scopes are generally not needed in UI Toolkit. See `BeginScrollView()`.  
[`SelectableLabel()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.SelectableLabel.html) | EditorGUI, EditorGUILayout |  [`Label`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) with [`isSelectable`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ITextSelection-isSelectable.html) and [`focusable`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Focusable-focusable.html) set to true.  
[`SelectionGrid()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.SelectionGrid.html) | GUI, GUILayout | [`RadioButton`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RadioButton.html)  
[`SetNextControlName()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.SetNextControlName.html) | GUI | [`VisualElement.name`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-name.html)  
[`singleLineHeight`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-singleLineHeight.html) | EditorGUIUtility | Use USS variable `--unity-metrics-single_line-height`.  
[`Slider()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Slider.html) | EditorGUI, EditorGUILayout | [`Slider`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html)  
[`Space()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Space.html) | EditorGUILayout, GUILayout | Use `flex` properties to configure spacing between visual elements.  
[`TagField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.TagField.html) | EditorGUI, EditorGUILayout | [`TagField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TagField.html)  
[`TextArea()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.TextArea.html) | EditorGUI, EditorGUILayout, GUI, GUILayout |  [`TextField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextField.html) with [`multiline`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextField-multiline.html) set to true, [`style.whiteSpace`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-whiteSpace.html) set to [`Normal`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.WhiteSpace.Normal.html), and [`ScrollView.verticalScrollerVisibility`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollView-verticalScrollerVisibility.html) set to [`Auto`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollerVisibility.Auto.html).  
[`TextField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.TextField.html) | EditorGUI, EditorGUILayout, GUI, GUILayout |  [`TextField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextField.html) with [`multiline`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TextField-multiline.html) set to true and [`style.whiteSpace`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-whiteSpace.html) set to [`NoWrap`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.WhiteSpace.NoWrap.html).  
[`Toggle()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Toggle.html) | EditorGUI, EditorGUILayout, GUI, GUILayout | [`Toggle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html)  
[`ToggleGroupScope`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ToggleGroupScope.html) | EditorGUILayout | Scopes are generally not needed in UI Toolkit. See `BeginToggleGroup()`.  
[`ToggleLeft()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ToggleLeft.html) | EditorGUI, EditorGUILayout |  [`Toggle`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html), but instead of setting [`label`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseField_1-label.html), set [`text`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseBoolField-text.html).  
[`Toolbar()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toolbar.html) | GUI, GUILayout | No equivalent.  
[`UnfocusWindow()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.UnfocusWindow.html) | GUI | See `Window()`.  
[`Vector2Field()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Vector2Field.html) | EditorGUI, EditorGUILayout | [`Vector2Field`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vector2Field.html)  
[`Vector2IntField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Vector2IntField.html) | EditorGUI, EditorGUILayout | [`Vector2IntField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vector2IntField.html)  
[`Vector3Field()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Vector3Field.html) | EditorGUI, EditorGUILayout | [`Vector3Field`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vector3Field.html)  
[`Vector3IntField()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Vector3IntField.html) | EditorGUI, EditorGUILayout | [`Vector3IntField`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vector3IntField.html)  
[`Vector4Field()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.Vector4Field.html) | EditorGUI, EditorGUILayout | [`Vector4Field`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Vector4Field.html)  
[`VerticalScope`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.VerticalScope.html) | EditorGUILayout, GUILayout | Scopes are generally not needed in UI Toolkit. See `BeginArea()`.  
[`VerticalScrollbar()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.VerticalScrollbar.html) | GUI, GUILayout |  [`Scroller`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scroller.html) with [`direction`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scroller-direction.html) set to [`Vertical`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SliderDirection.Vertical.html).  
[`VerticalSlider()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.VerticalSlider.html) | GUI, GUILayout |  [`Slider`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Slider.html) with [`direction`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseSlider_1-direction.html) set to [`Vertical`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SliderDirection.Vertical.html).  
[`Width()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html) | GUILayout | [`VisualElement.style.width`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-width.html)  
[`Window()`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html) | GUI, GUILayout | No equivalent.  
## Additional resources
  * [Get started with UI Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-simple-ui-toolkit-workflow.html)
  * [Unity style sheets (USS)](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-USS.html)
  * [Examples](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-examples.html)
  * [IMGUI events](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-IMGUI-Events.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-Transitioning-From-UGUI.html)
Migrate from uGUI to UI Toolkit
[](https://docs.unity3d.com/6000.0/Documentation/Manual/com.unity.ugui.html)
Unity UI 
