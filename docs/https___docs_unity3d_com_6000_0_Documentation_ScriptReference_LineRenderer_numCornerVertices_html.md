* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer-numCornerVertices.html

#  [LineRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html).numCornerVertices
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
numCornerVertices; 
### Description
Set this to a value greater than 0, to get rounded corners between each segment of the line.
The value controls how many vertices are added to each joint, where a higher value will give a smoother result.
```
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int numCapVertices = 0;
    public int numCornerVertices = 0;
    private LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html) lr;  
  
    void Start()
    {
        lr = GetComponent<LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html)>();
        lr.material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Sprites/Default"));  
  
        // Set some positions
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] positions = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[3];
        positions[0] = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-2.0f, -2.0f, 0.0f);
        positions[1] = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, 2.0f, 0.0f);
        positions[2] = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(2.0f, -2.0f, 0.0f);
        lr.positionCount = positions.Length;
        lr.SetPositions(positions);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        lr.numCapVertices = numCapVertices;
        lr.numCornerVertices = numCornerVertices;
    }  
  
    void OnGUI()
    {
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 20, 200, 30), "Num Cap Vertices");
        numCapVertices = (int)GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(165, 25, 200, 30), (float)numCapVertices, 0.0f, 20.0f);  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 60, 200, 30), "Num Corner Vertices");
        numCornerVertices = (int)GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(165, 65, 200, 30), (float)numCornerVertices, 0.0f, 20.0f);
    }
}

```

* * *
