* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-transparencySortAxis.html

#  [GraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.html).transparencySortAxis
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) transparencySortAxis; 
### Description
An axis that describes the direction along which the distances of objects are measured for the purpose of sorting.
This is the default axis used by the rendering pipeline for sorting in [TransparencySortMode.CustomAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TransparencySortMode.CustomAxis.html) mode for all Cameras including the SceneView's. You may override this for each invididual Camera by calling [Camera.transparencySortAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-transparencySortAxis.html) and [Camera.transparencySortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-transparencySortMode.html) APIs.  
  
Additional resources: [TransparencySortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TransparencySortMode.html) enum, [Camera.transparencySortAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-transparencySortAxis.html), [Camera.transparencySortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-transparencySortMode.html).
* * *
