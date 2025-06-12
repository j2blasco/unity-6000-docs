* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.OverlapBox.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).OverlapBox
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
public static Collider[] OverlapBox([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) halfExtents, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) orientation = Quaternion.identity, int layerMask = AllLayers, [QueryTriggerInteraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QueryTriggerInteraction.html) queryTriggerInteraction = QueryTriggerInteraction.UseGlobal); 
### Parameters
Parameter | Description  
---|---  
center | Center of the box.  
halfExtents | Half of the size of the box in each dimension.  
orientation | Rotation of the box.  
layerMask | A [Layer mask](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html) that is used to selectively filter which colliders are considered when casting a ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
### Returns
**Collider[]** Colliders that overlap with the given box. 
### Description
Find all colliders touching or inside of the given box.
Creates an invisible box you define that tests collisions by outputting any colliders that come into contact with the box.
```
//Attach this script to your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). This GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) doesn’t need to have a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) component
//Set the Layer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.Layer.html) Mask field in the Inspector to the layer you would like to see collisions in (set to **Everything** if you are unsure).
//Create a second Gameobject for testing collisions. Make sure your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) has a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) component (if it doesn’t, click on the **Add Component** button in the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s Inspector, and go to **Physics**>**Box Collider**).
//Place it so it is overlapping your other GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
//Press Play to see the console output the name of your second GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)  
  
//This script uses the OverlapBox that creates an invisible Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Box.html) Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) that detects multiple collisions with other colliders. The OverlapBox in this case is the same size and position as the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you attach it to (acting as a replacement for the BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html) component).  
  
using UnityEngine;  
  
public class OverlapBoxExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public LayerMask[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html) m_LayerMask;  
  
    void FixedUpdate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.FixedUpdate.html)()
    {
        MyCollisions();
    }  
  
    void MyCollisions()
    {
        // Use the OverlapBox to detect if there are any other colliders within this box area.
        // Use the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s center, half the size (as a radius), and rotation. This creates an invisible box around your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
        Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)[] hitColliders = Physics.OverlapBox[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.OverlapBox.html)(gameObject.transform.position, transform.localScale / 2, Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html), m_LayerMask);
        int i = 0;
        // Check when there is a new collider coming into contact with the box
        while (i < hitColliders.Length)
        {
            // Output all of the collider names
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Hit : " + hitColliders[i].name + i);
            // Increase the number of Colliders in the array
            i++;
        }
    }  
  
    // Draw the Box[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Box.html) Overlap as a gizmo to show where it currently is testing. Click the Gizmos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html) button to see this.
    void OnDrawGizmos()
    {
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
        // Check that it is being run in Play Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html), so it doesn't try to draw this in Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) mode
        if (Application.isPlaying[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-isPlaying.html))
            // Draw a cube where the OverlapBox is (positioned where your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) is as well as a size)
            Gizmos.DrawWireCube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawWireCube.html)(transform.position, transform.localScale);
    }
}

```

* * *
