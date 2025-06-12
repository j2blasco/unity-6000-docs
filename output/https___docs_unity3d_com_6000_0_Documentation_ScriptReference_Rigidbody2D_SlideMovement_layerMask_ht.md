* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideMovement-layerMask.html

#  [Rigidbody2D.SlideMovement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideMovement.html).layerMask
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
[LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html) layerMask; 
### Description
A [LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html) that will be used when determining what [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) should be detected.
This [Layer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.Layer.html) will only be used when [Rigidbody2D.SlideMovement.useLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideMovement-useLayerMask.html) is true in which case, the specified [LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html) will be used to determine which [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) will be detected and any Layer Collision Matrix configuration will be ignored.  
  
In other words, this [LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html) can be used to override and explicitly specify which layers will be used to detect [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).  
  
Additional resources: [Rigidbody2D.SlideMovement.useLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideMovement-useLayerMask.html), [Rigidbody2D.Slide](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.Slide.html) and [SlideResults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideResults.html).
* * *
