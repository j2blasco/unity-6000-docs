* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-rotationUniform.html

#  [Random](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.html).rotationUniform
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-random.html "Go to Random Component in the Manual")
[Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotationUniform; 
### Description
Returns a random rotation with uniform distribution (Read Only).
Employs [Hopf fibration](https://en.wikipedia.org/wiki/Hopf_fibration) to return a random [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) within a uniformly distributed selection space. Gives higher quality results compared to the more naive approach employed by [rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-rotation.html), though at a 40% performance cost.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Sets a random orientation for the object.
        transform.rotation = Random.rotationUniform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-rotationUniform.html);
    }
}

```

* * *
