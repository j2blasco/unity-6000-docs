* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer-shadowBias.html

#  [LineRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html).shadowBias
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html "Go to LineRenderer Component in the Manual")
shadowBias; 
### Description
Apply a shadow bias to prevent self-shadowing artifacts. The specified value is the proportion of the line width at each segment.
```
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html) lr;  
  
    void Start()
    {
        lr = GetComponent<LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html)>();
        lr.material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Standard"));
        lr.castShadows = true;
        lr.receiveShadows = true;
        lr.shadowBias = 0.3f;  
  
        // Set some positions
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] positions = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[3];
        positions[0] = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-2.0f, -2.0f, 0.0f);
        positions[1] = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, 2.0f, 0.0f);
        positions[2] = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(2.0f, -2.0f, 0.0f);
        lr.positionCount = positions.Length;
        lr.SetPositions(positions);
    }
}

```

* * *
