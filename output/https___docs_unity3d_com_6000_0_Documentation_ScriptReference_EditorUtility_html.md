* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html

# EditorUtility
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
Editor utility functions.
### Static Properties
Property | Description  
---|---  
[scriptCompilationFailed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility-scriptCompilationFailed.html) | True if there are any compilation error messages in the log.  
### Static Methods
Method | Description  
---|---  
[ClearDefaultParentObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.ClearDefaultParentObject.html) | Clears the default parent GameObject from either a specific Scene or the active Scene.  
[ClearDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.ClearDirty.html) | Clear target's dirty flag.  
[ClearProgressBar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.ClearProgressBar.html) | Removes the progress bar.  
[CollectDeepHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CollectDeepHierarchy.html) | Collect all objects in the hierarchy rooted at each of the given objects.  
[CollectDependencies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CollectDependencies.html) | Calculates and returns a list of all assets the assets listed in roots depend on.  
[CompressCubemapTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CompressCubemapTexture.html) | Compress a cubemap texture.  
[CompressTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CompressTexture.html) | Compress a texture.  
[CopySerialized](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CopySerialized.html) | Copy all settings of a Unity Object.  
[CopySerializedIfDifferent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CopySerializedIfDifferent.html) | Copy all settings of a Unity Object to a second Object if they differ.  
[CopySerializedManagedFieldsOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CopySerializedManagedFieldsOnly.html) | Copies the serializable fields from one managed object to another.  
[CreateGameObjectWithHideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CreateGameObjectWithHideFlags.html) | Creates a game object with HideFlags and specified components.  
[DisplayCancelableProgressBar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayCancelableProgressBar.html) | Displays or updates a progress bar that has a cancel button.  
[DisplayDialog](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayDialog.html) | This method displays a modal dialog.  
[DisplayDialogComplex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayDialogComplex.html) | Displays a modal dialog with three buttons.  
[DisplayPopupMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayPopupMenu.html) | Displays a popup menu.  
[DisplayProgressBar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayProgressBar.html) | Displays or updates a progress bar.  
[FocusProjectWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.FocusProjectWindow.html) | Brings the project window to the front and focuses it.  
[FormatBytes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.FormatBytes.html) | Returns a text for a number of bytes.  
[GetDialogOptOutDecision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.GetDialogOptOutDecision.html) | This method displays a modal dialog that lets the user opt-out of being shown the current dialog box again.  
[GetDirtyCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.GetDirtyCount.html) | Returns an integer that indicates the number of times the specified object's serialized properties have changed.  
[GetObjectEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.GetObjectEnabled.html) | Is the object enabled (0 disabled, 1 enabled, -1 has no enabled button).  
[InstanceIDToObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html) | Translates an instance ID to a reference to an object.  
[IsDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.IsDirty.html) | Gets a boolean value that indicates whether the specified object has changed since the last time it was saved.  
[IsPersistent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.IsPersistent.html) | Determines if an object is stored on disk.  
[IsRunningUnderCPUEmulation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.IsRunningUnderCPUEmulation.html) | Gets a boolean value. This value indicates whether your CPU is unable to execute Unity natively and is running an emulated version.  
[IsUnityExtensionsInitialized](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.IsUnityExtensionsInitialized.html) | Returns a boolean value which represents the state of initialization of Unity extensions.  
[IsValidUnityYAML](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.IsValidUnityYAML.html) | Returns true if the provided string can be parsed as YAML.  
[NaturalCompare](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.NaturalCompare.html) | Human-like sorting.  
[OpenFilePanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.OpenFilePanel.html) | Displays the "open file" dialog and returns the selected path name.  
[OpenFilePanelWithFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.OpenFilePanelWithFilters.html) | Displays the "open file" dialog and returns the selected path name.  
[OpenFolderPanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.OpenFolderPanel.html) | Displays the "open folder" dialog and returns the selected path name.  
[OpenPropertyEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.OpenPropertyEditor.html) | Open properties editor for an Object.  
[RequestScriptReload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.RequestScriptReload.html) | The Unity Editor reloads script assemblies asynchronously on the next frame. This resets the state of all the scripts, but Unity does not compile any code that has changed since the previous compilation.  
[SaveFilePanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SaveFilePanel.html) | Displays the "save file" dialog and returns the selected path name.  
[SaveFilePanelInProject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SaveFilePanelInProject.html) | Displays the "save file" dialog in the Assets folder of the project and returns the selected path name.  
[SaveFolderPanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SaveFolderPanel.html) | Displays the "save folder" dialog and returns the selected path name.  
[SetCameraAnimateMaterials](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetCameraAnimateMaterials.html) | Sets this camera to allow animation of materials in the Editor.  
[SetCameraAnimateMaterialsTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetCameraAnimateMaterialsTime.html) | Sets the global time for this camera to use when rendering.  
[SetCustomDiffTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetCustomDiffTool.html) | Set custom diff tool settings.  
[SetDefaultParentObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetDefaultParentObject.html) | Sets the default parent object for the active Scene.  
[SetDialogOptOutDecision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetDialogOptOutDecision.html) | This method displays a modal dialog that lets the user opt-out of being shown the current dialog box again.  
[SetDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetDirty.html) | Marks target object as dirty.  
[SetObjectEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetObjectEnabled.html) | Set the enabled state of the object.  
[SetSelectedRenderState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetSelectedRenderState.html) | Set the Scene View selected display mode for this Renderer.  
[UnloadUnusedAssetsImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.UnloadUnusedAssetsImmediate.html) | Unloads assets that are not used.  
[UpdateGlobalShaderProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.UpdateGlobalShaderProperties.html) | Updates the global shader properties to use when rendering.  
* * *
