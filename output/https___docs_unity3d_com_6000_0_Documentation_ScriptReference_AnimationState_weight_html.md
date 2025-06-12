* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-weight.html

#  [AnimationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.html).weight
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
weight; 
### Description
The weight of animation.
This calculates the blend weights for one curve.  
  
Weights are distributed so that the top layer gets everything. If it doesn't use the full weight then the next layer gets to distribute the remaining weights and so on. Once all weights are used by the top layers, no weights will be available for lower layers anymore Unity uses fair weighting, which means if a lower layer wants 80% and 50% have already been used up, the layer will NOT use up all weights. instead it will take up 80% of the 50%.  
  
**Example:** a upper body which is affected by wave, walk and idle a lower body which is affected by only walk and idle.  
  
- Blend weights can change per animated value because of mixing. Even without mixing, sometimes a curve is just not defined. Still you want the blend weights to add up to 1. Most of the time weights are similar between curves.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) anim;  
  
    void Start()
    {
        // Set the blend weight of the walk animation to 0.5
        anim["Walk"].weight = 0.5f;
    }
}

```

* * *
