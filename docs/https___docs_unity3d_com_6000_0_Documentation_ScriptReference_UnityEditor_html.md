* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html

# UnityEditor
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
The UnityEditor assembly implements the editor-specific APIs in Unity. It cannot be referenced by runtime code compiled into players.
### Classes
Class | Description  
---|---  
[AddAndRemoveRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.AddAndRemoveRequest.html) | Represents an asynchronous request to add package dependencies to the project and/or remove package dependencies from the project.  
[AddedComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.AddedComponent.html) | Class with information about a component that has been added to a Prefab instance.  
[AddedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.AddedGameObject.html) | Class with information about a GameObject that has been added as a child under a Prefab instance.  
[AddRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.AddRequest.html) | Represents an asynchronous request to add a package to the project.  
[AdvancedDropdown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdown.html) | Inherit from this class to implement your own drop-down control.  
[AdvancedDropdownItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdownItem.html) | Items that build the drop-down list.  
[AdvancedDropdownState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.AdvancedDropdownState.html) | The state of the drop-down. This Object can be serialized.  
[AdvancedObjectSelectorAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.AdvancedObjectSelectorAttribute.html) | This attribute lets you register a custom advanced object selector.  
[AdvancedObjectSelectorValidatorAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.AdvancedObjectSelectorValidatorAttribute.html) | This attribute lets you register a custom advanced object selector validator.  
[AdvertisementSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Advertisements.AdvertisementSettings.html) | Editor API for the Unity Services editor feature. Normally UnityAds is enabled from the Services window, but if writing your own editor extension, this API can be used.  
[AnalyticsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Analytics.AnalyticsSettings.html) | Editor API for the Unity Services editor feature. Normally Analytics is enabled from the Services window, but if writing your own editor extension, this API can be used.  
[AndroidAssetPackImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidAssetPackImporter.html) | Represents an Android asset pack directory in a project.  
[AnimationClipCurveData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClipCurveData.html) | An AnimationClipCurveData object contains all the information needed to identify a specific curve in an AnimationClip. The curve animates a specific property of a component / material attached to a game object / animated bone.  
[AnimationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationMode.html) |  AnimationMode is used by the AnimationWindow to store properties modified by the AnimationClip playback.  
[AnimationModeDriver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationModeDriver.html) |  AnimationMode uses AnimationModeDriver to identify the animation driver.  
[AnimationUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.html) | Editor utility functions for modifying animation clips.  
[AnimationWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationWindow.html) | Use the AnimationWindow class to select and edit Animation clips.  
[AnimatorController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorController.html) | The Animator Controller controls animation through layers with state machines, controlled by parameters.  
[AnimatorControllerLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerLayer.html) | The Animation Layer contains a state machine that controls animations of a model or part of it.  
[AnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorState.html) | States are the basic building blocks of a state machine. Each state contains a Motion ( AnimationClip or BlendTree) which will play while the character is in that state. When an event in the game triggers a state transition, the character will be left in a new state whose animation sequence will then take over.  
[AnimatorStateMachine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateMachine.html) | A graph controlling the interaction of states. Each state references a motion.  
[AnimatorStateTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorStateTransition.html) | Transitions define when and how the state machine switch from one state to another. AnimatorStateTransition always originate from an Animator State (or AnyState) and have timing parameters.  
[AnimatorTransition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorTransition.html) | Transitions define when and how the state machine switch from on state to another. AnimatorTransition always originate from a StateMachine or a StateMachine entry. They do not define timing parameters.  
[AnimatorTransitionBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorTransitionBase.html) | Base class for animator transitions. Transitions define when and how the state machine switches from one state to another.  
[AnimBool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.AnimBool.html) | Lerp from 0 - 1.  
[AnimFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.AnimFloat.html) | An animated float value.  
[AnimQuaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.AnimQuaternion.html) | An animated Quaternion value.  
[AnimVector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.AnimVector3.html) | An animated Vector3 value.  
[ApplicationTitleDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationTitleDescriptor.html) | Utility class containing all the information necessary to format Unity Editor main window title. All the various fields are concatenated to create a fully formed title. If only ApplicationTitleDescriptor.title is provided, this will become the complete title.  
[ApplyRulesIfGraphicsAPIAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.ApplyRulesIfGraphicsAPIAttribute.html) | Enable or disable shader keyword filter attributes based on the graphics API.  
[ApplyRulesIfNotGraphicsAPIAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.ApplyRulesIfNotGraphicsAPIAttribute.html) | Enable or disable shader keyword filter attributes based on the graphics API.  
[ApplyRulesIfTagsEqualAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.ApplyRulesIfTagsEqualAttribute.html) | Enable or disable shader keyword filter attributes based on shader tags.  
[ApplyRulesIfTagsNotEqualAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.ApplyRulesIfTagsNotEqualAttribute.html) | Enable or disable shader keyword filter attributes based on shader tags.  
[ArcHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.ArcHandle.html) | A class for a compound handle to edit an angle and a radius in the Scene view.  
[ArrayUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArrayUtility.html) | Helpers for builtin arrays.  
[Assembly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.Assembly.html) | Class that represents an assembly compiled by Unity.  
[AssemblyDefinitionException](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.AssemblyDefinitionException.html) | An exception throw for Assembly Definition Files errors.  
[AssemblyReloadEvents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssemblyReloadEvents.html) | This class has event dispatchers for assembly reload events.  
[Asset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) | This class containes information about the version control state of an asset.  
[AssetBundleInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.AssetBundleInfo.html) | Container for holding asset loading information for an AssetBundle to be built.  
[AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html) | An Interface for accessing assets and performing operations on assets.  
[AssetDatabaseLoadOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabaseLoadOperation.html) | This operation allows you to track the progress and access the result of an asynchronus AssetDatabase load operation.  
[AssetImportContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImportContext.html) | Defines the import context for scripted importers during an import event.  
[AssetImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.html) | Base class from which asset importers for specific asset types derive.  
[AssetImporterEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.html) | Default editor for all asset importer settings.  
[AssetList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.AssetList.html) | A list of version control information about assets.  
[AssetLoadInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.AssetLoadInfo.html) | Container for holding preload information for a given serialized Asset.  
[AssetModificationProcessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.html) | AssetModificationProcessor lets you hook into saving of serialized assets and scenes which are edited inside Unity.  
[AssetMonitoringUtilities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.AssetMonitoringUtilities.html) | Utility that manages asset monitoring features of UI Toolkit panels.  
[AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html) | AssetPostprocessor lets you hook into the import pipeline and run scripts prior or after importing assets.  
[AssetPostprocessorStaticVariableIgnoreAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessorStaticVariableIgnoreAttribute.html) | Allows you to decorate static variables in AssetPostprocessor and ScriptedImporter classes that should be ignored by the static variable warning system in the Import Activity window.This attribute is introduced to decorate static variables in PostProcessors and ScripttedImporters to prevent warnings about the usage of static variables. Though static variables in these classes can lead to subtle bugs when running on different Asset Import Workers as each worker has its own Mono Domain separate from the Main Editor, this attribute has been added to reduce the noise which could be generated in some difficult to fix situations involving static variables in said clasess.  
[AssetPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPreview.html) | Utility for fetching asset previews by instance ID of assets, See AssetPreview.GetAssetPreview. Since previews are loaded asynchronously methods are provided for requesting if all previews have been fully loaded, see AssetPreview.IsLoadingAssetPreviews. Loaded previews are stored in a cache, the size of the cache can be controlled by calling [AssetPreview.SetPreviewTextureCacheSize].  
[AssetSettingsProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.html) | AssetSettingsProvider is a specialization of the SettingsProvider class that converts legacy settings to Unified Settings. Legacy settings include any settings that used the Inspector to modify themselves, such as the *.asset files under the ProjectSettings folder. Under the hood, AssetSettingsProvider creates an Editor for specific Assets and builds the UI for the Settings window by wrapping the Editor.OnInspectorGUI function.Internally we use this class to wrap our existing settings.  
[Attacher](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Attacher.html) | Helper object that attaches a visual element next to its target, regarless of their respective location in the visual tree hierarchy.  
[AudioCurveRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioCurveRendering.html) | Antialiased curve rendering functionality used by audio tools in the editor.  
[AudioImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html) | Use this class to modify AudioClip import settings from editor scripts.  
[AuthorInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.AuthorInfo.html) | Identifies the author of a package.  
[BakeProgressState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BakeProgressState.html) | Interface for progress reporting.  
[BaseAnimValue<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.BaseAnimValue_1.html) | Abstract base class for Animated Values.  
[BaseAnimValueNonAlloc<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatedValues.BaseAnimValueNonAlloc_1.html) | Abstract base class that provides an allocation free version of BaseAnimValue.  
[BaseMaskField<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseMaskField_1.html) |  Base class implementing the shared functionality for editing bit mask values. For more information, refer to UXML element MaskField.   
[BindingExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BindingExtensions.html) |  Provides VisualElement extension methods that implement data binding between INotifyValueChanged fields and SerializedObjects.   
[Blackboard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Blackboard.html) | GraphElement that enables user to dynamically define members of a Graph (such as fields/properties) grouped by sections (BlackboardSection).  
[BlackboardField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.BlackboardField.html) | GraphElement that represents a field of a Graph.  
[BlackboardRow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.BlackboardRow.html) | Collapsible GraphElement that represents a row in a BlackboardSection.  
[BlackboardSection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.BlackboardSection.html) | GraphElement that represents a section of members in a Blackboard.  
[BlendTree](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTree.html) | Blend trees are used to blend continuously animation between their children. They can either be 1D or 2D.  
[BoxBoundsHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.BoxBoundsHandle.html) | A compound handle to edit a box-shaped bounding volume in the Scene view.  
[BrokenPrefabAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BrokenPrefabAsset.html) | BrokenPrefabAsset is for Prefab files where the file content cannot be loaded without errors.  
[BrushesOverlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.BrushesOverlay.html) | Contains functions that help display Terrain Tools overlays.  
[BuildCallbackVersionAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildCallbackVersionAttribute.html) | Attribute to provide a version number for IProcessSceneWithReport callbacks.  
[BuildFailedException](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildFailedException.html) | An exception class that represents a failed build.  
[BuildPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.html) | Lets you programmatically build players or AssetBundles which can be loaded from the web.  
[BuildPipelineContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildPipelineContext.html) | Defines the build context for IProcessSceneWithReport during a build event.  
[BuildPlayerContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildPlayerContext.html) | Get a BuildPlayerContext object from a BuildPlayerProcessor.PrepareForBuild callback.  
[BuildPlayerProcessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildPlayerProcessor.html) | Extend BuildPlayerProcessor to receive callbacks during a player build.  
[BuildPlayerWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerWindow.html) | The default build settings window.  
[BuildProfile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile.html) | Provides a set of configuration settings you can use to build your application on a particular platform.  
[BuildReferenceMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildReferenceMap.html) | Container for holding information about where objects will be serialized in a build.  
[BuildReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildReport.html) | The BuildReport API gives you information about the Unity build process.  
[BuildUsageCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildUsageCache.html) | Caching object for the Scriptable Build Pipeline.  
[BuildUsageTagSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildUsageTagSet.html) | Container for holding information about how objects are being used in a build.  
[BuildUtilities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.BuildUtilities.html) | Utility class that allows packages to register build callbacks with the Unity Package Manager.  
[CacheServer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServer.html) | This class provides an interface for performing operations on a cache server.  
[CallbackOrderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CallbackOrderAttribute.html) | Base class for Attributes that require a callback index.  
[CameraDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.CameraDescription.html) | Represents camera information from an imported file.  
[CameraEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.html) | Unity Camera Editor.  
[CameraEditorUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.html) | Utilities for cameras.  
[CanEditMultipleObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanEditMultipleObjects.html) | Attribute used to make a custom editor support multi-object editing.  
[CapsuleBoundsHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.CapsuleBoundsHandle.html) | A compound handle to edit a capsule-shaped bounding volume in the Scene view.  
[ChangeSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ChangeSet.html) | Wrapper around a changeset description and ID.  
[ChangeSets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ChangeSets.html) | A list of the ChangeSet class.  
[ChannelClient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelClient.html) | ChannelClient is a WebSocket client that connects to Unity's ChannelService, which is a WebSocket server.  
[ChannelService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.html) | The ChannelService encapsulates a WebSocket server running in Unity.  
[ClearCacheRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.ClearCacheRequest.html) | Represents an asynchronous request to clear the global package cache on the disk.  
[ClickSelector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ClickSelector.html) | Selects element on single click.  
[Client](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html) | Use the Unity Package Manager Client class to manage the packages used in a project.  
[ClipboardUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClipboardUtility.html) | A class containing methods to assist with clipboard operations.  
[CloudProjectSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CloudProjectSettings.html) | Use this class to retrieve information about the currently selected project and the current Unity ID that is logged in.  
[CloudProjectSettingsEventManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CloudProjectSettingsEventManager.html) | Manages the events related to the project state.  
[ClutchShortcutAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ClutchShortcutAttribute.html) | Registers a static method as the action for a clutch shortcut.  
[CodeEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.html) | Handles interaction with the code editor.  
[CollectImportedDependenciesAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.CollectImportedDependenciesAttribute.html) | Use this method attribute to specify which methods declare dependancies on imported assets. The methods are called by AssetDatabase during import.  
[ColorField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ColorField.html) |  Makes a field for selecting a color. For more information, refer to UXML element ColorField.   
[ColorPickerHDRConfig](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorPickerHDRConfig.html) | Used as input to ColorField to configure the HDR color ranges in the ColorPicker.  
[CommonRoles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.CommonRoles.html) | This class provides constant values for some of the common roles used by files in the build. The role of each file in the build is available in BuildFile.role.  
[CompilationPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilationPipeline.html) | Methods and properties for script compilation pipeline.  
[ComputeShaderImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShaderImporter.html) | Define compute shader import settings in the Unity Editor.  
[ConfigField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ConfigField.html) | Describes the configuration fields of the version control that the user has selected in the Unity Editor.  
[ConnectedPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.ConnectedPlayer.html) | Information of the connected player.  
[ConsoleWindowUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConsoleWindowUtility.html) | Console Window Utility class.  
[ContentBuildInterface](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildInterface.html) | Low level interface for building content for Unity.  
[ContentDragger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ContentDragger.html) | Manipulator that allows mouse-dragging of one or more elements.  
[ContentZoomer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ContentZoomer.html) | Manipulator that allows zooming in GraphView.  
[ContextMenuUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.ContextMenuUtility.html) | Provides methods to add menu items to the Scene view context menu.  
[ConvertToPrefabInstanceSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConvertToPrefabInstanceSettings.html) | Settings controlling the behavior of PrefabUtility.ConvertToPrefabInstance.  
[CoppaDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Connect.CoppaDrawer.html) | A container that fetches the UIElements that draw the COPPA compliance UI and subscribes to its events.  
[CrashReportingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CrashReporting.CrashReportingSettings.html) | Editor API for the Unity Services editor feature. Normally CrashReporting is enabled from the Services window, but if writing your own editor extension, this API can be used.  
[CurveField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CurveField.html) |  Makes a field for editing an AnimationCurve. For more information, refer to UXML element CurveField.   
[CustomEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html) | Tells an Editor class which run-time type it's an editor for.  
[CustomObjectIndexerAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.CustomObjectIndexerAttribute.html) | Allows a user to register a custom Indexing function for a specific type.  
[CustomPreviewAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomPreviewAttribute.html) | Adds an extra preview in the Inspector for the specified type.  
[CustomPropertyDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomPropertyDrawer.html) | Tells a custom PropertyDrawer or DecoratorDrawer which run-time Serializable class or PropertyAttribute it's a drawer for.  
[DecoratorDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DecoratorDrawer.html) | Base class to derive custom decorator drawers from.  
[DefaultAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DefaultAsset.html) | DefaultAsset is used for assets that do not have a specific type (yet).  
[DefaultLightingExplorerExtension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DefaultLightingExplorerExtension.html) | Default definition for the Lighting Explorer. Can be overridden completely or partially.  
[DependencyInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.DependencyInfo.html) | A descriptor that stores one of a template Scene's dependency Assets, and specifies whether to clone or reference it when the template is instantiated.  
[DetailBrushRepresentation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.DetailBrushRepresentation.html) |  Represents data associated with the brush used for scattering details.   
[DeviceSimulator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceSimulation.DeviceSimulator.html) | Class for interacting with a Device Simulator window from a script.  
[DeviceSimulatorPlugin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceSimulation.DeviceSimulatorPlugin.html) | Extend this class to create a Device Simulator plug-in.  
[DidReloadScripts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.DidReloadScripts.html) | Add this attribute to a method to get a notification after scripts have been reloaded.  
[DiffuseProfileCallbackAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTree.Importer.DiffuseProfileCallbackAttribute.html) |  This attribute is used as a callback to set SRP specific properties from the importer.   
[Dispatcher](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.Dispatcher.html) | The search dispatcher is used to synchronize events from the search provider threads and the main UI threads.  
[DragAndDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.html) | Editor drag & drop operations.  
[Dragger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Dragger.html) | Base manipulator for mouse-dragging elements.  
[DrawGizmo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawGizmo.html) | The DrawGizmo attribute allows you to supply a gizmo renderer for any Component.  
[Edge](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Edge.html) | The GraphView edge element.  
[EdgeConnector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.EdgeConnector.html) | Manipulator for creating new edges.  
[EdgeConnector<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.EdgeConnector_1.html) | Manipulator for creating new edges.  
[EdgeControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.EdgeControl.html) | VisualElement that draws the edge lines and detects if mouse is on top of edge.  
[EdgeDragHelper](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.EdgeDragHelper.html) | EdgeDragHelper's constructor.  
[EdgeDragHelper<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.EdgeDragHelper_1.html) | Edge drag helper class.  
[EdgeManipulator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.EdgeManipulator.html) | Edge manipulator used to drag edges off ports and reconnect them elsewhere.  
[Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) | Derive from this base class to create a custom inspector or editor for your custom object.  
[EditorAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorAction.html) | An EditorAction is a temporary tool that can represent either an atomic action or an interactive utility.  
[EditorAnalytics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorAnalytics.html) | Editor API for the EditorAnalytics feature.  
[EditorAnalyticsSessionInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorAnalyticsSessionInfo.html) | Provides access to Editor Analytics session information.  
[EditorApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html) | Main Application class.  
[EditorBuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.html) | This class allows you to modify the Editor Build Settings via script.  
[EditorBuildSettingsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettingsScene.html) | Represents entries in the Scenes list, as displayed in the Build Profiles window.  
[EditorCameraUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.EditorCameraUtils.html) | Utilities for Camera rendering in the Editor.  
[EditorConnection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.EditorConnection.html) | Handles the connection from the Editor to the Player.  
[EditorGraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.EditorGraphicsSettings.html) | Editor-specific script interface for Graphics Settings.  
[EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html) | These work pretty much like the normal GUI functions - and also have matching implementations in EditorGUILayout.  
[EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html) | Auto laid out version of EditorGUI.  
[EditorGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.html) | Miscellaneous helper stuff for EditorGUI.  
[EditorJsonUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorJsonUtility.html) | Utility functions for working with JSON data and engine objects.  
[EditorPrefs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.html) | Stores and accesses Unity Editor preferences.  
[EditorSceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.html) | Scene management in the Editor.  
[EditorSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings.html) | User settings for Unity Editor.  
[EditorSnapSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSnapSettings.html) | Control the behavior of handle snapping in the editor.  
[EditorStyles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles.html) | Common GUIStyles used for EditorGUI controls.  
[EditorTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorTool.html) | Use this class to implement editor tools. This is the base class from which all editor tools are inherited.  
[EditorToolAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolAttribute.html) | Registers an EditorTool as either a Global tool or a Component tool for a specific target type.  
[EditorToolbarButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Toolbars.EditorToolbarButton.html) | A clickable button used with EditorToolbarElementAttribute.  
[EditorToolbarDropdown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Toolbars.EditorToolbarDropdown.html) | A clickable dropdown used with EditorToolbarElementAttribute.  
[EditorToolbarDropdownToggle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Toolbars.EditorToolbarDropdownToggle.html) | A control that is both a toggle and a dropdown used with EditorToolbarElementAttribute.  
[EditorToolbarElementAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Toolbars.EditorToolbarElementAttribute.html) | The EditorToolbarElement attribute allows you to make available a specific VisualElement for use in an Editor Toolbar.  
[EditorToolbarFloatField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Toolbars.EditorToolbarFloatField.html) | A float field used with EditorToolbarElementAttribute.  
[EditorToolbarToggle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Toolbars.EditorToolbarToggle.html) | A toggle used with EditorToolbarElementAttribute.  
[EditorToolbarUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Toolbars.EditorToolbarUtility.html) | Editor utility functions when working with EditorToolbar.  
[EditorToolContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContext.html) | Use this class to implement specialized versions of the built-in transform tools. Built-in transform tools include Move, Rotate, Scale, Rect, and Transform.  
[EditorToolContextAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.EditorToolContextAttribute.html) | Registers an EditorToolContext as either a global context or a Component context for a specific target type.  
[EditorUserBuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings.html) | User build settings for the Editor  
[EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html) | Editor utility functions.  
[EditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) | Derive from this class to create a custom Editor window.  
[EditorWindowTitleAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindowTitleAttribute.html) | Use this class to set title text and icon for an Editor window.  
[EmbedRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.EmbedRequest.html) | Represents an asynchronous request to embed a package inside a project.  
[EndNameEditAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProjectWindowCallback.EndNameEditAction.html) | Base class to implement callbacks to be used when creating assets via the project window. You can extend the EndNameEditAction and write your own callback.  
[EntitlementGroupInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Licensing.EntitlementGroupInfo.html) | Data structure for entitlement group information (often synonymous with a license file), accessed through EntitlementInfo.  
[EntitlementInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Licensing.EntitlementInfo.html) | Data structure for an individual entitlement, the results of a call to LicensingUtility.HasEntitlementsExtended.  
[EnumFlagsField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EnumFlagsField.html) |  Makes a dropdown for switching between enum flag values that are marked with the Flags attribute.   
[Error](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Error.html) | Structure describing the error of a package operation.  
[Events](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Events.html) | An Interface for accessing the package manager events.  
[EventService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.html) | The EventService is a singleton implementation of a ChannelClient that runs on all instances of Unity. It is connected to the "events" channel and allows a Unity instance to send JSON messages to other EventServices in external process, or other instances of Unity.  
[FBXMaterialDescriptionPreprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.FBXMaterialDescriptionPreprocessor.html) | This is a default implementation for AssetPostProcessor.OnPreprocessMaterialDescription, this implementation converts material descriptions imported from FBX assets into materials for the internal rendering pipeline.  
[FilePathAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilePathAttribute.html) | An attribute that specifies a file location relative to the Project folder or Unity's preferences folder. Additional resources: Location.  
[FileUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FileUtil.html) | Lets you do move, copy, delete operations over files or directories.  
[FilterAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.FilterAttribute.html) | Tell the shader system which shader keywords to include or remove from the build, based on the data field underneath.  
[FrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.html) | Base funtionality for accessing the Profiler data.  
[FreehandSelector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.FreehandSelector.html) | Freehand selection tool.  
[FuzzySearch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FuzzySearch.html) | Provides a method to match query text using a fuzzy search algorithm.  
[GameObjectRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GameObjectRecorder.html) | Records the changing properties of a GameObject as the Scene runs and saves the information into an AnimationClip.  
[GameObjectToolContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.GameObjectToolContext.html) | This class represents the default context for manipulation tools. When GameObjectToolContext is active, manipulation tools affect the transform property of GameObjects in the SceneView Selection.  
[GameObjectUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObjectUtility.html) | GameObject utility functions.  
[GenericMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html) | GenericMenu lets you create custom context menus and dropdown menus.  
[GitInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.GitInfo.html) | Identifies a specific revision for a Git package using a Git commit hash.  
[GizmoInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoInfo.html) | GizmoInfo contains information about the Scene View gizmo and icon for a component type.  
[GizmoUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoUtility.html) | A static class for interacting with the Scene View icons and gizmos for types.  
[GradientField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GradientField.html) |  Makes a field for editing an Gradient. For more information, refer to UXML element GradientField.   
[GraphElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphElement.html) | Base class for main GraphView VisualElements.  
[GraphElementScopeExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphElementScopeExtensions.html) | Set of extension methods useful for Scope.  
[GraphicsAPIConstraintAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.GraphicsAPIConstraintAttribute.html) | Enable or disable shader keyword filter attributes based on the graphics API.  
[GraphicsSettingsInspectorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Inspector.GraphicsSettingsInspectors.GraphicsSettingsInspectorUtility.html) | Utility class for GraphicsSettings page.  
[GraphView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.html) | Main GraphView class.  
[GraphViewBlackboardWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphViewBlackboardWindow.html) | The base class for a floating window that contains a Blackboard.  
[GraphViewEditorWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphViewEditorWindow.html) | Abstract base class for an editor window that contains a GraphView.  
[GraphViewMinimapWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphViewMinimapWindow.html) | A floating window containing a MiniMap.  
[GraphViewToolWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphViewToolWindow.html) | Abstract base class for a GraphView tool window.  
[GridBackground](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GridBackground.html) | Default GraphView background.  
[GridPalette](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridPalette.html) | GridPalette stores settings for Palette assets when shown in the Palette window.  
[Group](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Group.html) | Allows interactive insertion of elements in a named scope.  
[GUIDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIDrawer.html) | Base class for PropertyDrawer and DecoratorDrawer.  
[Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html) | Custom 3D GUI controls and drawing in the Scene view.  
[HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html) | Helper functions for Scene View style 3D GUI.  
[Help](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Help.html) | Helper class to access Unity documentation.  
[HierarchyFrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.html) | Provides access to the Profiler data for a specific frame and thread.  
[Highlighter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Highlighter.html) | Use this class to highlight elements in the editor for use in in-editor tutorials and similar.  
[HyperLinkClickedEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HyperLinkClickedEventArgs.html) | Arguments for the event EditorGUI.hyperLinkClicked.  
[IconBadge](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.IconBadge.html) | A rectangular badge, usually attached to another visual element.  
[IHVImageFormatImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IHVImageFormatImporter.html) | Use IHVImageFormatImporter to modify Texture2D import settings for Textures in IHV (Independent Hardware Vendor) formats such as .DDS and .PVR from Editor scripts.  
[IMGUIOverlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.IMGUIOverlay.html) | IMGUIOverlay is an implementation of Overlay that provides a IMGUIContainer.  
[ImportLog](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ImportLog.html) | Container class that holds the collection of logs generated by an importer during the import process.  
[InitializeOnEnterPlayModeAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InitializeOnEnterPlayModeAttribute.html) | Allow an editor class method to be initialized when Unity enters Play Mode.  
[InitializeOnLoadAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InitializeOnLoadAttribute.html) | Allows you to initialize an Editor class when Unity loads, and when your scripts are recompiled.  
[InitializeOnLoadMethodAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InitializeOnLoadMethodAttribute.html) | Allow an editor class method to be initialized when Unity loads without action from the user.  
[InputExtraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.InputExtraction.html) | Class used when extracting BakeInput from the set of open scenes.  
[InSceneAssetUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetUtility.html) | Provides methods related to in-scene assets.  
[InspectorElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.InspectorElement.html) |  Create a VisualElement inspector from a SerializedObject.   
[InstantiationResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.InstantiationResult.html) | A class that holds the data created when a SceneTemplateAsset is instantiated.  
[IntegrationContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IntegrationContext.html) | Interface for integration-specific data.  
[iOSDeviceRequirement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOSDeviceRequirement.html) | A device requirement description used for configuration of App Slicing.  
[ItemSelectors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ItemSelectors.html) | Utility class to generate search column with item selectors.  
[JointAngularLimitHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.JointAngularLimitHandle.html) | A class for a compound handle to edit multiaxial angular motion limits in the Scene view.  
[L10n](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/L10n.html) | Class for text localization.  
[LayerField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LayerField.html) |  A LayerField editor. For more information, refer to UXML element LayerField.   
[LayerMaskField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.LayerMaskField.html) |  A LayerMaskField editor. For more information, refer to UXML element LayerMaskField.   
[LicensingUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Licensing.LicensingUtility.html) | Use the Licensing Utility class to request user permissions. User permissions are referred to as entitlements, which are simple strings, ie. "com.unity.editor.ui".  
[LightDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.LightDescription.html) | Represents light information from an imported file.  
[LightEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightEditor.html) | The class used to render the Light Editor when a Light is selected in the Unity Editor.  
[LightingDataAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingDataAsset.html) | The lighting data asset used by the active Scene.  
[LightingExplorerTab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingExplorerTab.html) | Create custom tabs for the Lighting Explorer.  
[LightingExplorerTableColumn](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingExplorerTableColumn.html) | This is used when defining how a column should look and behave in the Lighting Explorer.  
[LightingWindowEnvironmentSection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowEnvironmentSection.html) | Base class for the Inspector that overrides the Environment section of the Lighting window.  
[LightingWindowTab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingWindowTab.html) | Base class to add custom tabs to the Lighting window.  
[LightmapEditorSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapEditorSettings.html) | This class is now obsolete. Use LightingSettings.  
[LightmapParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapParameters.html) | Configures how Unity bakes lighting and can be assigned to a LightingSettings instance or asset.  
[Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.html) | Allows to control the lightmapping job.  
[Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping.html) | Experimental lightmapping features.  
[ListRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.ListRequest.html) | Represents an asynchronous request to list the packages in the project.  
[LocalizationAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LocalizationAttribute.html) | An attribute to the assembly for Localization.  
[LocalizationGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LocalizationGroup.html) | This provides an auto dispose Localization system. This can be called recursively.  
[LODUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LODUtility.html) | LOD Utility Helpers.  
[MainStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.MainStage.html) | The Main Stage contains all the currently open regular Scenes and is always available.  
[ManagedDebugger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.ManagedDebugger.html) | Representation of managed debugger in UnityEditor.  
[MaskField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MaskField.html) |  Make a field for masks.   
[MaterialDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.MaterialDescription.html) | Contains a set of typed properties for describing a texture input of a MaterialDescription.  
[MaterialEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.html) | The Unity Material Editor.  
[MaterialEditorExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditorExtensions.html) | Extension methods for the Material asset type in the editor.  
[MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) | Describes information and value of a single shader property.  
[MaterialPropertyDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyDrawer.html) | Base class to derive custom material property drawers from.  
[MaterialSettingsCallbackAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTree.Importer.MaterialSettingsCallbackAttribute.html) |  This attribute is used as a callback to set SRP specific properties from the importer.   
[MediaEncoder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaEncoder.html) | Encodes images and audio samples into an audio or movie file.  
[Menu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Menu.html) | Provides methods to manipulate a menu item.  
[MenuCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuCommand.html) | Used to extract the context for a MenuItem.  
[MenuItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html) | The MenuItem attribute allows you to add menu items to the main menu and Inspector window context menus.  
[MeshPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshPreview.html) | Use this class to render an interactive preview of a mesh.  
[MeshUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshUtility.html) | Various utilities for mesh manipulation.  
[Message](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Message.html) | Messages from the version control system.  
[MiniMap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.MiniMap.html) | MiniMap.  
[ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html) | Model importer lets you modify model import settings from editor scripts.  
[ModelImporterClipAnimation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterClipAnimation.html) | Animation clips to split animation into.  
[MonoImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html) | Represents a C# script in the project.  
[MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html) | Representation of Script assets.  
[MultiColumnHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.html) | The MultiColumnHeader is a general purpose class that e.g can be used with the TreeView to create multi-column tree views and list views.  
[MultiColumnHeaderState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeaderState.html) | State used by the MultiColumnHeader.  
[NavMeshBuilder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshBuilder.html) | Navigation mesh builder interface.  
[NavMeshEditorHelpers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshEditorHelpers.html) | NavMesh utility functionality effective only in the Editor.  
[NavMeshVisualizationSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AI.NavMeshVisualizationSettings.html) | Represents the visualization state of the navigation debug graphics.  
[Node](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Node.html) | Main GraphView node class.  
[ObjectChangeEvents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEvents.html) | Exposes events that allow you to track undoable changes to objects in the editor.  
[ObjectFactory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectFactory.html) | Use the DefaultObject to create a new UnityEngine.Object in the editor.  
[ObjectField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectField.html) | Object field used with the advanced search picker.  
[ObjectField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ObjectField.html) |  Makes a field to receive any object type. For more information, refer to UXML element ObjectField.   
[ObjectIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.html) | A specialized SearchIndexer which provides methods to index a Unity Object from custom indexers.  
[ObjectNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectNames.html) | Helper class for constructing displayable names for objects.  
[ObjectOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.ObjectOverride.html) | Class with information about an object on a Prefab instance with overridden properties.  
[ObjectPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectPreview.html) | Base Class to derive from when creating Custom Previews.  
[ObjectSelectorEngineAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ObjectSelectorEngineAttribute.html) | Use this class attribute to register ObjectSelector search engines automatically. Search engines with this attribute must implement the IObjectSelectorEngine interface.  
[ObjectSelectorSearch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ObjectSelectorSearch.html) | Use this API to select objects. Engines for this type of search implement the IObjectSelectorEngine interface.  
[ObjectSelectorSearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ObjectSelectorSearchContext.html) | A search context implementation for ObjectSelector search engines. All methods that are called on an ObjectSelector search engine, and expect a ISearchContext, receive an object of this type.  
[OnInspectorGUIContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.OnInspectorGUIContext.html) | The context for drawing IMGUI elements pertaining to terrain tools brushes.  
[OnOpenAssetAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.OnOpenAssetAttribute.html) | Invokes a static callback method when the Unity Editor attempts to open an asset.  
[Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html) | Overlays are persistent and customizable panels and toolbars that are available within Editor Windows. Use Overlays to expose actions and tool options in a convenient and user-controllable way.  
[OverlayAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayAttribute.html) | Attribute used to register a class as an overlay.  
[OverlayCanvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayCanvas.html) | OverlayCanvas is a container for collections of Overlays.  
[OverlayToolbar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.OverlayToolbar.html) | Base class for toolbar elements intended to be drawn in an Overlay.  
[PackageCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageCollection.html) | A collection of PackageInfo objects that you can iterate over.  
[PackageInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo.html) | Structure describing a Unity Package.  
[PackageManagerExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.UI.PackageManagerExtensions.html) | Package Manager UI Extensions.  
[PackageRegistrationEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageRegistrationEventArgs.html) | Structure describing the PackageInfo entries to register or unregister during the Package Manager registration process.  
[PackedAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.PackedAssets.html) | An extension to the BuildReport class that tracks how Assets contribute to the size of the build.  
[Packer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprites.Packer.html) | Sprite Packer helpers.  
[PackerJob](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprites.PackerJob.html) | Current Sprite Packer job definition.  
[PackOperationResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackOperationResult.html) | Structure describing the result of a Client.Pack operation.  
[PackRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.PackRequest.html) | Represents an asynchronous request to pack a package folder.  
[PaintDetailsToolUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintDetailsToolUtility.html) | Provides utility methods for painting details.  
[PaintTreesDetailsContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.PaintTreesDetailsContext.html) | Represents a context object for information used when scattering trees and detail objects across terrains.  
[ParsedQuery<T0,T1>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ParsedQuery_2.html) | Provides methods to define an operation that can be used to filter a data set.  
[ParsedQuery<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ParsedQuery_1.html) | Provides methods to define an operation that can be used to filter a data set.  
[PhysicsDebugWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsDebugWindow.html) | Displays the Physics Debug Visualization options.The Physics Debug Visualization is only displayed if this window is visible.Additional resources: PhysicsVisualizationSettings.  
[PhysicsVisualizationSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.html) | This class contains the settings controlling the Physics Debug Visualization.  
[Pill](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Pill.html) | The Pill class includes methods for creating and managing a VisualElement that resembles a capsule. The Pill class includes text, an icon, and two optional child VisualElements: one to the left of the pill, and one to the right of the pill.  
[Placemat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Placemat.html) | Allows interactive manipulation of elements (drag, hide) over a virtual placemat.  
[PlacematContainer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.PlacematContainer.html) | The GraphView layer for placemats.  
[PlatformIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIcon.html) | Icon slot container.  
[PlatformIconKind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlatformIconKind.html) | Icon kind wrapper.  
[PlayableOutputEditorExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputEditorExtensions.html) | Editor extensions for all types that implement IPlayableOutput.  
[PlayerBuildInterface](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Player.PlayerBuildInterface.html) | Low level interface for building scripts for Unity.  
[PlayerConnectionGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.PlayerConnectionGUI.html) | This class contains methods to draw IMGUI Editor UI that relates to the Player Connection.  
[PlayerConnectionGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.PlayerConnectionGUILayout.html) | This class contains methods to draw and automatically layout IMGUI Editor UI that relates to the Player Connection.  
[PlayerConnectionGUIUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.PlayerConnectionGUIUtility.html) | Miscellaneous helper methods for PlayerConnectionGUI.  
[PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html) | Use Player settings to define how Unity builds and displays your final application.  
[PlayModeWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayModeWindow.html) | Class containing methods to interact with the selected Unity PlayModeView (GameView, Simulator).  
[Plugin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Plugin.html) | The plug-in class describes the currently active version control plug-in and its configuration options.  
[PluginImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.html) | Represents a plugin importer.  
[PopupWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PopupWindow.html) | Class used to display popup windows that inherit from PopupWindowContent.  
[PopupWindowContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PopupWindowContent.html) | Class used to implement content for a popup window.  
[Port](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Port.html) | GraphView Port class.  
[PortSource<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.PortSource_1.html) | Port source.  
[PostProcessBuildAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.PostProcessBuildAttribute.html) | Add this attribute to a method to get a notification just after building the player.  
[PostProcessSceneAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.PostProcessSceneAttribute.html) | Add this attribute to a method to get a notification just after building the Scene.  
[PrefabOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabOverride.html) | Class with information about a given override on a Prefab instance.  
[PrefabReplacingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabReplacingSettings.html) | Settings controlling the behavior of PrefabUtility.ReplacePrefabAssetOfPrefabInstance.  
[PrefabStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStage.html) | The PrefabStage class represents an editing context for Prefab Assets.  
[PrefabStageUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PrefabStageUtility.html) | Utility methods related to Prefab stages.  
[PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html) | Utility class for any Prefab related operations.  
[PreloadInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.PreloadInfo.html) | Container for holding a list of preload objects for a Scene to be built.  
[Preset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.Preset.html) | A Preset contains default values for an Object.  
[PresetSelector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetSelector.html) | This class implements a modal window that selects a Preset asset from the Project.  
[PreviewSceneStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.PreviewSceneStage.html) | The PreviewSceneStage class represents an editing context based on a single preview Scene.  
[PrimitiveBoundsHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.PrimitiveBoundsHandle.html) | Base class for a compound handle to edit a bounding volume in the Scene view.  
[ProcessService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessService.html) | *This is an experimental feature.* The ProcessService allows you to start slave instance of UnityEditor, opened to the same Project as the master instance, with a specific RoleProviderAttribute.  
[ProfilerEditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.ProfilerEditorUtility.html) | A Utility class for Profiler tooling in the Unity Editor.  
[ProfilerModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Editor.ProfilerModule.html) | Represents a Profiler module in the Profiler window.  
[ProfilerModuleMetadataAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Editor.ProfilerModuleMetadataAttribute.html) | Provides metadata related to a ProfilerModule, such as its name and icon path.  
[ProfilerModuleViewController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Editor.ProfilerModuleViewController.html) | Provides a single view of content for a ProfilerModule displayed in the Profiler window.  
[ProfilerTimeSampleSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.ProfilerTimeSampleSelection.html) | An object describing a selection made in a frame time sample based Profiler module.  
[ProfilerWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProfilerWindow.html) | Use the ProfilerWindow class for interactions with the Profiler Window such as checking which frame it currently shows and controlling the selected Profiler sample in the CPU or GPU Usage Modules.  
[Progress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.html) | The Progress utility class reports the progress of asynchronous tasks to Unity.  
[ProjectBindDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Connect.ProjectBindDrawer.html) | A container that fetches the UIElements that draw the Project Binding UI, and subscribes to its events.  
[ProjectSearch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ProjectSearch.html) | Use this API to perform searches in the Project. Engines for this type of search implement the IProjectSearchEngine interface.  
[ProjectSearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ProjectSearchContext.html) | A search context implementation for Project search engines. All methods that are called on a Project search engine, and expect a ISearchContext, receive an object of this type.  
[ProjectSearchEngineAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ProjectSearchEngineAttribute.html) | A class attribute that registers Project search engines automatically. Search engines with this attribute must implement the IProjectSearchEngine interface.  
[PropertyDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabase.html) | The PropertyDatabase is a system that can store, in a thread-safe manner, properties of different kinds into a single file that we call a property database.  
[PropertyDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.html) | Base class to derive custom property drawers from. Use this to create custom drawers for your own Serializable classes or for script variables with custom PropertyAttributes.  
[PropertyField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PropertyField.html) |  A SerializedProperty wrapper VisualElement that, on Bind(), will generate the correct field elements with the correct binding paths. For more information, refer to UXML element PropertyField.   
[PropertyModification](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyModification.html) | Defines a single modified property.  
[Provider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.html) | This class provides access to the version control API.  
[PurchasingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Purchasing.PurchasingSettings.html) | Editor API for the Unity Services editor feature. Normally Purchasing is enabled from the Services window, but if writing your own editor extension, this API can be used.  
[QueryBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryBlock.html) | A query block is the visual element of a query node in a query.  
[QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html) | A QueryEngine defines how to build a query from an input string. It can be customized to support custom filters and operators. Default query engine of type object.  
[QueryEngine<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html) | A QueryEngine defines how to build a query from an input string. It can be customized to support custom filters and operators.  
[QueryEngineFilterAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngineFilterAttribute.html) | Base attribute class used to define a custom filter on a QueryEngine. All filter types supported by QueryEngine.AddFilter are supported by this attribute.  
[QueryEngineParameterTransformerAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngineParameterTransformerAttribute.html) | Base attribute class that defines a custom parameter transformer function.  
[QueryError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryError.html) | A QueryError holds the definition of a query parsing error.  
[QueryGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryGraph.html) | Class that represents a query graph.  
[QueryListBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryListBlock.html) | A query list block represents a special query block that will list a set of value for a given filter.  
[QueryListBlockAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryListBlockAttribute.html) | This attribute can be used on a class deriving from QueryListBlock to display in query builder mode a special block that will propose a fixed set of values when clicked.  
[RadeonRaysContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.html) |  RadeonRaysContext implements the IDeviceContext interface. It uses the RadeonRays SDK for intersection testing and the OpenCL 1.2 API for compute.  
[RadeonRaysProbeIntegrator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysProbeIntegrator.html) | RadeonRays-based light probe integrator.  
[RadeonRaysProbePostProcessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.PostProcessing.RadeonRaysProbePostProcessor.html) | RadeonRaysProbePostProcessor.  
[RadeonRaysWorld](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysWorld.html) | RadeonRays integration world.  
[RawFrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.RawFrameDataView.html) | Provides access to the Profiler data for a specific frame and thread.  
[RectangleSelector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.RectangleSelector.html) | Rectangle selection box manipulator.  
[RectUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.RectUtils.html) | Utilities for rectangle selections.  
[ReferenceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.html) | The ReferenceContext implements the IDeviceContext interface.  
[ReferenceProbePostProcessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.PostProcessing.ReferenceProbePostProcessor.html) | The ReferenceProbePostProcessor implements the IProbePostProcessor interface.  
[RegistryInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.RegistryInfo.html) | Provides information about a package registry.  
[RemovedComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.RemovedComponent.html) | Class with information about a component that has been removed from a Prefab instance.  
[RemovedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.RemovedGameObject.html) | Class with information about a GameObject that has been removed from a Prefab instance.  
[RemoveIfAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.RemoveIfAttribute.html) | Remove the specified shader keywords from the build if the data field matches the condition.  
[RemoveIfNotAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.RemoveIfNotAttribute.html) | Remove the specified shader keywords from the build if the data field doesn't match the condition.  
[RemoveOrSelectAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.RemoveOrSelectAttribute.html) | Either remove or include the specified shader keywords in the build, depending on the data field underneath.  
[RemoveRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.RemoveRequest.html) | Represents an asynchronous request to remove a package from the project.  
[RenderingLayerMaskField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.RenderingLayerMaskField.html) | Drawer for RenderingLayerMask.  
[RenderingLayersLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingLayersLimitSettings.html) | Define a number of supported Rendering Layers on the Render Pipeline.  
[RenderPipelineEditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineEditorUtility.html) | Helper class that contains a utility function on ScriptableRenderPipeline for Editor.  
[RenderPipelineGraphicsSettingsEditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineGraphicsSettingsEditorUtility.html) | Helper class that contains a utility function on IRenderPipelineGraphicsSettings for Editor.  
[RepositoryInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.RepositoryInfo.html) | Includes information about the repository that hosts the package.  
[Request](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.Request.html) | Tracks the state of an asynchronous Unity Package Manager (Upm) server operation.  
[Request<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.Request_1.html) | Tracks the state of an asynchronous Unity Package Manager (Upm) server operation that returns a non-empty response.  
[ReserveModifiersAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ReserveModifiersAttribute.html) | Provides an attribute that reserves one or multiple modifiers for a specific shortcut.  
[ResetToEditorDefaultsRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.ResetToEditorDefaultsRequest.html) | Represents an asynchronous request to reset the project packages to the current Editor default configuration.  
[ResizableElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ResizableElement.html) | Instantiates a [ResizableElement] that you add as a child of the [VisualElement] that you want to resize.  
[Resizer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Resizer.html) | Resizer manipulator element.  
[ResponseFileData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.ResponseFileData.html) | Data class used for storing parsed response file data.  
[RoleProviderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.RoleProviderAttribute.html) | An attribute used to decorate function that defines how a slave process can interact with a main instance of Unity.  
[RunAfterAssemblyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunAfterAssemblyAttribute.html) | Add this attribute to a callback method to mark that this callback must be run after any callbacks that are part of the specified assembly.  
[RunAfterClassAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunAfterClassAttribute.html) | Add this attribute to a callback method to mark that this callback must be run after any callbacks that are part of the specified class.  
[RunAfterPackageAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunAfterPackageAttribute.html) | Add this attribute to a callback method to mark that this callback must be run after any callbacks that are part of the specified package.  
[RunBeforeAssemblyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunBeforeAssemblyAttribute.html) | Add this attribute to a callback method to indicate that this callback must be run before any callbacks that are part of the specified assembly.  
[RunBeforeClassAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunBeforeClassAttribute.html) | Add this attribute to a callback method to mark that this callback must be run before any callbacks that are part of the specified class.  
[RunBeforePackageAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.RunBeforePackageAttribute.html) | Add this attribute to a callback method to mark that this callback must be run before any callbacks that are part of the specified package.  
[SaveData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.SaveData.html) | A serializable storage for the state of an Overlay.  
[SceneAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneAsset.html) | SceneAsset is used to reference Scene objects in the Editor.  
[SceneBundleInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.SceneBundleInfo.html) | Container for holding asset loading information for a streamed Scene AssetBundle to be built.  
[SceneCullingMasks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneCullingMasks.html) | Masks that control what kind of Scene views and Game views Unity should render a GameObject in.  
[SceneLoadInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.SceneLoadInfo.html) | Container for holding preload information for a given serialized Scene in an AssetBundle.  
[SceneQueryEngineFilterAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.Providers.SceneQueryEngineFilterAttribute.html) | Custom attribute is used to customize the search engine used by the scene search provider.  
[SceneQueryEngineParameterTransformerAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.Providers.SceneQueryEngineParameterTransformerAttribute.html) | Attribute class that defines a custom parameter transformer function applied for a query running in a scene provider defined by a scene custom filter using SceneQueryEngineFilterAttribute.  
[SceneSearch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.SceneSearch.html) | Use this API to perform searches in the Scene. Engines for this type of search implement the ISceneSearchEngine interface.  
[SceneSearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.SceneSearchContext.html) | A search context implementation for Scene search engines. All methods that are called on a Scene search engine, and expect a ISearchContext, receive an object of this type.  
[SceneSearchEngineAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.SceneSearchEngineAttribute.html) | A class attribute that registers Scene search engines automatically. Search engines with this attribute must implement the ISceneSearchEngine interface.  
[SceneSetup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneSetup.html) | The setup information for a Scene in the SceneManager. This cannot be used in Play Mode.   
[ScenesUsingAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.ScenesUsingAssets.html) | An extension to the BuildReport class that tracks which scenes in the build have references to a specific asset in the build.  
[SceneTemplateAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateAsset.html) | An Asset that stores everything required to instantiate a new Scene from a templated Scene.  
[SceneTemplatePipelineAdapter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplatePipelineAdapter.html) | An adapter that implements all the functions of ISceneTemplatePipeline for easier usage. Use it to partially override a ISceneTemplatePipeline.  
[SceneTemplateService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateService.html) | A utility class that manages SceneTemplateAsset instantiation.  
[SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html) | Use this class to manage SceneView settings, change the SceneView camera properties, subscribe to events, call SceneView methods, and render open scenes.  
[SceneViewCameraWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneViewCameraWindow.html) | Use this class to instantiate a SceneViewCameraWindow window.  
[SceneVisibilityManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.html) | Manages Scene Visibility in the editor.  
[Scope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Scope.html) | This class allows for nodes to be grouped into a common area, or Scope. This class includes methods that automatically resize and position the Scope to encompass the group of nodes.  
[ScriptableBakedReflectionSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ScriptableBakedReflectionSystem.html) | Empty implementation of IScriptableBakedReflectionSystem.  
[ScriptableBakedReflectionSystemSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ScriptableBakedReflectionSystemSettings.html) | Global settings for the scriptable baked reflection system.  
[ScriptablePacker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.ScriptablePacker.html) | ScriptablePacker Interface. Provides a custom implementation to pack sprites into textures. This is the Scriptable Packer interface.  
[ScriptableSingleton<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableSingleton_1.html) | Generic class for storing Editor state.  
[ScriptableWizard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableWizard.html) | Derive from this class to create an editor wizard.  
[ScriptCompilerOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.ScriptCompilerOptions.html) | Compiler options passed to the script compiler.  
[ScriptedImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporter.html) | Abstract base class for custom Asset importers.  
[ScriptedImporterAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporterAttribute.html) | Class attribute used to register a custom asset importer derived from ScriptedImporter with Unity's Asset import pipeline.  
[ScriptedImporterEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporterEditor.html) | Default editor for source assets handled by Scripted Importers.  
[SearchAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction.html) | Defines an action that can be applied on a SearchItem of a specific search provider type.  
[SearchActionsProviderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchActionsProviderAttribute.html) | Attribute used to declare a static method that defines new actions for specific search providers.  
[SearchColumn](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumn.html) | Search columns are used to display additional information in the Search Table view.  
[SearchColumnProviderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnProviderAttribute.html) | The search column provider attribute is used to define new formats for a given column.  
[SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) | The search context includes all the data necessary to perform a query. It allows the full customization of how a query may be performed.  
[SearchExpression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.html) | Search expressions allow you to add to the search query language to express complex queries that cross-reference multiple providers, for example, to search for all objects in a scene that use a shader that doesn’t compile.Search expressions can be chained together to transform or perform set manipulations on Search Items.The manual contains example on How to use Search Expression .  
[SearchExpressionEvaluatorAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionEvaluatorAttribute.html) | Attribute used to register new SearchExpressionEvaluator. This will allow to use new function in SearchExpression. As a side note all builtin evaluators (count{}, select{}, ...) are defined using this attribute.  
[SearchExpressionEvaluatorSignatureOverloadAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionEvaluatorSignatureOverloadAttribute.html) | Allows user to add more function signature overload to a SearchExpressionEvaluatorAttribute.  
[SearchField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.SearchField.html) | The SearchField control creates a text field for a user to input text that can be used for searching.  
[SearchFieldBase<T0,T1>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SearchFieldBase_2.html) |  The base class for a search field.   
[SearchIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html) | Base class for a document Indexer which provides methods for retrieving a document given a specific pattern in roughly log(n). This allows you to search a large index more quickly.  
[SearchItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) | Search items are returned by the search provider to show to the user after a search is performed. The search item holds all the data that is used to sort and present the search results. Some members of a SearchItem can be specified in an asynchronous callback (see SearchItem.fetchThumbnail, SearchItem.fetchDescription, etc).  
[SearchItemProviderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemProviderAttribute.html) | Attribute used to declare a static method that will create a new search provider at load time.  
[SearchMonitor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitor.html) | The search monitor is responsible to track any changes that occurs in Unity in order to update search indexes or other search data structure at runtime.  
[SearchPropositionFlagsExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchPropositionFlagsExtensions.html) | Search proposition flags extension used to manipulate flag bits.  
[SearchPropositionOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchPropositionOptions.html) | Search proposition options are used define how search propositions are fetched and displayed.  
[SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) | SearchProvider manages search for specific types of items and manages all fields of a SearchItem such as thumbnails, descriptions, subfilters.  
[SearchQueryError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchQueryError.html) | Represents a query parsing error.  
[SearchRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.SearchRequest.html) | Represents an asynchronous request to find a package.  
[SearchSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSelection.html) | Provides methods to give readonly access to the current list of selected items in Search.  
[SearchSelectorAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSelectorAttribute.html) | Search selector attribute used to define how a custom value can be selected from a search item.  
[SearchService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.html) | Principal Search API to initiate searches and fetch results.  
[SearchSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSettings.html) | Search settings give access to the user global preferences regarding Search.  
[SearchTable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchTable.html) | A search table configuration is used to define the columns when search results are displayed in table view.  
[SearchTreeEntry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.SearchTreeEntry.html) | This class describes a search tree entry. The search window displays search tree entries in the GraphView.  
[SearchTreeGroupEntry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.SearchTreeGroupEntry.html) | This class describes group entries in the search tree. The search tree is displayed in the search window.  
[SearchUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.html) | Provides various utility functions that are used by SearchProvider.  
[SearchViewState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewState.html) | Search view state is used to create new Search windows. See SearchService.ShowWindow.  
[SearchWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.SearchWindow.html) | This subclass displays a searchable menu of available graph nodes.  
[SelectIfAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.SelectIfAttribute.html) | Include only the specified shader keywords in the build if the data field matches the condition.  
[SelectIfNotAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.SelectIfNotAttribute.html) | Include only the specified shader keywords in the build if the data field doesn't match the condition.  
[Selection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html) | Access to the selection in the editor.  
[SelectionDragger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.SelectionDragger.html) | Selection dragger manipulator.  
[SelectionDropper](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.SelectionDropper.html) | Selection drag&drop manipulator.  
[SelectOrRemoveAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.SelectOrRemoveAttribute.html) | Either include or remove the specified shader keywords in the build, depending on the data field underneath.  
[SerializationInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.SerializationInfo.html) | Container for holding object serialization order information for a build.  
[SerializationUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializationUtility.html) | Utility functions related to Serialization.  
[SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) | SerializedObject and SerializedProperty are classes for editing serialized fields on Unity objects in a completely generic way. These classes automatically handle dirtying individual serialized fields so they will be processed by the Undo system and styled correctly for Prefab overrides when drawn in the Inspector.  
[SerializedObjectChangeEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SerializedObjectChangeEvent.html) |  An event sent when any value in a SerializedObject changes   
[SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) | SerializedProperty and SerializedObject are classes for editing properties on objects in a completely generic way that automatically handles undo, multi-object editing and Prefab overrides.  
[SerializedPropertyChangeEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.SerializedPropertyChangeEvent.html) |  An event sent when a value in a PropertyField changes.   
[SessionState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SessionState.html) | SessionState is a Key-Value Store intended for storing and retrieving Editor session state that should survive assembly reloading.  
[SettingsProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) | SettingsProvider is the configuration class that specifies how a Project setting or a preference should appear in the Settings or Preferences window.  
[SettingsProviderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProviderAttribute.html) | Attribute used to register a new SettingsProvider. Use this attribute to decorate a function that returns an instance of a SettingsProvider. If the function returns null, no SettingsProvider appears in the Settings window.  
[SettingsProviderGroupAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProviderGroupAttribute.html) | Attribute used to register multiple SettingsProvider items. Use this attribute to decorate a function that returns an array of SettingsProvider instances. If the function returns null, no SettingsProvider appears in the Settings window.  
[SettingsService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsService.html) | This class provides global APIs to interact with the Settings window.  
[ShaderData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderData.html) | This class describes a shader.  
[ShaderGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.html) | Abstract class to derive from for defining custom GUI for shader properties and for extending the material preview.  
[ShaderImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderImporter.html) | Shader importer lets you modify shader import settings from Editor scripts.  
[ShaderInclude](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderInclude.html) | Shader include file asset.  
[ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html) | Utility functions to assist with working with shaders from the editor.  
[ShortcutAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutAttribute.html) | Registers a static method as the action for an action shortcut.  
[ShortcutBaseAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutBaseAttribute.html) | Abstract base class for ShortcutAttribute and ClutchShortcutAttribute.  
[ShortcutHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ShortcutHandler.html) | Shortcut handler.  
[ShortcutManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutManager.html) | Provides access to an instance of IShortcutManager for managing shortcuts.  
[SketchUpImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImporter.html) | Derives from AssetImporter to handle importing of SketchUp files.  
[SketchupMaterialDescriptionPreprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.SketchupMaterialDescriptionPreprocessor.html) | This is a default implementation for AssetPostProcessor.OnPreprocessMaterialDescription, this implementation converts material descriptions imported from Sketchup assets into materials for the internal rendering pipeline.  
[SourceTextureInformation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.SourceTextureInformation.html) | Original texture data information.  
[SpeedTree9Importer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTree.Importer.SpeedTree9Importer.html) | Represents the SpeedTree 9 asset importer, providing methods for processing and post-processing SpeedTree assets during import.  
[SpeedTreeImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter.html) | AssetImporter for importing SpeedTree model assets.  
[SphereBoundsHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.SphereBoundsHandle.html) | A compound handle to edit a sphere-shaped bounding volume in the Scene view.  
[SpriteAtlasAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasAsset.html) | SpriteAtlasAsset stores inputs for generating SpriteAtlas and generates atlas textures on Import.  
[SpriteAtlasExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasExtensions.html) | Method extensions for SpriteAtlas in Editor.  
[SpriteAtlasImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasImporter.html) | SpriteAtlasImporter imports SpriteAtlasAsset and generates SpriteAtlas.  
[SpriteAtlasUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasUtility.html) | Utility methods to pack atlases in the Project.  
[SpriteEditorExtension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteEditorExtension.html) |  Sprite extension methods that are accessible in Editor only.  
[SpriteUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprites.SpriteUtility.html) | Helper utilities for accessing Sprite data.  
[StackNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.StackNode.html) | Use this class to customize StackNodes and to manage dragging GraphElements over StackNodes.  
[Stage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.html) | The Stage class represents an editing context which includes a collection of Scenes.  
[StageUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.StageUtility.html) | Utility methods related to stages.  
[StateMachineBehaviourContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.StateMachineBehaviourContext.html) | This class contains all the owner's information for this State Machine Behaviour.  
[StaticOcclusionCulling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticOcclusionCulling.html) | StaticOcclusionCulling lets you perform static occlusion culling operations.  
[StaticOcclusionCullingVisualization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticOcclusionCullingVisualization.html) | Used to visualize static occlusion culling at development time in Scene view.  
[StickyNote](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.StickyNote.html) | Instantiates a [GraphElement] used for comment text.  
[StickyNoteChangeEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.StickyNoteChangeEvent.html) | The event sent when a [StickyNote] was changed.  
[StrippingInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.StrippingInfo.html) | The StrippingInfo object contains information about which native code modules in the engine are still present in the build, and the reasons why they are still present.  
[Sysroot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sysroot.html) | Base class for implementing sysroots and toolchains for IL2CPP  
[TagConstraintAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.TagConstraintAttribute.html) | Enable or disable shader keyword filter attributes based on shader tags.  
[TagField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TagField.html) |  A TagField editor. For more information, refer to UXML element TagField.   
[Task](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Task.html) | A Task describes an instance of a version control operation.  
[TerrainDetailMeshWizard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainDetailMeshWizard.html) | Provides methods for displaying the detail mesh wizard.  
[TerrainDetailTextureWizard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainDetailTextureWizard.html) | Provides methods for displaying the detail texture wizard.  
[TerrainInspectorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainInspectorUtility.html) | Utility class for Terrain Inspector GUI.  
[TerrainLayerInspector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayerInspector.html) | The default Inspector class for Terrain Layer.  
[TerrainLayerUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainLayerUtility.html) | A set of helper functions for using terrain layers.  
[TerrainPaintTool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintTool_1.html) | Base class for terrain painting tools.  
[TerrainPaintToolWithOverlays<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintToolWithOverlays_1.html) | Base class for Terrain painting tools, which inherit from Editor Tools.  
[TerrainPaintToolWithOverlaysBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintToolWithOverlaysBase.html) | The abstract class that TerrainPaintToolWithOverlays inherits from.  
[TerrainPaintUtilityEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainPaintUtilityEditor.html) | Terrain paint utility editor helper functions.  
[TerrainToolShortcutContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainToolShortcutContext.html) | The shortcut context that is active while editing Terrain.  
[TerrainWizard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainWizard.html) | Provides methods for displaying the terrain wizard.  
[TextureGenerator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.TextureGenerator.html) | Experimental utilities for generating Texture2D.  
[TextureImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html) | Texture importer lets you modify Texture2D import settings from editor scripts.  
[TextureImporterPlatformSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterPlatformSettings.html) | Stores platform specifics settings of a TextureImporter.  
[TextureImporterSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings.html) | Stores settings of a TextureImporter.  
[ThreeDSMaterialDescriptionPreprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ThreeDSMaterialDescriptionPreprocessor.html) | This is a default implementation for AssetPostProcessor.OnPreprocessMaterialDescription, this implementation converts material descriptions imported from .3DS assets into materials for the internal rendering pipeline.  
[TileBaseEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TileBaseEditor.html) | Default editor for TileBase assets.  
[TileEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TileEditor.html) | Default editor for Tile assets.  
[TokenNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.TokenNode.html) | The TokenNode class includes methods for creating and managing a Node that resembles a capsule. The TokenNode class includes a title, an icon, one input Port, and one output Port.  
[ToolAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolAttribute.html) | Base class from which EditorToolAttribute and EditorToolContextAttribute inherit.  
[Toolbar](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toolbar.html) |  A toolbar for tool windows. For more information, refer to UXML element Toolbar.   
[ToolbarBreadcrumbs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToolbarBreadcrumbs.html) |  Creates a breadcrumb UI element for the toolbar to help users navigate a hierarchy. For example, the visual scripting breadcrumb toolbar makes it easier to explore scripts because users can jump to any level of the script by clicking a breadcrumb item. For more information, refer to UXML element ToolbarBreadcrumbs.   
[ToolbarButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToolbarButton.html) |  A button for the toolbar. For more information, refer to UXML element ToolbarButton.   
[ToolbarMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToolbarMenu.html) |  A drop-down menu for the toolbar. For more information, refer to UXML element ToolbarMenu.   
[ToolbarMenuElementExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToolbarMenuElementExtensions.html) |  An extension class that handles menu management for elements that are implemented with the IToolbarMenuElement interface, but are identical to DropdownMenu.   
[ToolbarOverlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.ToolbarOverlay.html) |  ToolbarOverlay is an implementation of Overlay that provides a base for Overlays that can be placed in horizontal or vertical toolbars.  
[ToolbarPopupSearchField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToolbarPopupSearchField.html) |  The pop-up search field for the toolbar. The search field includes a menu button. For more information, refer to UXML element ToolbarPopupSearchField.   
[ToolbarSearchField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToolbarSearchField.html) |  A search field for the toolbar. For more information, refer to UXML element ToolbarSearchField.   
[ToolbarSpacer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToolbarSpacer.html) |  A toolbar spacer of static size. For more information, refer to UXML element ToolbarSpacer.   
[ToolbarToggle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToolbarToggle.html) |  A toggle for the toolbar. For more information, refer to UXML element ToolbarToggle.   
[ToolManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorTools.ToolManager.html) | This class manipulates editor tools in the Scene view.  
[Tools](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tools.html) | Class used to manipulate the tools used in Unity's Scene View.  
[TransformUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TransformUtils.html) | Editor Transform Utility Class.  
[TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html) | The TreeView is an IMGUI control that lets you create tree views, list views and multi-column tables for Editor tools.  
[TreeViewItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html) | The TreeViewItem is used to build the tree representation of a tree data structure.  
[TreeViewState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewState.html) | The TreeViewState contains serializable state information for the TreeView.  
[TrueTypeFontImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrueTypeFontImporter.html) | AssetImporter for importing Fonts.  
[TypeCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TypeCache.html) | Provides methods for fast type extraction from assemblies loaded into the Unity Domain.  
[TypeDB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Player.TypeDB.html) | Container for holding information about script type and property data.  
[Undo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.html) | Lets you register undo operations on specific objects you are about to perform changes on.  
[UnityEventTools](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventTools.html) | Editor tools for working with persistent UnityEvents.  
[UnityLinkerBuildPipelineData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityLinker.UnityLinkerBuildPipelineData.html) | Contains information for various IUnityLinkerProcessor callbacks.  
[Unwrapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unwrapping.html) | Utility class for computing mesh UVs.  
[Utility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Utility.html) | Editor utility functions for the Playable graph and its nodes.  
[UxmlAttributeConverter<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlAttributeConverter_1.html) |  Converts a UxmlAttribute type to and from a string.   
[UxmlNamespacePrefixAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlNamespacePrefixAttribute.html) |  Attribute that can be used on an assembly to define an XML namespace prefix for a namespace.   
[UxmlSerializedDataCreator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UxmlSerializedDataCreator.html) |  Editor utility methods for dealing with UxmlSerializedData.   
[VersionControlAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlAttribute.html) | Allows you to mark a class as a version control system object.  
[VersionControlDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlDescriptor.html) | Contains unique version control system name.  
[VersionControlManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlManager.html) | Manages version control systems.  
[VersionControlObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlObject.html) | The abstract base class for representing a version control system.  
[VersionControlUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.VersionControlUtils.html) | Contains version control system specific utility methods.  
[VersionsInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.VersionsInfo.html) | Identifies the available versions of a package and which are the compatible, latest, and recommended versions.  
[VideoClipImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoClipImporter.html) | VideoClipImporter lets you modify VideoClip import settings from Editor scripts.  
[VideoImporterTargetSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoImporterTargetSettings.html) | Importer settings that can have platform-specific values.  
[Viewpoint<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Viewpoint_1.html) | Defines a Viewpoint that can be selected from the Cameras overlay.  
[WriteCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.WriteCommand.html) | Container for holding information about a serialized file to be written.  
### Structs
Struct | Description  
---|---  
[ActiveProfileChangedEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ActiveProfileChangedEventArgs.html) | Provides data for the IShortcutManager.activeProfileChanged event.  
[AdvancedObjectSelectorParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.AdvancedObjectSelectorParameters.html) | Struct containing the different parameters passed to the advanced object selector.  
[AlbedoSwatchInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AlbedoSwatchInfo.html) | Contains the custom albedo swatch data.  
[AndroidDeviceFilterData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidDeviceFilterData.html) | Set of parameters used to define an Android device or group of Android devices.  
[AnimatorCondition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorCondition.html) | Condition that is used to determine if a transition must be taken.  
[ArtifactID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.ArtifactID.html) | Uniquely identifies a produced artifact such as an imported asset (e.g. result of importing a texture).  
[ArtifactKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.ArtifactKey.html) | An ArtifactKey is used for specifying an artifact to lookup or produce.  
[AssemblyDefinitionPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.AssemblyDefinitionPlatform.html) | Contains information about a platform supported by the assembly definition files.  
[AssetBundleBuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleBuild.html) | AssetBundle building map entry.  
[AssetIndexChangeSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.AssetIndexChangeSet.html) | Defines a set of changes that happens in order to update a search asset index.  
[AtlasSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprites.AtlasSettings.html) | Describes the final atlas texture.  
[AudioImporterSampleSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporterSampleSettings.html) | This structure contains a collection of settings used to define how an AudioClip should be imported.  
[AudioTrackAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.AudioTrackAttributes.html) | Descriptor for audio track format.  
[BufferID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferID.html) | Abstraction layer for memory buffers.  
[BufferSlice<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferSlice_1.html) | Unity uses the BufferSlice struct to split one large buffer allocation into one or more smaller buffers, each with explicit types.  
[BuildAssetBundlesParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundlesParameters.html) | Provide various options to control the behavior of BuildPipeline.BuildAssetBundles.  
[BuildFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildFile.html) | Contains information about a single file produced by the build process.  
[BuildPlayerOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerOptions.html) | Provide various options to control the behavior of BuildPipeline.BuildPlayer.  
[BuildPlayerWithProfileOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPlayerWithProfileOptions.html) | Provide various options to control the behavior of BuildPipeline.BuildPlayer when using a build profile.  
[BuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildSettings.html) | Struct containing information on how to build content.  
[BuildStep](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildStep.html) |  Contains information about a single step in the build process. Additional resources: BuildReport.steps   
[BuildStepMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildStepMessage.html) |  Contains information about a single log message recorded during the build process. Additional resources: BuildStep.messages   
[BuildSummary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildSummary.html) | Contains overall summary information about a build.  
[BuildUsageTagGlobal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.BuildUsageTagGlobal.html) | Container for holding information about lighting information being used in a build.  
[CacheServerConnectionChangedParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServerConnectionChangedParameters.html) | Struct used for AssetDatabase.cacheServerConnectionChanged.  
[CameraProjectionCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraProjectionCache.html) | Project points from world to screen space.  
[ChangeAssetObjectPropertiesEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeAssetObjectPropertiesEventArgs.html) | A change of this type indicates that a property of an asset object in memory has changed. This happens for example when Undo.RecordObject is used with an instance of an asset (e.g. Texture). Note that this only covers changes to asset objects in memory and not changes to assets in the project on disk.  
[ChangeChildrenOrderEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeChildrenOrderEventArgs.html) | A change of this type indicates that a GameObject's children have been reordered. This happens when Undo.RegisterChildrenOrderUndo is called or when reordering a child in the hierarchy under the same parent.  
[ChangeGameObjectOrComponentPropertiesEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeGameObjectOrComponentPropertiesEventArgs.html) | A change of this type indicates that a property of a GameObject or Component has changed. This happens for example when Undo.RecordObject is used with an instance of a Component.  
[ChangeGameObjectParentEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeGameObjectParentEventArgs.html) | A change of this type indicates that the parent of a GameObject has changed. This happens when Undo.SetTransformParent or SceneManager.MoveGameObjectToScene is used.  
[ChangeGameObjectStructureEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeGameObjectStructureEventArgs.html) | A change of this type indicates that the structure of a GameObject has changed. This happens when a component is added to or removed from the GameObject using Undo.AddComponent or Undo.DestroyObjectImmediate.  
[ChangeGameObjectStructureHierarchyEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeGameObjectStructureHierarchyEventArgs.html) | A change of this type indicates that the structure of a GameObject has changed and any GameObject in the hierarchy below it might have changed. This happens for example when Undo.RegisterFullObjectHierarchyUndo is used.  
[ChangeRootOrderEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeRootOrderEventArgs.html) | A change of this type indicates that a GameObject placed at the scene root has been reordered. This happens when Undo.SetSiblingIndex is called or when reordering a root GameObject in the hierarchy under the same parent.  
[ChangeSceneEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ChangeSceneEventArgs.html) | A change of this type indicates that an open scene has been changed ("dirtied") without any more specific information available. This happens for example when EditorSceneManager.MarkSceneDirty is used.  
[ChannelClientInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelClientInfo.html) | A structure that contains all of a ChannelClient's connection data.  
[ChannelClientScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelClientScope.html) | Scope that can be use to open a channel client on a specific channel and close the channel when the scope ends.  
[ChannelInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelInfo.html) | A structure that contains the connection information of a Channel in ChannelService.  
[ChannelScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelScope.html) | Scope that cna be use to open a channel and that will close the channel when the scope ends.  
[ChildAnimatorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.ChildAnimatorState.html) | Structure that represents a state in the context of its parent state machine.  
[ChildAnimatorStateMachine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.ChildAnimatorStateMachine.html) | Structure that represents a state machine in the context of its parent state machine.  
[ChildMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.ChildMotion.html) | Structure that represents a motion in the context of its parent blend tree.  
[ClipAnimationInfoCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClipAnimationInfoCurve.html) | Stores a curve and its name that will be used to create additional curves during the import process.  
[CompilerMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilerMessage.html) | Compiler Message.  
[ContentBuildProfileEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildProfileEvent.html) | Details about a profile event captured using the ContentBuildInterface.BeginProfileCapture and ContentBuildInterface.EndProfileCapture APIs.  
[CreateAssetObjectEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CreateAssetObjectEventArgs.html) | A change of this type indicates that an asset object has been created. This happens for example when Undo.RegisterCreatedObjectUndo is used with an instance of an asset (e.g. Texture). Note that this only covers creation of asset objects in memory and not creation of new assets in the project on disk.  
[CreateGameObjectHierarchyEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CreateGameObjectHierarchyEventArgs.html) | A change of this type indicates that a GameObject has been created, possibly with additional objects below it in the hierarchy. This happens for example when Undo.RegisterCreatedObjectUndo is used with a GameObject.  
[CurveFilterOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.CurveFilterOptions.html) | The keyframe reduction settings for compressing animation curves.  
[CustomObjectIndexerTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.CustomObjectIndexerTarget.html) | Represents a descriptor for the object that is about to be indexed. It stores a reference to the object itself as well as an already set up SerializedObject.  
[DataModeChangeEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DataModeChangeEventArgs.html) | Container for the different parameters of the IDataModeController.dataModeChanged event.  
[DefaultPreset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.DefaultPreset.html) | This structure defines a default Preset. See Preset.GetDefaultListForType and Preset.SetDefaultListForType for usage.  
[DependencyInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.DependencyInfo.html) | Structure describing dependencies to other packages in PackageInfo.  
[DestroyAssetObjectEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DestroyAssetObjectEventArgs.html) | A change of this type indicates that an asset object has been destroyed. This happens for example when Undo.DestroyObjectImmediate is used with an instance of an asset (e.g. Texture). Note that this only covers destruction of asset objects in memory and not deletion of assets in the project on disk.  
[DestroyGameObjectHierarchyEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DestroyGameObjectHierarchyEventArgs.html) | A change of this type indicates that a GameObject and the entire hierarchy below it has been destroyed. This happens for example when Undo.DestroyObjectImmediate is used with an GameObject.  
[DetailBrushBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.DetailBrushBounds.html) | Represents a container for brush bound data.  
[DragAndDropWindowTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropWindowTarget.html) | IDs for core windows. These are used by the DragAndDrop.RemoveHandler API.  
[EditorCurveBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorCurveBinding.html) | Defines how a curve is attached to an object that it controls.  
[EventID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.EventID.html) | The EventID is used to keep track of asynchronous operations executing on a context. The ID describes the unique identifier of an event.  
[ExternalFileReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ExternalFileReference.html) | Desribes an externally referenced file. This is returned as part of the WriteResult when writing a serialized file.  
[GameManagerDependencyInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.GameManagerDependencyInfo.html) | Contains dependency information for internal Unity game manager classes. Call ContentBuildInterface.WriteGameManagersSerializedFile or ContentBuildInterface.CalculatePlayerDependenciesForGameManagers to get an instance of this class.  
[GlobalObjectId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GlobalObjectId.html) | Unique and stable project-scoped identifier for objects in scenes and in other types of assets for use at authoring time.  
[GpuBvhBuildOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Embree.GpuBvhBuildOptions.html) | Options for bounding volume hierarchy (BVH) build.  
[GpuBvhPrimitiveDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Embree.GpuBvhPrimitiveDescriptor.html) | Characteristics of a primitive used in the BVH build.  
[GraphViewChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphViewChange.html) | Set of changes in the graph that can be intercepted.  
[H264EncoderAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.H264EncoderAttributes.html) | Descriptor for H.264 encoder attributes.  
[InSceneAssetInformation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InSceneAssetInformation.html) | Provides information related to an in-scene asset collected during a InSceneAssetUtility.CollectInSceneAssets call.  
[KeyCombination](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.KeyCombination.html) | Represents a combination of a non-modifier key and zero or more modifier keys.  
[ManagedReferenceMissingType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedReferenceMissingType.html) | Represents a managed reference object that has a missing type.  
[MediaRational](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaRational.html) | Rational number useful for expressing fractions precisely.  
[MediaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaTime.html) | Time representation for use with media containers.  
[NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) | Build Target by name. This allows to describe and identify build targets that are not fully represented by BuildTargetGroup and BuildTarget.  
[NodeCreationContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.NodeCreationContext.html) | This struct represents the context when the user initiates creating a graph node.  
[ObjectChangeEventStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeEventStream.html) | Represents a stream of events that describes the changes applied to objects in memory over the course of a frame.  
[ObjectIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectIdentifier.html) | Struct that identifies a specific object project wide.  
[ObjectSerializedInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ObjectSerializedInfo.html) | Struct containing details about how an object was serialized.  
[PackedAssetInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.PackedAssetInfo.html) | Contains information about a single packed Asset.  
[ParseResult<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ParseResult_1.html) | A ParseResult represents the result of a parsing operation.  
[PickingIncludeExcludeList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PickingIncludeExcludeList.html) | Represents a list of Unity Object and DOTS Entity IDs that picking algorithms can either consider or discard.  
[PresetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Presets.PresetType.html) | Stores a type to which a Preset can be applied.  
[ProfilerCategoryInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.ProfilerCategoryInfo.html) | Category information descriptor structure.  
[ProfilerCounterDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Editor.ProfilerCounterDescriptor.html) | Provides a descriptor for a Profiler counter.  
[PropertyDatabaseRecordKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabaseRecordKey.html) | The key of a record that is stored in the PropertyDatabase.  
[QueryFilterOperator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryFilterOperator.html) | A QueryFilterOperator defines a boolean operator between a value returned by a filter and an operand inputted in the search query.  
[QueryGraphOptimizationOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryGraphOptimizationOptions.html) | Structure containing the different options used to optimize a query graph.  
[QueryToken](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryToken.html) | Represents a token of a query string.  
[QueryValidationOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryValidationOptions.html) | Struct containing the available query validation options.  
[RenderPickingArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingArgs.html) | Provides information about what is expected to render during the current picking rendering callback.  
[RenderPickingResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingResult.html) | This struct contains information to notify Unity the outcome of this render picking callback.  
[ResourceFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ResourceFile.html) | Details about a specific file written by the ContentBuildInterface.WriteSerializedFile or ContentBuildInterface.WriteSceneSerializedFile APIs.  
[Sample](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.UI.Sample.html) | Struct for Package Sample.  
[SceneDependencyInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.SceneDependencyInfo.html) | Scene dependency information generated from the ContentBuildInterface.PrepareScene API.  
[SceneStateHash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.SceneStateHash.html) | This class contains hashes that represents the Scene state.  
[ScenesUsingAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.ScenesUsingAsset.html) | Contains information about which scenes in a build have references to an Asset in the build.  
[ScriptCompilationResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Player.ScriptCompilationResult.html) | Struct with result information returned from the PlayerBuildInterface.CompilePlayerScripts API.  
[ScriptCompilationSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Player.ScriptCompilationSettings.html) | Struct containing information on how to build scripts.  
[SearchColumnCompareArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnCompareArgs.html) | Search column compare arguments are used by SearchColumn.comparer to sort search results.  
[SearchColumnEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnEventArgs.html) | Search column event arguments are used by SearchColumn.getter, SearchColumn.drawer and SearchColumn.setter delegates.  
[SearchDocument](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchDocument.html) | Represents a searchable document that has been indexed.  
[SearchExpressionContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.html) | This context encapsulate all the datas needed to evaluate a SearchExpression and it allows user to interact with the evaluation runtime of an expression. A SearchExpressionContext is created automatically with a SearchExpressionRuntime anytime SearchExpression.Execute is called.  
[SearchExpressionRuntime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionRuntime.html) | Encapsulate all the runtime data needed to evaluate a root expression and all its parameters. This class contains the SearchContext that created the root SearchExpression and all the stack frames needed to evaluate all the nested SearchExpression.  
[SearchField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchField.html) | Search item field used by the property table and selector systems.  
[SearchMonitorView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchMonitorView.html) | Scoped search monitor view.  
[SearchProposition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProposition.html) | Search propositions are used to display choices to the user to add new filters to a search query.  
[SearchResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchResult.html) | Contains a SearchItem that was retrieved from a query.  
[SearchSelectorArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchSelectorArgs.html) | Search selector arguments used when the search selector callback is invoked.  
[SearchValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchValue.html) | Search value is used to extend a query engine with custom type parsers and filters to search results by value.  
[SearchWindowContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.SearchWindowContext.html) | This structure includes parameters for configuring the search window.  
[SerializedLocation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.SerializedLocation.html) | Struct containing information about where an object was serialized.  
[ShaderCompilerData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderCompilerData.html) | Collection of data used for shader variants generation, including targeted platform data and the keyword set representing a specific shader variant.  
[ShaderInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderInfo.html) | Contains the following information about a shader: -If the shader has compilation errors or warnings. -If the shader is supported on the currently selected platform. -The name of the shader.  
[ShaderMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderMessage.html) | Contains information about messages generated by Unity's Shader Compiler.  
[ShaderSnippetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderSnippetData.html) | Collection of properties about the specific shader code being compiled.  
[ShortcutArguments](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutArguments.html) | Provides data for shortcut action methods invoked by the shortcut system.  
[ShortcutBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutBinding.html) | Represents a key binding used to trigger a shortcut.  
[ShortcutBindingChangedEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutBindingChangedEventArgs.html) | Provides data for the IShortcutManager.shortcutBindingChanged event.  
[SketchUpImportCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportCamera.html) | Structure to hold camera data extracted from a SketchUp file.  
[SketchUpImportScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportScene.html) | Structure to hold scene data extracted from a SketchUp file.  
[SpriteAtlasPackingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasPackingSettings.html) | Settings to use during the packing process for this SpriteAtlas.  
[SpriteAtlasTextureSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasTextureSettings.html) | Texture settings for the packed texture generated by SpriteAtlas.  
[SpriteImportData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.SpriteImportData.html) | Struct that represents how Sprite asset should be generated when calling TextureGenerator.GenerateTexture.  
[SpriteMetaData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMetaData.html) | Editor data used in producing a Sprite.  
[StageHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.StageHandle.html) | Struct that represents a stage handle.  
[StringView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.StringView.html) | Structure that holds a view on a string, with a specified range of [startIndex, endIndex[.  
[TakeInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TakeInfo.html) | A Takeinfo object contains all the information needed to describe a take.  
[TextureGenerationOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.TextureGenerationOutput.html) | Structure that represents the result from calling TextureGenerator.GenerateTexture.  
[TextureGenerationSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.TextureGenerationSettings.html) | Represents how a texture should be generated from calling TextureGenerator.GenerateTexture.  
[TexturePropertyDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.TexturePropertyDescription.html) | Contains a set of typed properties for describing a texture input of a MaterialDescription.  
[TierSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.TierSettings.html) | A struct that represents graphics settings for a given build target and graphics tier.  
[TouchEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceSimulation.TouchEvent.html) | Representation of a single touch event coming from a Device Simulator. Subscribe to DeviceSimulator.touchScreenInput to receive these events.  
[UndoPropertyModification](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UndoPropertyModification.html) | Additional resources: Undo.postprocessModifications.  
[UndoRedoInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UndoRedoInfo.html) | Additional resources: Undo.undoRedoEvent.  
[UnwrapParam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnwrapParam.html) | Unwrapping settings.  
[UpdatePrefabInstancesEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UpdatePrefabInstancesEventArgs.html) | A change of this type indicates that prefab instances in an open scene have been updated due to a change to the source prefab.  
[VideoTrackAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackAttributes.html) | Descriptor for audio track format.  
[VideoTrackEncoderAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackEncoderAttributes.html) | Descriptor for video track format.  
[VP8EncoderAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VP8EncoderAttributes.html) | Descriptor for VP8 encoder attributes.  
[WriteManagerParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.WriteManagerParameters.html) | Defines the write parameters for the ContentBuildInterface.WriteGameManagersSerializedFile function.  
[WriteParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.WriteParameters.html) | This struct collects all the WriteSerializedFile parameters in to a single place.  
[WriteResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.WriteResult.html) | Struct containing the results from the ContentBuildPipeline.WriteSerialziedFile and ContentBuildPipeline.WriteSceneSerialziedFile APIs.  
[WriteSceneParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.WriteSceneParameters.html) | This struct collects all the WriteSceneSerializedFile parameters in to a single place.  
### Enumerations
Enumeration | Description  
---|---  
[ActionOnDotNetUnhandledException](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ActionOnDotNetUnhandledException.html) | The behavior in case of unhandled .NET exception.  
[AdvancedObjectSelectorEventType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.AdvancedObjectSelectorEventType.html) | Enum that defines the type of events that are possible when calling a custom advanced object selector.  
[AndroidApplicationEntry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidApplicationEntry.html) | Options for which application entries to include when Unity generates a Gradle project.  
[AndroidArchitecture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidArchitecture.html) | Android CPU architecture.  
[AndroidAutoRotationBehavior](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidAutoRotationBehavior.html) | Options to control the application window orientation when Default orientation is set to Auto rotation.  
[AndroidBlitType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidBlitType.html) | Describes the method for how content is displayed on the screen.  
[AndroidBuildSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidBuildSystem.html) | Type of Android build system.  
[AndroidBuildType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidBuildType.html) | Build configurations for the generated project.  
[AndroidETC2FallbackOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidETC2FallbackOverride.html) | This enumeration has values for different qualities to decompress an ETC2 texture on Android devices that don't support the ETC2 texture format.  
[AndroidGamepadSupportLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidGamepadSupportLevel.html) | Gamepad support level for Android TV.  
[AndroidPreferredInstallLocation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidPreferredInstallLocation.html) | Preferred application install location.  
[AndroidSdkVersions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidSdkVersions.html) | API levels that can be specified in scripts. Note that the lowest API level here strictly corresponds to the lowest supported API level, however these values should not be used to determine the highest supported API level.  
[AndroidShowActivityIndicatorOnLoading](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidShowActivityIndicatorOnLoading.html) | Application should show ActivityIndicator when loading.  
[AndroidSplashScreenScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidSplashScreenScale.html) | Android splash screen scale modes.  
[AnimatorConditionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorConditionMode.html) | The mode of the condition.  
[AnimatorLayerBlendingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorLayerBlendingMode.html) | Specifies how the layer is blended with the previous layers.  
[ApiCompatibilityLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApiCompatibilityLevel.html) | .NET API compatibility level.  
[AppleMobileArchitecture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AppleMobileArchitecture.html) | Apple Mobile CPU architecture.  
[AppleMobileArchitectureSimulator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AppleMobileArchitectureSimulator.html) | Apple mobile CPU architecture options for the Simulator.  
[AscentCalculationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AscentCalculationMode.html) | Method used for calculating a font's ascent.  
[AssembliesType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.AssembliesType.html) | Flags for Assembly.  
[AssemblyBuilderFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.AssemblyBuilderFlags.html) | Flags used by AssemblyBuilder to control assembly build.  
[AssemblyBuilderStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.AssemblyBuilderStatus.html) | Status of the AssemblyBuilder build.  
[AssemblyDefinitionReferenceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.AssemblyDefinitionReferenceType.html) | Assembly definition file reference type.  
[AssemblyFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.AssemblyFlags.html) | Flags for Assembly.  
[AssetDeleteResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDeleteResult.html) | Result of Asset delete operation  
[AssetMoveResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetMoveResult.html) | Result of Asset move  
[AssetPathToGUIDOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPathToGUIDOptions.html) | Asset path to GUID options.  
[AssetPipelineMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPipelineMode.html) | Selects the Assetpipeline mode to use.  
[AudioSampleRateSetting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSampleRateSetting.html) | The sample rate setting used within the AudioImporter. This defines the sample rate conversion of audio on import.  
[BatchRendererGroupStrippingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroupStrippingMode.html) | Enum of the different modes of operation for BatchRendererGroup shader variant stripping.  
[BlendTreeType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BlendTreeType.html) | The type of blending algorithm that the blend tree uses.  
[BrushGUIEditFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.BrushGUIEditFlags.html) | Flags that specify which brush controls the [IOnInspectorGUI.ShowBrushesGUI] method displays.  
[BuildAssetBundleOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.html) | Asset Bundle building options.  
[BuildOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.html) | Options to configure a build. You can combine multiple build options together.  
[BuildResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildResult.html) | Describes the outcome of the build process.  
[BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) | Target build platform.  
[BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) | Build target group.  
[BuildType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Reporting.BuildType.html) | Build type.  
[CacheServerMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServerMode.html) | Selects the cache server configuration mode.  
[CacheServerValidationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServerValidationMode.html) | Options for the accelerate server validation mode.  
[CanAppendBuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanAppendBuild.html) | Whether you can append an existing build using BuildOptions.AcceptExternalModificationsToPlayer.  
[Capabilities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Capabilities.html) | Capabilities used by Manipulators to easily determine valid actions on a GraphElement.  
[CheckoutMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.CheckoutMode.html) | What to checkout when starting the Checkout task through the version control Provider.  
[ClipAnimationMaskType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ClipAnimationMaskType.html) | AnimationClip mask options for ModelImporterClipAnimation.  
[CodeOptimization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CodeOptimization.html) | Code optimization mode defines whether UnityEditor compiles scripts in Debug or Release mode.  
[CompilerMessageType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.CompilerMessageType.html) | Compiler message type.  
[CompletionAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.CompletionAction.html) | Different actions a version control task can do upon completion.  
[ContentBuildFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ContentBuildFlags.html) | Build options for content.  
[CoppaCompliance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CoppaCompliance.html) | The enumerated states of the project's Coppa compliance setting.  
[D3D11FullscreenMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/D3D11FullscreenMode.html) | Direct3D 11 fullscreen mode.  
[DataMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DataMode.html) | Options for the different DataModes of an EditorWindow.  
[DependencyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.DependencyType.html) | Dependency calculation flags to control what is returned, and how it operates.  
[DialogOptOutDecisionType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DialogOptOutDecisionType.html) | The type of opt-out decision a user can make.  
[Direction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Direction.html) | Port direction (in or out).  
[DisplayMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.DisplayMode.html) | Options for setting the display mode to use for a search view.  
[DockPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.DockPosition.html) | DockPosition describes the alignment of an Overlay within a DockZone.  
[DockZone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.DockZone.html) | DockZone describes the area of the screen that an Overlay is displayed in.  
[DragAndDropVisualMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.html) | Visual indication mode for Drag & Drop operation.  
[DrawCameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.html) | Drawing modes for Handles.DrawCamera.  
[EditorActionResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Actions.EditorActionResult.html) | The state that the EditorAction was completed in.  
[EditorAssembliesCompatibilityLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorAssembliesCompatibilityLevel.html) | .NET API compatibility level.  
[EditorSelectedRenderState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSelectedRenderState.html) | The editor selected render mode for Scene View selection.  
[EditorSkin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSkin.html) | Enum that selects which skin to return from EditorGUIUtility.GetBuiltinSkin.  
[EnterPlayModeOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EnterPlayModeOptions.html) | Determines the flags for the Enter Play Mode Options in the Unity Editor.  
[ErrorCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.ErrorCode.html) | Package operation Error.  
[EventDataSerialization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventDataSerialization.html) | The Serialization type for sending a message, with arguments, using the EventService. For more information about argument serialization, see ChannelService.Broadcast and ChannelService.Emit.  
[EventPropagation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.EventPropagation.html) | Value that determines if a event handler stops propagation of events or allows it to continue.  
[ExportPackageOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExportPackageOptions.html) | Export package option. Multiple options can be combined together using the | operator.  
[FetchPreviewOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FetchPreviewOptions.html) | Options for the search provider on how the preview should be fetched.  
[FileMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.FileMode.html) | Mode of the file.  
[FileType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.FileType.html) | Enum description of the type of file an object comes from.  
[FilterAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.FilterAction.html) | Whether shader keyword filter attributes include the keywords, remove the keywords or do nothing, based on the attribute condition evaluation.  
[FoliageIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.FoliageIndex.html) | The index at which you should place the foliage tools in the Terrain Tools overlay.  
[FontRenderingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FontRenderingMode.html) | Font rendering mode constants for TrueTypeFontImporter.  
[FontTextureCase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FontTextureCase.html) | Texture case constants for TrueTypeFontImporter.  
[ForceReserializeAssetsOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ForceReserializeAssetsOptions.html) | Options for AssetDatabase.ForceReserializeAssets.  
[GfxThreadingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GfxThreadingMode.html) | Enum used to specify the threading mode to use.  
[GizmoType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GizmoType.html) | Determines how a gizmo is drawn or picked in the Unity editor.  
[GpuBvhBuildQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Embree.GpuBvhBuildQuality.html) | BVH build quality.  
[GraphicsJobMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsJobMode.html) | Enum used to specify the graphics jobs mode to use.  
[HierarchyDropFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HierarchyDropFlags.html) | Define how dragged objects should be dropped relative to already existing Hierarchy items.  
[HighlightSearchMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HighlightSearchMode.html) | Used to specify how to find a given element in the editor to highlight.  
[IconKind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IconKind.html) | Icon kind.  
[IconOverlayType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.IconOverlayType.html) | Type of icon overlay.  
[Il2CppCodeGeneration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Il2CppCodeGeneration.html) | Options to control code generation for IL2CPP compiler.  
[Il2CppCompilerConfiguration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Il2CppCompilerConfiguration.html) | C++ compiler configuration used when compiling IL2CPP generated code.  
[Il2CppStacktraceInformation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Il2CppStacktraceInformation.html) | Stack trace information options to choose how much information to include in IL2CPP generated stack traces.  
[ImportAssetOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImportAssetOptions.html) | Asset importing options.  
[ImportLogFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ImportLogFlags.html) | A value indicating the severity of an import log.  
[IndexingOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IndexingOptions.html) | Use Indexing options to specify the contents of your search index.  
[InsecureHttpOption](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InsecureHttpOption.html) | Options for allowing plain text HTTP connections for UnityWebRequest.  
[InteractionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html) | The mode of interaction, user or automated, that an API method is called with.  
[iOSAppInBackgroundBehavior](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOSAppInBackgroundBehavior.html) | Application behavior when entering background.  
[iOSBackgroundMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOSBackgroundMode.html) | Background modes supported by the application corresponding to project settings in Xcode.  
[iOSLaunchScreenImageType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOSLaunchScreenImageType.html) | iOS launch screen settings.  
[iOSLaunchScreenType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOSLaunchScreenType.html) | iOS launch screen settings.  
[iOSSdkVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOSSdkVersion.html) | Supported iOS SDK versions.  
[iOSShowActivityIndicatorOnLoading](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOSShowActivityIndicatorOnLoading.html) | Activity Indicator on loading.  
[iOSStatusBarStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOSStatusBarStyle.html) | iOS status bar style.  
[iOSTargetDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOSTargetDevice.html) | Target iOS device.  
[Layout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Layout.html) | Possible layouts for an overlay.  
[LineEndingsMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineEndingsMode.html) | Defines the type of line endings used when creating new C# files from within the editor.  
[LogLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.LogLevel.html) | Describes different levels of log information the Package Manager supports.  
[MacFullscreenMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MacFullscreenMode.html) | Mac fullscreen mode.  
[ManagedStrippingLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedStrippingLevel.html) | Defines how aggressively Unity strips unused managed (C#) code.  
[MaterialIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.MaterialIndex.html) | The index at which you should place the material tools in the Terrain Tools overlay.  
[MeshDeformation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshDeformation.html) | Specifies which method Unity uses to process mesh deformations for skinning.  
[MeshOptimizationFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshOptimizationFlags.html) | Options to control the optimization of mesh data during asset import.  
[MessageType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MessageType.html) | User message types.  
[MobileTextureSubtarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MobileTextureSubtarget.html) | Compressed texture format for target build platform.  
[ModelImporterAnimationCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterAnimationCompression.html) | Animation compression options for ModelImporter.  
[ModelImporterAnimationType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterAnimationType.html) | Animation mode for ModelImporter.  
[ModelImporterAvatarSetup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterAvatarSetup.html) | Set the Avatar generation mode for ModelImporter.  
[ModelImporterGenerateAnimations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterGenerateAnimations.html) | Animation generation options for ModelImporter. These options relate to the legacy Animation system, they should only be used when ModelImporter.animationType==ModelImporterAnimationType.Legacy.  
[ModelImporterHumanoidOversampling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterHumanoidOversampling.html) | Humanoid Oversampling available multipliers.  
[ModelImporterIndexFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterIndexFormat.html) | Format of the imported mesh index buffer data.  
[ModelImporterMaterialImportMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterMaterialImportMode.html) | Material import options for ModelImporter.  
[ModelImporterMaterialLocation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterMaterialLocation.html) | Material import options for ModelImporter.  
[ModelImporterMaterialName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterMaterialName.html) | Material naming options for ModelImporter.  
[ModelImporterMaterialSearch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterMaterialSearch.html) | Material search options for ModelImporter.  
[ModelImporterMeshCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterMeshCompression.html) | Mesh compression options for ModelImporter.  
[ModelImporterNormalCalculationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterNormalCalculationMode.html) | Normal generation options for ModelImporter.  
[ModelImporterNormals](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterNormals.html) | Normal generation options for ModelImporter.  
[ModelImporterNormalSmoothingSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterNormalSmoothingSource.html) | Source of smoothing information for calculation of normals in ModelImporter.  
[ModelImporterSecondaryUVMarginMethod](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterSecondaryUVMarginMethod.html) | Methods for handling margins during lightmap UV generation in ModelImporter.  
[ModelImporterSkinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterSkinWeights.html) | Skin weights options for ModelImporter.  
[ModelImporterTangents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterTangents.html) | Vertex tangent generation options for ModelImporter.  
[ModelImporterTangentSpaceMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporterTangentSpaceMode.html) | Tangent space generation options for ModelImporter.  
[MouseCursor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MouseCursor.html) | Custom mouse cursor shapes used with EditorGUIUtility.AddCursorRect.  
[NeighborTerrainsIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.NeighborTerrainsIndex.html) | The index at which you should place the neighbor terrain tools in the Terrain Tools overlay.  
[NewSceneMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.NewSceneMode.html) | Used when creating a new Scene in the Editor.  
[NewSceneSetup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.NewSceneSetup.html) | Used when creating a new Scene in the Editor.  
[NormalMapEncoding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NormalMapEncoding.html) | Describes the encoding of normal maps.  
[ObjectChangeKind](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectChangeKind.html) | This enumeration describes the different kind of changes that can be tracked in an ObjectChangeEventStream. Each event has a corresponding type in ObjectChangeEvents.  
[ObjectMatchMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectMatchMode.html) | Enum for controlling how e.g. GameObjects and Components are matched.  
[ObjectSelectorSearchEndSessionModes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ObjectSelectorSearchEndSessionModes.html) | A bit field that contains the different modes to end an Object Selector Search session.  
[OnlineState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.OnlineState.html) | Represent the connection state of the version control provider.  
[OnOpenAssetAttributeMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Callbacks.OnOpenAssetAttributeMode.html) | Indicates whether OnOpenAssetAttribute decorated method is a validation function that checks if asset opening is handled by Unity or a custom script.  
[OpenSceneMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.OpenSceneMode.html) | Used when opening a Scene in the Editor to specify how a Scene should be opened.  
[Orientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Orientation.html) | Graph element orientation.  
[OSArchitecture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.OSArchitecture.html) | Enum representing processor architectures that are supported by certain operating systems.  
[OverrideTextureCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.OverrideTextureCompression.html) | Sets which texture compression override to use when importing assets.  
[PackageSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageSource.html) | Source of packages.  
[PauseState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PauseState.html) | Enumeration specifying the current pause state of the Editor.Additional resources: PlayModeStateChange, EditorApplication.pauseStateChanged, EditorApplication.isPaused.  
[PivotMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PivotMode.html) | Where is the tool handle placed.  
[PivotRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PivotRotation.html) | How is the tool handle oriented.  
[PlayerConnectionInitiateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerConnectionInitiateMode.html) | Describes how the player connects to the Editor.  
[PlayModeStateChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayModeStateChange.html) | Enumeration specifying a change in the Editor's play mode state.Additional resources: PauseState, EditorApplication.playModeStateChanged, EditorApplication.isPlaying.  
[PrefabAssetType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabAssetType.html) | Enum indicating the type of Prefab Asset, such as Regular, Model and Variant.  
[PrefabInstanceStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabInstanceStatus.html) | Enum with status about whether a Prefab instance is properly connected to its asset.  
[PrefabOverridesOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabOverridesOptions.html) | Flags that can be used to control which overrides shoud be kept or cleared when using ReplacePrefabAssetOfPrefabInstance.  
[PrefabUnpackMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUnpackMode.html) | Enum used to determine how a Prefab should be unpacked.  
[PreprocessorOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PreprocessorOverride.html) | This enum is now obsolete. Unity always uses the Caching Shader Preprocessor.  
[ProcessEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessEvent.html) | Enum that represents the events a RoleProvider can receive.  
[ProcessLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessLevel.html) | The type of the current process. It can be a Unity master instance, or a secondary instance connected to the master.  
[ProcessState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ProcessState.html) | Describes the state of a specifc UnityEditor process.  
[ProfileCaptureOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ProfileCaptureOptions.html) | Options for filtering captured profile events using the ContentBuildInterface.BeginProfileCapture and ContentBuildInterface.EndProfileCapture APIs.  
[ProfileEventType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Content.ProfileEventType.html) | Options for labelling captured profile events using the ContentBuildInterface.BeginProfileCapture and ContentBuildInterface.EndProfileCapture APIs.  
[ProfilerModuleChartType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Editor.ProfilerModuleChartType.html) | Options for a Profiler module’s chart type.  
[PropertyDatabaseType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.PropertyDatabaseType.html) | An enum representing the type of data stored in a record.  
[ProvisioningProfileType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ProvisioningProfileType.html) | The type of the iOS provisioning profile if manual signing is used.  
[QueryNodeType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryNodeType.html) | Options for representing the query node types.  
[ReferencesOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.ReferencesOptions.html) | Options to control the Unity References to other assembly definition files that Unity uses during compilation.  
[RefreshFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.RefreshFlags.html) | Refresh flags are used to indicate why search view needs to be refreshed or updated.  
[RemoveAssetOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RemoveAssetOptions.html) | Options for removing assets  
[RenderPickingType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderPickingType.html) | Specifies the type of a render picking callback.  
[RepaintFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.RepaintFlags.html) | Flags that indicate what to repaint on the Terrain tools.  
[RequestScriptCompilationOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compilation.RequestScriptCompilationOptions.html) | Options for specifying the behavior of CompilationPipeline.RequestScriptCompilation.  
[ResizerDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ResizerDirection.html) | Enum that specifies in which direction to resize the element.  
[ResolveMethod](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.ResolveMethod.html) | How assets should be resolved.  
[RevertMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.RevertMode.html) | Defines the behaviour of the version control revert methods.  
[ScriptCallOptimizationLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptCallOptimizationLevel.html) | Script call optimization level.  
[ScriptCompilationOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Player.ScriptCompilationOptions.html) | Script compilation options.  
[ScriptingImplementation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptingImplementation.html) | Scripting implementation (backend).  
[SculptIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.SculptIndex.html) | The index at which you should place the sculpt tools in the Terrain Tools overlay.  
[SearchColumnFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchColumnFlags.html) | Search column flags are used to set multiple states.  
[SearchDocumentFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchDocumentFlags.html) | Search document flags are used by the indexing system to provide additional information of an indexed document, like its source.  
[SearchEngineScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.SearchEngineScope.html) | An enumeration that contains the available search engine scopes.  
[SearchExpressionEvaluationHints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionEvaluationHints.html) | Hints provided to the SearchExpression runtime to specify how a certain SearchExpressionEvaluatorAttribute should be executed.  
[SearchExpressionKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionKeyword.html) | Enum contaning all keywords used as configuration parameter in builtin evaluator of SearchExpression.  
[SearchExpressionType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.html) | Type used to characterize an expression. An expression might have multiple types. For example a Set is also an iterable. A keyword is also considered a string value. SearchExpressionType can be used with SearchExpressionEvaluatorAttribute to describe the parameter list of an evaluator.  
[SearchFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchFlags.html) | Search options used to fetch items. Mostly with SearchContext to specify how a search should be handled.  
[SearchItemOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemOptions.html) | Indicates how the search item description needs to be formatted when presented to the user.  
[SearchPropositionFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchPropositionFlags.html) | The search proposition flags are used to give additional context to the search proposition.  
[SearchQueryErrorType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchQueryErrorType.html) | Enum representing the possible types of query errors.  
[SelectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.html) | SelectionMode can be used to tweak the selection returned by Selection.GetTransforms.  
[SemanticMergeMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SemanticMergeMode.html) | Behavior of semantic merge.  
[SerializedPropertyNumericType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyNumericType.html) | Returns the precise type for Integer or Floating point properties.  
[SerializedPropertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.html) | Represents the type of a SerializedProperty.  
[SettingsScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsScope.html) | Sets the scope of a SettingsProvider. The Scope determines where it appears in the UI. For example, whether it appears with the Project settings in the Settings window, or in the Preferences window, or in both windows.  
[ShaderCompilerMessageSeverity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderCompilerMessageSeverity.html) | Indicates the severity of a message returned by the Unity Shader Compiler.  
[ShaderCompilerPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderCompilerPlatform.html) | Shader compiler used to generate player data shader variants.  
[ShaderPrecisionModel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderPrecisionModel.html) | Options for the shader precision model.  
[ShaderQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderQuality.html) | Shader quality preset.  
[ShaderRequirements](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderRequirements.html) | Shader features required by a specific shader. Features are bit flags.  
[ShaderType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderType.html) | Identifies the stage in the rendering pipeline.  
[ShortcutModifiers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutModifiers.html) | Represents modifier keys for use in a shortcut binding.  
[ShortcutStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShortcutManagement.ShortcutStage.html) | Represents the stage at which a shortcut action was invoked.  
[ShowDetailsOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.html) | Defines what details are shown in the preview inspector panel for the search view.  
[SpriteImportMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteImportMode.html) | Texture importer modes for Sprite import.  
[SpritePackerMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpritePackerMode.html) | Sprite Packer mode for the current project.  
[StandaloneBuildSubtarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StandaloneBuildSubtarget.html) | Desktop platform subtarget type.  
[StaticEditorFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.html) | Describes which Unity systems consider the GameObject as static, and include the GameObject in their precomputations in the Unity Editor.  
[StatusCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.StatusCode.html) | Unity Package Manager operation status.  
[StatusQueryOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StatusQueryOptions.html) | Options for querying the version control system status of a file.  
[StereoRenderingPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StereoRenderingPath.html) | Enum used to specify what stereo rendering path to use.  
[StickyNoteChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.StickyNoteChange.html) | Enum that specifies the type of change to the [StickyNote].  
[StickyNoteFontSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.StickyNoteFontSize.html) | Enum used to describe the font size used by the [StickyNote].  
[StickyNoteTheme](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.StickyNoteTheme.html) | Enum used to describe the visual theme used by the [StickyNote].  
[StrippingLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StrippingLevel.html) | Managed code stripping level.  
[SubmitResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.SubmitResult.html) | The status of an operation returned by the VCS.  
[TemplateInstantiationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.TemplateInstantiationMode.html) | An enumeration of options for handling a Scene dependency Asset when you instantiate a SceneTemplateAsset.  
[TerrainBrushPreviewMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainBrushPreviewMode.html) | Enum to specify whether DrawBrushPreview previews the source render texture or the destination render texture of a PaintContext.  
[TerrainCategory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainTools.TerrainCategory.html) | A category with which to define tools that inherit from the ITerrainPaintToolWithOverlays interface.  
[TerrainDetailMeshRenderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainDetailMeshRenderMode.html) | Options for determining the render mode of the mesh detail.  
[TextCursorPlacement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.TextCursorPlacement.html) | Where to place the cursor in the text. (see ISearchView.SetSearchText).  
[TextureCompressionFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureCompressionFormat.html) | Options for the compressed texture formats that are available on the target build platform.  
[TextureCompressionQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureCompressionQuality.html) | Compression Quality.  
[TextureImporterAlphaSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterAlphaSource.html) | Select how the alpha of the imported texture is generated.  
[TextureImporterCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterCompression.html) | Select the kind of compression you want for your texture.  
[TextureImporterCubemapConvolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterCubemapConvolution.html) | Defines Cubemap convolution mode.  
[TextureImporterFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.html) | Imported texture format for TextureImporter.  
[TextureImporterGenerateCubemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterGenerateCubemap.html) | Cubemap generation mode for TextureImporter.  
[TextureImporterMipFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterMipFilter.html) | Mip map filter for TextureImporter.  
[TextureImporterNormalFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterNormalFilter.html) | Normal map filtering mode for TextureImporter.  
[TextureImporterNPOTScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterNPOTScale.html) | Scaling mode for non power of two textures in TextureImporter.  
[TextureImporterRGBMMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterRGBMMode.html) | RGBM encoding mode for HDR textures in TextureImporter.  
[TextureImporterShape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterShape.html) | The shape of the imported texture.  
[TextureImporterSingleChannelComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSingleChannelComponent.html) | Selects which Color/Alpha channel Single Channel Textures uses.  
[TextureImporterSwizzle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSwizzle.html) | Options for where texture color channel data comes from in the TextureImporter.  
[TextureImporterType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterType.html) | Select this to set basic parameters depending on the purpose of your texture.  
[TextureResizeAlgorithm](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureResizeAlgorithm.html) | For Texture to be scaled down choose resize algorithm. ( Applyed only when Texture dimension is bigger than Max Size ).  
[Tool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tool.html) | Which tool is active in the editor.  
[TouchPhase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceSimulation.TouchPhase.html) | Indicates where in its lifecycle a given touch is.  
[TransitionInterruptionSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.TransitionInterruptionSource.html) | Which AnimatorState transitions can interrupt the Transition.  
[TreeViewSelectionOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewSelectionOptions.html) | Enum used by the TreeView.SetSelection method.  
[tvOSSdkVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/tvOSSdkVersion.html) | Supported tvOS SDK versions.  
[UIOrientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIOrientation.html) | Default mobile device orientation.  
[VertexChannelCompressionFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VertexChannelCompressionFlags.html) | Use these enum flags to specify which elements of a vertex to compress.  
[VideoBitrateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoBitrateMode.html) | Bit rate after the clip is transcoded.  
[VideoCodec](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoCodec.html) | Choose the video codec to use to import video clips.  
[VideoDeinterlaceMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoDeinterlaceMode.html) | Describes how the fields in the image, if any, should be interpreted.  
[VideoEncodeAspectRatio](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoEncodeAspectRatio.html) | Methods to compensate for aspect ratio discrepancies between the source resolution and the wanted encoding size.  
[VideoEncodingProfile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoEncodingProfile.html) | Use the options in this enumeration to change the encoder profile.  
[VideoResizeMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoResizeMode.html) | How the video clip's images will be resized during transcoding.  
[VideoSpatialQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VideoSpatialQuality.html) | Controls the imported clip's internal resize to save space at the cost of blurrier images.  
[ViewTool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ViewTool.html) | Enum for Tools.viewTool.  
[VisibleObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.VisibleObjects.html) | A bit field that contains the different categories of object that the object selector window can display.  
[VisionOSSdkVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VisionOSSdkVersion.html) | Supported VisionOS SDK versions.  
[WebGLClientBrowserType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLClientBrowserType.html) | An enum containing the supported client web browsers.  
[WebGLCompressionFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLCompressionFormat.html) | An enum containing different compression types.  
[WebGLDebugSymbolMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLDebugSymbolMode.html) | An enum containing different modes for debug symbols.  
[WebGLExceptionSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLExceptionSupport.html) | Options for Exception support in WebGL.  
[WebGLLinkerTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLLinkerTarget.html) | The build format options available when building to WebGL.  
[WebGLMemoryGrowthMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLMemoryGrowthMode.html) | An enum containing different memory growth modes.  
[WebGLPowerPreference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLPowerPreference.html) | An enum containing different power preference hints for the WebGL context.  
[WebGLTextureSubtarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLTextureSubtarget.html) | Compressed texture format for target build platform.  
[WebGLWasmArithmeticExceptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLWasmArithmeticExceptions.html) | An enum containing different trapping modes for WebAssembly code.  
[WindowsBuildAndRunDeployTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WindowsBuildAndRunDeployTarget.html) | Specifies which Windows device to deploy and launch the Windows app on when using Build and Run from the Editor.  
[WindowsGamepadBackendHint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WindowsGamepadBackendHint.html) | Specifies the desired Windows API to be used for input.  
[WSABuildAndRunDeployTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSABuildAndRunDeployTarget.html) | Specifies the Windows device to deploy and launch the UWP app on when using Build and Run from the Editor.  
[WSABuildType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSABuildType.html) | Build configurations for Windows Store Visual Studio solutions.  
[WSAUWPBuildType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSAUWPBuildType.html) | Determines the output build type when building to Universal Windows Platform.  
[XboxBuildSubtarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XboxBuildSubtarget.html) | Target Xbox build type.  
[XcodeBuildConfig](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XcodeBuildConfig.html) | Build configurations for the Xcode project Unity generates.  
* * *
