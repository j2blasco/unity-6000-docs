* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialGlobalIlluminationFlags.html

# MaterialGlobalIlluminationFlags
enumeration
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
How the material interacts with lightmaps and lightprobes.
Additional resources: [Material.globalIlluminationFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-globalIlluminationFlags.html).
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialGlobalIlluminationFlags.None.html) | The emissive lighting does not affect Global Illumination at all.  
[RealtimeEmissive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialGlobalIlluminationFlags.RealtimeEmissive.html) | The emissive lighting will affect Enlighten Realtime Global Illumination. It emits lighting into real-time lightmaps and real-time Light Probes.  
[BakedEmissive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialGlobalIlluminationFlags.BakedEmissive.html) | The emissive lighting affects baked Global Illumination. It emits lighting into baked lightmaps and baked lightprobes.  
[EmissiveIsBlack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialGlobalIlluminationFlags.EmissiveIsBlack.html) | The emissive lighting is guaranteed to be black. This lets the lightmapping system know that it doesn't have to extract emissive lighting information from the material and can simply assume it is completely black.  
[AnyEmissive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialGlobalIlluminationFlags.AnyEmissive.html) | Helper Mask to be used to query the enum only based on whether Enlighten Realtime Global Illumination or baked GI is set, ignoring all other bits.  
* * *
