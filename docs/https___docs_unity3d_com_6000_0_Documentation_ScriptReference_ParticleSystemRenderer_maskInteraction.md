* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer-maskInteraction.html

#  [ParticleSystemRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html).maskInteraction
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
[SpriteMaskInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.html) maskInteraction; 
### Description
Specifies how the Particle System Renderer interacts with [SpriteMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMask.html).
By default, particles do not interact with SpriteMasks and are visible regardless of whether you assign a SpriteMask or not. You can make the ParticleSystemRenderer visible either inside or outside a SpriteMask. To do the former, set this to [SpriteMaskInteraction.VisibleInsideMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.VisibleInsideMask.html). To do the latter, set this to [SpriteMaskInteraction.VisibleOutsideMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.VisibleOutsideMask.html). Additional resources: [SpriteMaskInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.html).
```
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(ParticleSystem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html) psr;
    public SpriteMaskInteraction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.html) maskInteraction;  
  
    void Start()
    {
        psr = GetComponent<ParticleSystemRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        psr.maskInteraction = maskInteraction;
    }  
  
    void OnGUI()
    {
        maskInteraction = (SpriteMaskInteraction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpriteMaskInteraction.html))GUI.SelectionGrid[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.SelectionGrid.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 25, 900, 30), (int)maskInteraction, new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)[] { new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("No Masking"), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Visible Inside Mask"), new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Visible Outside Mask") }, 3);
    }
}

```

* * *
