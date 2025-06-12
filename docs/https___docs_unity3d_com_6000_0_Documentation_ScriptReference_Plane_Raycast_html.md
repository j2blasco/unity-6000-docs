* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.Raycast.html

#  [Plane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html).Raycast
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
public bool Raycast([Ray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ray, out float enter); 
### Description
Intersects a ray with the plane.
This function sets `enter` to the distance along the ray, where it intersects the plane. If the ray is parallel to the plane, function returns `false` and sets `enter` to zero. If the ray is pointing in the opposite direction than the plane, function returns `false` and sets `enter` to the distance along the ray (negative value).
```
//This script detects mouse clicks on a plane using Plane.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.Raycast.html).
//In this example, the plane is set to the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)'s x and y position, but you can set the z position so the plane is in front of your Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).
//The normal of the plane is set to facing forward so it is facing the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html), but you can change this to suit your own needs.  
  
//In your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s Inspector, set your clickable distance and attach a cube GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in the appropriate fields  
  
using UnityEngine;  
  
public class PlaneRayExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Attach a cube GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in the Inspector before entering Play Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html)
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) m_Cube;  
  
    //This is the distance the clickable plane is from the camera. Set it in the Inspector before running.
    public float m_DistanceZ;  
  
    Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html) m_Plane;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_DistanceFromCamera;  
  
    void Start()
    {
        //This is how far away from the Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) the plane is placed
        m_DistanceFromCamera = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Camera.main.transform.position.x, Camera.main.transform.position.y, Camera.main.transform.position.z - m_DistanceZ);  
  
        //Create a new plane with normal (0,0,1) at the position away from the camera you define in the Inspector. This is the plane that you can click so make sure it is reachable.
        m_Plane = new Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Plane.html)(Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html), m_DistanceFromCamera);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Detect when there is a mouse click
        if (Input.GetMouseButton[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetMouseButton.html)(0))
        {
            //Create a ray from the Mouse click position
            Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ray = Camera.main.ScreenPointToRay(Input.mousePosition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePosition.html));  
  
            //Initialise the enter variable
            float enter = 0.0f;  
  
            if (m_Plane.Raycast(ray, out enter))
            {
                //Get the point that is clicked
                Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) hitPoint = ray.GetPoint(enter);  
  
                //Move your cube GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to the point where you clicked
                m_Cube.transform.position = hitPoint;
            }
        }
    }
}

```

Additional resources: [Physics.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html).
* * *
