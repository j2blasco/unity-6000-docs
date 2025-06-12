* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Play.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).Play
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
## Declaration
public void Play(); 
## Declaration
public void Play(bool withChildren = true); 
### Parameters
Parameter | Description  
---|---  
withChildren | Play all child Particle Systems as well.  
### Description
Starts the Particle System.
Sets the Particle Systems into play mode and enables emitting (if it has been disabled).  
  
If the Particle System has been **paused** , then this resumes playing from the previous time.  
If the Particle System has **stopped** , then the system starts from time 0, and, if it is relevant, the [startDelay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-startDelay.html) is applied. If the Particle System is **already playing** , the system continues to play and this function has no effect.  
  
**Note**: Unity does not apply [ParticleSystem.MainModule.prewarm](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-prewarm.html) when the Particle System resumes from a paused state. To apply `prewarm` when the Particle System resumes, call [Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Clear.html) after [Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Stop.html).  
  
**Note**: If you invoke this function again before the particle system has had time to spawn a particle, the particle system restarts its internal counters. This means that if you invoke this function continuously, a particle system with a low emission rate will never start to play.  
  
Additional resources: [Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Stop.html), [Pause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Pause.html), [isEmitting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-isEmitting.html) functions.  
  
The following example creates a GUI window for manipulating a Particle System.
```
using UnityEngine;  
  
public class ParticleSystemControllerWindow : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) system
    {
        get
        {
            if (_CachedSystem == null)
                _CachedSystem = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
            return _CachedSystem;
        }
    }
    private ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) _CachedSystem;  
  
    public Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) windowRect = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 300, 120);  
  
    public bool includeChildren = true;  
  
    void OnGUI()
    {
        windowRect = GUI.Window[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Window.html)("ParticleController".GetHashCode(), windowRect, DrawWindowContents, system.name);
    }  
  
    void DrawWindowContents(int windowId)
    {
        if (system)
        {
            GUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginHorizontal.html)();
            GUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Toggle.html)(system.isPlaying, "Playing");
            GUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Toggle.html)(system.isEmitting, "Emitting");
            GUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Toggle.html)(system.isPaused, "Paused");
            GUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndHorizontal.html)();  
  
            GUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginHorizontal.html)();
            if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Play"))
                system.Play(includeChildren);
            if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Pause"))
                system.Pause(includeChildren);
            if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Stop Emitting"))
                system.Stop(includeChildren, ParticleSystemStopBehavior.StopEmitting[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemStopBehavior.StopEmitting.html));
            if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Stop & Clear"))
                system.Stop(includeChildren, ParticleSystemStopBehavior.StopEmittingAndClear[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemStopBehavior.StopEmittingAndClear.html));
            GUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndHorizontal.html)();  
  
            includeChildren = GUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Toggle.html)(includeChildren, "Include Children");  
  
            GUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginHorizontal.html)();
            GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html)(" + system.time + ")");
            GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) Count(" + system.particleCount + ")");
            GUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndHorizontal.html)();
        }
        else
            GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("No Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html) found");  
  
        GUI.DragWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.DragWindow.html)();
    }
}

```

* * *
