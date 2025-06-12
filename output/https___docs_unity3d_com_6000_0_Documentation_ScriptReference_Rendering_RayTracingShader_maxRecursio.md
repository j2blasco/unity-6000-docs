* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader-maxRecursionDepth.html

#  [RayTracingShader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RayTracingShader.html).maxRecursionDepth
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
maxRecursionDepth; 
### Description
The maximum number of ray bounces this shader can trace (Read Only).
This value can be set in a .raytrace file using `#pragma max_recursion_depth` followed by a positive number.  
  
If you set `max_recursion_depth` value too low, your graphics device may go into removed state, and crash Unity. To generate rays, your `max_recursion_depth` value must be at least 0. However, if you invoke the `TraceRay` HLSL function inside a closest hit shader (for example) your `max_recursion_depth` value must be at least 1.
* * *
