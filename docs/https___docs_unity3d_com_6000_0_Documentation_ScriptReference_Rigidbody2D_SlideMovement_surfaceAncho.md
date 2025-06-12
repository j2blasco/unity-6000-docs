* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideMovement-surfaceAnchor.html

#  [Rigidbody2D.SlideMovement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideMovement.html).surfaceAnchor
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
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) surfaceAnchor; 
### Description
The direction and distance to use when detecting if a surface is nearby during a slide iteration.
During a Rigiodbody2D.Slide this vector is used to detect if a surface is nearby and will cause the slide to be anchored in that direction to the surface.  
  
The default is [Vector2.down](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-down.html) which is a typical direction and distance used in platformers however this can be reduced in distance so that the surface anchoring is more subtle. If the surface anchor is [Vector2.zero](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html) then surface anchoring will be disabled.  
  
Additional resources: [Rigidbody2D.Slide](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.Slide.html) and [SlideResults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideResults.html).
* * *
