* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.Simplify.html

#  [LineRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html).Simplify
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
public void Simplify(float tolerance); 
### Parameters
Parameter | Description  
---|---  
tolerance | This value is used to evaluate which points should be removed from the line. A higher value results in a simpler line (less points). A positive value close to zero results in a line with little to no reduction. A value of zero or less has no effect.  
### Description
Generates a simplified version of the original line by removing points that fall within the specified tolerance.
Uses [LineUtility.Simplify](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineUtility.Simplify.html) to perform the line simplification.  
  
This example shows how an existing line can be simplified:
```
using UnityEngine;  
  
// This example shows how to apply line simplification to a line that already contains points.
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html)))]
public class SimpleExampleLineRenderer : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float tolerance = 1;
    void Start()
    {
        var lineRenderer = GetComponent<LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html)>();
        int pointsBefore = lineRenderer.positionCount;
        lineRenderer.Simplify(tolerance);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Line reduced from " + pointsBefore + " to " + lineRenderer.positionCount);
    }
}

```

**This example generates a line in the shape of a sine wave and provides a GUI for customizing the line generation and simplification parameters.**
```
using System.Collections.Generic;
using UnityEngine;  
  
// This example creates a sine wave and then simplifies it using LineRenderer.Simplify[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.Simplify.html).
// The parameters can be adjusted through an in game GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) to allow for experimentation.
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html)))]
public class LineRendererExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int numberOfPoints = 1000;
    public float length = 50;
    public float waveHeight = 10;
    public float tolerance = 0.1f;  
  
    private LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html) lineRenderer;
    private List<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)> points = new List<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)>(); // Generated points before Simplify is used.  
  
    public void Start()
    {
        lineRenderer = GetComponent<LineRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.html)>();
        GeneratePoints();
    }  
  
    // Generates the sine wave points.
    public void GeneratePoints()
    {
        points.Clear();
        float halfWaveHeight = waveHeight * 0.5f;
        float step = length / numberOfPoints;
        for (int i = 0; i < numberOfPoints; ++i)
        {
            points.Add(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(i * step, Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(i * step) * halfWaveHeight, 0));
        }
        lineRenderer.SetPositions(points.ToArray());
    }  
  
    // Draw a simple GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) slider with a label.
    private static float GUISlider(string label, float value, float min, float max)
    {
        GUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.BeginHorizontal.html)(GUILayout.Width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html)(Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) / 2.0f));
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)(label + "(" + value + ") :", GUILayout.Width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html)(150));
        var val = GUILayout.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.HorizontalSlider.html)(value, min, max);
        GUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.EndHorizontal.html)();
        return val;
    }  
  
    public void OnGUI()
    {
        GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("LineRenderer.Simplify[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LineRenderer.Simplify.html)", GUI.skin.box);  
  
        // We use GUI.changed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-changed.html) to detect if a value was changed via the GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html), if it has we can then re-generate the points and simplify the line again.
        GUI.changed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-changed.html) = false;  
  
        numberOfPoints = (int)GUISlider("Number of Points", numberOfPoints, 0, 1000);
        length = GUISlider("Length[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Length.html)", length, 0, 100);
        waveHeight = GUISlider("Wave Height", waveHeight, 0, 100);
        if (GUI.changed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-changed.html))
            GeneratePoints();  
  
        tolerance = GUISlider("Simplify Tolerance", tolerance, 0, 2);
        if (GUI.changed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI-changed.html))
            lineRenderer.Simplify(tolerance);  
  
        float percentRemoved = 100.0f - ((float)lineRenderer.positionCount / numberOfPoints) * 100.0f;
        if (tolerance > 0.0f)
            GUILayout.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Label.html)("Points after simplification: " + lineRenderer.positionCount + "(Removed " + percentRemoved.ToString("##.##") + "%)");
    }
}

```

* * *
