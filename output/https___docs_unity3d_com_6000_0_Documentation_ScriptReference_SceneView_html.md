* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html

# SceneView
class in UnityEditor
/
Inherits from:[EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
Leave feedback
  

Implements interfaces:[IHasCustomMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IHasCustomMenu.html), [ISupportsOverlays](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ISupportsOverlays.html)
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
Use this class to manage [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) settings, change the [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) camera properties, subscribe to events, call [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) methods, and render open scenes.
### Static Properties
Property | Description  
---|---  
[currentDrawingSceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-currentDrawingSceneView.html) | The SceneView that is being drawn.  
[lastActiveSceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-lastActiveSceneView.html) | The SceneView that was most recently in focus.  
[lastActiveSceneViewChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-lastActiveSceneViewChanged.html) | Register to this callback to get notified when the active Scene View changes.  
[sceneViews](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-sceneViews.html) | The list of all open Scene view windows.  
[selectedOutlineColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-selectedOutlineColor.html) | Gets the Color of selected outline.  
### Properties
Property | Description  
---|---  
[audioPlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-audioPlay.html) | Enables or disables Scene view audio effects.  
[camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-camera.html) | The Camera that is rendering this SceneView.  
[cameraDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-cameraDistance.html) | The distance from camera to pivot.  
[cameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-cameraMode.html) | The current DrawCameraMode for the Scene view camera.  
[cameraSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-cameraSettings.html) | Use CameraSettings to set the properties for the SceneView Camera.  
[cameraViewport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-cameraViewport.html) | The position and size of the area that the camera renders.  
[drawGizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-drawGizmos.html) | Sets the visibility of all Gizmos in the Scene view.  
[in2DMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-in2DMode.html) | Whether the SceneView is in 2D mode.  
[isRotationLocked](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-isRotationLocked.html) | Whether the Scene view camera can be rotated.  
[isUsingSceneFiltering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-isUsingSceneFiltering.html) | Whether this SceneView is using scene filtering.  
[lastSceneViewRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-lastSceneViewRotation.html) | When the Scene view is in 2D mode, this property contains the last camera rotation.  
[orthographic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-orthographic.html) | Whether the Scene view camera is set to orthographic mode.  
[pivot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-pivot.html) | The central point that the camera orbits within the Scene view.  
[rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-rotation.html) | The direction of the camera to the pivot of the SceneView.  
[sceneLighting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-sceneLighting.html) | Whether lighting is enabled or disabled in the Scene view.  
[sceneViewState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-sceneViewState.html) | Use SceneViewState to set the debug options for the Scene view.  
[showGrid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-showGrid.html) | Gets or sets whether to enable the grid for an instance of the SceneView.  
[size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-size.html) | The size of the Scene view measured diagonally.  
[validateTrueMetals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-validateTrueMetals.html) | Whether the albedo is black for materials with an average specular color above 0.45.  
### Public Methods
Method | Description  
---|---  
[AlignViewToObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.AlignViewToObject.html) | Moves the Scene view to frame a transform.  
[AlignWithView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.AlignWithView.html) | Aligns the current selection with the position and rotation of the Scene view camera.  
[Frame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.Frame.html) | Frames the given bounds in the Scene view.  
[FrameSelected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.FrameSelected.html) | Frame the object selection in the Scene view.  
[IsCameraDrawModeEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.IsCameraDrawModeEnabled.html) | Returns true if mode is enabled in the current rendering setup, including custom validators.  
[IsCameraDrawModeSupported](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.IsCameraDrawModeSupported.html) | Checks if the current rendering configuration supports the CameraMode. The check includes custom validators.  
[LookAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.LookAt.html) | Moves the Scene view to focus on a target.  
[LookAtDirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.LookAtDirect.html) |  LookAt without animating the scene movement.  
[MoveToView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.MoveToView.html) | Transforms all selected object to the scene pivot.  
[ResetCameraSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.ResetCameraSettings.html) | Resets the CameraSettings for the SceneView Camera to default.  
[SetSceneViewShaderReplace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.SetSceneViewShaderReplace.html) | Sets a replacement shader for rendering this Scene view.  
### Protected Methods
Method | Description  
---|---  
[SupportsStageHandling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.SupportsStageHandling.html) | Override this method to control whether the Scene view should change when you switch from one stage to another stage.  
### Static Methods
Method | Description  
---|---  
[AddCameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.AddCameraMode.html) | Add a custom camera mode to the Scene view camera mode list.  
[AddOverlayToActiveView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.AddOverlayToActiveView.html) | Add an Overlay to be displayed in the last focused Scene View. Overlays added to this static list will be automatically moved to the last active Scene View, and are displayed until removed.  
[ClearUserDefinedCameraModes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.ClearUserDefinedCameraModes.html) | Remove all user-defined camera modes.  
[FrameLastActiveSceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.FrameLastActiveSceneView.html) | Frames the currently selected object(s) in the last active Scene view.  
[GetAllSceneCameras](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.GetAllSceneCameras.html) | Retrieves an array of all camera components from all open Scene views.  
[GetBuiltinCameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.GetBuiltinCameraMode.html) | Gets the built-in CameraMode that matches the specified DrawCameraMode.  
[RemoveOverlayFromActiveView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.RemoveOverlayFromActiveView.html) | Remove an Overlay from displaying in the last focused Scene View.  
[RepaintAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.RepaintAll.html) | Repaints every open SceneView.  
### Events
Event | Description  
---|---  
[beforeSceneGui](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-beforeSceneGui.html) | The event issued when the OnGUI method is called.  
[duringSceneGui](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-duringSceneGui.html) | Subscribe to this event to receive a callback whenever the Scene view calls the OnGUI method.  
[gridVisibilityChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-gridVisibilityChanged.html) | Invoked when grid visibility changes.  
[onCameraModeChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-onCameraModeChanged.html) | An event that is invoked when the selected cameraMode changes.  
[onValidateCameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-onValidateCameraMode.html) | A multicast delegate for custom render pipelines to specify support for a requested CameraMode.  
### Inherited Members
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
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
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
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
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
[Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Awake.html) | Called when an instance of ScriptableObject is created.  
[OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDestroy.html) | This function is called when the scriptable object will be destroyed.  
[OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDisable.html) | This function is called when the scriptable object goes out of scope.  
[OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnEnable.html) | This function is called when the object is loaded.  
[OnValidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnValidate.html) | Editor-only function that Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Reset.html) | Reset to default values.  
### Events
Event | Description  
---|---  
[windowFocusChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-windowFocusChanged.html) | Called whenever the focused editor window is changed.  
* * *
