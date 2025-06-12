* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds-extents.html

#  [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html).extents
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) extents; 
### Description
The extents of the Bounding Box. This is always half of the [size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds-size.html) of the Bounds.
**Note:** If [Bounds.extents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds-extents.html) has a negative value for any axis, [Bounds.Contains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.Contains.html) always returns False.
```
//Attach this script to a visible GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
//Click on the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to expand it and output the Bound extents to the Console.  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) m_ObjectCollider;
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_MyScale;  
  
    void Start()
    {
        //Fetch the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s collider (make sure they have a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) component)
        m_ObjectCollider = gameObject.GetComponent<Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)>();
        //Output the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) Bound extents
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("extents : " + m_ObjectCollider.bounds.extents);
    }  
  
    //Detect when the user clicks the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
    void OnMouseDown()
    {
        //Change the scale of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to the size you define in the Inspector
        transform.localScale = m_MyScale;
        //Output the extents of the Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) after clicking the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). Extents change to half of the scale.
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("extents : " + m_ObjectCollider.bounds.extents);
    }
}

```

* * *
