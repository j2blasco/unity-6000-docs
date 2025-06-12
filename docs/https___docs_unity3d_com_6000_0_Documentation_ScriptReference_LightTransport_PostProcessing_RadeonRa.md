* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.PostProcessing.RadeonRaysProbePostProcessor.AddSphericalHarmonicsL2.html

#  [RadeonRaysProbePostProcessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.PostProcessing.RadeonRaysProbePostProcessor.html).AddSphericalHarmonicsL2
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
public bool AddSphericalHarmonicsL2([LightTransport.IDeviceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.html) context, BufferSlice<SphericalHarmonicsL2> a, BufferSlice<SphericalHarmonicsL2> b, BufferSlice<SphericalHarmonicsL2> sum, int probeCount); 
### Parameters
Parameter | Description  
---|---  
context | Device context.  
A | Source buffer A.  
B | Source buffer B.  
sum | Destination buffer where the sum of A and B is written.  
probeCount | Number of SphericalHarmonicsL2 probes to add.  
### Returns
**bool** True if the operation is successfully added to the command queue in the context. 
### Description
Add two arrays of [SphericalHarmonicsL2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.html) together.
Sum = A + B.
* * *
