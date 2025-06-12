* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.SetPosition.html

#  [LineRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html).SetPosition
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
## Declaration
public void SetPosition(int index, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position); 
### Parameters
Parameter | Description  
---|---  
index | Which position to set.  
position | The new position.  
### Description
Set the position of a vertex in the line.
Consider using [SetPositions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.SetPositions.html) instead, if setting multiple positions, as it is much faster than making individual function calls for each position.  
  
Additional resources: [positionCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer-positionCount.html) property.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Creates a line renderer that follows a Sin() function
    // and animates it.  
  
    public Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) c1 = Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html);
    public Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) c2 = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
    public int lengthOfLineRenderer = 20;  
  
    void Start()
    {
        LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html) lineRenderer = gameObject.AddComponent<LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html)>();
        lineRenderer.material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Sprites/Default"));
        lineRenderer.widthMultiplier = 0.2f;
        lineRenderer.positionCount = lengthOfLineRenderer;  
  
        // A simple 2 color gradient with a fixed alpha of 1.0f.
        float alpha = 1.0f;
        Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) gradient = new Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html)();
        gradient.SetKeys(
            new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)[] { new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)(c1, 0.0f), new GradientColorKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientColorKey.html)(c2, 1.0f) },
            new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)[] { new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)(alpha, 0.0f), new GradientAlphaKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientAlphaKey.html)(alpha, 1.0f) }
        );
        lineRenderer.colorGradient = gradient;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html) lineRenderer = GetComponent<LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html)>();
        var t = Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html);
        for (int i = 0; i < lengthOfLineRenderer; i++)
        {
            lineRenderer.SetPosition(i, new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(i * 0.5f, Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(i + t), 0.0f));
        }
    }
}

```

* * *
