* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.PostProcessing.ReferenceProbePostProcessor.WindowSphericalHarmonicsL2.html

#  [ReferenceProbePostProcessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.PostProcessing.ReferenceProbePostProcessor.html).WindowSphericalHarmonicsL2
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
## Declaration
public bool WindowSphericalHarmonicsL2([LightTransport.IDeviceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.html) context, BufferSlice<SphericalHarmonicsL2> shIn, BufferSlice<SphericalHarmonicsL2> shOut, int probeCount); 
### Parameters
Parameter | Description  
---|---  
context | Device context.  
shIn | Source buffer of irradiance light probes encoded as SphericalHarmonicsL2.  
shOut | Destination buffer of the windowed spherical irradiance encoded as SphericalHarmonicsL2.  
probeCount | Number of SphericalHarmonicsL2 probes to window.  
### Returns
**bool** True if the operation was successfully added to the command queue on the context. 
### Description
Apply a windowing operation on an array of [SphericalHarmonicsL2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.html) probes.
Ringing is an artifact that can occur on light probes if they are subject to drastic changes in lighting. Light may overshoot and appear in the opposite end of the probe. This method is useful to reduce the artifact and its suggested use is to apply it on the direct part of the lighting before combining it with the indirect contribution.
* * *
