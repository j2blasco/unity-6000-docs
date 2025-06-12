* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.PixelPerfectRendering-pixelSnapSpacing.html

#  [PixelPerfectRendering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/U2D.PixelPerfectRendering.html).pixelSnapSpacing
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
pixelSnapSpacing; 
### Description
To achieve a pixel perfect render, Sprites must be displaced to discrete positions at render time. This value defines the minimum distance between these positions. This doesn’t affect the GameObject's transform position.
By default, a Sprite can be moved freely along all axes of the world space. By setting this property to a non-zero positive value, Sprite movement will always appear displaced to multiples of this value at render time.  
  
For a pixel perfect render, this value should be set to the size of a single on-screen pixel. Calculate this value with [Camera.orthographicSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-orthographicSize.html) * 2.0 / [Camera.pixelHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-pixelHeight.html) , when viewing the world space through the Orthographic Camera.  
  
This property is to be used together with the PixelPerfectCamera component for complete configuration of pixel perfect rendering.
* * *
