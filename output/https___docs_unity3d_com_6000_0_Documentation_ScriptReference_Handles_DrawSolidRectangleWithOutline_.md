* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawSolidRectangleWithOutline.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).DrawSolidRectangleWithOutline
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
## Declaration
public static void DrawSolidRectangleWithOutline(Vector3[] verts, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) faceColor, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) outlineColor); 
### Parameters
Parameter | Description  
---|---  
verts | The 4 vertices of the rectangle in world coordinates.  
faceColor | The color of the rectangle's face.  
outlineColor | The outline color of the rectangle.  
### Description
Draw a solid outlined rectangle in 3D space.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/DrawSolidRectangle.png)   
_Solid rectangle with a black outline in the Scene View._
```
// Create a semi transparent rectangle that lets you modify
// the "range" that resides in "SolidRectangleExample.cs"  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(SolidRectangleExample))]
public class DrawSolidRectangle : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    void OnSceneGUI()
    {
        SolidRectangleExample t = target as SolidRectangleExample;
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) pos = t.transform.position;  
  
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[] verts = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[]
        {
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(pos.x - t.range, pos.y, pos.z - t.range),
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(pos.x - t.range, pos.y, pos.z + t.range),
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(pos.x + t.range, pos.y, pos.z + t.range),
            new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(pos.x + t.range, pos.y, pos.z - t.range)
        };  
  
        Handles.DrawSolidRectangleWithOutline[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawSolidRectangleWithOutline.html)(verts, new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0.5f, 0.5f, 0.5f, 0.1f), new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(0, 0, 0, 1));  
  
        foreach (Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) posCube in verts)
        {
            t.range = Handles.ScaleValueHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.ScaleValueHandle.html)(t.range,
                posCube,
                Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html),
                1.0f,
                Handles.CubeHandleCap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.CubeHandleCap.html),
                1.0f);
        }
    }
}

```

And the script attached to this Handle:
```
using UnityEngine;  
  
public class SolidRectangleExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float range = 5.0f;
}

```

* * *
