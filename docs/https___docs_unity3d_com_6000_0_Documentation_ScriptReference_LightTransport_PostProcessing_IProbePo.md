* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.PostProcessing.IProbePostProcessor.html

# IProbePostProcessor
interface in UnityEngine.LightTransport.PostProcessing
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
Interface for light probe post processing.
The interface provides common operations for light probes encoded as [SphericalHarmonicsL2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.html). Operations include radiance to irradiance conversion, conversion to the format expected by Unity for rendering (refer to [IProbePostProcessor.ConvertToUnityFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.PostProcessing.IProbePostProcessor.ConvertToUnityFormat.html)), addition, and scaling.
### Public Methods
Method | Description  
---|---  
[AddSphericalHarmonicsL2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.PostProcessing.IProbePostProcessor.AddSphericalHarmonicsL2.html) | Add two arrays of SphericalHarmonicsL2 together.  
[ConvertToUnityFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.PostProcessing.IProbePostProcessor.ConvertToUnityFormat.html) | Converts light probes encoded as SphericalHarmonicsL2 to the format expected by the Unity renderer.  
[ConvolveRadianceToIrradiance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.PostProcessing.IProbePostProcessor.ConvolveRadianceToIrradiance.html) | Convolve radiance to irradiance.  
[DeringSphericalHarmonicsL2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.PostProcessing.IProbePostProcessor.DeringSphericalHarmonicsL2.html) | De-ring an array of SphericalHarmonicsL2 probes.  
[Initialize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.PostProcessing.IProbePostProcessor.Initialize.html) | Initialize the IProbePostProcessor.  
[ScaleSphericalHarmonicsL2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.PostProcessing.IProbePostProcessor.ScaleSphericalHarmonicsL2.html) | Scale an array of SphericalHarmonicsL2 probes.  
[WindowSphericalHarmonicsL2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.PostProcessing.IProbePostProcessor.WindowSphericalHarmonicsL2.html) | Apply a windowing operation on an array of SphericalHarmonicsL2 probes.  
* * *
