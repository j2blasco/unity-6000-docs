* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html

# EditorApplication
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
Main Application class.
### Static Properties
Property | Description  
---|---  
[applicationContentsPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-applicationContentsPath.html) | Path to the Unity editor contents folder. (Read Only)  
[applicationPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-applicationPath.html) | Gets the path to the Unity Editor application. (Read Only)  
[contextualPropertyMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-contextualPropertyMenu.html) | Callback raised whenever the user context-clicks on a property in an Inspector.  
[delayCall](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-delayCall.html) | Delegate which is called once after all inspectors update.  
[hierarchyWindowItemOnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-hierarchyWindowItemOnGUI.html) | Delegate for OnGUI events for every visible list item in the HierarchyWindow.  
[isCompiling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isCompiling.html) | Is editor currently compiling scripts? (Read Only)  
[isCreateFromTemplate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isCreateFromTemplate.html) | Returns true if the current project was created from a template project.  
[isFocused](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isFocused.html) | Whether the Editor is the focused window of the operating system. (Read Only)  
[isPaused](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isPaused.html) | Whether the Editor is paused.  
[isPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isPlaying.html) | Whether the Editor is in Play mode.  
[isPlayingOrWillChangePlaymode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isPlayingOrWillChangePlaymode.html) | Editor application state which is true only when the Editor is currently in or about to enter Play mode. (Read Only)  
[isRemoteConnected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isRemoteConnected.html) | Is editor currently connected to Unity Remote 4 client app.  
[isTemporaryProject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isTemporaryProject.html) | Returns true if the current project was created as a temporary project.  
[isUpdating](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-isUpdating.html) | True if the Editor is currently refreshing the AssetDatabase.  
[modifierKeysChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-modifierKeysChanged.html) | Delegate for changed keyboard modifier keys.  
[projectWindowItemInstanceOnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-projectWindowItemInstanceOnGUI.html) | Delegate for OnGUI events for every visible list item in the ProjectWindow.  
[projectWindowItemOnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-projectWindowItemOnGUI.html) | Delegate for OnGUI events for every visible list item in the ProjectWindow.  
[searchChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-searchChanged.html) | Callback raised whenever the contents of a window's search box are changed.  
[timeSinceStartup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-timeSinceStartup.html) | The time since the editor was started. (Read Only)  
[update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-update.html) | Delegate for generic updates.  
### Static Methods
Method | Description  
---|---  
[Beep](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.Beep.html) | Plays system beep sound.  
[DirtyHierarchyWindowSorting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.DirtyHierarchyWindowSorting.html) | Set the hierarchy sorting method as dirty.  
[EnterPlaymode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.EnterPlaymode.html) | Switches the editor to Play mode.  
[ExecuteMenuItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.ExecuteMenuItem.html) | Invokes the menu item in the specified path.  
[Exit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.Exit.html) | Exit the Unity editor application.  
[ExitPlaymode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.ExitPlaymode.html) | Switches the editor to Edit mode.  
[LockReloadAssemblies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.LockReloadAssemblies.html) | Prevents loading of assemblies when it is inconvenient.  
[OpenProject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.OpenProject.html) | Open another project.  
[QueuePlayerLoopUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.QueuePlayerLoopUpdate.html) | Normally, a player loop update will occur in the editor when the Scene has been modified. This method allows you to queue a player loop update regardless of whether the Scene has been modified.  
[RepaintHierarchyWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.RepaintHierarchyWindow.html) | Can be used to ensure repaint of the HierarchyWindow.  
[RepaintProjectWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.RepaintProjectWindow.html) | Can be used to ensure repaint of the ProjectWindow.  
[SetTemporaryProjectKeepPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.SetTemporaryProjectKeepPath.html) | Sets the path that Unity should store the current temporary project at, when the project is closed.  
[Step](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.Step.html) | Perform a single frame step.  
[UnlockReloadAssemblies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.UnlockReloadAssemblies.html) | Must be called after LockReloadAssemblies, to reenable loading of assemblies.  
[UpdateMainWindowTitle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.UpdateMainWindowTitle.html) | Force Unity Editor to update its window title. This function is automatically called when a new scene is loaded or when the editor starts. A user having register a callback on EditorApplication.updateMainWindowTitle can call this function to force an update of the title.  
### Events
Event | Description  
---|---  
[focusChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-focusChanged.html) | Raises when the Editor gets or loses focus in the operating system.  
[hierarchyChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-hierarchyChanged.html) | Event that is raised when an object or group of objects in the hierarchy changes.  
[pauseStateChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-pauseStateChanged.html) | Event that is raised whenever the Editor's pause state changes.  
[playModeStateChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-playModeStateChanged.html) | Event that is raised whenever the Editor's play mode state changes.  
[projectChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-projectChanged.html) | Event that is raised whenever the state of the project changes.  
[quitting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-quitting.html) | Unity raises this event when the editor application is quitting.  
[updateMainWindowTitle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-updateMainWindowTitle.html) | Register a custom callback to specify how the Unity Editor title can be generated. Unity will trigger this callback when a new scene is loaded , when Unity starts or when EditorApplication.UpdateMainWindowTitle is called.  
[wantsToQuit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-wantsToQuit.html) | Unity raises this event when the editor application wants to quit.  
### Delegates
Delegate | Description  
---|---  
[CallbackFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.CallbackFunction.html) | Delegate to be called from EditorApplication callbacks.  
[HierarchyWindowItemCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.HierarchyWindowItemCallback.html) | Delegate to be called for every visible list item in the HierarchyWindow on every OnGUI event.  
[ProjectWindowItemCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.ProjectWindowItemCallback.html) | Delegate to be called for every visible list item in the ProjectWindow on every OnGUI event. Use this if you if you want to extend the functionality of the Project window. For example, to display information or tools relating to the assets that are visible.  
[ProjectWindowItemInstanceCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.ProjectWindowItemInstanceCallback.html) | Delegate to be called for every visible list item in the ProjectWindow on every OnGUI event. Use this if you if you want to extend the functionality of the Project window. For example, to display information or tools relating to the assets or sub-assets that are visible.  
[SerializedPropertyCallbackFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.SerializedPropertyCallbackFunction.html) | Delegate to be called from EditorApplication contextual inspector callbacks.  
* * *
