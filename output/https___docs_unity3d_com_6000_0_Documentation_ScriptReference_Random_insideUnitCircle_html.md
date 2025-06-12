* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-insideUnitCircle.html

#  [Random](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.html).insideUnitCircle
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
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) insideUnitCircle; 
### Description
Returns a random point inside or on a circle with radius 1.0 (Read Only).
Note that the probability space includes the perimeter of the circle because [value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-value.html), which is inclusive to 1.0, is used to acquire a random radius.
```
using UnityEngine;  
  
public class ScriptExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Sets the position to be somewhere inside a circle
        // with radius 5 and the center at zero. Note that
        // assigning a Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) to a Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) is fine - it will
        // just set the X and Y values.
        transform.position = Random.insideUnitCircle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-insideUnitCircle.html) * 5;
    }
}

```

* * *
