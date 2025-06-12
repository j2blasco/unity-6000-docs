* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.NVIDIAModule.html

# UnityEngine.NVIDIAModule
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
A module that contains API you can use to interact with NVIDIA graphics cards.
To activate this module at runtime, call NVIDIA.Plugins.LoadPlugin with the NVIDIA.Plugins.Plugin.NVUnityPlugin value during application startup. The class NVIDIA.Device contains the APIs to interact with the graphics cards' specific features.
### Classes
Class | Description  
---|---  
[DLSSContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NVIDIA.DLSSContext.html) | Represents the state of DLSS.  
[GraphicsDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NVIDIA.GraphicsDevice.html) | Provides the main entry point for the NVIDIA Module. Use this to interact with specific NVIDIA graphics card features.  
[GraphicsDeviceDebugView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NVIDIA.GraphicsDeviceDebugView.html) | Represents a memory snapshot of the current feature states. The memory of the arrays/buffers in this struct are tied to the lifetime of the debug view. Additional resources: GraphicsDevice.CreateDebugView, GraphicsDevice.UpdateDebugView and GraphicsDevice.DeleteDebugView.  
[NVUnityPlugin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NVIDIA.NVUnityPlugin.html) | Provides methods to manage loading and unloading NVIDIA module plugins.  
### Structs
Struct | Description  
---|---  
[DLSSCommandExecutionData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NVIDIA.DLSSCommandExecutionData.html) | Represents the state of a DLSSContext. If you call Device.ExecuteDLSS, Unity sends the values in this struct to the runtime. After this, you can change the values in this struct without any side effects.  
[DLSSCommandInitializationData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NVIDIA.DLSSCommandInitializationData.html) | Represent the initialization state of a DLSSContext. You can only use and set this when calling GraphicsDevice.CreateFeature.  
[DLSSDebugFeatureInfos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NVIDIA.DLSSDebugFeatureInfos.html) | Represents debug information for a particular DLSSContext.  
[DLSSTextureTable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NVIDIA.DLSSTextureTable.html) | The set of texture slots available for the DLSSContext. SA GraphicsDevice.ExecuteDLSS  
[OptimalDLSSSettingsData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NVIDIA.OptimalDLSSSettingsData.html) | Represents the performance settings that DLSS recommends based on the system's graphics card and the size of the input and output color buffers. Additional resources: GraphicsDevice.GetOptimalSettings  
### Enumerations
Enumeration | Description  
---|---  
[DLSSFeatureFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NVIDIA.DLSSFeatureFlags.html) | Options that represent subfeatures of DLSS.  
[DLSSQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NVIDIA.DLSSQuality.html) | Options for DLSS performance modes.  
[GraphicsDeviceFeature](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/NVIDIA.GraphicsDeviceFeature.html) | Lists every feature ID the GraphicsDevice API supports. For now, this only includes Deep Learning Super Sampling (DLSS). To check if the device supports a feature, call GraphicsDevice.IsFeatureAvailable.  
* * *
