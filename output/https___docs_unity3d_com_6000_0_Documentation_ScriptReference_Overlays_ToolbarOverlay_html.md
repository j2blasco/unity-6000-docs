* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ToolbarOverlay.html

# ToolbarOverlay
class in UnityEditor.Overlays
/
Inherits from:[Overlays.Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html)
Leave feedback
  

Implements interfaces:[ICreateToolbar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ICreateToolbar.html)
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
[ToolbarOverlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ToolbarOverlay.html) is an implementation of [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) that provides a base for Overlays that can be placed in horizontal or vertical toolbars.
The constructor for [ToolbarOverlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ToolbarOverlay.html) accepts a list of IDs corresponding to UnityEditor.Toolbars.EditorToolbarElement::id.  
  
Toolbars are composed of collections of UnityEditor.Toolbars.EditorToolbarElement. In this way it is very simple to reuse elements to create customized toolbars.  
  
Toolbar overlays require specific styling, so in most cases it is preferable to inherit one of the predefined EditorToolbar types when creating Visual Elements. If custom UI is required, it is valid to inherit any UnityEngine.UIElements.VisualElement type and provide styling yourself.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Overlays;
using UnityEditor.Toolbars;
using UnityEngine;

// [EditorToolbarElement(Identifier, EditorWindowType)] is used to register toolbar elements for use in ToolbarOverlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ToolbarOverlay.html)
// implementations.
[EditorToolbarElement(id, typeof(SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html)))]
class CreateCubes : EditorToolbarButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Toolbars.EditorToolbarButton.html), IAccessContainerWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Toolbars.IAccessContainerWindow.html)
{
    // This ID is used to populate toolbar elements.
    public const string id = "ExampleToolbar/Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)";

    // IAccessContainerWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Toolbars.IAccessContainerWindow.html) provides a way for toolbar elements to access the `EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)` in which they exist.
    // Here we use `containerWindow` to focus the camera on our newly instantiated objects after creation.
    public EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) containerWindow { get; set; }

    // As this is ultimately just a VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html), it is appropriate to place initialization logic in the constructor.
    // In this method you can also register to any additional events as required. Here we will just set up the basics:
    // a tooltip, icon, and action.
    public CreateCubes()
    {
        // A toolbar element can be either text, icon, or a combination of the two. Keep in mind that if a toolbar is
        // docked horizontally the text will be clipped, so usually it's a good idea to specify an icon.
        text = "Create Cubes";
        icon = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)>("Assets/CreateCubesIcon.png");

        tooltip = "Instantiate some cubes in the scene.";
        clicked += OnClick;
    }

    // This method will be invoked when the `CreateCubes` button is clicked.
    void OnClick()
    {
        var parent = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Cubes").transform;

        // When writing editor tools don't forget to be a good citizen and implement Undo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.html)!
        Undo.RegisterCreatedObjectUndo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RegisterCreatedObjectUndo.html)(parent.gameObject, "Create Cubes in Sphere");

        for (int i = 0; i < 50; i++)
        {
            var cube = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html)).transform;

            Undo.RegisterCreatedObjectUndo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RegisterCreatedObjectUndo.html)(cube.gameObject, "Create Cubes in Sphere");
            cube.position = Random.insideUnitSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-insideUnitSphere.html) * 25;
            cube.rotation = Quaternion.LookRotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.LookRotation.html)(Random.onUnitSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-onUnitSphere.html));

            Undo.SetTransformParent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.SetTransformParent.html)(cube, parent, "Create Cubes in Sphere");
            cube.SetParent(parent);
        }

        Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html) = parent;

        if (containerWindow is SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) view)
            view.FrameSelected();
    }
}

// Same as above, except this time we'll create a toggle + dropdown toolbar item.
[EditorToolbarElement(id, typeof(SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html)))]
class DropdownToggleExample : EditorToolbarDropdownToggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Toolbars.EditorToolbarDropdownToggle.html), IAccessContainerWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Toolbars.IAccessContainerWindow.html)
{
    public const string id = "ExampleToolbar/DropdownToggle";

    // This property is specified by IAccessContainerWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Toolbars.IAccessContainerWindow.html) and is used to access the Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html)'s EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html).
    public EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) containerWindow { get; set; }
    static int colorIndex = 0;
    static readonly Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[] colors = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[] { Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html), Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html), Color.cyan[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-cyan.html) };

    DropdownToggleExample()
    {
        text = "Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) Bar";
        tooltip = "Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) a color swatch in the top left of the scene view. Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) on or off, and open the dropdown" +
            "to change the color.";

        // When the dropdown is opened, ShowColorMenu is invoked and we can create a popup menu.
        dropdownClicked += ShowColorMenu;

        // Subscribe to the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) View OnGUI callback so that we can draw our color swatch.
        SceneView.duringSceneGui[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-duringSceneGui.html) += DrawColorSwatch;
    }

    void DrawColorSwatch(SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) view)
    {
        // Test that this callback is for the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) View that we're interested in, and also check if the toggle is on
        // or off (value).
        if (view != containerWindow || !value)
            return;

        Handles.BeginGUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.BeginGUI.html)();
        GUI.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html) = colors[colorIndex];
        GUI.DrawTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DrawTexture.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(8, 8, 120, 24), Texture2D.whiteTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-whiteTexture.html));
        GUI.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-color.html) = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);
        Handles.EndGUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.EndGUI.html)();
    }

    // When the dropdown button is clicked, this method will create a popup menu at the mouse cursor position.
    void ShowColorMenu()
    {
        var menu = new GenericMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html)();
        menu.AddItem(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Red"), colorIndex == 0, () => colorIndex = 0);
        menu.AddItem(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Green"), colorIndex == 1, () => colorIndex = 1);
        menu.AddItem(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Blue"), colorIndex == 2, () => colorIndex = 2);
        menu.ShowAsContext();
    }
}

// All Overlays must be tagged with the OverlayAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayAttribute.html)
[Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html)(typeof(SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html)), "Placement Tools[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tools.html)")]
// IconAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IconAttribute.html) provides a way to define an icon for when an Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) is in collapsed form. If not provided, the first
// two letters of the Overlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) name will be used.
[Icon("Assets/PlacementToolsIcon.png")]
// Toolbar[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toolbar.html) overlays must inherit `ToolbarOverlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ToolbarOverlay.html)` and implement a parameter-less constructor. The contents of a toolbar
// are populated with string IDs, which are passed to the base constructor. IDs are defined by
// EditorToolbarElementAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Toolbars.EditorToolbarElementAttribute.html).
public class EditorToolbarExample : ToolbarOverlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ToolbarOverlay.html)
{
    // ToolbarOverlay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ToolbarOverlay.html) implements a parameterless constructor, passing 2 EditorToolbarElementAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Toolbars.EditorToolbarElementAttribute.html) IDs. This will
    // create a toolbar overlay with buttons for the CreateCubes and DropdownToggleExample examples.
    // This is the only code required to implement a toolbar overlay. Unlike panel overlays, the contents are defined
    // as standalone pieces that will be collected to form a strip of elements.
    EditorToolbarExample() : base(
        CreateCubes.id,
        DropdownToggleExample.id)
    {}
}

```

### Properties
Property | Description  
---|---  
[toolbarElements](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ToolbarOverlay-toolbarElements.html) | Use toolbarElements to specify the contents of this Overlay.  
### Public Methods
Method | Description  
---|---  
[CreatePanelContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ToolbarOverlay.CreatePanelContent.html) | Creates the root VisualElement of the ToolbarOverlay's content in panel layout.  
### Inherited Members
### Static Properties
Property | Description  
---|---  
[ussClassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-ussClassName.html) | USS class name of elements of this type.  
### Properties
Property | Description  
---|---  
[collapsed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-collapsed.html) | Defines whether the overlay is in collapsed form.  
[collapsedIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-collapsedIcon.html) | Defines a custom icon to use when that overlay is in collapsed form.  
[containerWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-containerWindow.html) | EditorWindow the overlay is contained within.  
[defaultSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-defaultSize.html) | Set defaultSize to define the size of an Overlay when it hasn't been resized by the user.  
[displayed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-displayed.html) | Shows or hides the overlay.  
[displayName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-displayName.html) | Name of overlay used as title.  
[floating](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-floating.html) | Returns true if overlay is floating, returns false if overlay is docked in a corner or in a toolbar.  
[floatingPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-floatingPosition.html) | Local position of closest overlay corner to closest dockposition when floating.  
[id](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-id.html) | Overlay unique ID.  
[isInToolbar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-isInToolbar.html) | Returns true if overlay is docked in a toolbar.  
[layout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-layout.html) | The preferred layout for the Overlay.  
[maxSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-maxSize.html) | Maximum size of the Overlay.  
[minSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-minSize.html) | Minimum size of the Overlay.  
[rootVisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-rootVisualElement.html) | The root VisualElement.  
[size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-size.html) | Size of the Overlay.  
### Public Methods
Method | Description  
---|---  
[Close](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.Close.html) | Remove the Overlay from its OverlayCanvas.  
[CreateContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.CreateContent.html) | Creates a new VisualElement containing the contents of this Overlay.  
[OnCreated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.OnCreated.html) | OnCreated is invoked when an Overlay is instantiated in an Overlay Canvas.  
[OnWillBeDestroyed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.OnWillBeDestroyed.html) | Called when an Overlay is about to be destroyed.  
[RefreshPopup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.RefreshPopup.html) | Resize the OverlayPopup to fit the content.  
[Undock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.Undock.html) | If this Overlay is currently in a toolbar, it will be removed and return to a floating state.  
### Events
Event | Description  
---|---  
[collapsedChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-collapsedChanged.html) | Invoked when Overlay.collapsed value is changed.  
[displayedChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-displayedChanged.html) | This callback is invoked when the Overlay.displayed value has been changed.  
[floatingChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-floatingChanged.html) | Called when the value of floating has changed.  
[floatingPositionChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-floatingPositionChanged.html) | This event is invoked when Overlay.floatingPosition is changed.  
[layoutChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay-layoutChanged.html) | Subscribe to this event to be notified when the Overlay.Layout property is modified.  
* * *
