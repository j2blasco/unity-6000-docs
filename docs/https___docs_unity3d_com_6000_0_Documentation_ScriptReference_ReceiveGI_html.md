* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReceiveGI.html

# ReceiveGI
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
This property only takes effect if you enable a global illumination setting such as [Baked Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html#MixedLighting.html) or [Enlighten Realtime Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html#RealtimeLighting.html) for the target Scene. When you enable ReceiveGI, you can determine whether illumination data at runtime will come from [Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html) or Lightmaps. When you set ReceiveGI to Lightmaps, the Mesh Renderer receives global illumination from lightmaps. That means the Renderer is included in lightmap atlases, possibly increasing their size, memory consumption and storage costs. Calculating global illumination values for texels in this Renderer also adds to bake times. When you set ReceiveGI to Light Probes, the Mesh Renderer is not assigned space in lightmap atlases. Instead it receives global illumination stored by Light Probes in the target Scene. This can reduce bake times by avoiding the memory consumption and storage cost associated with lightmaps. ReceiveGI is only editable if you enable [StaticEditorFlags.ContributeGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/StaticEditorFlags.ContributeGI.html) for the GameObject associated with the target Mesh Renderer. Otherwise this property defaults to the Light Probes setting.
### Properties
Property | Description  
---|---  
[Lightmaps](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReceiveGI.Lightmaps.html) | Makes the GameObject use lightmaps to receive Global Illumination.   
[LightProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReceiveGI.LightProbes.html) | The object will have the option to use Light Probes to receive Global Illumination. See LightProbeUsage.  
* * *
