* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-value.html

#  [Random](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.html).value
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
value; 
### Description
Returns a random float within [0.0..1.0] (range is inclusive) (Read Only).
**Important** : Both the lower and upper bounds are **inclusive**. Any given float value between 0.0 and 1.0, _including both 0.0 and 1.0_ , will appear on average approximately once every ten million random samples.  
  
See [Random](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.html) for more examples of how `UnityEngine.Random` may be different from other random number generators. 
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) randomColor = RandomColor();
    }  
  
    // Generate a random color value.
    Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) RandomColor()
    {
        // A different random value is used for each color component (if
        // the same is used for R, G and B, a shade of grey is produced).
        return new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(Random.value[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-value.html), Random.value[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-value.html), Random.value[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-value.html));
    }
}

```

* * *
