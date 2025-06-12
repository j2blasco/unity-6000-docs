* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer-textureScale.html

#  [TrailRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.html).textureScale
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TrailRenderer.html "Go to TrailRenderer Component in the Manual")
[Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) textureScale; 
### Description
A multiplier for the UV coordinates of the trail texture.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using System.Collections;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(TrailRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public LineTextureMode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineTextureMode.html) textureMode = LineTextureMode.Stretch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineTextureMode.Stretch.html);
    public float textureScale = 1.0f;
    private TrailRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.html) tr;  
  
    void Start()
    {
        tr = GetComponent<TrailRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.html)>();
        tr.material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Sprites/Default"));
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        tr.textureMode = textureMode;
        tr.textureScale = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(textureScale, 1.0f);
        tr.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) * 1.51f) * 7.0f, Mathf.Cos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Cos.html)(Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) * 1.27f) * 4.0f, 0.0f);
    }  
  
    void OnGUI()
    {
        textureMode = GUI.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Toggle.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 25, 200, 30), textureMode == LineTextureMode.Tile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineTextureMode.Tile.html), "Tiled") ? LineTextureMode.Tile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineTextureMode.Tile.html) : LineTextureMode.Stretch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineTextureMode.Stretch.html);  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 60, 200, 30), "Tile[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Tile.html) Amount");
        textureScale = GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(125, 65, 200, 30), textureScale, 0.1f, 4.0f);
    }
}

```

* * *
