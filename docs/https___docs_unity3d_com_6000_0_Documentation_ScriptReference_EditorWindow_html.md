* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html

# EditorWindow
class in UnityEditor
/
Inherits from:[ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
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
Derive from this class to create a custom Editor window.
Use this class to create Editor windows that can either float independently or dock as tabs, similar to the default windows in the Unity Editor.  
  
You can use the [MenuItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html) attribute to configre an Editor windows to be opened in the Unity Editor menu.  
  
When creating a custom Editor window, follow these guidelines: 
  * Put code dependent on UXML/USS loading in the [CreateGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.CreateGUI.html) method to ensure that all necessary assets are available.
  * Keep the event registration code inside [CreateGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.CreateGUI.html) or after [CreateGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.CreateGUI.html) is called.


The following diagram shows the order of execution of an Editor window:  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/UIE-order-of-editor-window.png)
  * [OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnEnable.html): Called when the script is loaded or when the object is enabled.
  * [EditorApplication.isUpdating](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isUpdating.html): If true, the Editor is currently refreshing the [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).
  * [CreateGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.CreateGUI.html): Generates the graphical user interface if the Editor is not updating.
  * [Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.Update.html): Called once per frame to update the script's logic.
  * [OnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnGUI.html): Called multiple times per frame for rendering and handling GUI events.
  * [OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDisable.html): Called when the script is disabled or the object is destroyed to finalize and clean up resources.


For an example on how to create an Editor window that reacts to user input, refer to [Create a custom Editor window with C# script](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-HowTo-CreateEditorWindow.html). 
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEngine.UIElements;

public class MyEditorWindow : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/My Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Window")]
    public static void ShowExample()
    {
        MyEditorWindow wnd = GetWindow<MyEditorWindow>();
        wnd.titleContent = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("MyEditorWindow");
    }

    public void CreateGUI()
    {
        // Each editor window contains a root VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) object
        VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) root = rootVisualElement;

        // VisualElements objects can contain other VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) following a tree hierarchy
        Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) label = new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)("Hello World!");
        root.Add(label);

        // Create button
        Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) button = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)();
        button.name = "button";
        button.text = "Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)";
        root.Add(button);

        // Create toggle
        Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) toggle = new Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html)();
        toggle.name = "toggle";
        toggle.label = "Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html)";
        root.Add(toggle);
    }
}

```

### Static Properties
Property | Description  
---|---  
[focusedWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-focusedWindow.html) | The EditorWindow which currently has keyboard focus. (Read Only)  
[mouseOverWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-mouseOverWindow.html) | The EditorWindow currently under the mouse cursor. (Read Only)  
### Properties
Property | Description  
---|---  
[autoRepaintOnSceneChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-autoRepaintOnSceneChange.html) | Enable this property to automatically repaint the window when the SceneView is modified.  
[dataModeController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-dataModeController.html) | An instance of IDataModeController to handle DataMode functionalities for the current window.  
[docked](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-docked.html) | Returns true if EditorWindow is docked.  
[hasFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-hasFocus.html) | Returns true if EditorWindow is focused.  
[hasUnsavedChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-hasUnsavedChanges.html) | This property specifies whether the Editor prompts the user to save or discard unsaved changes before the window closes.  
[maximized](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-maximized.html) | Whether or not this window is maximized?  
[maxSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-maxSize.html) | The maximum size of this window when it is floating or modal. The maximum size is not used when the window is docked.  
[minSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-minSize.html) | The minimum size of this window when it is floating or modal. The minimum size is not used when the window is docked.  
[overlayCanvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-overlayCanvas.html) | The OverlayCanvas for this window.  
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-position.html) | The desired position of the window in screen space.  
[rootVisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-rootVisualElement.html) | Retrieves the root visual element of this window hierarchy.  
[saveChangesMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-saveChangesMessage.html) | The message that displays to the user if they are prompted to save  
[titleContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-titleContent.html) | The GUIContent used for drawing the title of EditorWindows.  
[wantsLessLayoutEvents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-wantsLessLayoutEvents.html) | Specifies whether a layout pass is performed before all user events (for example, EventType.MouseDown or EventType.KeyDown), or is only performed before repaint events.  
[wantsMouseEnterLeaveWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-wantsMouseEnterLeaveWindow.html) | Checks whether MouseEnterWindow and MouseLeaveWindow events are received in the GUI in this Editor window.  
[wantsMouseMove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-wantsMouseMove.html) | Checks whether MouseMove events are received in the GUI in this Editor window.  
### Public Methods
Method | Description  
---|---  
[BeginWindows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.BeginWindows.html) | Mark the beginning area of all popup windows.  
[Close](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.Close.html) | Close the editor window.  
[DiscardChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.DiscardChanges.html) | Discards unsaved changes to the contents of the window.  
[EndWindows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.EndWindows.html) | Close a window group started with EditorWindow.BeginWindows.  
[Focus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.Focus.html) | Moves keyboard focus to another EditorWindow.  
[GetExtraPaneTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetExtraPaneTypes.html) | Gets the extra panes associated with the window.  
[RemoveNotification](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.RemoveNotification.html) | Stop showing notification message.  
[Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.Repaint.html) | Make the window repaint.  
[SaveChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.SaveChanges.html) | Performs a save action on the contents of the window.  
[SendEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.SendEvent.html) | Sends an Event to a window.  
[Show](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.Show.html) | Show the EditorWindow window.  
[ShowAsDropDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.ShowAsDropDown.html) | Shows a window with dropdown behaviour and styling.  
[ShowAuxWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.ShowAuxWindow.html) | Show the editor window in the auxiliary window.  
[ShowModal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.ShowModal.html) | Show modal editor window.  
[ShowModalUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.ShowModalUtility.html) | Shows the EditorWindow as a floating modal window.  
[ShowNotification](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.ShowNotification.html) | Show a notification message.  
[ShowPopup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.ShowPopup.html) | Shows an Editor window using popup-style framing.  
[ShowTab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.ShowTab.html) | Shows a docked Editor window.  
[ShowUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.ShowUtility.html) | Show the EditorWindow as a floating utility window.  
[TryGetOverlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.TryGetOverlay.html) | Get an Overlay with matching ID from an EditorWindow canvas.  
### Protected Methods
Method | Description  
---|---  
[OnBackingScaleFactorChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnBackingScaleFactorChanged.html) | Called when the UI scaling for this EditorWindow is changed.  
### Static Methods
Method | Description  
---|---  
[CreateWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.CreateWindow.html) | Creates an EditorWindow of type T.  
[FocusWindowIfItsOpen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.FocusWindowIfItsOpen.html) | Focuses the first found EditorWindow of specified type if it is open.  
[GetWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html) | Returns the first EditorWindow of type windowType which is currently on the screen.  
[GetWindowWithRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindowWithRect.html) | Returns the first EditorWindow of type t which is currently on the screen.  
[HasOpenInstances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.HasOpenInstances.html) | Checks if an editor window is open.  
### Messages
Message | Description  
---|---  
[Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.Awake.html) | Called as the new window is opened.  
[CreateGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.CreateGUI.html) |  CreateGUI is called when the EditorWindow's rootVisualElement is ready to be populated.  
[hasUnsavedChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-hasUnsavedChanges.html) | This property specifies whether the Editor prompts the user to save or discard unsaved changes before the window closes.  
[OnBecameInvisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnBecameInvisible.html) | Called after the window is removed from a container view, or is no longer visible within a tabbed collection of EditorWindow.  
[OnBecameVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnBecameVisible.html) | Called after the window is added to a container view.  
[OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnDestroy.html) | OnDestroy is called to close the EditorWindow window.  
[OnFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnFocus.html) | Called when the window gets keyboard focus.  
[OnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnGUI.html) | Implement your own editor GUI here.  
[OnHierarchyChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnHierarchyChange.html) | Handler for message that is sent when an object or group of objects in the hierarchy changes.  
[OnInspectorUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnInspectorUpdate.html) | OnInspectorUpdate is called at 10 frames per second to give the inspector a chance to update.  
[OnLostFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnLostFocus.html) | Called when the window loses keyboard focus.  
[OnProjectChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnProjectChange.html) | Handler for message that is sent whenever the state of the project changes.  
[OnSelectionChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.OnSelectionChange.html) | Called whenever the selection has changed.  
[saveChangesMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-saveChangesMessage.html) | The message that displays to the user if they are prompted to save  
[Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.Update.html) | Called multiple times per second on all visible windows.  
### Events
Event | Description  
---|---  
[windowFocusChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-windowFocusChanged.html) | Called whenever the focused editor window is changed.  
### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
[CreateInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html) | Creates an instance of a scriptable object.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
### Messages
Message | Description  
---|---  
[Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Awake.html) | Called when an instance of ScriptableObject is created.  
[OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDisable.html) | This function is called when the scriptable object goes out of scope.  
[OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnEnable.html) | This function is called when the object is loaded.  
[OnValidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnValidate.html) | Editor-only function that Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Reset.html) | Reset to default values.  
* * *
