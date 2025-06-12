* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideMovement-gravitySlipAngle.html

#  [Rigidbody2D.SlideMovement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideMovement.html).gravitySlipAngle
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
gravitySlipAngle; 
### Description
When the gravity movement causes a contact with a [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html), slippage maybe occur if the surface angle is greater than this angle.
Use this angle threshold to control whether slippage will occur on surface slopes above the threshold.  
  
The angle is in degrees and is relative to the [Rigidbody2D.SlideMovement.surfaceUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideMovement-surfaceUp.html) vector.  
  
**NOTE:** Slippage will only occur if no initial `velocity` is passed to the [Rigidbody2D.Slide](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.Slide.html) method. Slippage will always occur if [Rigidbody2D.SlideMovement.surfaceUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideMovement-surfaceUp.html) has zero magnitude.  
  
Additional resources: [Rigidbody2D.SlideMovement.surfaceSlideAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideMovement-surfaceSlideAngle.html), [Rigidbody2D.Slide](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.Slide.html) and [SlideResults](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideResults.html).
* * *
