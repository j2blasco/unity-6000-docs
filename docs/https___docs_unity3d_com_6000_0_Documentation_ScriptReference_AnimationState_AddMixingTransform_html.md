* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.AddMixingTransform.html

#  [AnimationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.html).AddMixingTransform
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
## Declaration
public void AddMixingTransform([Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) mix, bool recursive = true); 
### Parameters
Parameter | Description  
---|---  
mix | The transform to animate.  
recursive | Whether to also animate all children of the specified transform.  
### Description
Adds a transform which should be animated. This allows you to reduce the number of animations you have to create.
For example you might have a handwaving animation. You might want to play the hand waving animation on a idle character or on a walking character. Either you have to create 2 hand waving animations one for idle, one for walking. By using mixing the hand waving animation will have full control of the shoulder. But the lower body will not be affected by it, and continue playing the idle or walk animation. Thus you only need one hand waving animation.  
  
If `recursive` is true all children of the `mix` transform will also be animated. If you don't call AddMixingTransform, all animation curves will be used.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) anim;
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) shoulder;  
  
    void Start()
    {
        // Add mixing transform
        anim["wave_hand"].AddMixingTransform(shoulder);
    }
}

```

Another example using a path:
```
using UnityEngine;
using System.Collections;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) anim;  
  
    void Start()
    {
        // Adds a mixing transform using a path instead
        Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) mixTransform = transform.Find("root/upper_body/left_shoulder");  
  
        // Add mixing transform
        anim["wave_hand"].AddMixingTransform(mixTransform);
    }
}

```

* * *
