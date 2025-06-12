* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-alignment.html

#  [ParticleSystemRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html).alignment
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
[ParticleSystemRenderSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderSpace.html) alignment; 
### Description
Control the direction that particles face.
For many applications, it is beneficial for particles to always face the Camera. This property allows you to change whether particles in the system face the Camera or not.  
  
Particles can face the Camera in two ways:  
  
1) Aligned to the Camera plane, so that all particles are aligned with the same facing direction.  
2) Aligned individually to face the eye position, which can be more convincing for particles that approach the Camera in close proximity or for VR environments.  
  
Unaligned particles can be set to align to the world or to their local transform, as required.
```
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) {  
  
    private ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html) ps;
    private ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html) psr;
    public ParticleSystemRenderSpace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderSpace.html) alignment = ParticleSystemRenderSpace.View[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderSpace.View.html);  
  
    void Start() {  
  
        Camera.main.transform.rotation = Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(0.0f, 20.0f, 0.0f);   // rotate the camera so we can see the difference between view and world space  
  
        ps = GetComponent<ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)>();
        psr = GetComponent<ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html)>();  
  
        var main = ps.main;
        main.startSpeed = 2.0f;  
  
        psr.material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Sprites/Default"));
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)() {
        psr.alignment = alignment;
    }  
  
    void OnGUI() {
        alignment = (ParticleSystemRenderSpace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderSpace.html))GUI.SelectionGrid[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.SelectionGrid.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 25, 300, 30), (int)alignment, new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)[] { new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("View"), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("World"), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Local"), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Facing") }, 4);
    }
}

```

* * *
