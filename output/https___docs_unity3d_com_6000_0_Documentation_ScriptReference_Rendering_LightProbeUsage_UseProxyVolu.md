* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.UseProxyVolume.html

#  [LightProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.html).UseProxyVolume
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
Uses a 3D grid of interpolated light probes.
A **Light Probe Proxy Volume** component which may reside on the same game object or on another game object will be required. In order to use a **Light Probe Proxy Volume** component which resides on another game object, you must use the **Proxy Volume Override** property where you can specify the source game object.  
  
Surface shaders use the information associated with the proxy volume automatically. To use the proxy volume information in your custom shaders, you can use ShadeSHPerPixel function in your pixel shader.  
  
Additional resources: [Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html), [Light Probe Proxy Volume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeProxyVolume.html).
* * *
