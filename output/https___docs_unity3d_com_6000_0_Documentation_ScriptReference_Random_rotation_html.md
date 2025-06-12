* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-rotation.html

#  [Random](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.html).rotation
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
[Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation; 
### Description
Returns a random rotation (Read Only).
Randomize the `x`, `y`, `z`, and `w` of a [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) each to [-1.0..1.0] (inclusive) via [Range](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html) and normalize the result. See also [rotationUniform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-rotationUniform.html) for a slower but higher quality algorithm.
```
using UnityEngine;  
  
// Click the "Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html)!" button and a rotation will be applied  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnGUI()
    {
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 100, 50), "Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html)!"))
        {
            transform.rotation = Random.rotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-rotation.html);
        }
    }
}

```

* * *
