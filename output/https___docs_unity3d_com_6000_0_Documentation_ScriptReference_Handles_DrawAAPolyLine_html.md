* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawAAPolyLine.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).DrawAAPolyLine
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
public static void DrawAAPolyLine(Color[] colors, Vector3[] points); 
## Declaration
public static void DrawAAPolyLine(float width, Color[] colors, Vector3[] points); 
## Declaration
public static void DrawAAPolyLine(params Vector3[] points); 
## Declaration
public static void DrawAAPolyLine(float width, params Vector3[] points); 
## Declaration
public static void DrawAAPolyLine([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) lineTex, params Vector3[] points); 
## Declaration
public static void DrawAAPolyLine(float width, int actualNumberOfPoints, params Vector3[] points); 
## Declaration
public static void DrawAAPolyLine([Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) lineTex, float width, params Vector3[] points); 
### Parameters
Parameter | Description  
---|---  
lineTex | The AA texture used for rendering.  
width | The width of the line.  
points | List of points to build the line from.  
colors | The colors to apply to each point. Must match the length of the points array or actualNumberOfPoints, whichever is lower and greater than zero.  
actualNumberOfPoints | The total number of vertices to draw of the points array. Use this to keep a reusable buffer of point values without the need to resize frequently.  
### Description
Draw anti-aliased line specified with point array and width.
**Note:** Use [HandleUtility.GetHandleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html) where you might want to have constant screen-sized handles.  
  
**Note:** To get an anti-aliased effect use a texture that is 1x2 pixels with one transparent white pixel and one opaque white pixel.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;

public class ArrowDrawer : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public void DrawArrow(Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, float arrowThickness, float lineThickness, float shorten, Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) start, Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) end)
    {
        var length = (end - start).magnitude;
        if (length < 0.001f)
            return;

        var forward = (end - start) / length;
        var right = Vector3.Cross[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Cross.html)(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html), forward).normalized;

        var width = arrowThickness * 0.5f;
        var height = arrowThickness * 0.7f;

        start += forward * shorten;
        end -= forward * shorten;

        var arrowHead = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[3]
        {
            end,
            end - forward * height + right * width,
            end - forward * height - right * width
        };

        var arrowLine = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)[2]
        {
            start,
            end - forward * height
        };

        Handles.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-color.html) = color;
        Handles.DrawAAPolyLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawAAPolyLine.html)(lineThickness, 2, arrowLine);
        Handles.DrawAAConvexPolygon[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.DrawAAConvexPolygon.html)(arrowHead);
    }

    void OnDrawGizmos()
    {
        DrawArrow(Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html), 1f, 3f, 0f, transform.position, transform.position + transform.TransformDirection(Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html)) * 4f);
    }
}

```

* * *
