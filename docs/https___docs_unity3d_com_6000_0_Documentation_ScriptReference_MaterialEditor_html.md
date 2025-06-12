* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.html

# MaterialEditor
class in UnityEditor
/
Inherits from:[Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
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
The Unity Material Editor.
Extend this class to write your own custom material editor. For more detailed information see the [Custom Material Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-CustomEditor.html) section of the [ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html).
### Static Properties
Property | Description  
---|---  
[kMiniTextureFieldLabelIndentLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor-kMiniTextureFieldLabelIndentLevel.html) | Useful for indenting shader properties that need the same indent as mini texture field.  
### Properties
Property | Description  
---|---  
[customShaderGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor-customShaderGUI.html) | Returns the custom ShaderGUI implemented by the shader.  
[isVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor-isVisible.html) | Is the current material expanded.  
### Public Methods
Method | Description  
---|---  
[Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.Awake.html) | Called when the Editor is woken up.  
[BeginAnimatedCheck](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.BeginAnimatedCheck.html) | Creates a Property wrapper, useful for making regular GUI controls work with MaterialProperty.  
[ColorProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.ColorProperty.html) | Draw a property field for a color shader property.  
[CreatePreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.CreatePreview.html) | See Editor.CreatePreview.  
[DefaultPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.DefaultPreviewGUI.html) | Default handling of preview area for materials.  
[DefaultPreviewSettingsGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.DefaultPreviewSettingsGUI.html) | Default toolbar for material preview area.  
[DefaultShaderProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.DefaultShaderProperty.html) | Handles UI for one shader property ignoring any custom drawers.  
[DoubleSidedGIField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.DoubleSidedGIField.html) | Display UI for editing a material's Double Sided Global Illumination setting. Returns true if the UI is indeed displayed i.e. the material supports the Double Sided Global Illumination setting. +Additional resources: Material.doubleSidedGI.  
[EmissionEnabledProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.EmissionEnabledProperty.html) | This function will draw the UI for controlling whether emission is enabled or not on a material.  
[EnableInstancingField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.EnableInstancingField.html) | Display UI for editing material's render queue setting.  
[EndAnimatedCheck](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.EndAnimatedCheck.html) | Ends a Property wrapper started with BeginAnimatedCheck.  
[FloatProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.FloatProperty.html) | Draw a property field for a float shader property.  
[GetPropertyHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.GetPropertyHeight.html) | Calculate height needed for the property.  
[GetTexturePropertyCustomArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.GetTexturePropertyCustomArea.html) | Returns the free rect below the label and before the large thumb object field. Is used for e.g. tiling and offset properties.  
[HasPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.HasPreviewGUI.html) | Can this component be Previewed in its current state?  
[HelpBoxWithButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.HelpBoxWithButton.html) | Make a help box with a message and button. Returns true, if button was pressed.  
[IntegerProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.IntegerProperty.html) | Draw a property field for an integer shader property.  
[IsInstancingEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.IsInstancingEnabled.html) | Determines whether the Enable Instancing checkbox is checked.  
[LightmapEmissionFlagsProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.LightmapEmissionFlagsProperty.html) | Draws the UI for setting the global illumination flag of a material.  
[LightmapEmissionProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.LightmapEmissionProperty.html) | This function will draw the UI for the lightmap emission property. (None, Realtime, baked)Additional resources: MaterialLightmapFlags.  
[OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.OnDisable.html) | Called when the editor is disabled, if overridden please call the base OnDisable() to ensure that the material inspector is set up properly.  
[OnEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.OnEnable.html) | Called when the editor is enabled, if overridden please call the base OnEnable() to ensure that the material inspector is set up properly.  
[OnInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.OnInspectorGUI.html) | Implement specific MaterialEditor GUI code here. If you want to simply extend the existing editor call the base OnInspectorGUI () before doing any custom GUI code.  
[OnPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.OnPreviewGUI.html) | Custom preview for Image component.  
[PropertiesChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.PropertiesChanged.html) | Whenever a material property is changed call this function. This will rebuild the inspector and validate the properties.  
[PropertiesDefaultGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.PropertiesDefaultGUI.html) | Default rendering of shader properties.  
[PropertiesGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.PropertiesGUI.html) | Render the standard material properties. This method will either render properties using a ShaderGUI instance if found otherwise it uses PropertiesDefaultGUI.  
[RangeProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.RangeProperty.html) | Draw a range slider for a range shader property.  
[RegisterPropertyChangeUndo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.RegisterPropertyChangeUndo.html) | Call this when you change a material property. It will add an undo for the action.  
[RenderQueueField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.RenderQueueField.html) | Display UI for editing material's render queue setting.  
[RequiresConstantRepaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.RequiresConstantRepaint.html) | Does this edit require to be repainted constantly in its current state?  
[SetDefaultGUIWidths](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.SetDefaultGUIWidths.html) | Set EditorGUIUtility.fieldWidth and labelWidth to the default values that PropertiesGUI uses.  
[SetShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.SetShader.html) | Set the shader of the material.  
[ShaderProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.ShaderProperty.html) | Handes UI for one shader property.  
[TextureCompatibilityWarning](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.TextureCompatibilityWarning.html) | Checks if particular property has incorrect type of texture specified by the material, displays appropriate warning and suggests the user to automatically fix the problem.  
[TextureProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.TextureProperty.html) | Draw a property field for a texture shader property.  
[TexturePropertyMiniThumbnail](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.TexturePropertyMiniThumbnail.html) | Draw a property field for a texture shader property that only takes up a single line height.  
[TexturePropertySingleLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.TexturePropertySingleLine.html) | Method for showing a texture property control with additional inlined properites.  
[TexturePropertyTwoLines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.TexturePropertyTwoLines.html) | Method for showing a compact layout of properties.  
[TexturePropertyWithHDRColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.TexturePropertyWithHDRColor.html) | Method for showing a texture property control with a HDR color field and its color brightness float field.  
[TextureScaleOffsetProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.TextureScaleOffsetProperty.html) | Draws tiling and offset properties for a texture.  
[VectorProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.VectorProperty.html) | Draw a property field for a vector shader property.  
### Protected Methods
Method | Description  
---|---  
[OnShaderChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.OnShaderChanged.html) | A callback that is invoked when a Material's Shader is changed in the Inspector.  
### Static Methods
Method | Description  
---|---  
[ApplyMaterialPropertyDrawers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.ApplyMaterialPropertyDrawers.html) | Apply initial MaterialPropertyDrawer values.  
[BeginProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.BeginProperty.html) | Creates a wrapper enabling the Unity Editor to display GUI controls for the property.  
[EndProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.EndProperty.html) | Closes a property wrapper that begins with MaterialEditor.BeginProperty.  
[FixupEmissiveFlag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.FixupEmissiveFlag.html) | Returns a properly set global illlumination flag based on the passed in flag and the given color.  
[GetDefaultPropertyHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.GetDefaultPropertyHeight.html) | Calculate height needed for the property, ignoring custom drawers.  
[GetFlexibleRectBetweenFieldAndRightEdge](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.GetFlexibleRectBetweenFieldAndRightEdge.html) | Utility method for GUI layouting ShaderGUI. Used e.g for the rect after a left aligned Color field.  
[GetFlexibleRectBetweenLabelAndField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.GetFlexibleRectBetweenLabelAndField.html) | Utility method for GUI layouting ShaderGUI.  
[GetLeftAlignedFieldRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.GetLeftAlignedFieldRect.html) | Utility method for GUI layouting ShaderGUI.  
[GetMaterialProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.GetMaterialProperties.html) | Get shader property information of the materials you pass in.  
[GetMaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.GetMaterialProperty.html) | Get information about a single shader property.  
[GetMaterialPropertyNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.GetMaterialPropertyNames.html) | Gets the shader property names of the materials you pass in.  
[GetRectAfterLabelWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.GetRectAfterLabelWidth.html) | Utility method for GUI layouting ShaderGUI. This is the rect after the label which can be used for multiple properties. The input rect can be fetched by calling: EditorGUILayout.GetControlRect.  
[GetRightAlignedFieldRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.GetRightAlignedFieldRect.html) | Utility method for GUI layouting ShaderGUI.  
### Inherited Members
### Properties
Property | Description  
---|---  
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
[CreateInspectorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateInspectorGUI.html) | Implement this method to make a custom UIElements inspector.  
[DiscardChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.DiscardChanges.html) | Discards unsaved changes to the contents of the editor.  
[DrawDefaultInspector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.DrawDefaultInspector.html) | Draws the built-in Inspector.  
[DrawHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.DrawHeader.html) | Call this function to draw the header of the editor.  
[DrawPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.DrawPreview.html) | The first entry point for Preview Drawing.  
[GetInfoString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.GetInfoString.html) | Implement this method to show asset information on top of the asset preview.  
[GetPreviewTitle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.GetPreviewTitle.html) | Override this method if you want to change the label of the Preview area.  
[OnInteractivePreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnInteractivePreviewGUI.html) | Implement to create your own interactive custom preview. Interactive custom previews are used in the preview area of the inspector and the object selector.  
[OnPreviewSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnPreviewSettings.html) | Override this method if you want to show custom controls in the preview header.  
[RenderStaticPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.RenderStaticPreview.html) | Override this method if you want to render a static preview.  
[Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.Repaint.html) | Redraw any inspectors that shows this editor.  
[SaveChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.SaveChanges.html) | Performs a save action on the contents of the editor.  
[UseDefaultMargins](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.UseDefaultMargins.html) | Override this method in subclasses to return false if you don't want default margins.  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Protected Methods
Method | Description  
---|---  
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
[OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnDestroy.html) | This function is called when the scriptable object will be destroyed.  
[OnValidate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.OnValidate.html) | Editor-only function that Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.Reset.html) | Reset to default values.  
### Events
Event | Description  
---|---  
[finishedDefaultHeaderGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-finishedDefaultHeaderGUI.html) | An event raised while drawing the header of the Inspector window, after the default header items have been drawn.  
* * *
