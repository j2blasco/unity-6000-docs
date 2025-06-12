* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-additionalShaderChannels.html

#  [Canvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html).additionalShaderChannels
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
[AdditionalCanvasShaderChannels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AdditionalCanvasShaderChannels.html) additionalShaderChannels; 
### Description
Get or set the mask of additional shader channels to be used when creating the [Canvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html) mesh.
The [Canvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html) will always include Position, Color, and Uv0 shader channels when generating the mesh for a overlay [Canvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html) and will also include Normal and Tangent for ScreenSpace.Camera and World space [Canvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html). These are the optional additional parameters to be copied.
```
using UnityEngine;  
  
public class SetCanvasShaderChannels : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Canvas[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html) canvas;  
  
    void Start()
    {
        canvas.additionalShaderChannels |= AdditionalCanvasShaderChannels.Normal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AdditionalCanvasShaderChannels.Normal.html);
        canvas.additionalShaderChannels |= AdditionalCanvasShaderChannels.TexCoord1[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AdditionalCanvasShaderChannels.TexCoord1.html);
        canvas.additionalShaderChannels |= AdditionalCanvasShaderChannels.Tangent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AdditionalCanvasShaderChannels.Tangent.html);
    }
}

```

* * *
