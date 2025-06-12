* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawBezier.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).DrawBezier
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
public static void DrawBezier([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) startPosition, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) endPosition, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) startTangent, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) endTangent, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture, float width); 
### Parameters
Parameter | Description  
---|---  
startPosition | The start point of the bezier line.  
endPosition | The end point of the bezier line.  
startTangent | The start tangent of the bezier line.  
endTangent | The end tangent of the bezier line.  
color | The color to use for the bezier line.  
texture | The texture to use for drawing the bezier line.  
width | The width of the bezier line.  
### Description
Draw textured bezier line through start and end points with the given tangents.
To get an anti-aliased effect use a texture that is 1x2 pixels with one transparent white pixel and one opaque white pixel. The bezier curve will be swept using this texture.  
  
**Note:** Use [HandleUtility.GetHandleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html) where you might want to have constant screen-sized handles.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/DrawBezier.png)  
_Bezier Line in the Scene View._
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(BezierExample))]
public class DrawBezierExample : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    void OnSceneGUI()
    {
        BezierExample be = target as BezierExample;  
  
        be.startPoint = Handles.PositionHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.PositionHandle.html)(be.startPoint, Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html));
        be.endPoint = Handles.PositionHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.PositionHandle.html)(be.endPoint, Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html));
        be.startTangent = Handles.PositionHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.PositionHandle.html)(be.startTangent, Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html));
        be.endTangent = Handles.PositionHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.PositionHandle.html)(be.endTangent, Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html));  
  
        // Visualize the tangent lines
        Handles.DrawDottedLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawDottedLine.html)(be.startPoint, be.startTangent, 5);
        Handles.DrawDottedLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawDottedLine.html)(be.endPoint, be.endTangent, 5);  
  
        Handles.DrawBezier[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawBezier.html)(be.startPoint, be.endPoint, be.startTangent, be.endTangent, Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html), null, 5f);
    }
}
```

And the script attached to this Handle:
```
using UnityEngine;  
  
public class BezierExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) startPoint = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-5f, 2f, 0f);
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) endPoint = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(5f, -2f, 0f);
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) startTangent = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0f, 2f, 0f);
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) endTangent = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0f, -2f, 0f);
}
```

* * *
