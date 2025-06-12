* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.AddPositions.html

#  [TrailRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.html).AddPositions
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
## Declaration
public void AddPositions(Vector3[] positions); 
## Declaration
public void AddPositions(out NativeArray<Vector3> positions); 
## Declaration
public void AddPositions(out NativeSlice<Vector3> positions); 
### Parameters
Parameter | Description  
---|---  
positions | The positions to add to the trail.  
### Description
Add an array of positions to the trail.
All points inside a TrailRenderer store a timestamp when they are born. This, together with the [TrailRenderer.time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/time.html) property, is used to determine when they will be removed. For trails to disappear smoothly, each position must have a unique, increasing timestamp. When positions are supplied from script and the current time is identical for multiple points, position timestamps are adjusted to interpolate smoothly between the timestamp of the newest existing point in the trail and the current time.
```
using UnityEngine;
using System.Collections;
using System.Collections.Generic;  
  
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(TrailRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.html)))]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int numExtraPositions = 0;
    public float speed = 20.0f;
    public float radius = 4.0f;  
  
    private TrailRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.html) tr;  
  
    void Start()
    {
        tr = GetComponent<TrailRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TrailRenderer.html)>();
        tr.material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Sprites/Default"));
        tr.time = 0.2f;
        tr.widthMultiplier = 0.3f;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        float time = Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html);
        tr.transform.position = CalculatePosition(time);  
  
        if (numExtraPositions > 0)
        {
            float prevTime = time - Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);
            List<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)> extraPositions = new List<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)>(numExtraPositions);  
  
            for (int i = 0; i < numExtraPositions; i++)
            {
                float percentage = (float)(i + 1) / (numExtraPositions + 1);
                float blendedTime = Mathf.LerpUnclamped[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.LerpUnclamped.html)(prevTime, time, percentage);
                extraPositions.Add(CalculatePosition(blendedTime));
            }  
  
            tr.AddPositions(extraPositions.ToArray());
        }
    }  
  
    void OnGUI()
    {
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(25, 20, 200, 30), "Extra Positions");
        numExtraPositions = (int)GUI.HorizontalSlider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.HorizontalSlider.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(165, 25, 200, 30), (float)numExtraPositions, 0, 5);
    }  
  
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) CalculatePosition(float time)
    {
        return new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(time * speed) * radius, Mathf.Cos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Cos.html)(time * speed) * radius, 0.0f);
    }
}

```

* * *
