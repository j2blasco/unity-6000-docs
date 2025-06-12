* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-textureSheetAnimation.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).textureSheetAnimation
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
[ParticleSystem.TextureSheetAnimationModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TextureSheetAnimationModule.html) textureSheetAnimation; 
### Description
Script interface for the TextureSheetAnimationModule of a Particle System.
This module allows you to add animations to your particle textures. This is achieved by authoring flipbook textures.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/ParticleFlipbook.png)  
_A flipbook texture sheet that contains eight sub-images of the numbers 1-8 across two rows of four columns. The first row contains the numbers 1-4 and the second row contains the numbers 5-8._  
  
Each numbered region represents a frame of the animation, and must be distributed evenly across the texture. Select a variable below to see script examples. You may want to use this texture on your Particle System with each example, to see how the module works.  
  
Particle System modules do not need to be reassigned back to the system; they are interfaces and not independent objects.
```
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {
    void Start() {
        ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        var ts = ps.textureSheetAnimation;
            ts.enabled = true;
        ts.numTilesX = 2;
        ts.rowMode = ParticleSystemAnimationRowMode.Random[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemAnimationRowMode.Random.html);
    }
}
```

* * *
