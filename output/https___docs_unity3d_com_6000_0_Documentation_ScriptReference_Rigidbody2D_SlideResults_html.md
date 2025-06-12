* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideResults.html

# SlideResults
struct in UnityEngine
/
Implemented in:[UnityEngine.Physics2DModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.Physics2DModule.html)
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
The results of a slide movement performed with [Rigidbody2D.Slide](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.Slide.html).
These results can be used to both tune movement configuration and to implement further logic to react to the specific surfaces encountered when a slide occurs.  
  
**NOTE:** This struct can be used in the Unity Inspector for display purposes.  
  
Additional resources: [Rigidbody2D.Slide](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.Slide.html) and [SlideMovement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideMovement.html).
### Properties
Property | Description  
---|---  
[iterationsUsed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideResults-iterationsUsed.html) | Returns the number of iterations used when performing a Rigidbody2D.Slide.  
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideResults-position.html) | The position that was calculate as a target position to move to when performing a Rigidbody2D.Slide.  
[remainingVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideResults-remainingVelocity.html) | Returns the remaining velocity that couldn't be used when performing a Rigidbody2D.Slide.  
[slideHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideResults-slideHit.html) | The specific contact found when a slide movement is performed with Rigidbody2D.Slide.  
[surfaceHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.SlideResults-surfaceHit.html) | The specific contact found when a slide movement is performed with Rigidbody2D.Slide.  
* * *
