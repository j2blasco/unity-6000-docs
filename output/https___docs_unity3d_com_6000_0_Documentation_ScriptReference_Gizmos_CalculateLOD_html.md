* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.CalculateLOD.html

#  [Gizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html).CalculateLOD
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
public static float CalculateLOD([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, float radius); 
### Parameters
Parameter | Description  
---|---  
position | The centre of the gizmo in world space.  
radius | The maximum extent of the gizmo.  
### Returns
**float** Returns a value between 0 and 1 that represents the level of detail for the gizmo. 
### Description
Determines the appropriate level of detail for a gizmo in the Scene view at a specified position with a specified radius.
A return value of 0 indicates the gizmo is not visible. The gizmo might not be visible because it is too small on the screen or because it is outside of the Scene view camera frustum. The return value is quantized to eighths to reduce the number of produced batches. This can be further controlled with the 'Fade Gizmos' options in the [Gizmos menu](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html). 
```
using UnityEngine;  
  
public class MyLODedComponent : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Draw a blue sphere at the transform's position, fading out as it gets further away
    private void OnDrawGizmos()
    {
        float lod = Gizmos.CalculateLOD[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.CalculateLOD.html)(transform.position, 1);  
  
        // Cull any gizmos that are too small or off screen
        if (lod == 0.0f)
            return;  
  
        // Fade the gizmos out so that they don't pop in and out when scrolling around the scene
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html) * lod;
        Gizmos.DrawSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawSphere.html)(transform.position, 1);
    }
}

```

* * *
