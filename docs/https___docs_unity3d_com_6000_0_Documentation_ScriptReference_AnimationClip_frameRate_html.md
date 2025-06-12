* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip-frameRate.html

#  [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html).frameRate
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html "Go to AnimationClip Component in the Manual")
frameRate; 
### Description
Frame rate at which keyframes are sampled. (Read Only)
This is the frame rate that was used in the animation program you used to create the animation or model.  
  

```
using UnityEngine;
using System.Collections;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) anim;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Prints the frame rate of the animation clip to the console
        print(anim["walk"].clip.frameRate);
    }
}

```

* * *
