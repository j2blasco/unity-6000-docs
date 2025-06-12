* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-isPlaying.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).isPlaying
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
isPlaying; 
### Description
Determines whether the Particle System is playing.
[isPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-isPlaying.html) is `true` from when the Particle System begins to play until its last live particle dies. [isPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-isPlaying.html) is `false` when the Particle System is no longer spawning particles and is not simulating any live particles. (Read Only).
```
using UnityEngine;  
  
// A particle sprite example of isPlaying. A button is created
// that shows whether the Particle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html) System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html) is running.  If not, then
// it can be started.  If it is running then it can be stopped.  
  
using UnityEngine;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex;
    private ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps;
    private Sprite[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html) sprite;  
  
    void Start()
    {
        ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        sprite = Sprite.Create[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.Create.html)(tex, new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0.0f, 0.0f, tex.width, tex.height), Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html));  
  
        var textureSheetAnimation = ps.textureSheetAnimation;
        textureSheetAnimation.enabled = true;
        textureSheetAnimation.mode = ParticleSystemAnimationMode.Sprites[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemAnimationMode.Sprites.html);
        textureSheetAnimation.AddSprite(sprite);
    }  
  
    void OnGUI()
    {
        if (ps.isPlaying)
        {
            if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 70, 150, 50), "Stop and clear"))
            {
                ps.Stop(true, ParticleSystemStopBehavior.StopEmittingAndClear[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemStopBehavior.StopEmittingAndClear.html));
            }
        }
        else
        {
            if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 70, 150, 50), "Play"))
            {
                ps.Play(false);
            }
        }
    }
}

```

* * *
