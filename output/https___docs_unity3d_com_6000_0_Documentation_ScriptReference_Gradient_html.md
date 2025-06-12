* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html

# Gradient
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Represents a Gradient used for animating colors.
Gradients allow animating or interpolating colors by having several "color keys" and "alpha keys". Color keys and alpha keys are separate, and each key has a time specified for it, ranging from 0.0 (0%) to 1.0 (100%). Note that the alpha and colors keys will be automatically sorted by time value and that it is ensured to always have a minimum of 2 color keys and 2 alpha keys.  
  
How the colors are interpolated between the keys is controlled by [GradientMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientMode.html).  
  
Public Gradient variables used in scripts automatically display the gradient editor in the inspector window. [GradientUsageAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientUsageAttribute.html) allows specifying whether the gradient colors should be high dynamic range for editing.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        var gradient = new Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html)();  
  
        // Blend color from red at 0% to blue at 100%
        var colors = new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)[2];
        colors[0] = new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)(Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html), 0.0f);
        colors[1] = new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)(Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html), 1.0f);  
  
        // Blend alpha from opaque at 0% to transparent at 100%
        var alphas = new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)[2];
        alphas[0] = new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)(1.0f, 0.0f);
        alphas[1] = new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)(0.0f, 1.0f);  
  
        gradient.SetKeys(colors, alphas);  
  
        // What's the color at the relative time 0.25 (25%) ?
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(gradient.Evaluate(0.25f));
    }
}

```

Additional resources: [GradientColorKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html), [GradientAlphaKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html), [SerializedProperty.gradientValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-gradientValue.html).
### Properties
Property | Description  
---|---  
[alphaKeys](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient-alphaKeys.html) | All alpha keys defined in the gradient.  
[colorKeys](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient-colorKeys.html) | All color keys defined in the gradient.  
[colorSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient-colorSpace.html) | Indicates the color space that the gradient color keys are using.  
[mode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient-mode.html) | Controls how the gradient colors are interpolated.  
### Constructors
Constructor | Description  
---|---  
[Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient-ctor.html) | Create a new Gradient object.  
### Public Methods
Method | Description  
---|---  
[Evaluate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.Evaluate.html) | Calculate color at a given time.  
[SetKeys](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.SetKeys.html) | Setup Gradient with an array of color keys and alpha keys.  
* * *
