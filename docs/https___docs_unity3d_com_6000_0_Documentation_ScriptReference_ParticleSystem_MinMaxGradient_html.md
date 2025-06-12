* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient.html

# MinMaxGradient
struct in UnityEngine
/
Implemented in:[UnityEngine.ParticleSystemModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.ParticleSystemModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html "Go to ParticleSystem Component in the Manual")
### Description
Script interface for a Min-Max Gradient.
This contains two [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html)s, and returns a [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) based on [ParticleSystem.MinMaxGradient.mode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient-mode.html). Depending on the mode, this may return the value randomized. Gradients are edited via the ParticleSystem Inspector once a [ParticleSystemGradientMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemGradientMode.html) requiring them has been selected. Some modes do not require gradients, only colors. Additional resources: [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).
```
using UnityEngine;  
  
// This example shows setting a constant color value.
public class ConstantColorExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) myParticleSystem;
    ParticleSystem.ColorOverLifetimeModule[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ColorOverLifetimeModule.html) colorModule;  
  
    void Start()
    {
        // Get the system and the color module.
        myParticleSystem = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        colorModule = myParticleSystem.colorOverLifetime;  
  
        GetValue();
        SetValue();
    }  
  
    void GetValue()
    {
        print("The constant color is " + colorModule.color.color);
    }  
  
    void SetValue()
    {
        colorModule.color = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
    }
}

```

```
using UnityEngine;  
  
// This example shows using 2 colors to drive the color over lifetime.
public class TwoConstantColorsExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) myParticleSystem;
    ParticleSystem.ColorOverLifetimeModule[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ColorOverLifetimeModule.html) colorModule;  
  
    void Start()
    {
        // Get the system and the color module.
        myParticleSystem = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        colorModule = myParticleSystem.colorOverLifetime;  
  
        GetValue();
        SetValue();
    }  
  
    void GetValue()
    {
        print(string.Format("The constant values are: min {0} max {1}.", colorModule.color.colorMin, colorModule.color.colorMax));
    }  
  
    void SetValue()
    {
        colorModule.color = new ParticleSystem.MinMaxGradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient.html)(Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html), Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html));
    }
}

```

```
using UnityEngine;  
  
// This example shows using a gradient to drive the color over lifetime.
public class GradientColorExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) myParticleSystem;
    ParticleSystem.ColorOverLifetimeModule[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ColorOverLifetimeModule.html) colorModule;
    Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) ourGradient;  
  
    void Start()
    {
        // Get the system and the color module.
        myParticleSystem = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        colorModule = myParticleSystem.colorOverLifetime;  
  
        // A simple 2 color gradient with a fixed alpha of 1.0f.
        float alpha = 1.0f;
        ourGradient = new Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html)();
        ourGradient.SetKeys(
            new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)[] { new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)(Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html), 0.0f), new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)(Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html), 1.0f) },
            new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)[] { new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)(alpha, 0.0f), new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)(alpha, 1.0f) }
        );  
  
        // Apply the gradient.
        colorModule.color = ourGradient;  
  
        // In 5 seconds we will modify the gradient.
        Invoke("ModifyGradient", 5.0f);
    }  
  
    void ModifyGradient()
    {
        // Reduce the alpha
        float alpha = 0.5f;
        ourGradient.SetKeys(
            new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)[] { new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)(Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html), 0.0f), new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)(Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html), 1.0f) },
            new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)[] { new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)(alpha, 0.0f), new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)(alpha, 1.0f) }
        );  
  
        // Apply the changed gradient.
        colorModule.color = ourGradient;
    }
}

```

```
using UnityEngine;  
  
// This example shows using 2 gradients to drive the color over lifetime.
public class TwoGradientColorExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) myParticleSystem;
    ParticleSystem.ColorOverLifetimeModule[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ColorOverLifetimeModule.html) colorModule;  
  
    Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) ourGradientMin;
    Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) ourGradientMax;  
  
    void Start()
    {
        // Get the system and the emission module.
        myParticleSystem = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        colorModule = myParticleSystem.colorOverLifetime;  
  
        // A simple 2 color gradient with a fixed alpha of 1.0f.
        float alpha1 = 1.0f;
        ourGradientMin = new Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html)();
        ourGradientMin.SetKeys(
            new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)[] { new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)(Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html), 0.0f), new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)(Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html), 1.0f) },
            new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)[] { new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)(alpha1, 0.0f), new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)(alpha1, 1.0f) }
        );  
  
        // A simple 2 color gradient with a fixed alpha of 0.0f.
        float alpha2 = 0.0f;
        ourGradientMax = new Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html)();
        ourGradientMax.SetKeys(
            new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)[] { new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)(Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html), 0.0f), new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)(Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html), 1.0f) },
            new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)[] { new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)(alpha2, 0.0f), new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)(alpha2, 1.0f) }
        );  
  
        // Apply the gradients.
        colorModule.color = new ParticleSystem.MinMaxGradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient.html)(ourGradientMin, ourGradientMax);  
  
        // In 5 seconds we will modify the gradient.
        Invoke("ModifyGradient", 5.0f);
    }  
  
    void ModifyGradient()
    {
        // Reduce the alpha
        float alpha = 0.5f;
        ourGradientMin.SetKeys(
            new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)[] { new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)(Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html), 0.0f), new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)(Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html), 1.0f) },
            new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)[] { new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)(alpha, 0.0f), new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)(alpha, 1.0f) }
        );  
  
        // Apply the changed gradients.
        colorModule.color = new ParticleSystem.MinMaxGradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient.html)(ourGradientMin, ourGradientMax);
    }
}

```

```
using UnityEngine;  
  
// This example shows how to retrieve existing color and alpha keys from a MinMaxGradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient.html)
public class ReadGradientExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Get the system and the color module.
        var myParticleSystem = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        var colorModule = myParticleSystem.colorOverLifetime;  
  
        // Get the gradient (assuming the MinMaxGradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient.html) is in Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) mode)
        Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) gradient = colorModule.color.gradient;  
  
        // Get the keys
        GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)[] colorKeys = gradient.colorKeys;
        GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)[] alphaKeys = gradient.alphaKeys;
    }
}

```

### Properties
Property | Description  
---|---  
[color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient-color.html) | Set a constant color.  
[colorMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient-colorMax.html) | Set a constant color for the upper bound.  
[colorMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient-colorMin.html) | Set a constant color for the lower bound.  
[gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient-gradient.html) | Set the gradient.  
[gradientMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient-gradientMax.html) | Set a gradient for the upper bound.  
[gradientMin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient-gradientMin.html) | Set a gradient for the lower bound.  
[mode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient-mode.html) | Set the mode that the Min-Max Gradient uses to evaluate colors.  
### Constructors
Constructor | Description  
---|---  
[ParticleSystem.MinMaxGradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient-ctor.html) | A single constant color for the entire gradient.  
### Public Methods
Method | Description  
---|---  
[Evaluate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxGradient.Evaluate.html) | Manually query the gradient to calculate colors based on what mode it is in.  
* * *
