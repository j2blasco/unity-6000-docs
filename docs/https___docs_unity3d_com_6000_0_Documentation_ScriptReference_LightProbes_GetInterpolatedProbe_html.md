* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.GetInterpolatedProbe.html

#  [LightProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.html).GetInterpolatedProbe
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
public static void GetInterpolatedProbe([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Renderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) renderer, out [Rendering.SphericalHarmonicsL2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SphericalHarmonicsL2.html) probe); 
### Description
Returns an interpolated probe for the given position for both real-time and baked light probes combined.
Renderer is only needed to speed up the search for the current tetrahedron, as it caches the index of the tetrahedron it was in the last frame.
* * *
