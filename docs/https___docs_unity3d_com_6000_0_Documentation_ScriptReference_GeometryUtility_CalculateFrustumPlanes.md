* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GeometryUtility.CalculateFrustumPlanes.html

#  [GeometryUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GeometryUtility.html).CalculateFrustumPlanes
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
public static Plane[] CalculateFrustumPlanes([Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera); 
### Parameters
Parameter | Description  
---|---  
camera | The camera with the view frustum that you want to calculate planes from.  
### Returns
**Plane[]** The planes that form the camera's view frustum. 
### Description
Calculates frustum planes.
This function takes the given camera's view frustum and returns six planes that form it.  
  
Ordering: [0] = Left, [1] = Right, [2] = Down, [3] = Up, [4] = Near, [5] = Far  
  
Additional resources: [Plane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html), [GeometryUtility.TestPlanesAABB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GeometryUtility.TestPlanesAABB.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Calculate the planes from the main camera's view frustum
        Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html)[] planes = GeometryUtility.CalculateFrustumPlanes[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GeometryUtility.CalculateFrustumPlanes.html)(Camera.main[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html));  
  
        // Create a "Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html)" GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) aligned to each of the calculated planes
        for (int i = 0; i < 6; ++i)
        {
            GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) p = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Plane.html));
            p.name = "Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html) " + i.ToString();
            p.transform.position = -planes[i].normal * planes[i].distance;
            p.transform.rotation = Quaternion.FromToRotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.FromToRotation.html)(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html), planes[i].normal);
        }
    }
}

```

* * *
## Declaration
public static void CalculateFrustumPlanes([Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera, Plane[] planes); 
### Parameters
Parameter | Description  
---|---  
camera | The camera with the view frustum that you want to calculate planes from.  
planes | An array of 6 Planes that will be overwritten with the calculated plane values.  
### Description
Calculates frustum planes.
This function takes the given camera's view frustum and returns six planes that form it. This is similar to the previous overload, except that instead of allocating a new array for the calculated planes, the function will use an array that you have provided. This array must always be exactly of length 6.  
  
Ordering: [0] = Left, [1] = Right, [2] = Down, [3] = Up, [4] = Near, [5] = Far  
  
Additional resources: [Plane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html), [GeometryUtility.TestPlanesAABB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GeometryUtility.TestPlanesAABB.html).
* * *
## Declaration
public static Plane[] CalculateFrustumPlanes([Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) worldToProjectionMatrix); 
### Parameters
Parameter | Description  
---|---  
worldToProjectionMatrix | A matrix that transforms from world space to projection space, from which the planes will be calculated.  
### Returns
**Plane[]** The planes that enclose the projection space described by the matrix. 
### Description
Calculates frustum planes.
This function returns six planes of a frustum defined by the given view & projection matrix.  
  
Additional resources: [Plane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html), [GeometryUtility.TestPlanesAABB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GeometryUtility.TestPlanesAABB.html).
* * *
## Declaration
public static void CalculateFrustumPlanes([Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) worldToProjectionMatrix, Plane[] planes); 
### Parameters
Parameter | Description  
---|---  
worldToProjectionMatrix | A matrix that transforms from world space to projection space, from which the planes will be calculated.  
planes | An array of 6 Planes that will be overwritten with the calculated plane values.  
### Description
Calculates frustum planes.
This function returns six planes of a frustum defined by the given view & projection matrix. This is similar to the previous overload, except that instead of allocating a new array for the calculated planes, the function will use an array that you have provided. This array must always be exactly of length 6.  
  
Additional resources: [Plane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html), [GeometryUtility.TestPlanesAABB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GeometryUtility.TestPlanesAABB.html).
* * *
