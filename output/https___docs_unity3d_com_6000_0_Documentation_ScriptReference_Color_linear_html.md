* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-linear.html

#  [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html).linear
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
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) linear; 
### Description
A linear value of an sRGB color.
Colors are typically expressed in sRGB color space. This property returns "linearized" color value, i.e. with inverse of sRGB gamma curve applied.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) newColor = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.3f, 0.4f, 0.6f);
        print(newColor.linear);
    }
}

```

Additional resources: [Linear and Gamma rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/LinearLighting.html), [ColorSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorSpace.html), [Mathf.GammaToLinearSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.GammaToLinearSpace.html), [Mathf.LinearToGammaSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.LinearToGammaSpace.html).
* * *
