* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer-textureMode.html

#  [LineRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html).textureMode
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
[LineTextureMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineTextureMode.html) textureMode; 
### Description
Choose whether the U coordinate of the line texture is tiled or stretched.
Stretching maps the texture along the line with no repeats. Tiling maps the texture along the line with repeats every world unit. To change the repeat rate, use [LineRenderer.textureScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer-textureScale.html) or [Material.SetTextureScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetTextureScale.html).
```
using UnityEngine;
using System.Collections;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public LineTextureMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineTextureMode.html) textureMode = LineTextureMode.Stretch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineTextureMode.Stretch.html);
    public float textureScale = 1.0f;
    private LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html) lr;  
  
    void Start()
    {
        lr = GetComponent<LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html)>();
        lr.material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Sprites/Default"));  
  
        // Set some positions
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] positions = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[3];
        positions[0] = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-2.0f, -1.0f, 0.0f);
        positions[1] = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, -0.5f, 0.0f);
        positions[2] = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(2.0f, -1.0f, 0.0f);
        lr.positionCount = positions.Length;
        lr.SetPositions(positions);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        lr.textureMode = textureMode;
        lr.textureScale = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(textureScale, 1.0f);
    }  
  
    void OnGUI()
    {
        textureMode = GUI.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 25, 200, 30), textureMode == LineTextureMode.Tile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineTextureMode.Tile.html), "Tiled") ? LineTextureMode.Tile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineTextureMode.Tile.html) : LineTextureMode.Stretch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineTextureMode.Stretch.html);  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 60, 200, 30), "Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html)");
        textureScale = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(125, 65, 200, 30), textureScale, 0.1f, 4.0f);
    }
}

```

* * *
