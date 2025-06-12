* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.BlendProbes.html

#  [LightProbeUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.html).BlendProbes
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
Simple light probe interpolation is used.
If baked light probes are present in the Scene, an interpolated light probe will be calculated for this object and set as built-in shader uniform variables. Surface shaders use this information automatically. To add light probe contribution to your custom non-surface shaders, use ShadeSH9(worldSpaceNormal) in your vertex or pixel shader.  
  
Additional resources: [Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html).
* * *
