* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.BoxCast.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).BoxCast
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
public static bool BoxCast([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) halfExtents, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) orientation = Quaternion.identity, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
center | Center of the box.  
halfExtents | Half the size of the box in each dimension.  
direction | The direction in which to cast the box.  
orientation | Rotation of the box.  
maxDistance | The max length of the cast.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**bool** True, if any intersections were found. 
### Description
Casts the box along a ray and returns detailed information on what was hit.
* * *
## Declaration
public static bool BoxCast([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) halfExtents, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction, out [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hitInfo, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) orientation = Quaternion.identity, float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
center | Center of the box.  
halfExtents | Half the size of the box in each dimension.  
direction | The direction in which to cast the box.  
hitInfo | If true is returned, `hitInfo` will contain more information about where the collider was hit. (Additional resources: [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html)).  
orientation | Rotation of the box.  
maxDistance | The max length of the cast.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**bool** True, if any intersections were found. 
### Description
Casts the box along a ray and returns detailed information on what was hit.
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). Make sure it has a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) component by clicking the **Add Component** button. Then click **Physics**>**Box Collider** to attach a Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Box.html) Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) component.
//This script creates a BoxCast in front of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and outputs a message if another Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) is hit with the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)’s name.
//It also draws where the ray and BoxCast extends to. Just press the Gizmos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html) button to see it in Play Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html).
//Make sure to have another GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) component for the BoxCast to collide with.  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    float m_MaxDistance;
    float m_Speed;
    bool m_HitDetect;  
  
    Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) m_Collider;
    RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) m_Hit;  
  
    void Start()
    {
        //Choose the distance the Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Box.html) can reach to
        m_MaxDistance = 300.0f;
        m_Speed = 20.0f;
        m_Collider = GetComponent<Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Simple movement in x and z axes
        float xAxis = Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Horizontal") * m_Speed;
        float zAxis = Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Vertical") * m_Speed;
        transform.Translate(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(xAxis, 0, zAxis));
    }  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        //Test to see if there is a hit using a BoxCast
        //Calculate using the center of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)(could also just use the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s position), half the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s size, the direction, the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s rotation, and the maximum distance as variables.
        //Also fetch the hit data
        m_HitDetect = Physics.BoxCast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.BoxCast.html)(m_Collider.bounds.center, transform.localScale*0.5f, transform.forward, out m_Hit, transform.rotation, m_MaxDistance);
        if (m_HitDetect)
        {
            //Output the name of the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) your Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Box.html) hit
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Hit : " + m_Hit.collider.name);
        }
    }  
  
    //Draw the BoxCast as a gizmo to show where it currently is testing. Click the Gizmos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html) button to see this
    void OnDrawGizmos()
    {
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);  
  
        //Check if there has been a hit yet
        if (m_HitDetect)
        {
            //Draw a Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) forward from GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) toward the hit
            Gizmos.DrawRay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawRay.html)(transform.position, transform.forward * m_Hit.distance);
            //Draw a cube that extends to where the hit exists
            Gizmos.DrawWireCube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawWireCube.html)(transform.position + transform.forward * m_Hit.distance, transform.localScale);
        }
        //If there hasn't been a hit yet, draw the ray at the maximum distance
        else
        {
            //Draw a Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) forward from GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) toward the maximum distance
            Gizmos.DrawRay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawRay.html)(transform.position, transform.forward * m_MaxDistance);
            //Draw a cube at the maximum distance
            Gizmos.DrawWireCube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawWireCube.html)(transform.position + transform.forward * m_MaxDistance, transform.localScale);
        }
    }
}

```

* * *
