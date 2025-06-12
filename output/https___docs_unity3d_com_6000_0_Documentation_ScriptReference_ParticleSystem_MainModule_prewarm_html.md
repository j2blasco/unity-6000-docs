* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-prewarm.html

#  [ParticleSystem.MainModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule.html).prewarm
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
prewarm; 
### Description
If [ParticleSystem.MainModule.loop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-loop.html) is true, when you enable this property, the Particle System looks like it has already simulated for one loop when first becoming visible.
```
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps;
    public bool usePrewarm;  
  
    void Start()
    {
        ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();  
  
        var main = ps.main;
        main.loop = true;   // prewarm only works on looping systems  
  
        Restart();
    }  
  
    void OnGUI()
    {
        bool newPrewarm = GUI.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 60, 200, 30), usePrewarm, "Use Prewarm");  
  
        if (newPrewarm != usePrewarm)
        {
            usePrewarm = newPrewarm;
            Restart();
        }
    }  
  
    void Restart()
    {
        ps.Stop();
        ps.Clear();  
  
        var main = ps.main;
        main.prewarm = usePrewarm;  
  
        ps.Play();
    }
}

```

* * *
