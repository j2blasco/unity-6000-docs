* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GeometryUtility.CalculateBounds.html

#  [GeometryUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GeometryUtility.html).CalculateBounds
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
public static [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) CalculateBounds(Vector3[] positions, [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) transform); 
### Parameters
Parameter | Description  
---|---  
positions | An array that stores the location of 3d positions.  
transform | A matrix that changes the position, rotation and size of the bounds calculation.  
### Returns
**Bounds** Calculates the axis-aligned bounding box. 
### Description
Calculates the bounding box from the given array of [positions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GeometryUtility-positions.html) and the transformation matrix.
[GeometryUtility.CalculateBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GeometryUtility.CalculateBounds.html) generates a [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounding box. The positions parameter stores a 3d point array. Each point is inside the generated axis-aligned bounding box. The transform parameter provides a transformation [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) that uses a Vector3 position, Quaternion rotation, and Vector3 scale.  
  
The example below shows how to use [CalculateBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GeometryUtility.CalculateBounds.html). A [LightProbeGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeGroup.html) passes [positions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GeometryUtility-positions.html) into [CalculateBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GeometryUtility.CalculateBounds.html). The example code creates a bounding box with eight Light Probes. By default, the Light Probes are one unit from each corner of a unit cube.  
  
To run the example:
  1. Create a Project and add an empty [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) called `GameObject`.
  2. Add a 3D cube as a child of `GameObject` and call it `Cube`.
  3. Add a [LightProbeGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeGroup.html) component to `Cube`.
  4. Add the script below to `Cube`.
  5. Run the `Project` and switch back to the `Scene` view.


In the `Scene` view, you can see the [LightProbeGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeGroup.html). When the game runs, the rotation changes in `Awake`. The eight yellow spheres that indicate the [LightProbeGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeGroup.html) change position and the Cube appears rotated. `Scene` mode shows the `Cube` rotated in the x, y and z axes, and shows in the `Local tool handle`. Rotating the `Cube` changes the positions of the eight [LightProbeGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeGroup.html) Light Probes. The `Scene` mode rotates and zooms to show the Light Probes. Also, the `Cube` rotates and the [LightProbeGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeGroup.html) updates. If you rescale the `Cube`, the [LightProbeGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeGroup.html) changes size.
```
using UnityEngine;
using System.Collections;  
  
// GeometryUtility.CalculateBounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GeometryUtility.CalculateBounds.html) - example  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Awake()
    {
        transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, 0.0f, 0.0f);
        transform.Rotate(10.0f, 30.0f, -50.0f, Space.Self[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.Self.html));  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(transform.localToWorldMatrix);
    }  
  
    void OnDrawGizmosSelected()
    {
        LightProbeGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeGroup.html) lightProbeGroup = GetComponent<LightProbeGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbeGroup.html)>();  
  
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center = transform.position;
        Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds = GeometryUtility.CalculateBounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GeometryUtility.CalculateBounds.html)(lightProbeGroup.probePositions, transform.localToWorldMatrix);
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)(1, 1, 1, 0.25f);
        Gizmos.DrawCube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawCube.html)(center, bounds.size);
        Gizmos.DrawWireCube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawWireCube.html)(center, bounds.size);
    }
}

```

* * *
