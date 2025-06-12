* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-maxParticleSize.html

#  [ParticleSystemRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html).maxParticleSize
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
maxParticleSize; 
### Description
Clamp the maximum particle size.
Particles can become very heavy on fillrate. Use this setting to make sure they don't use too much performance when up close to the viewer.
```
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {  
  
    private ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps;
    private ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html) psr;
    public float minSize = 0.0f;
    public float maxSize = 1.0f;  
  
    void Start() {  
  
        ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        psr = GetComponent<ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html)>();  
  
        var main = ps.main;
        main.startSize = new ParticleSystem.MinMaxCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MinMaxCurve.html)(0.1f, 5.0f);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)() {
        psr.minParticleSize = minSize;
        psr.maxParticleSize = maxSize;
    }  
  
    void OnGUI() {
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 40, 200, 30), "Minimum Screen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html) Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) Size");
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 80, 200, 30), "Maximum Screen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html) Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) Size");  
  
        minSize = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(245, 45, 100, 30), minSize, 0.0f, 1.0f);
        maxSize = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(245, 85, 100, 30), maxSize, 0.0f, 1.0f);
    }
}

```

* * *
