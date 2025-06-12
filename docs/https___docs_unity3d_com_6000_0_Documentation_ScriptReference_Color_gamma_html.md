* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-gamma.html

#  [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html).gamma
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
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) gamma; 
### Description
A version of the color that has had the gamma curve applied.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) newColor = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.3f, 0.4f, 0.6f);
        print(newColor.gamma);
    }
}

```

* * *
