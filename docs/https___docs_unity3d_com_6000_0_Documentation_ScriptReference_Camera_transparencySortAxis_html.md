* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-transparencySortAxis.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).transparencySortAxis
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) transparencySortAxis; 
### Description
An axis that describes the direction along which the distances of objects are measured for the purpose of sorting.
If the [TransparencySortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TransparencySortMode.html) of the [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) or [GraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.html) are set to [TransparencySortMode.CustomAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TransparencySortMode.CustomAxis.html), the rendering pipeline evaluates the distance of the object along the axis specified by this property.  
  
This is used for sorting Renderer components when other, higher priority, criterias fail to distinguish the render order.  
  
This is a useful technique in 2.5D games or isometric games where the [SpriteRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteRenderer.html)s need to be sorted along the vertical screen axis. For this specific use case, set the TransparencySortMode to [TransparencySortMode.CustomAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TransparencySortMode.CustomAxis.html) and set the axis to (0.0f, 1.0f, 0.0f).
* * *
