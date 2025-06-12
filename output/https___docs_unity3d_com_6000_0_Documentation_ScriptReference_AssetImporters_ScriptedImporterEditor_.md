* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporterEditor.html

# ScriptedImporterEditor
class in UnityEditor.AssetImporters
/
Inherits from:[AssetImporters.AssetImporterEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.html)
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
Default editor for source assets handled by Scripted Importers.
See [ScriptedImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html) and [AssetImporterEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.html).
### Inherited Members
### Properties
Property | Description  
---|---  
[extraDataSerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor-extraDataSerializedObject.html) | A SerializedObject that represents the extraDataTarget or the extraDataTargets of the AssetImporterEditor.  
[extraDataTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor-extraDataTarget.html) | The extra data object associated with the Editor.target.  
[extraDataTargets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor-extraDataTargets.html) | An array of objects associated with each Editor.targets.  
[extraDataType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor-extraDataType.html) | Override this property to return a type that inherits from ScriptableObject. This makes the AssetImporterEditor aware of serialized data outside of the Importer.  
[needsApplyRevert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor-needsApplyRevert.html) | Whether the ApplyRevertGUI method is required to draw in the Inspector.  
[showImportedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor-showImportedObject.html) | Should imported object be shown as a separate editor?  
[useAssetDrawPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor-useAssetDrawPreview.html) | Determines if the asset preview is handled by the AssetEditor or the Importer DrawPreview  
[hasUnsavedChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-hasUnsavedChanges.html) | This property specifies whether the Editor prompts the user to save or discard unsaved changes before the Inspector gets rebuilt.  
[saveChangesMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-saveChangesMessage.html) | The message that displays to the user if they are prompted to save.  
[serializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-serializedObject.html) | A SerializedObject representing the object or objects being inspected.  
[target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-target.html) | The object being inspected.  
[targets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-targets.html) | An array of all the object being inspected.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[HasModified](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.HasModified.html) | Determine if the import settings have been modified.  
[OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.OnDisable.html) | This function is called when the editor object goes out of scope.  
[OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.OnEnable.html) | This function is called when the object is loaded.  
[OnInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.OnInspectorGUI.html) | Override this method to create your own Inpsector GUI for a ScriptedImporter.  
[CreateInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateInspectorGUI.html) | Implement this method to make a custom UIElements inspector.  
[CreatePreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreatePreview.html) | Implement this method to make a custom UIElements inspector preview.  
[DiscardChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.DiscardChanges.html) | Discards unsaved changes to the contents of the editor.  
[DrawDefaultInspector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.DrawDefaultInspector.html) | Draws the built-in Inspector.  
[DrawHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.DrawHeader.html) | Call this function to draw the header of the editor.  
[DrawPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.DrawPreview.html) | The first entry point for Preview Drawing.  
[GetInfoString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.GetInfoString.html) | Implement this method to show asset information on top of the asset preview.  
[GetPreviewTitle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.GetPreviewTitle.html) | Override this method if you want to change the label of the Preview area.  
[HasPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.HasPreviewGUI.html) | Override this method in subclasses if you implement OnPreviewGUI.  
[OnInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInspectorGUI.html) | Implement this function to make a custom inspector.  
[OnInteractivePreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInteractivePreviewGUI.html) | Implement to create your own interactive custom preview. Interactive custom previews are used in the preview area of the inspector and the object selector.  
[OnPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnPreviewGUI.html) | Creates a custom preview for the preview area of the Inspector, the headers of the primary Editor, and the object selector.You must implement Editor.HasPreviewGUI for this method to be called.  
[OnPreviewSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnPreviewSettings.html) | Override this method if you want to show custom controls in the preview header.  
[RenderStaticPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.RenderStaticPreview.html) | Override this method if you want to render a static preview.  
[Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.Repaint.html) | Redraw any inspectors that shows this editor.  
[RequiresConstantRepaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.RequiresConstantRepaint.html) | Checks if this editor requires constant repaints in its current state.  
[SaveChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.SaveChanges.html) | Performs a save action on the contents of the editor.  
[UseDefaultMargins](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.UseDefaultMargins.html) | Override this method in subclasses to return false if you don't want default margins.  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Protected Methods
Method | Description  
---|---  
[Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.Apply.html) | Saves any changes from the Editor's control into the asset's import settings object.  
[ApplyButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.ApplyButton.html) | Implements the 'Apply' button of the inspector.  
[ApplyRevertGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.ApplyRevertGUI.html) | Add's the 'Apply' and 'Revert' buttons to the editor.  
[Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.Awake.html) | This function is called when the Editor script is started.  
[CanApply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.CanApply.html) | Determines if the modifications to import settings can be applied.  
[InitializeExtraDataInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.InitializeExtraDataInstance.html) | This method is called during the initialization process of the Editor, after Awake and before OnEnable.  
[OnApplyRevertGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.OnApplyRevertGUI.html) | Process the 'Apply' and 'Revert' buttons.  
[RevertButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.RevertButton.html) | Implements the 'Revert' button of the inspector.  
[ShouldHideOpenButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.ShouldHideOpenButton.html) | Returns the visibility setting of the "open" button in the Inspector.  
### Static Methods
Method | Description  
---|---  
[CreateCachedEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateCachedEditor.html) | On return previousEditor is an editor for targetObject or targetObjects. The function either returns if the editor is already tracking the objects, or destroys the previous editor and creates a new one.  
[CreateCachedEditorWithContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateCachedEditorWithContext.html) | Creates a cached editor using a context object.  
[CreateEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateEditor.html) | Make a custom editor for targetObject or targetObjects.  
[CreateEditorWithContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateEditorWithContext.html) | Make a custom editor for targetObject or targetObjects with a context object.  
[DrawFoldoutInspector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.DrawFoldoutInspector.html) | Draws the inspector GUI with a foldout header for target.  
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
[HasFrameBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.HasFrameBounds.html) | Validates whether custom bounds can be calculated for this Editor.  
[OnGetFrameBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnGetFrameBounds.html) | Gets custom bounds for the target of this editor.  
[OnSceneGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnSceneGUI.html) | Enables the Editor to handle an event in the Scene view.  
[Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Awake.html) | Called when an instance of ScriptableObject is created.  
[OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDestroy.html) | This function is called when the scriptable object will be destroyed.  
[OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDisable.html) | This function is called when the scriptable object goes out of scope.  
[OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnEnable.html) | This function is called when the object is loaded.  
[OnValidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnValidate.html) | Editor-only function that Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Reset.html) | Reset to default values.  
### Events
Event | Description  
---|---  
[finishedDefaultHeaderGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-finishedDefaultHeaderGUI.html) | An event raised while drawing the header of the Inspector window, after the default header items have been drawn.  
* * *
