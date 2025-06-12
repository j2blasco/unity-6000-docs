* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html

# UnityEngine.CoreModule
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
The Core module implements basic classes required for Unity to function.
This module cannot be disabled.
### Classes
Class | Description  
---|---  
[AddComponentMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AddComponentMenu.html) | The AddComponentMenu attribute allows you to place a script anywhere in the "Component" menu, instead of just the "Component->Scripts" menu.  
[AlwaysLinkAssemblyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.AlwaysLinkAssemblyAttribute.html) | Ensure an assembly is always processed during managed code stripping.  
[AnimationCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) | Store a collection of Keyframes that can be evaluated over time.  
[Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.html) | Provides access to application runtime data.  
[Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Application.html) | Provides essential methods related to Window Store application.  
[Application](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Application.html) | Access to platform-specific application runtime data.  
[ArchiveFileInterface](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveFileInterface.html) | Provides methods for managing Unity archive files.  
[Arguments](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DedicatedServer.Arguments.html) | DedicatedServer.Arguments provides accessors for common CLI options  
[AssemblyIsEditorAssembly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssemblyIsEditorAssembly.html) | Assembly level attribute. Any classes in an assembly with this attribute will be considered to be Editor Classes.  
[Assert](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.html) | The Assert class contains assertion methods for setting invariants in the code.  
[AssertionException](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.AssertionException.html) | An exception that is thrown when an assertion fails.  
[AsyncGPUReadback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadback.html) | Allows the asynchronous read back of GPU resources.  
[AsyncInstantiateOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncInstantiateOperation.html) | Asynchronous instantiate operation on UnityEngine.Object type.  
[AsyncInstantiateOperation<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncInstantiateOperation_1.html) | Provides a generic method to instantiate operations asynchronously on a UnityEngine.Object.  
[AsyncOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AsyncOperation.html) | Asynchronous operation coroutine.  
[AsyncReadManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManager.html) | With the AsyncReadManager, you can perform asynchronous I/O operations through Unity's virtual file system. You can perform these operations on any thread or job.  
[AsyncReadManagerMetrics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.html) | Manages the recording and retrieval of metrics from the AsyncReadManager.  
[AsyncReadManagerMetricsFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html) | Defines a filter for selecting specific categories of data when summarizing AsyncReadManager metrics.  
[AsyncReadManagerSummaryMetrics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.html) | A summary of the metrics collected for AsyncReadManager read operations.  
[Awaitable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.html) | Custom Unity type that can be awaited and used as an async return type in the C# asynchronous programming model.  
[Awaitable<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable_1.html) | Custom Unity type that can be awaited and used as an async return type in the C# asynchronous programming model.  
[AwaitableCompletionSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AwaitableCompletionSource.html) | Objects allowing to control completion of an Awaitable object from user code.  
[AwaitableCompletionSource<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AwaitableCompletionSource_1.html) | Objects allowing to control completion of an Awaitable object from user code.  
[BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.html) | A BatchRendererGroup is an object that lets you perform customizable high performance rendering.  
[BeforeRenderOrderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BeforeRenderOrderAttribute.html) | Use this BeforeRenderOrderAttribute when you need to specify a custom callback order for Application.onBeforeRender.  
[Behaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour.html) | Behaviours are Components that can be enabled or disabled.  
[BillboardAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardAsset.html) | BillboardAsset describes how a billboard is rendered.  
[BillboardRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BillboardRenderer.html) | Renders a billboard from a BillboardAsset.  
[BurstAuthorizedExternalMethodAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Burst.BurstAuthorizedExternalMethodAttribute.html) | The BurstAuthorizedExternalMethod attribute lets you mark a function as being authorized for Burst to call from within a static constructor.  
[BurstDiscardAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Burst.BurstDiscardAttribute.html) | Use this attribute to exclude a method or property from being compiled to native code by the Burst compiler.  
[Caching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html) | The Caching class lets you manage cached AssetBundles, downloaded using UnityWebRequestAssetBundle.GetAssetBundle.  
[Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) | A Camera is a device through which the player views the world.  
[CategoryInfoAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Categorization.CategoryInfoAttribute.html) | Provide a information to order and categorize at category level.  
[CollectionPool<T0,T1>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.CollectionPool_2.html) | A Collection such as List, HashSet, Dictionary etc can be pooled and reused by using a CollectionPool.  
[ColorGamutUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorGamutUtility.html) | Utility class to query properties of a ColorGamut.  
[ColorUsageAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorUsageAttribute.html) | Attribute used to configure the usage of the ColorField and Color Picker for a color.  
[ColorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorUtility.html) | A collection of common color functions.  
[CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) | List of graphics commands to execute.  
[CommandBufferExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBufferExtensions.html) | Static class providing extension methods for CommandBuffer.  
[Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) | Base class for everything attached to a GameObject.  
[ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) | GPU data buffer, mostly for use with compute shaders.  
[ComputeShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html) | Compute Shader asset.  
[ContextMenu](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContextMenu.html) | Use the ContextMenu attribute to add commands to the context menu of the Inspector window.  
[ContextMenuItemAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContextMenuItemAttribute.html) | Use this attribute to add a context menu to a field that calls a named method.  
[Coroutine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Coroutine.html) |  MonoBehaviour.StartCoroutine returns a Coroutine. Instances of this class are only used to reference these coroutines, and do not hold any exposed properties or functions.  
[Coverage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.Coverage.html) | Describes the interface for the code coverage data exposed by mono.  
[CrashReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CrashReport.html) | Holds data for a single application crash event and provides access to all gathered crash reports.  
[CrashReporting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.CrashReporting.html) | Provides information specific to crash reporting on Windows platform.  
[CreateAssetMenuAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CreateAssetMenuAttribute.html) | Mark a ScriptableObject-derived type to be automatically listed in the Assets/Create submenu, so that instances of the type can be easily created and stored in the project as ".asset" files.  
[Crypto](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Crypto.html) | Class representing cryptography algorithms.  
[Cubemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html) | Class for handling cube maps, Use this to create or modify existing cube map assets.  
[CubemapArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.html) | Class for handling Cubemap arrays.  
[CullingGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.html) | Describes a set of bounding spheres that should have their visibility and distances maintained.  
[Cursor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cursor.html) | Cursor API for setting the cursor (mouse pointer).  
[Cursor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Cursor.html) | Cursor API for Windows Store Apps.  
[CustomRenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTexture.html) | Custom Render Textures are an extension to Render Textures that allow you to render directly to the Texture using a Shader.  
[CustomRenderTextureManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTextureManager.html) | Custom Render Texture Manager.  
[CustomSampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.CustomSampler.html) | Custom CPU Profiler label used for profiling arbitrary code blocks.  
[CustomYieldInstruction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomYieldInstruction.html) | Base class for custom yield instructions to suspend coroutines.  
[DataUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprites.DataUtility.html) | Helper utilities for accessing Sprite data.  
[DeallocateOnJobCompletionAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.DeallocateOnJobCompletionAttribute.html) | Automatically deallocates a native container when a job is finished.  
[Debug](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html) | Class containing methods to ease debugging while developing a game.  
[DefaultExecutionOrder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DefaultExecutionOrder.html) | Specifies the script execution order for a MonoBehaviour-derived class relative to other MonoBehaviour-derived types.  
[DelayedAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DelayedAttribute.html) | Attribute used to make a float, int, or string variable in a script be delayed.  
[Device](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/tvOS.Device.html) | Interface into tvOS specific functionality.  
[Device](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device.html) | Interface into iOS specific functionality.  
[DictationRecognizer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationRecognizer.html) | DictationRecognizer listens to speech input and attempts to determine what phrase was uttered.  
[DictionaryPool<T0,T1>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.DictionaryPool_2.html) | A version of CollectionPool<T0,T1> for Dictionaries.  
[Directory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.html) | Exposes static methods for directory operations.  
[DisallowMultipleComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DisallowMultipleComponent.html) | Prevents MonoBehaviour of same type (or subtype) to be added more than once to a GameObject.  
[DiscreteTimeTimeExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTimeTimeExtensions.html) | Extension methods for the DiscreteTime.  
[Display](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) | Provides access to a display / screen for rendering operations.  
[DisposeSentinel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.DisposeSentinel.html) | Contains methods that automatically detect memory leaks.  
[DynamicGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI.html) | Allows to control the dynamic Global Illumination.  
[ElementInfoAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Categorization.ElementInfoAttribute.html) | Provide a information to order and categorize at element level (in a category).  
[EnumButtonsAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EnumButtonsAttribute.html) | Attribute to enable editing an enum with a ToggleButtonGroup.  
[ExcludeFromCoverageAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.ExcludeFromCoverageAttribute.html) | Allows you to exclude an Assembly, Class, Constructor, Method or Struct from Coverage.  
[ExcludeFromObjectFactoryAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExcludeFromObjectFactoryAttribute.html) | Add this attribute to a class to prevent the class and its inherited classes from being created with ObjectFactory methods.  
[ExcludeFromPresetAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExcludeFromPresetAttribute.html) | Add this attribute to a class to prevent creating a Preset from the instances of the class.  
[ExecuteAlways](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteAlways.html) | Causes a MonoBehaviour-derived class to execute in Edit mode and prefab editing mode in addition to at runtime.  
[ExecuteInEditMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExecuteInEditMode.html) | Causes a MonoBehaviour-derived class to execute in Edit mode in addition to at runtime.  
[ExpressionEvaluator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExpressionEvaluator.html) | Evaluates simple math expressions; supports int / float and operators: + - * / % ^ ( ).  
[ExternalGPUProfiler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ExternalGPUProfiler.html) | The ExternalGPUProfiler API allows developers to programatically take GPU frame captures in conjunction with supported external GPU profilers. GPU frame captures can be used to both analyze performance and debug graphics related issues.  
[File](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.html) | Provides static methods for file operations.  
[Flare](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Flare.html) | A flare asset. Read more about flares in the components reference.  
[FlareLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FlareLayer.html) | FlareLayer component.  
[FloatComparer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Comparers.FloatComparer.html) | A float comparer used by Assert performing approximate comparison.  
[FormerlySerializedAsAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Serialization.FormerlySerializedAsAttribute.html) | Use this attribute to rename a field without losing its serialized value.  
[FrameCapture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Apple.FrameCapture.html) | Interface to control XCode Frame Capture.  
[FrameDebugger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameDebugger.html) | Controls the Frame Debugger from a script.  
[FrameTimingManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTimingManager.html) | The FrameTimingManager allows the user to capture and access FrameTiming data for multiple frames.  
[GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) | Base class for all objects that can exist in a scene. Add components to a GameObject to control its appearance and behavior.  
[GarbageCollector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.html) | API to control the garbage collector on the Mono and IL2CPP scripting backends.  
[GenericPool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.GenericPool_1.html) | Provides a static implementation of ObjectPool<T0>.  
[GeometryUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GeometryUtility.html) | Utility class for common geometric functions.  
[Gizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html) | Gizmos are used to give visual debugging or setup aids in the Scene view.  
[GL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.html) | Low-level graphics library.  
[Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) | Represents a Gradient used for animating colors.  
[GradientUsageAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientUsageAttribute.html) | Controls how the Gradient inspector editor treats the color values.  
[GrammarRecognizer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.GrammarRecognizer.html) | The GrammarRecognizer is a complement to the KeywordRecognizer. In many cases developers will find the KeywordRecognizer fills all their development needs. However, in some cases, more complex grammars will be better expressed in the form of an xml file on disk. The GrammarRecognizer uses Extensible Markup Language (XML) elements and attributes, as specified in the World Wide Web Consortium (W3C) Speech Recognition Grammar Specification (SRGS) Version 1.0. These XML elements and attributes represent the rule structures that define the words or phrases (commands) recognized by speech recognition engines.  
[Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html) | Raw interface to Unity's drawing functions.  
[GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) | GPU graphics data buffer, for working with geometry or compute shader data.  
[GraphicsFormatUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormatUtility.html) | This utility class contains helper functions that enable you to query properties of a TextureFormat, RenderTextureFormat, or GraphicsFormat. This class also includes format conversion and size calculation functions.  
[GraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.html) | Script interface for Graphics Settings.  
[GraphicsStateCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsStateCollection.html) | Collection of shader variants and associated graphics states.  
[GraphicsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture.html) | Represents the view on a single texture resource that is uploaded to the graphics device.  
[Handheld](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handheld.html) | Interface into functionality unique to handheld devices.  
[HashSetPool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.HashSetPool_1.html) | A version of CollectionPool<T0,T1> for HashSets.  
[HashUnsafeUtilities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HashUnsafeUtilities.html) | Utilities to compute hashes with unsafe code.  
[HashUtilities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HashUtilities.html) | Utilities to compute hashes.  
[HDROutputSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDROutputSettings.html) | Provides access to HDR display settings and information.  
[HeaderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HeaderAttribute.html) | Use this PropertyAttribute to add a header above some fields in the Inspector.  
[HelpURLAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HelpURLAttribute.html) | Provide a custom documentation URL for a class.  
[HideInCallstackAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideInCallstackAttribute.html) | Marks the methods you want to hide from the Console window callstack. When you hide these methods they are removed from the detail area of the selected message in the Console window.  
[HideInInspector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideInInspector.html) | Flags a variable to not appear in the Inspector.  
[IconAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IconAttribute.html) | Attribute to specify an icon for a MonoBehaviour or ScriptableObject.  
[IgnoredByDeepProfilerAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.IgnoredByDeepProfilerAttribute.html) | IgnoredByDeepProfilerAttribute prevents Unity Profiler from capturing method calls.  
[IJobExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobExtensions.html) | Contains extension methods for jobs using the IJob interface.  
[IJobForExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobForExtensions.html) | Contains extension methods for IJobFor job types.  
[IJobParallelForExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.IJobParallelForExtensions.html) | Contains extension methods for IJobParallelFor job types.  
[IJobParallelForTransformExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.IJobParallelForTransformExtensions.html) | Contains extension methods for IJobParallelForTransform.  
[ImageEffectAfterScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageEffectAfterScale.html) | Any Image Effect with this attribute will be rendered after Dynamic Resolution stage.  
[ImageEffectAllowedInSceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageEffectAllowedInSceneView.html) | Any Image Effect with this attribute can be rendered into the Scene view camera.  
[ImageEffectOpaque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageEffectOpaque.html) | Any Image Effect with this attribute will be rendered after opaque geometry but before transparent geometry.  
[ImageEffectTransformsToLDR](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageEffectTransformsToLDR.html) | When using HDR rendering it can sometime be desirable to switch to LDR rendering during ImageEffect rendering.  
[ImageEffectUsesCommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageEffectUsesCommandBuffer.html) | Use this attribute when image effects are implemented using Command Buffers.  
[Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Input.html) | Provides static methods for Windows specific input manipulation.  
[InspectorNameAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InspectorNameAttribute.html) | Use this attribute on enum value declarations to change the display name shown in the Inspector.  
[InspectorOrderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InspectorOrderAttribute.html) | Shows sorted enum values in the Inspector enum UI dropdowns i.e. EditorGUI.EnumPopup, PropertyField etc. This attribute can be applied to enum types only.  
[InvalidImportException](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.InvalidImportException.html) | Exception raised by the Resource Loader on SRP's.  
[JobHandleUnsafeUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.LowLevel.Unsafe.JobHandleUnsafeUtility.html) | Contains unsafe utility methods for JobHandle instances.  
[JobProducerTypeAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.LowLevel.Unsafe.JobProducerTypeAttribute.html) | Indicates that a job interface's Execute method can be Burst compiled.  
[JobsUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.LowLevel.Unsafe.JobsUtility.html) | Provides methods for creating, running, and debugging jobs.  
[KeywordRecognizer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.KeywordRecognizer.html) | KeywordRecognizer listens to speech input and attempts to match uttered phrases to a list of registered keywords.  
[Launcher](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Launcher.html) | Class which is capable of launching user's default app for file type or a protocol. See also PlayerSettings where you can specify file or URI associations.  
[LensFlare](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LensFlare.html) | Script interface for a Lens flare component.  
[LicenseInformation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.LicenseInformation.html) | This class provides information regarding application's trial status and allows initiating application purchase.  
[Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) | Script interface for light components.  
[Light2DBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.Light2DBase.html) | Provides a base class for 2D lights.  
[LightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html) | An object containing settings for precomputing lighting data, that Unity can serialize as a Lighting Settings Asset.  
[LightmapData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapData.html) | Data of a lightmap.  
[LightmapperUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.LightmapperUtils.html) | Utility class for converting Unity Lights to light types recognized by the baking backends.  
[Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.Lightmapping.html) | Interface to the light baking backends.  
[LightmapSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapSettings.html) | Stores lightmaps of the Scene.  
[LightProbeGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeGroup.html) | Light Probe Group.  
[LightProbeProxyVolume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume.html) | The Light Probe Proxy Volume component offers the possibility to use higher resolution lighting for large non-static GameObjects.  
[LightProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.html) | Stores light probe data for all currently loaded Scenes.  
[LineRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html) | The line renderer is used to draw free-floating lines in 3D space.  
[LineUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineUtility.html) | A collection of common line functions.  
[LinkedPool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.LinkedPool_1.html) | A linked list version of IObjectPool<T0>.  
[ListPool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.ListPool_1.html) | A version of CollectionPool<T0,T1> for Lists.  
[LoadStoreActionDebugModeSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LoadStoreActionDebugModeSettings.html) | Whether to show undefined areas of the display that might cause rendering problems in your built application.  
[LODGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LODGroup.html) | LODGroup lets you group multiple Renderers into LOD levels.  
[Logger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Logger.html) | Initializes a new instance of the Logger.  
[ManagedReferenceUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Serialization.ManagedReferenceUtility.html) | Utility functions related to SerializeReference manipulation and access.  
[Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) | The material class.  
[MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) | A block of material values to apply.  
[MemoryProfiler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.MemoryProfiler.html) | The memory profiler API provides functionality for taking memory snapshots or adding metadata to them.  
[MemorySnapshotMetadata](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.MemorySnapshotMetadata.html) | Container for memory snapshot metadata.  
[Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) | A class that allows you to create or modify meshes.  
[MeshFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshFilter.html) | A class to access the Mesh of the mesh filter.  
[MeshRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html) | Renders meshes inserted by the MeshFilter or TextMesh.  
[MessageEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.MessageEventArgs.html) | Arguments passed to Action callbacks registered in PlayerConnection.  
[MinAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MinAttribute.html) | Attribute used to make a float or int variable in a script be restricted to a specific minimum value.  
[MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) | MonoBehaviour is a base class that many Unity scripts derive from.  
[MultilineAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MultilineAttribute.html) | Attribute to make a string be edited with a multi-line textfield.  
[NativeArrayUnsafeUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeArrayUnsafeUtility.html) | Contains unsafe methods for working with NativeArray instances.  
[NativeContainerAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeContainerAttribute.html) | Allows you to create your own custom native container.  
[NativeContainerIsAtomicWriteOnlyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeContainerIsAtomicWriteOnlyAttribute.html) | Indicates that the native container only allows writing, and can only be written to in safe, parallel contexts.  
[NativeContainerIsReadOnlyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeContainerIsReadOnlyAttribute.html) | Marks a native container type as read only.  
[NativeContainerSupportsDeallocateOnJobCompletionAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeContainerSupportsDeallocateOnJobCompletionAttribute.html) | Indicates that a NativeContainer can be automatically deallocated when a job is complete.  
[NativeContainerSupportsDeferredConvertListToArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeContainerSupportsDeferredConvertListToArray.html) | Indicates that the native container type can be passed to the Schedule method of an IJobParallelForDefer job.  
[NativeContainerSupportsMinMaxWriteRestrictionAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeContainerSupportsMinMaxWriteRestrictionAttribute.html) | Indicates that a native container type can restrict its writable ranges to be between a min and a max index.  
[NativeDisableContainerSafetyRestrictionAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeDisableContainerSafetyRestrictionAttribute.html) | Explicitly disable the safety system for a NativeContainer.  
[NativeDisableParallelForRestrictionAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeDisableParallelForRestrictionAttribute.html) | Indicates that multiple jobs can safely access the same NativeContainer at the same time.  
[NativeDisableUnsafePtrRestrictionAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeDisableUnsafePtrRestrictionAttribute.html) | Enable the use of unsafe pointers in jobs.  
[NativeFixedLengthAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeFixedLengthAttribute.html) | Indicates that a native container has a size that will never change.  
[NativeLeakDetection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeLeakDetection.html) | Contains settings for native leak detection.  
[NativeSetClassTypeToNullOnScheduleAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeSetClassTypeToNullOnScheduleAttribute.html) | Sets the managed reference to a class to null on a copy of the job struct that is passed to a job.  
[NativeSetThreadIndexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeSetThreadIndexAttribute.html) | Inject a worker thread index into an int on the job struct.  
[NativeSliceUnsafeUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeSliceUnsafeUtility.html) | Contains unsafe methods for working with NativeSlice instances.  
[NonReorderableAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NonReorderableAttribute.html) | Disables reordering of an array or list in the Inspector window.  
[Notification](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Notification.html) | Default implementation for Playable notifications.  
[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) | Base class for all objects Unity can reference.  
[ObjectIdRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ObjectIdRequest.html) | ObjectId request that can be used to determine the object corresponding to each pixel. Can be submitted using either Camera.SubmitRenderRequest or RenderPipeline.SubmitRenderRequest, and the results can be used either on the CPU in C# or the GPU in a shader.  
[ObjectIdResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ObjectIdResult.html) | The results of an ObjectIdRequest, stored in ObjectIdRequest._result, containing the ObjectIdResult.idToObjectMapping that is needed to interpret the color-encoded object IDs that are rendered in the ObjectIdRequest._destination RenderTexture.  
[ObjectPool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.ObjectPool_1.html) | A stack based IObjectPool<T0>.  
[OcclusionArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OcclusionArea.html) | OcclusionArea is an area in which occlusion culling is performed.  
[OcclusionPortal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OcclusionPortal.html) | The portal for dynamically changing occlusion at runtime.  
[OnDemandRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.OnDemandRendering.html) | Use the OnDemandRendering class to control and query information about your application's rendering speed independent from all other subsystems (such as physics, input, or animation).   
[OnDemandResources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResources.html) | On Demand Resources API.  
[OnDemandResourcesRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.OnDemandResourcesRequest.html) | Represents a request for On Demand Resources (ODR). It's an AsyncOperation and can be yielded in a coroutine.  
[PhotoCapture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCapture.html) | Captures a photo from the web camera and stores it in memory or on disk.  
[PhotoCaptureFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCaptureFrame.html) | Contains information captured from the web camera.  
[PhraseRecognitionSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.PhraseRecognitionSystem.html) | Phrase recognition system is responsible for managing phrase recognizers and dispatching recognition events to them.  
[PhraseRecognizer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.PhraseRecognizer.html) | A common base class for both keyword recognizer and grammar recognizer.  
[Ping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ping.html) | Ping any given IP address (given in dot notation).  
[PIX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PIX.html) | Provides an interface to control GPU frame capture in Microsoft's PIX software.  
[PixelPerfectRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.PixelPerfectRendering.html) | A collection of APIs that facilitate pixel perfect rendering of sprite-based renderers.  
[PlayableAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableAsset.html) | A base class for assets that can be used to instantiate a Playable at runtime.  
[PlayableBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBehaviour.html) | PlayableBehaviour is the base class from which every custom playable script derives.  
[PlayableExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableExtensions.html) | Extensions for all the types that implements IPlayable.  
[PlayableOutputExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutputExtensions.html) | Extensions for all the types that implements IPlayableOutput.  
[PlayerConnection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.PlayerConnection.html) | Used for handling the network connection from the Player to the Editor.  
[PlayerLoop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoop.html) | The class representing the player loop in Unity.  
[PlayerPrefs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html) |  PlayerPrefs is a class that stores Player preferences between game sessions. It can store string, float and integer values into the user’s platform registry.  
[PlayerPrefsException](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefsException.html) | An exception thrown by the PlayerPrefs class in a web player build.  
[PreferBinarySerialization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PreferBinarySerialization.html) | Prefer ScriptableObject derived type to use binary serialization regardless of project's asset serialization mode.  
[PreserveAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.PreserveAttribute.html) | PreserveAttribute prevents byte code stripping from removing a class, method, field, or property.  
[Profiler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html) | Controls the Profiler from script.  
[ProfilerUnsafeUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.html) | Utility class which provides access to low level Profiler API.  
[Projector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Projector.html) | A script interface for a projector component.  
[PropertyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute.html) | Base class to derive custom property attributes from. Use this to create custom attributes for script variables.  
[QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html) | This represents the script interface for Quality Settings.  
[Random](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.html) | Easily generate random data for games.  
[RangeAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RangeAttribute.html) | Attribute used to make a float or int variable in a script be restricted to a specific range.  
[RationalTimeExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.RationalTimeExtensions.html) | Extension method operations for RationalTime.  
[RayTracingAccelerationStructure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructure.html) | A data structure used to represent the geometry in the Scene for GPU ray tracing.  
[RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html) | A shader for GPU ray tracing.  
[ReadOnlyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.ReadOnlyAttribute.html) | Marks a member of a struct used in a job as read-only.  
[Recorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Recorder.html) | Records profiling data produced by a specific Sampler.  
[RecreatePipelineOnChangeAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RecreatePipelineOnChangeAttribute.html) | This attribute is used on field of a IRenderPipelineGraphicsSettings to ensure pipeline would be recreated if the value is changed.  
[RectOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectOffset.html) | Offsets for rectangles, borders, etc.  
[RectTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html) | Position, size, anchor and pivot information for a rectangle.  
[ReflectionProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html) | The reflection probe is used to capture the surroundings into a texture which is passed to the shaders and used for reflections.  
[Remote](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/tvOS.Remote.html) | A class for Apple TV remote input configuration.  
[Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) | General functionality for all renderers.  
[RendererExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RendererExtensions.html) | Extension methods to the Renderer class, used only for the UpdateGIMaterials method used by the Global Illumination System.  
[RenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html) | Defines a series of commands and settings that describes how Unity renders a frame.  
[RenderPipelineAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset.html) | An asset that produces a specific IRenderPipeline.  
[RenderPipelineAsset<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineAsset_1.html) | An asset that produces a specific IRenderPipeline.  
[RenderPipelineGlobalSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineGlobalSettings.html) | A ScriptableObject to associate with a RenderPipeline and store project-wide settings for that Pipeline.  
[RenderPipelineGraphicsSettingsCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineGraphicsSettingsCollection.html) | Container class for a list of IRenderPipelineGraphicsSettings objects.  
[RenderPipelineGraphicsSettingsExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineGraphicsSettingsExtensions.html) | Class that contains extensions for   
[RenderPipelineManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineManager.html) | Render Pipeline manager.  
[RenderSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.RenderSettings.html) | Experimental render settings features.  
[RenderSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings.html) | The Render Settings contain values for a range of visual elements in your Scene, like fog and ambient light.  
[RenderSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.RenderSettings.html) | Experimental render settings features.  
[RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) | Render textures are textures that can be rendered to.  
[RequireAttributeUsagesAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.RequireAttributeUsagesAttribute.html) | Only allowed on attribute types. If the attribute type is marked, then so too will all CustomAttributes of that type.  
[RequireComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html) | The RequireComponent attribute automatically adds required components as dependencies.  
[RequireDerivedAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.RequireDerivedAttribute.html) | When the type is marked, all types derived from that type will also be marked.  
[RequiredInterfaceAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.RequiredInterfaceAttribute.html) | When a type is marked, all interface implementations of the specified types will be marked.  
[RequiredMemberAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.RequiredMemberAttribute.html) | When a type is marked, all of its members with [RequiredMember] are marked.  
[RequireImplementorsAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.RequireImplementorsAttribute.html) | When the interface type is marked, all types implementing that interface will be marked.  
[ResourceFormattedPathsAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ResourceFormattedPathsAttribute.html) | Attribute specifying information about the paths where these resources are located.  
[ResourcePathAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ResourcePathAttribute.html) | This attribute is used to describe what path to the asset should be used.  
[ResourcePathsAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ResourcePathsAttribute.html) | Attribute specifying information about the paths where these resources are located.  
[ResourcePathsBaseAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ResourcePathsBaseAttribute.html) | This abstract attribute is used to describe what path to the asset should be used.  
[ResourceRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourceRequest.html) | Asynchronous load request from the Resources bundle.  
[Resources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html) | The Resources class allows you to find and access Objects including assets.  
[ResourcesAPI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ResourcesAPI.html) | Derive from this base class to provide alternative implementations to the C# behavior of specific Resources methods.  
[RuntimeInitializeOnLoadMethodAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeOnLoadMethodAttribute.html) | Use this attribute to get a callback when the runtime is starting up and loading the first scene.  
[Sampler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Sampler.html) | Provides control over a CPU Profiler label.  
[ScalableBufferManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScalableBufferManager.html) | Scales render textures to support dynamic resolution if the target platform/graphics API supports it.  
[SceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.html) | Scene management at run-time.  
[SceneManagerAPI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManagerAPI.html) | Derive from this base class to provide alternative implementations to the C# behavior of specific SceneManager methods.  
[SceneUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneUtility.html) | Scene and Build Settings related utilities.  
[Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html) | Provides access to display information.  
[Screen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.Screen.html) | Access platform-specific display information.  
[ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html) | A class you can derive from if you want to create objects that live independently of GameObjects.  
[ScriptableRuntimeReflectionSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ScriptableRuntimeReflectionSystem.html) | Empty implementation of IScriptableRuntimeReflectionSystem.  
[ScriptableRuntimeReflectionSystemSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ScriptableRuntimeReflectionSystemSettings.html) | Global settings for the scriptable runtime reflection system.  
[ScriptPlayableBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.ScriptPlayableBinding.html) | A PlayableBinding that contains information representing a ScriptingPlayableOutput.  
[SearchContextAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContextAttribute.html) | This attribute can be attached to a component object field in order to have the ObjectField use the advanced Object Picker.  
[Security](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Security.html) | Webplayer security related class. Not supported from 5.4.0 onwards.  
[SelectionBaseAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionBaseAttribute.html) | Add this attribute to a script class to mark its GameObject as a selection base object for Scene View picking.  
[SerializeField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html) | Force Unity to serialize a private field.  
[SerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html) | A scripting attribute that instructs Unity to serialize a field as a reference instead of as a value.  
[Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) | Shader scripts used for all rendering.  
[ShaderVariantCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderVariantCollection.html) | ShaderVariantCollection records which shader variants are actually used in each shader.  
[ShaderWarmup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ShaderWarmup.html) | Prewarms shaders in a way that is supported by all graphics APIs.  
[SkinnedMeshRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinnedMeshRenderer.html) | The Skinned Mesh filter.  
[Skybox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Skybox.html) | A script interface for the skybox component.  
[SleepTimeout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SleepTimeout.html) | Constants for special values of Screen.sleepTimeout.  
[Snapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Snapping.html) | Snap values to rounded increments.  
[SortingGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingGroup.html) | Adding a SortingGroup component to a GameObject will ensure that all Renderers within the GameObject's descendants will be sorted and rendered together.  
[SpaceAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpaceAttribute.html) | Use this PropertyAttribute to add some spacing in the Inspector.  
[SparseTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SparseTexture.html) | Class for handling Sparse Textures.  
[SplashScreen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SplashScreen.html) | Provides an interface to the Unity splash screen.  
[Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) | Represents a Sprite object for use in 2D gameplay.  
[SpriteAtlas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlas.html) | Sprite Atlas is an asset created within Unity. It is part of the built-in sprite packing solution.  
[SpriteAtlasManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteAtlasManager.html) | Manages SpriteAtlas during runtime.  
[SpriteDataAccessExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteDataAccessExtensions.html) | A list of methods designed for reading and writing to the rich internal data of a Sprite.  
[SpriteRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html) | Renders a Sprite for 2D graphics.  
[SpriteRendererDataAccessExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteRendererDataAccessExtensions.html) | A list of methods that allow the caller to override what the SpriteRenderer renders.  
[StaticBatchingUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticBatchingUtility.html) | StaticBatchingUtility can prepare your objects to take advantage of Unity's static batching.  
[SupportedOnRenderPipelineAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedOnRenderPipelineAttribute.html) | Set which render pipelines make a class active.  
[SupportedRenderingFeatures](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedRenderingFeatures.html) | Describes the rendering features supported by a given render pipeline.  
[SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html) | Access system and hardware information.  
[SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Device.SystemInfo.html) | Access platform-specific system and hardware information.  
[TextAreaAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAreaAttribute.html) | Attribute to make a string be edited with a height-flexible and scrollable text area.  
[TextAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html) | Represents a raw text or binary file asset.  
[Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) | Base class for Texture handling.  
[Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) | Class that represents textures in C# code.  
[Texture2DArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2DArray.html) | Class for handling 2D texture arrays.  
[Texture3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html) | Class for handling 3D Textures, Use this to create 3D texture assets.  
[TextureMipmapLimitGroups](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.html) | Script interface for texture mipmap limit groups.  
[TexturePlayableBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Playables.TexturePlayableBinding.html) | A PlayableBinding that contains information representing a TexturePlayableOutput.  
[Tile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.html) | Represents tile on Windows start screen   
[Time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html) | Provides an interface to get time information from Unity.  
[Toast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Toast.html) | Represents a toast notification in Windows Store Apps.   
[TooltipAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TooltipAttribute.html) | Specify a tooltip for a field in the Inspector window.  
[TouchScreenKeyboard](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboard.html) | Interface for on-screen keyboards. Only native iPhone, Android, and Windows Store Apps are supported.  
[TrailRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.html) | The trail renderer is used to make trails behind objects in the Scene as they move about.  
[Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) | Position, rotation and scale of an object.  
[UnityAPICompatibilityVersionAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityAPICompatibilityVersionAttribute.html) | Declares an assembly to be compatible (API wise) with a specific Unity API. Used by internal tools to avoid processing the assembly in order to decide whether assemblies may be using old Unity API.  
[UnityEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.html) | A zero argument persistent callback that can be saved with the Scene.  
[UnityEvent<T0,T1,T2,T3>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent_4.html) | Four argument version of UnityEvent.  
[UnityEvent<T0,T1,T2>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent_3.html) | Three argument version of UnityEvent.  
[UnityEvent<T0,T1>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent_2.html) | Two argument version of UnityEvent.  
[UnityEvent<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent_1.html) | One argument version of UnityEvent.  
[UnityEventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.html) | Abstract base class for UnityEvents.  
[UnsafeGenericPool<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.UnsafeGenericPool_1.html) | Provides a static implementation of ObjectPool<T0>.  
[UnsafeUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.html) | Contains unsafe utility methods.  
[Utils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Diagnostics.Utils.html) | A utility class that you can use for diagnostic purposes.  
[VideoCapture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.html) | Records a video from the web camera directly to disk.  
[VirtualFileSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.VirtualFileSystem.html) | Class that provides access to some of the Unity low level virtual file system APIs.  
[WaitForEndOfFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForEndOfFrame.html) | Waits until the end of the frame after Unity has rendered every Camera and GUI, just before displaying the frame on screen.  
[WaitForFixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForFixedUpdate.html) | Waits until next fixed frame rate update function. Additional resources: FixedUpdate.  
[WaitForSeconds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html) | Suspends the coroutine execution for the given amount of seconds using scaled time.  
[WaitForSecondsRealtime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSecondsRealtime.html) | Suspends the coroutine execution for the given amount of seconds using unscaled time.  
[WaitUntil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitUntil.html) | Suspends the coroutine execution until the supplied delegate evaluates to true.  
[WaitWhile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitWhile.html) | Suspends the coroutine execution until the supplied delegate evaluates to false.  
[Watermark](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.Watermark.html) | Provides an interface to the system that draws the Unity trial version and development build watermarks in screen space.  
[WebCam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.WebCam.html) | Contains general information about the current state of the web camera.  
[WriteAccessRequiredAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.WriteAccessRequiredAttribute.html) | Specify which struct method and property requires write access to be invoked.  
[WriteOnlyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.WriteOnlyAttribute.html) | Marks a member of a struct used in a job as write-only.  
[YieldInstruction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/YieldInstruction.html) | Base class for all yield instructions.  
### Structs
Struct | Description  
---|---  
[ApplicationMemoryUsageChange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsageChange.html) | Contains information about a change in the application's memory usage.  
[ArchiveFileInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveFileInfo.html) | Represents information about a file included in an archive.  
[ArchiveHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveHandle.html) | Represents an asynchronous operation handle that references an archive.  
[AsyncGPUReadbackRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AsyncGPUReadbackRequest.html) | Represents an asynchronous request for a GPU resource.  
[AsyncReadManagerRequestMetric](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.html) | Metrics for an individual read request.  
[AtomicSafetyHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.html) | Coordinate safe access to native container memory inside the job system.  
[AttachmentDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentDescriptor.html) | A declaration of a single color or depth rendering surface to be attached into a RenderPass.  
[AttachmentIndexArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AttachmentIndexArray.html) | Struct encapsulating a fixed list of attachment indices used when declaring native render passes.  
[BatchCullingContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingContext.html) | Culling context for a batch.  
[BatchCullingOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingOutput.html) | Contains the output data where OnPerformCulling will write draw commands into.  
[BatchCullingOutputDrawCommands](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingOutputDrawCommands.html) | Draw commands generated by the culling request.  
[BatchDrawCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommand.html) | Represents a draw command for a BatchRendererGroup.   
[BatchDrawCommandIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandIndirect.html) | Represents an indirect draw command for a BatchRendererGroup.   
[BatchDrawCommandProcedural](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandProcedural.html) | Represents a procedural draw command for a BatchRendererGroup.   
[BatchDrawCommandProceduralIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandProceduralIndirect.html) | Represents a procedural indirect draw command for a BatchRendererGroup.   
[BatchDrawRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawRange.html) | Specifies a draw range of draw commands.  
[BatchFilterSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchFilterSettings.html) | Represents settings that Unity applies to draw commands in this draw range.  
[BatchID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchID.html) | The batch ID.  
[BatchMaterialID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchMaterialID.html) | The batch Material ID.  
[BatchMeshID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchMeshID.html) | The batch mesh ID.  
[BatchPackedCullingViewID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchPackedCullingViewID.html) | The ID of the view from which Unity invoked the culling.  
[BatchQueryJob<T0,T1>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.LowLevel.Unsafe.BatchQueryJob_2.html) | Provides an implementation for batch query jobs.  
[BatchQueryJobStruct<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.LowLevel.Unsafe.BatchQueryJobStruct_1.html) | Provides an implementation for batch query jobs.  
[BatchRendererGroupCreateInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroupCreateInfo.html) | Struct is used to initialize BatchRendererGroup.  
[BlendShapeBufferRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BlendShapeBufferRange.html) | Describes the location of blend shape vertex data in a GraphicsBuffer.  
[BlendState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendState.html) | Values for the blend state.  
[BoneWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight.html) | Describes 4 skinning bone weights that affect a vertex in a mesh.  
[BoneWeight1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoneWeight1.html) | Describes a bone weight that affects a vertex in a mesh.  
[BoundingSphere](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundingSphere.html) | Describes a single bounding sphere for use by a CullingGroup.  
[Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) | Represents an axis aligned bounding box.  
[BoundsInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.html) | Represents an axis aligned bounding box with all values as integers.  
[BuildCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.html) | Contains information about compression methods, compression levels and block sizes that are supported by Asset Bundle compression at build time and recompression at runtime.  
[Cache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) | Data structure for cache. For more information, see Caching.AddCache.  
[CachedAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CachedAssetBundle.html) | Data structure for downloading AssetBundles to a customized cache path. Additional resources:UnityWebRequestAssetBundle.GetAssetBundle for more information.  
[CameraParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.CameraParameters.html) | When calling PhotoCapture.StartPhotoModeAsync, you must pass in a CameraParameters object that contains the various settings that the web camera will use.  
[CameraPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Playables.CameraPlayable.html) | An implementation of IPlayable that produces a Camera texture.  
[CameraProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraProperties.html) | Camera related properties in CullingParameters.  
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) | Representation of RGBA colors.  
[Color32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) | Representation of RGBA colors in 32 bit format.  
[CombineInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CombineInstance.html) | Struct used to describe meshes to be combined using Mesh.CombineMeshes.  
[ContentNamespace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Content.ContentNamespace.html) | Provides functionality for grouping loaded Archive files into separate namespaces.  
[Cookie](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.Cookie.html) | A helper structure used to initialize a LightDataGI structure with cookie information.  
[CoveredMethodStats](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.CoveredMethodStats.html) | Describes the summary of the code coverage for the specified method used by Coverage. For an example of typical usage, see Coverage.GetStatsFor.  
[CoveredSequencePoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.CoveredSequencePoint.html) | Describes a covered sequence point used by Coverage. For an example of typical usage, see Coverage.GetSequencePointsFor.  
[CreateSceneParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.CreateSceneParameters.html) | This struct collects all the CreateScene parameters in to a single place.  
[CullingGroupEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroupEvent.html) | Provides information about the current and previous states of one sphere in a CullingGroup.  
[CullingResults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingResults.html) | A struct containing the results of a culling operation.  
[CullingSplit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingSplit.html) | This struct contains the properties of a culling split.  
[CustomRenderTextureUpdateZone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTextureUpdateZone.html) | Structure describing an Update Zone.  
[DebugScreenCapture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.DebugScreenCapture.html) | A raw data representation of a screenshot.  
[DepthState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DepthState.html) | Values for the depth state.  
[DirectionalLight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.DirectionalLight.html) | A helper structure used to initialize a LightDataGI structure as a directional light.  
[DiscLight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.DiscLight.html) | A helper structure used to initialize a LightDataGI structure as a disc light.  
[DiscreteTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.DiscreteTime.html) | Data-type representing a discrete time value.  
[DisplayInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DisplayInfo.html) | Represents a connected display.  
[DrawingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DrawingSettings.html) | Settings for ScriptableRenderContext.DrawRenderers.  
[DrivenRectTransformTracker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrivenRectTransformTracker.html) | A component can be designed to drive a RectTransform. The DrivenRectTransformTracker struct is used to specify which RectTransforms it is driving.  
[EarlyUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.EarlyUpdate.html) | Update phase in the native player loop.  
[ExposedPropertyResolver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExposedPropertyResolver.html) | Object that is used to resolve references to an ExposedReference field.  
[ExposedReference<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExposedReference_1.html) | Creates a type whos value is resolvable at runtime.  
[FileHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileHandle.html) | A handle to an asynchronously opened file.  
[FileInfoResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileInfoResult.html) | The results of an asynchronous AsyncReadManager.GetFileInfo call.  
[FilteringSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FilteringSettings.html) | A struct that represents filtering settings for ScriptableRenderContext.DrawRenderers.  
[FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html) | Update phase in the native player loop.  
[FrameData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.FrameData.html) | This structure contains the frame information a Playable receives in Playable.PrepareFrame.  
[FrameTiming](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTiming.html) | Struct containing basic FrameTimings and accompanying relevant data.  
[FrustumPlanes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrustumPlanes.html) | This struct contains the view space coordinates of the near projection plane.  
[GlobalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GlobalKeyword.html) | Represents a global shader keyword.  
[GradientAlphaKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html) | Alpha key used by Gradient.  
[GradientColorKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html) | Color key used by Gradient.  
[GraphicsBufferHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBufferHandle.html) | Represents the internal handle/id of a GraphicsBuffer.  
[GraphicsFence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsFence.html) | Used to manage synchronisation between tasks on async compute queues and the graphics queue.  
[GraphicsTextureDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureDescriptor.html) | Contains all the information Unity uses to create a GraphicsTexture.  
[Hash128](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Hash128.html) | Represents a 128-bit hash value.  
[Initialization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Initialization.html) | Update phase in the native player loop.  
[InstantiateParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InstantiateParameters.html) | Parameters for Object.Instantiate and Object.InstantiateAsync.  
[JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) | Represents a handle to a job, which uniquely identifies a job scheduled in the job system.  
[JobRanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.LowLevel.Unsafe.JobRanges.html) | Provides information about a range that a job is allowed to work on.  
[Keyframe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html) | A single keyframe that can be injected into an animation curve.  
[LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html) | Specifies Layers to use in a Physics.Raycast.  
[LazyLoadReference<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LazyLoadReference_1.html) | Serializable lazy reference to a UnityEngine.Object contained in an asset file.  
[LightBakingOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightBakingOutput.html) | Struct describing the result of a Global Illumination bake for a given light.  
[LightDataGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.LightDataGI.html) | The interop structure to pass light information to the light baking backends. There are helper structures for Directional, Point, Spot and Rectangle lights to correctly initialize this structure.  
[LightProbesQuery](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbesQuery.html) | Thread-safe struct for batch sampling Light Probes in a Scene.  
[LightShadowCasterCullingInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightShadowCasterCullingInfo.html) | This structure contains the information to perform shadow caster culling for a given light.  
[LinearColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.LinearColor.html) | Contains normalized linear color values for red, green, blue in the range of 0 to 1, and an additional intensity value.  
[LoadSceneParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneParameters.html) | This struct collects all the LoadScene parameters in to a single place.  
[LocalKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeyword.html) | Represents a shader keyword declared in a shader source file.  
[LocalKeywordSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LocalKeywordSpace.html) | Represents the local keyword space of a Shader or ComputeShader.  
[LOD](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LOD.html) | Structure for building a LOD for passing to the SetLODs function.  
[LODParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LODParameters.html) |  LODGroup culling parameters.  
[MaterialEffectPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Playables.MaterialEffectPlayable.html) | An implementation of IPlayable that allows application of a Material shader to one or many texture inputs to produce a texture output.  
[Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html) | A collection of common math functions.  
[Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) | A standard 4x4 transformation matrix.  
[MetadataValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MetadataValue.html) | Contains a single metadata value for a batch.  
[MipmapLimitDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MipmapLimitDescriptor.html) | Determines whether a texture uses a mipmap limit, and which mipmap limit the texture uses, when you create the texture using a constructor.  
[NativeArray<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.html) | Provides a buffer of native memory to managed code, making it possible to share data between managed and native code without marshalling costs.  
[NativeSlice<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeSlice_1.html) | Provides a view on a buffer of native memory most commonly acquired from a NativeArray<T0>.  
[PassIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassIdentifier.html) | Represents an identifier of a specific Pass in a Shader.  
[PhraseRecognizedEventArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.PhraseRecognizedEventArgs.html) | Provides information about a phrase recognized event.  
[Plane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html) | Representation of a plane in 3D space.  
[PlatformKeywordSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PlatformKeywordSet.html) | A collection of ShaderKeyword that represents a specific platform variant.  
[Playable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.Playable.html) | Playables are customizable runtime objects that can be connected together and are contained in a PlayableGraph to create complex behaviours.  
[PlayableBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableBinding.html) | Struct that holds information regarding an output of a PlayableAsset.  
[PlayableGraph](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableGraph.html) | Use the PlayableGraph to manage Playable creations and destructions.  
[PlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableOutput.html) | See: IPlayableOutput.  
[PlayerLoopSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevel.PlayerLoopSystem.html) | The representation of a single system being updated by the player loop in Unity.  
[PointLight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.PointLight.html) | A helper structure used to initialize a LightDataGI structure as a point light.  
[PooledObject<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pool.PooledObject_1.html) |  A pooled object wraps a reference to an instance returned to the pool when the pooled object is disposed of.   
[Pose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Pose.html) | Representation of a Position, and a Rotation in 3D Space  
[PostLateUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.PostLateUpdate.html) | Update phase in the native player loop.  
[PreLateUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.PreLateUpdate.html) | Update phase in the native player loop.  
[PreUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.PreUpdate.html) | Update phase in the native player loop.  
[ProfilerCategory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategory.html) | Use to specify category for instrumentation Profiler markers.  
[ProfilerCategoryDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerCategoryDescription.html) | Provides information about Profiler category.  
[ProfilerMarker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarker.html) | Performance marker used for profiling arbitrary code blocks.  
[ProfilerMarkerData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.html) | Describes Profiler metadata parameter that can be associated with a sample.  
[ProfilerRecorder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorder.html) | Records the Profiler metric data that a Profiler marker or counter produces.  
[ProfilerRecorderDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderDescription.html) | Gets the description of a Profiler metric.  
[ProfilerRecorderHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderHandle.html) | Gets the handle of a Profiler metric.  
[ProfilerRecorderSample](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorderSample.html) | Sample value structure.  
[PropertyName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyName.html) | Represents a string as an int for efficient lookup and comparison. Use this for common PropertyNames.Internally stores just an int to represent the string. A PropertyName can be created from a string but can not be converted back to a string. The same string always results in the same int representing that string. Thus this is a very efficient string representation in both memory and speed when all you need is comparison.PropertyName is serializable.ToString() is only implemented for debugging purposes in the editor it returns "theName:3737" in the player it returns "Unknown:3737".  
[Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) | Quaternions are used to represent rotations.  
[RangeInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RangeInt.html) | Describes an integer range.  
[RasterState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RasterState.html) | Values for the raster state.  
[RationalTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IntegerTime.RationalTime.html) | Data type that represents time as an integer count of a rational number.  
[Ray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) | Representation of rays.  
[Ray2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray2D.html) | A ray in 2D space.  
[RayTracingAABBsInstanceConfig](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAABBsInstanceConfig.html) | The parameters you use to add an instance of ray tracing axis-aligned bounding boxes (AABBs) to a RayTracingAccelerationStructure.  
[RayTracingGeometryInstanceConfig](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingGeometryInstanceConfig.html) | Parameters you can use to configure ray tracing triangle geometry instances that are part of a RayTracingAccelerationStructure.  
[RayTracingInstanceCullingConfig](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingInstanceCullingConfig.html) | Parameters for culling and filtering ray tracing instances in RayTracingAccelerationStructure.CullInstances.  
[RayTracingInstanceCullingMaterialTest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingInstanceCullingMaterialTest.html) | This structure is used by RayTracingAccelerationStructure.CullInstances function to avoid adding Renderers to the acceleration structure or to ignore individual sub-meshes in a Mesh based on Shaders used by Materials when building the acceleration structure.  
[RayTracingInstanceCullingResults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingInstanceCullingResults.html) | A structure containing results of the culling operation performed by RayTracingAccelerationStructure.CullInstances.  
[RayTracingInstanceCullingShaderTagConfig](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingInstanceCullingShaderTagConfig.html) | A Shader Tag configuration used by RayTracingAccelerationStructure.CullInstances to filter and classify Materials.  
[RayTracingInstanceCullingTest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingInstanceCullingTest.html) | A testing configuration used in RayTracingAccelerationStructure.CullInstances for adding Renderers to an acceleration structure based on their layer, ShadowCastingMode and Material type.  
[RayTracingInstanceMaterialConfig](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingInstanceMaterialConfig.html) | This structure is used by RayTracingAccelerationStructure.CullInstances function to determine which types of Materials are used by Renderers when populating the acceleration structure with ray tracing instances.  
[RayTracingInstanceMaterialCRC](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingInstanceMaterialCRC.html) | A Material instance id and CRC hash value pair. This information is returned by a RayTracingAccelerationStructure.CullInstances call.  
[RayTracingInstanceTriangleCullingConfig](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingInstanceTriangleCullingConfig.html) | This structure is used by RayTracingAccelerationStructure.CullInstances function to determine triangle culling and vertex winding order for ray tracing instances.  
[RayTracingMeshInstanceConfig](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingMeshInstanceConfig.html) | Parameters you can use to configure ray tracing Mesh instances that are part of a RayTracingAccelerationStructure.  
[RayTracingSubMeshFlagsConfig](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingSubMeshFlagsConfig.html) | A structure used by RayTracingAccelerationStructure.CullInstances that defines the RayTracingSubMeshFlags values for different Material types.  
[ReadCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadCommand.html) | Describes the offset, size, and destination buffer of a single read operation.  
[ReadCommandArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadCommandArray.html) | An array of ReadCommand instances to pass to AsyncReadManager.Read and AsyncReadManager.ReadDeferred.  
[ReadHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadHandle.html) | You can use this handle to query the status of an asynchronous read operation. Note: To avoid a memory leak, you must call Dispose.  
[Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) | A 2D Rectangle defined by X and Y position, width and height.  
[RectangleLight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.RectangleLight.html) | A helper structure used to initialize a LightDataGI structure as a rectangle light.  
[RectInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectInt.html) | A 2D Rectangle defined by x, y, width, height with integers.  
[ReflectionProbeBlendInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeBlendInfo.html) | ReflectionProbeBlendInfo contains information required for blending probes.  
[RefreshRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RefreshRate.html) | Represents the display refresh rate. This is how many frames the display can show per second.  
[RenderBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderBuffer.html) | Color or depth buffer part of a RenderTexture.  
[RendererList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererList.html) | Represents a set of visible GameObjects.  
[RendererListDesc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererUtils.RendererListDesc.html) | Represents the set of GameObjects that a RendererList contains.  
[RendererListParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererListParams.html) | Struct holding the arguments that are needed to create a renderers RendererList.  
[RenderingLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingLayerMask.html) | The Render Pipeline allows you to use Rendering Layers, which are LayerMasks to make Lights or effects only affect specific Renderers.  
[RenderParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderParams.html) | Rendering parameters used by various rendering functions.  
[RenderQueueRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderQueueRange.html) | Describes a material render queue range.  
[RenderStateBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock.html) | A set of values that Unity uses to override the GPU's render state.  
[RenderTargetBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetBinding.html) | Describes a render target with one or more color buffers, a depth/stencil buffer and the associated load/store-actions that are applied when the render target is active.  
[RenderTargetBlendState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetBlendState.html) | Values for the blend state.  
[RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) | Identifies a RenderTexture for a CommandBuffer.  
[RenderTargetSetup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTargetSetup.html) | Fully describes setup of RenderTarget.  
[RenderTextureDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureDescriptor.html) | This struct contains all the information required to create a RenderTexture. It can be copied, cached, and reused to easily create RenderTextures that all share the same properties. Avoid using the default constructor as it does not initialize some flags with the recommended values.  
[Resolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resolution.html) | Represents a display resolution.  
[Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) | Run-time data structure for *.unity file.  
[ScopedRenderPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScopedRenderPass.html) | Represents an active render pass until disposed.  
[ScopedSubPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScopedSubPass.html) | Represents an active sub pass until disposed.  
[ScriptableCullingParameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableCullingParameters.html) | Parameters that configure a culling operation in the Scriptable Render Pipeline.  
[ScriptableRenderContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ScriptableRenderContext.html) | Defines state and drawing commands that custom render pipelines use.  
[ScriptPlayable<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.ScriptPlayable_1.html) | A IPlayable implementation that contains a PlayableBehaviour for the PlayableGraph. PlayableBehaviour can be used to write custom Playable that implement their own PrepareFrame callback.  
[ScriptPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.ScriptPlayableOutput.html) | A IPlayableOutput implementation that contains a script output for the a PlayableGraph.  
[SecondarySpriteTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SecondarySpriteTexture.html) | Encapsulates a Texture2D and its shader property name to give Sprite-based renderers access to a secondary texture, in addition to the main Sprite texture.  
[SecondaryTileData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.SecondaryTileData.html) | Defines the default look of secondary tile.   
[SemanticMeaning](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.SemanticMeaning.html) | Semantic meaning is a collection of semantic properties of a recognized phrase. These semantic properties can be specified in SRGS grammar files.  
[ShaderKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeyword.html) | Represents an identifier for a specific code path in a shader.  
[ShaderKeywordSet](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeywordSet.html) | A collection of ShaderKeyword that represents a specific shader variant.  
[ShaderTagId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderTagId.html) | Shader tag ids are used to refer to various names in shaders.  
[ShaderWarmupSetup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.ShaderWarmupSetup.html) | The rendering configuration to use when prewarming shader variants.  
[ShadowCastersCullingInfos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastersCullingInfos.html) | This structure contains the information to perform shadow casters culling for one camera.  
[ShadowDrawingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowDrawingSettings.html) | Settings for ScriptableRenderContext.DrawShadows.  
[ShadowSplitData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSplitData.html) | Describes the culling information for a given shadow split (e.g. directional cascade).  
[SortingLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SortingLayer.html) | SortingLayer allows you to set the render order of multiple sprites easily. There is always a default SortingLayer named "Default" which all sprites are added to initially. Added more SortingLayers to easily control the order of rendering of groups of sprites. Layers can be ordered before or after the default layer.  
[SortingLayerRange](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingLayerRange.html) | Describes a renderer's sorting layer range.  
[SortingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingSettings.html) | This struct describes the methods to sort objects during rendering.  
[SphericalHarmonicsL2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.html) | Spherical harmonics up to the second order (3 bands, 9 coefficients).  
[SpotLight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.SpotLight.html) | A helper structure used to initialize a LightDataGI structure as a spot light.  
[SpotLightBoxShape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.SpotLightBoxShape.html) | Use this Struct to help initialize a LightDataGI structure as a box-shaped spot light.  
[SpotLightPyramidShape](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.SpotLightPyramidShape.html) | Use this Struct to help initialize a LightDataGI structure as a pyramid-shaped spot light.  
[SpriteBone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.SpriteBone.html) | Stores a set of information that describes the bind pose of this Sprite.  
[StencilState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilState.html) | Values for the stencil state.  
[SubMeshDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubMeshDescriptor.html) | Contains information about a single sub-mesh of a Mesh.  
[SubPassDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubPassDescriptor.html) | Structure discribing a single native subpass.  
[TagHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TagHandle.html) | A handle to one of the tag values that can be applied to a GameObject.  
[TextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings.html) | Structure that represents texture mipmap limit settings.  
[TextureMixerPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Playables.TextureMixerPlayable.html) | An implementation of IPlayable that allows mixing two textures.  
[TexturePlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Playables.TexturePlayableOutput.html) | An IPlayableOutput implementation that will be used to manipulate textures.  
[ThreadedBatchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ThreadedBatchContext.html) | Thread-safe and Burst-safe API for interacting with a BatchRendererGroup from Burst jobs.  
[TimeUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.TimeUpdate.html) | Update phase in the native player loop that waits for the operating system (OS) to flip the back buffer to the display and update the time in the engine.  
[TransformAccess](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess.html) | Represents the position, rotation and scale of an object.  
[TransformAccessArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccessArray.html) | TransformAccessArray.   
[Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) | Update phase in the native player loop.  
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) | Representation of 2D vectors and points.  
[Vector2Int](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2Int.html) | Representation of 2D vectors and points using integers.  
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) | Representation of 3D vectors and points.  
[Vector3Int](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3Int.html) | Representation of 3D vectors and points using integers.  
[Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) | Representation of four-dimensional vectors.  
[VertexAttributeDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeDescriptor.html) | Information about a single VertexAttribute of a Mesh vertex.  
[VisibleLight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleLight.html) | Holds data of a visible light.  
[VisibleReflectionProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VisibleReflectionProbe.html) | Holds data of a visible reflection reflectionProbe.  
### Enumerations
Enumeration | Description  
---|---  
[ActivityIndicatorStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.ActivityIndicatorStyle.html) | ActivityIndicator Style (iOS Specific).  
[Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html) | Sets which allocation type to use for a NativeArray.  
[AmbientMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.AmbientMode.html) | Ambient lighting mode.  
[AndroidActivityIndicatorStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidActivityIndicatorStyle.html) | ActivityIndicator Style (Android Specific).  
[AngularFalloffType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.AngularFalloffType.html) | Sets the method to use to compute the angular attenuation of spot lights.  
[AnisotropicFiltering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnisotropicFiltering.html) | Anisotropic filtering mode.  
[ApplicationInstallMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationInstallMode.html) | Application installation mode (Read Only).  
[ApplicationMemoryUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationMemoryUsage.html) | Describes the application memory usage level.  
[ApplicationSandboxType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApplicationSandboxType.html) | Application sandbox type.  
[ArchiveStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveStatus.html) | Options for tracking the status of the archive operation.  
[AssetLoadingSubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.html) | Subsystem tags for the read request, describing broad asset type or subsystem that triggered the read request.  
[AtomicSafetyErrorType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.AtomicSafetyErrorType.html) | Error code for errors related to accessing native container instances in different situations.  
[AudioType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioType.html) | The format type of the imported (native) data.  
[BatchBufferTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchBufferTarget.html) | Expected target for the buffer passed to BatchRendererGroup.AddBatch.  
[BatchCullingFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingFlags.html) | Additional parameters for the current culling context  
[BatchCullingProjectionType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingProjectionType.html) | The projection type of a view that is being culled.  
[BatchCullingViewType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchCullingViewType.html) | The type of an object that is requesting culling.  
[BatchDrawCommandFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandFlags.html) | Rendering options for the BatchDrawCommand struct.  
[BatchDrawCommandType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchDrawCommandType.html) | Enumerates the different draw command types a BatchRendererGroup can draw.  
[BatteryStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BatteryStatus.html) | Enumeration for SystemInfo.batteryStatus which represents the current status of the device's battery.  
[BlendMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendMode.html) | Blend mode for controlling the blending.  
[BlendOp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendOp.html) | Blend operation.  
[BlendShapeBufferLayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BlendShapeBufferLayout.html) | Determines the data that Unity returns when you call Mesh.GetBlendShapeBuffer.  
[BuiltinRenderTextureType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinRenderTextureType.html) | Built-in temporary render textures produced during camera's rendering.  
[BuiltinShaderDefine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderDefine.html) | Defines set by editor when compiling shaders, based on the target platform and GraphicsTier.  
[BuiltinShaderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderMode.html) | Built-in shader modes used by GraphicsSettings.  
[BuiltinShaderType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BuiltinShaderType.html) | Built-in shader types used by GraphicsSettings.  
[CameraClearFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraClearFlags.html) | Values for Camera.clearFlags, determining what to clear when rendering a Camera.  
[CameraEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraEvent.html) | Defines a place in camera's rendering to attach CommandBuffer objects to.  
[CameraHDRMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraHDRMode.html) | The HDR mode to use for rendering.  
[CameraLateLatchMatrixType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CameraLateLatchMatrixType.html) | The types of camera matrices that support late latching.  
[CameraType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraType.html) | Describes different types of camera.  
[CaptureFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Memory.CaptureFlags.html) | Flags that specify what kind of data to capture in a snapshot.  
[CapturePixelFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.CapturePixelFormat.html) | The encoded image or video pixel format to use for PhotoCapture and VideoCapture.  
[ColorGamut](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorGamut.html) | Represents a color gamut.  
[ColorPrimaries](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorPrimaries.html) | Represents a color space based on its set of red, green, and blue color primaries.  
[ColorSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorSpace.html) | Color space for player settings.  
[ColorWriteMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ColorWriteMask.html) | Specifies which color components will get written into the target framebuffer.  
[CommandBufferExecutionFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBufferExecutionFlags.html) | Flags describing the intention for how the command buffer will be executed. Set these via CommandBuffer.SetExecutionFlags.  
[CompareFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CompareFunction.html) | Depth or stencil comparison function.  
[CompressionLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompressionLevel.html) | Compression Levels relate to how much time should be spent compressing Assets into an Asset Bundle.  
[CompressionType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompressionType.html) | Compression Method for Asset Bundles.  
[ComputeBufferMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferMode.html) | Intended usage of the buffer.  
[ComputeBufferType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferType.html) |  ComputeBuffer type.  
[ComputeQueueType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ComputeQueueType.html) | Describes the desired characteristics with respect to prioritisation and load balancing of the queue that a command buffer being submitted via Graphics.ExecuteCommandBufferAsync or [[ScriptableRenderContext.ExecuteCommandBufferAsync] should be sent to.  
[ConfidenceLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.ConfidenceLevel.html) | Used by KeywordRecognizer, GrammarRecognizer, DictationRecognizer. Phrases under the specified minimum level will be ignored.  
[ConnectionTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.PlayerConnection.ConnectionTarget.html) | The type of the connected target.  
[CopyTextureSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CopyTextureSupport.html) | Support for various Graphics.CopyTexture cases.  
[CubemapFace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html) |  Cubemap face.  
[CullingOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullingOptions.html) | Flags used by ScriptableCullingParameters.cullingOptions to configure a culling operation.  
[CullMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CullMode.html) | Determines which faces Unity culls.  
[CursorLockMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CursorLockMode.html) | How the cursor should behave.  
[CursorMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CursorMode.html) | Determines whether the mouse cursor is rendered using software rendering or, on supported platforms, hardware rendering.  
[CustomMarkerCallbackFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CustomMarkerCallbackFlags.html) | Flags that determine what custom events get called when native plugin callback is issued.  
[CustomRenderTextureInitializationSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTextureInitializationSource.html) | Specify the source of a Custom Render Texture initialization.  
[CustomRenderTextureUpdateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTextureUpdateMode.html) | Frequency of update or initialization of a Custom Render Texture.  
[CustomRenderTextureUpdateZoneSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomRenderTextureUpdateZoneSpace.html) | Space in which coordinates are provided for Update Zones.  
[DefaultFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.DefaultFormat.html) |  Use a default format to create either Textures or RenderTextures from scripts based on platform specific capability.   
[DefaultReflectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DefaultReflectionMode.html) | Default reflection mode.  
[DepthTextureMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DepthTextureMode.html) | Depth texture generation mode for Camera.  
[DeviceGeneration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/tvOS.DeviceGeneration.html) | tvOS device generation.  
[DeviceGeneration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.DeviceGeneration.html) | iOS device generation.  
[DeviceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DeviceType.html) | Enumeration for SystemInfo.deviceType, denotes a coarse grouping of kinds of devices.  
[DictationCompletionCause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationCompletionCause.html) | Represents the reason why dictation session has completed.  
[DictationTopicConstraint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.DictationTopicConstraint.html) | DictationTopicConstraint enum specifies the scenario for which a specific dictation recognizer should optimize.  
[DirectorUpdateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.DirectorUpdateMode.html) | Defines what time source is used to update a Director graph.  
[DirectorWrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.DirectorWrapMode.html) | Wrap mode for Playables.  
[DistanceMetric](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DistanceMetric.html) | Type of sorting to use while rendering.  
[DrivenTransformProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrivenTransformProperties.html) | An enumeration of transform properties that can be driven on a RectTransform by an object.  
[EnforceJobResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.EnforceJobResult.html) | Enumerates the possible values returned by AtomicSafetyHandle methods that wait for all jobs accessing the native container associated with the handle to finish.  
[FalloffType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.FalloffType.html) | Available falloff models for baking.  
[FastMemoryFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FastMemoryFlags.html) | Control Fast Memory render target layout.  
[FileReadType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileReadType.html) | The type of file read requested from the AsyncReadManager.  
[FileState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileState.html) | Defines the possible existential states of a file.  
[FileStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileStatus.html) | The possible statuses of a FileHandle.  
[FilterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilterMode.html) | Filtering mode for textures. Corresponds to the settings in a texture inspector.  
[FindObjectsInactive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FindObjectsInactive.html) | Options to control whether object find functions return inactive objects.  
[FindObjectsSortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FindObjectsSortMode.html) | Options to specify if and how to sort objects returned by a function.  
[FogMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FogMode.html) | Fog mode to use.  
[Folder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Folder.html) | List of accessible folders on Windows Store Apps.  
[ForcedCrashCategory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Diagnostics.ForcedCrashCategory.html) | Specifies the category of crash to cause when calling ForceCrash().  
[FormatSwizzle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FormatSwizzle.html) | Graphics Format Swizzle.  
[FoveatedRenderingCaps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FoveatedRenderingCaps.html) | Capabilities of the foveated rendering implementation.  
[FoveatedRenderingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.FoveatedRenderingMode.html) | Operation mode for the foveated rendering system.  
[FrameCaptureDestination](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Apple.FrameCaptureDestination.html) | Destination of Frame Capture This is a wrapper for MTLCaptureDestination.  
[FullScreenMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FullScreenMode.html) | Sets the full-screen mode. For information on platform compatibility, refer to the description of each mode.  
[FullScreenMovieControlMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FullScreenMovieControlMode.html) | Describes options for displaying movie playback controls.  
[FullScreenMovieScalingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FullScreenMovieScalingMode.html) | Describes scaling modes for displaying movies.  
[GizmoSubset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GizmoSubset.html) | Specifies whether gizmos render before or after postprocessing for a camera render.  
[GradientMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientMode.html) | Color interpolation mode used by Gradient.  
[GraphicsDeviceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsDeviceType.html) | Graphics device API type.  
[GraphicsFenceType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsFenceType.html) | The type of GraphicFence.  
[GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html) | Use this format to create either Textures or RenderTextures from scripts.  
[GraphicsFormatUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormatUsage.html) | Use this format usages to figure out the capabilities of specific GraphicsFormat  
[GraphicsTextureDescriptorFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureDescriptorFlags.html) | The rendering and read/write access mode of a GraphicsTexture.  
[GraphicsTextureState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTextureState.html) | The state of a GraphicsTexture.  
[GraphicsTier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTier.html) | An enum that represents graphics tiers.  
[HDRDisplayBitDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDRDisplayBitDepth.html) | Options for the number of bits for HDR output in each color channel of swap chain buffers. Applicable when an HDR display is active.  
[HDRDisplaySupportFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HDRDisplaySupportFlags.html) | A set of flags that describe the level of HDR display support available on the GPU and driver.  
[HideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.html) | Bit mask that controls object destruction, saving and visibility in inspectors.  
[IndexFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.IndexFormat.html) | Format of the mesh index buffer data.  
[InspectorSort](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InspectorSort.html) | Defines if enum should be shown sorted by name or by value.  
[InspectorSortDirection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InspectorSortDirection.html) | Defines if enum should be shown in ascending or descending order.  
[IntegrityCheckLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IntegrityCheckLevel.html) |  Enumeration specifying a integrity check level.Additional resources: Debug.CheckIntegrity  
[KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html) | Key codes returned by Event.keyCode. These map directly to a physical key on the keyboard. If "Use Physical Keys" is enabled in Input Manager settings, these map directly to a physical key on the keyboard. If "Use Physical Keys" is disabled these map to language dependent mapping, different for every platform and cannot be guaranteed to work. "Use Physical Keys" is enabled by default from 2022.1  
[LightEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightEvent.html) | Defines a place in light's rendering to attach CommandBuffer objects to.  
[LightmapBakeType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapBakeType.html) | Enum describing what part of a light contribution can be baked.  
[LightmapCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapCompression.html) | A set of options for the level of compression the Editor uses for lightmaps.  
[LightmapsMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapsMode.html) | Lightmap (and lighting) configuration mode, controls how lightmaps interact with lighting and what kind of information they store.  
[LightmapsModeLegacy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightmapsModeLegacy.html) | Single, dual, or directional lightmaps rendering mode, used only in GIWorkflowMode.Legacy  
[LightMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.LightMode.html) | The lightmode. A light can be real-time, mixed, baked or unknown. Unknown lights will be ignored by the baking backends.  
[LightProbeOutsideHullStrategy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeOutsideHullStrategy.html) | Defines the way Unity chooses a probe to light a Renderer that is lit by Light Probes but positioned outside the bounds of the Light Probe tetrahedral hull.  
[LightProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.html) | Light probe interpolation type.  
[LightRenderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightRenderMode.html) | How the Light is rendered.  
[LightShadowCasterMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightShadowCasterMode.html) | Allows mixed lights to control shadow caster culling when Shadowmasks are present.  
[LightShadowResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightShadowResolution.html) | Shadow resolution options for a Light.  
[LightShadows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightShadows.html) | Shadow casting options for a Light.  
[LightType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightType.html) | The type of a Light.  
[LightType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GlobalIllumination.LightType.html) | The light type.  
[LightUnit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightUnit.html) | The unit of a Light's intensity.  
[LineAlignment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineAlignment.html) | Control the direction lines face, when using the LineRenderer or TrailRenderer.  
[LineTextureMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineTextureMode.html) | Choose how textures are applied to Lines and Trails.  
[LoadSceneMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.html) | Used when loading a Scene in a player.  
[LocalPhysicsMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LocalPhysicsMode.html) | Provides options for 2D and 3D local physics.  
[LODFadeMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LODFadeMode.html) | The LOD (level of detail) fade modes. Modes other than LODFadeMode.None will result in Unity calculating a blend factor for blending/interpolating between two neighbouring LODs and pass it to your shader.  
[LogOption](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogOption.html) | Option flags for specifying special treatment of a log message.  
[LogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html) | The type of the log message in Debug.unityLogger.Log or delegate registered with Application.RegisterLogCallback.  
[MarkerFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.MarkerFlags.html) | Profiler marker usage flags.  
[MaterialGlobalIlluminationFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialGlobalIlluminationFlags.html) | How the material interacts with lightmaps and lightprobes.  
[MaterialPropertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyType.html) | The type of a given material property.  
[MeshTopology](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshTopology.html) | Topology of Mesh faces.  
[MeshUpdateFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MeshUpdateFlags.html) | Mesh data update flags.  
[MixedLightingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MixedLightingMode.html) | Enum describing what lighting mode to be used with Mixed lights.  
[MotionVectorGenerationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MotionVectorGenerationMode.html) | The type of motion vectors that should be generated.  
[NativeArrayOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArrayOptions.html) | Options for controlling how memory is cleared.  
[NativeLeakDetectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeLeakDetectionMode.html) | Sets which native leak memory leak detection mode to use.  
[NetworkReachability](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NetworkReachability.html) | Describes network reachability options.  
[NPOTSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NPOTSupport.html) | NPOT textures support.  
[OpaqueSortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.OpaqueSortMode.html) | Opaque object sorting mode of a Camera.  
[OpenGLESVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.OpenGLESVersion.html) | Specifies the OpenGL ES version.  
[OperatingSystemFamily](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OperatingSystemFamily.html) | Enumeration for SystemInfo.operatingSystemFamily.  
[PassType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassType.html) | Shader pass type for Unity's lighting pipeline.  
[PerObjectData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PerObjectData.html) | What kind of per-object data to setup during rendering.  
[PersistentListenerMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.PersistentListenerMode.html) | The mode that a listener is operating in.  
[PhotoCaptureFileOutputFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCaptureFileOutputFormat.html) | Image Encoding Format.  
[PlayableTraversalMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayableTraversalMode.html) | Traversal mode for Playables.  
[PlayState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Playables.PlayState.html) | Status of a Playable.  
[PrimitiveType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.html) | The various primitives that can be created using the GameObject.CreatePrimitive function.  
[Priority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.Priority.html) | The priority level attached to the AsyncReadManager read request.  
[ProcessingState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ProcessingState.html) | The state of the read request at the time of retrieval of AsyncReadManagerMetrics.  
[ProfilerArea](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.ProfilerArea.html) | The different areas of profiling, corresponding to the charts in ProfilerWindow.  
[ProfilerCategoryColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategoryColor.html) | Profiler category colors enum.  
[ProfilerCategoryFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerCategoryFlags.html) | Options for determining if a Profiler category is built into Unity by default.  
[ProfilerFlowEventType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerFlowEventType.html) | Defines Profiler flow event type.  
[ProfilerMarkerDataType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.LowLevel.ProfilerMarkerDataType.html) | Options for the Profiler metadata type.  
[ProfilerMarkerDataUnit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerMarkerDataUnit.html) | Options for Profiler marker data unit types.  
[ProfilerRecorderOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.ProfilerRecorderOptions.html) | ProfilerRecorder lifecycle and collection options.  
[RayTracingAccelerationStructureBuildFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingAccelerationStructureBuildFlags.html) | Specifies how Unity builds the acceleration structure on the GPU.  
[RayTracingInstanceCullingFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingInstanceCullingFlags.html) | Flags used by RayTracingAccelerationStructure.CullInstances.  
[RayTracingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.RayTracingMode.html) | Indicates how a Renderer is updated.  
[RayTracingSubMeshFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingSubMeshFlags.html) | Flags that determine how rays intersect the geometry for each submesh relative to Material type during ray tracing.  
[ReadStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadStatus.html) | The state of an asynchronous file request.  
[RealtimeGICPUUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RealtimeGICPUUsage.html) | How much CPU usage to assign to the final lighting calculations at runtime.  
[ReceiveGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReceiveGI.html) | This property only takes effect if you enable a global illumination setting such as Baked Global Illumination or Enlighten Realtime Global Illumination for the target Scene. When you enable ReceiveGI, you can determine whether illumination data at runtime will come from Light Probes or Lightmaps. When you set ReceiveGI to Lightmaps, the Mesh Renderer receives global illumination from lightmaps. That means the Renderer is included in lightmap atlases, possibly increasing their size, memory consumption and storage costs. Calculating global illumination values for texels in this Renderer also adds to bake times. When you set ReceiveGI to Light Probes, the Mesh Renderer is not assigned space in lightmap atlases. Instead it receives global illumination stored by Light Probes in the target Scene. This can reduce bake times by avoiding the memory consumption and storage cost associated with lightmaps. ReceiveGI is only editable if you enable StaticEditorFlags.ContributeGI for the GameObject associated with the target Mesh Renderer. Otherwise this property defaults to the Light Probes setting.  
[ReflectionCubemapCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionCubemapCompression.html) | Determines how Unity will compress baked reflection cubemap.  
[ReflectionProbeClearFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeClearFlags.html) | Values for ReflectionProbe.clearFlags, determining what to clear when rendering a ReflectionProbe.  
[ReflectionProbeMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeMode.html) | Reflection probe's update mode.  
[ReflectionProbeRefreshMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeRefreshMode.html) | An enum describing the way a real-time reflection probe refreshes in the Player.  
[ReflectionProbeSortingCriteria](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeSortingCriteria.html) | Visible reflection probes sorting options.  
[ReflectionProbeTimeSlicingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeTimeSlicingMode.html) | When a probe's ReflectionProbe.refreshMode is set to ReflectionProbeRefreshMode.EveryFrame, this enum specify whether or not Unity should update the probe's cubemap over several frames or update the whole cubemap in one frame. Updating a probe's cubemap is a costly operation. Unity needs to render the entire Scene for each face of the cubemap, as well as perform special blurring in order to get glossy reflections. The impact on frame rate can be significant. Time-slicing helps maintaning a more constant frame rate during these updates by performing the rendering over several frames.  
[ReflectionProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ReflectionProbeUsage.html) | Reflection Probe usage.  
[RenderBufferLoadAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferLoadAction.html) | This enum describes what should be done on the render target when it is activated (loaded).  
[RenderBufferStoreAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderBufferStoreAction.html) | This enum describes what should be done on the render target when the GPU is done rendering into it.  
[RendererListStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RendererListStatus.html) | Options that represent the result of a ScriptableRenderContext.QueryRendererList operation.  
[RenderingPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingPath.html) | Rendering path of a Camera.  
[RenderingThreadingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderingThreadingMode.html) | Options for the application's actual rendering threading mode.  
[RenderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderQueue.html) | Determine in which order objects are renderered.  
[RenderStateMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateMask.html) | Specifies which parts of the render state that is overriden.  
[RenderTargetFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetFlags.html) | This enum describes optional flags for the RenderTargetBinding structure.  
[RenderTextureCreationFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureCreationFlags.html) | Set of flags that control the state of a newly-created RenderTexture.  
[RenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html) | Format of a RenderTexture.  
[RenderTextureMemoryless](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureMemoryless.html) | Flags enumeration of the render texture memoryless modes.  
[RenderTextureReadWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureReadWrite.html) | Color space conversion mode of a RenderTexture.  
[RenderTextureSubElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTextureSubElement.html) | Types of data that you can encapsulate within a render texture.  
[RTClearFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RTClearFlags.html) | Flags that determine which render targets Unity clears when you use CommandBuffer.ClearRenderTarget.  
[RuntimeInitializeLoadType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeLoadType.html) | Specifies when to get a callback during the startup of the runtime or when entering play mode in the Editor. Used with RuntimeInitializeOnLoadMethodAttribute.  
[RuntimePlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimePlatform.html) | The platform application is running. Returned by Application.platform.  
[ScheduleMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.LowLevel.Unsafe.ScheduleMode.html) | Options for scheduling a managed job.  
[ScreenOrientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScreenOrientation.html) | Describes screen orientation.  
[SearchType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SearchType.html) | Describe how to use the path in ResourcePathsBaseAttribute.  
[SearchViewFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchViewFlags.html) | Search view flags used to open the Object Picker in various states.  
[SendMessageOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SendMessageOptions.html) | Options for how to send a message.  
[ShaderConstantType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderConstantType.html) | Options for the shader constant value type.  
[ShaderKeywordType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderKeywordType.html) | Type of a shader keyword, eg: built-in or user defined.  
[ShaderParamType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderParamType.html) | Options for the data type of a shader constant's members.  
[ShaderPropertyFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderPropertyFlags.html) | Flags that control how a shader property behaves.  
[ShaderPropertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShaderPropertyType.html) | Type of a given shader property.  
[ShadowCastingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowCastingMode.html) | How shadows are cast from this object.  
[ShadowMapPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowMapPass.html) | Allows precise control over which shadow map passes to execute CommandBuffer objects attached using Light.AddCommandBuffer.  
[ShadowmaskMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShadowmaskMode.html) | The rendering mode of Shadowmask.  
[ShadowObjectsFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShadowObjectsFilter.html) | The filters that Unity can use when it renders GameObjects in the shadow pass.  
[ShadowProjection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShadowProjection.html) | Shadow projection type for Quality Settings.  
[ShadowQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShadowQuality.html) | Determines which type of shadows should be used.  
[ShadowResolution](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShadowResolution.html) | Default shadow resolution. Each decrease in quality level halves the resolution of shadows.  
[ShadowSamplingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ShadowSamplingMode.html) | Used by CommandBuffer.SetShadowSamplingMode.  
[SinglePassStereoMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SinglePassStereoMode.html) | Enum type defines the different stereo rendering modes available.  
[SkinQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinQuality.html) | The maximum number of bones affecting a single vertex.  
[SkinWeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SkinWeights.html) | Skin weights.  
[SnapAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SnapAxis.html) | Defines the axes that can be snapped.  
[SortingCriteria](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SortingCriteria.html) | How to sort objects during rendering.  
[Space](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) | The coordinate spaces in which to apply transformation to a GameObject.  
[SpeechError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.SpeechError.html) | Represents an error in a speech recognition system.  
[SpeechSystemStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Speech.SpeechSystemStatus.html) | Represents the current status of the speech recognition system or a dictation recognizer.  
[SpriteAlignment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteAlignment.html) | How a Sprite's graphic rectangle is aligned with its pivot point.  
[SpriteDrawMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteDrawMode.html) |  SpriteRenderer draw mode.  
[SpriteMaskInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.html) | This enum controls the mode under which the sprite will interact with the masking system.  
[SpriteMeshType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMeshType.html) | Defines the type of mesh generated for a sprite.  
[SpritePackingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpritePackingMode.html) | Sprite packing modes for the Sprite Packer.  
[SpritePackingRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpritePackingRotation.html) | Sprite rotation modes for the Sprite Packer.  
[SpriteSortPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteSortPoint.html) | Determines the position of the Sprite used for sorting the Renderer.  
[SpriteTileMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteTileMode.html) | Tiling mode for SpriteRenderer.tileMode.  
[StackTraceLogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StackTraceLogType.html) | Stack trace logging options.  
[StencilOp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.StencilOp.html) | Specifies the operation that's performed on the stencil buffer when rendering.  
[StereoTargetEyeMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StereoTargetEyeMask.html) | Enum values for the Camera's targetEye property.  
[SubPassFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SubPassFlags.html) | Flags to indicate specialized native subpass behaviour.  
[SynchronisationStage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SynchronisationStage.html) | The stages of the draw call processing on the GPU.  
[SynchronisationStageFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SynchronisationStageFlags.html) | Describes the various stages of GPU processing against which the GraphicsFence can be set and waited against.  
[SystemGestureDeferMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.SystemGestureDeferMode.html) | Bit-mask used to control the deferring of system gestures on iOS.  
[SystemLanguage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemLanguage.html) | The language the user's operating system is running in. Returned by Application.systemLanguage.  
[TerrainQualityOverrides](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainQualityOverrides.html) | Flags used by QualitySettings to specify which Terrain fields the quality settings should override.   
[TextureDimension](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.TextureDimension.html) | Texture "dimension" (type).  
[TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html) | Format used when creating textures from scripts.  
[TextureMipmapLimitBiasMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitBiasMode.html) | An enumeration that represents the bias mode to use for TextureMipmapLimitSettings.limitBias.  
[TextureWrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureWrapMode.html) | Wrap mode for textures.  
[ThreadPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ThreadPriority.html) | Priority of a thread.  
[TileForegroundText](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.TileForegroundText.html) | Style for foreground text on a secondary tile.  
[TileTemplate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.TileTemplate.html) | Templates for various tile styles.   
[ToastTemplate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.ToastTemplate.html) | Templates for various toast styles.   
[TouchScreenKeyboardType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchScreenKeyboardType.html) | Enumeration of the different types of supported touchscreen keyboards.  
[TransferFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TransferFunction.html) | Contains electro-optical transfer function options.  
[TransparencySortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TransparencySortMode.html) | Transparent object sorting mode of a Camera.  
[UISubset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.UISubset.html) | Bit mask that specifies which UI subset to render when calling ScriptableRenderContext.CreateUIOverlayRendererList. For any frame, UI subsets must be rendered in the following order: UIToolkit_UGUI, LowLevel.  
[UnityEventCallState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventCallState.html) | Controls the scope of UnityEvent callbacks.  
[UnloadSceneOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.UnloadSceneOptions.html) | Scene unloading options passed to SceneManager.UnloadScene.  
[UserAuthorization](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UserAuthorization.html) | Use this enum to request permission from the user’s device for access to system features.  
[ValidationLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ValidationLevel.html) |  Enumeration specifying a validation level.Additional resources: Debug.IsValidationLevelEnabled  
[VertexAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttribute.html) | Possible attribute types that describe a vertex in a Mesh.  
[VertexAttributeFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VertexAttributeFormat.html) | Data type of a VertexAttribute.  
[VideoShadersIncludeMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VideoShadersIncludeMode.html) | Video shaders mode used by GraphicsSettings.  
[VRTextureUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VRTextureUsage.html) | This enum describes how the RenderTexture is used as a VR eye texture. Instead of using the values of this enum manually, use the value returned by eyeTextureDesc or other VR functions returning a RenderTextureDescriptor.  
[WaitTimeoutMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitTimeoutMode.html) |  Determines which mode of time measurement to use in wait operations.   
[WebCamMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.WebCamMode.html) | Describes the active mode of the Web Camera resource.  
[WeightedMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WeightedMode.html) | Sets which weights to use when calculating curve segments.  
[WhitePoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WhitePoint.html) | The reference white point of a color space.  
[WindowActivationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.WindowActivationState.html) | Specifies the set of reasons that a windowActivated event was raised.  
[WrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WrapMode.html) | Determines how time is treated outside of the keyframed range of an AnimationClip or AnimationCurve.  
* * *
