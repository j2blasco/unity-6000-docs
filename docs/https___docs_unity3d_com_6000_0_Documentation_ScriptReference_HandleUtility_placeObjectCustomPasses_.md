* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility-placeObjectCustomPasses.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).placeObjectCustomPasses
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
### Description
Subscribe to this event to handle object placement in the [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html).
This delegate is invoked by [PlaceObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PlaceObject.html) when drag and dropping objects from the Hierarchy and Project views.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
static class PlaceObjectExample
{
    static readonly Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html) s_GroundPlane = new Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html)(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html), Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html));  
  
    [InitializeOnLoadMethod]
    static void InitPlaceObjectHandler()
    {
        HandleUtility.placeObjectCustomPasses[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility-placeObjectCustomPasses.html) += PlaneRaycast;
    }  
  
    // In this example, we register a plane at the scene origin to test for object placement.
    static bool PlaneRaycast(Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) mousePosition, out Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, out Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) normal)
    {
        Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) worldRay = HandleUtility.GUIPointToWorldRay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GUIPointToWorldRay.html)(mousePosition);
        float distance;  
  
        if (s_GroundPlane.Raycast(worldRay, out distance))
        {
            position = worldRay.GetPoint(distance);
            normal = s_GroundPlane.normal;
            return true;
        }  
  
        position = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
        normal = Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html);
        return false;
    }
}

```

* * *
