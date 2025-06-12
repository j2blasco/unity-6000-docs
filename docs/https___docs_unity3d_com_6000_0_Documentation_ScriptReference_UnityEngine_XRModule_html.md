* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.XRModule.html

# UnityEngine.XRModule
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
The XR module contains the VR and AR related platform support functionality.
### Classes
Class | Description  
---|---  
[CommonUsages](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages.html) | Defines static variables that are used to retrieve input features from XR.InputDevice.TryGetFeatureValue.  
[InputDevices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevices.html) | An interface for accessing devices in the XR input subsytem.  
[InputTracking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputTracking.html) | A collection of methods and properties for accessing XR input devices by their XR Node representation.  
[XRDisplaySubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.html) | An XRDisplaySubsystem controls rendering to a head tracked display.  
[XRDisplaySubsystemDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystemDescriptor.html) | Class providing information about XRDisplaySubsystem registration.  
[XRInputSubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystem.html) | XRInputSubsystem Instance is used to enable and disable the inputs coming from a specific plugin.  
[XRInputSubsystemDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystemDescriptor.html) | Information about an Input subsystem.  
[XRMeshSubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.html) | Allows external systems to provide dynamic meshes to Unity.  
[XRMeshSubsystemDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystemDescriptor.html) | Information about an XRMeshSubsystem.  
[XRStats](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Provider.XRStats.html) | Provides timing and other statistics from XR subsystems.  
### Structs
Struct | Description  
---|---  
[Bone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Bone.html) | A tracked bone on the device at an XRNode in the XR input subsystem.  
[Eyes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Eyes.html) | Contains eye tracking data from the device at an XRNode in the XR input subsystem.  
[Hand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.html) | A tracked hand on the device at an XRNode in the XR input subsystem.  
[HapticCapabilities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.HapticCapabilities.html) | Describes the haptic capabilities of the device at an XRNode in the XR input subsystem.  
[InputDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice.html) | Defines an input device in the XR input subsystem.  
[InputFeatureUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputFeatureUsage.html) | Defines a generic usage that maps to an input feature on a device. Use the As method to turn into a generic usage.  
[InputFeatureUsage<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputFeatureUsage_1.html) | Defines a generic usage that maps to an input feature on a device.  
[MeshGenerationResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshGenerationResult.html) | Contains event information related to a generated mesh.  
[MeshId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshId.html) | A session-unique identifier for trackables in the environment, e.g., planes and feature points.  
[MeshInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshInfo.html) | Contains state information related to a tracked mesh.  
[MeshTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshTransform.html) | Contains transform information related to a tracked mesh.  
[XRMirrorViewBlitMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMirrorViewBlitMode.html) | Engine reserved blit modes. Blit mode capabilities should be queried from XRDisplaySubsystemDescriptor.GetAvailableMirrorBlitModeCount and XRDisplaySubsystemDescriptor.GetMirrorBlitModeByIndex.  
[XRMirrorViewBlitModeDesc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMirrorViewBlitModeDesc.html) | Struct that describes the mirror view blit mode.  
[XRNodeState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNodeState.html) | Describes the state of a node tracked by an XR system.  
### Enumerations
Enumeration | Description  
---|---  
[HandFinger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.HandFinger.html) | Enumeration describing the AR rendering mode used with Hand.  
[InputDeviceCharacteristics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.html) | A set of bit flags describing InputDevice characteristics.  
[InputDeviceRole](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceRole.html) | Enumeration describing the role of a InputDevice in providing input.  
[InputTrackingState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputTrackingState.html) | Represents the values being tracked for this device.  
[MeshChangeState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshChangeState.html) | The state of a tracked mesh since the last query.  
[MeshGenerationOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshGenerationOptions.html) | Options for generating meshes.  
[MeshGenerationStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshGenerationStatus.html) | The status of a XRMeshSubsystem.GenerateMeshAsync.  
[MeshVertexAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.MeshVertexAttributes.html) | A set of vertex attributes.  
[TrackingOriginModeFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.TrackingOriginModeFlags.html) | This enum provides context to where the 0,0,0 point of tracking for InputDevices is.  
[XRNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.html) | Enumeration of XR nodes which can be updated by XR input or sent haptic data.  
* * *
