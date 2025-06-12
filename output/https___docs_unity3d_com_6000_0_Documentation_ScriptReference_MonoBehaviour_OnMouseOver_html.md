* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseOver.html

#  [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).OnMouseOver()
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html "Go to MonoBehaviour Component in the Manual")
### Description
Called every frame while the mouse is over the [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).
A call to [OnMouseEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseEnter.html) occurs on the first frame the mouse is over the object. OnMouseOver is then called each frame until the mouse moves away, at which point [OnMouseExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnMouseExit.html) is called.  
  
This function is not called on objects that belong to Ignore Raycast layer.  
  
This function is called on Colliders and 2D Colliders marked as trigger when the following properties are set to true:   
  
- For 3D physics: [Physics.queriesHitTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-queriesHitTriggers.html)  
  
- For 2D physics: [Physics2D.queriesHitTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D-queriesHitTriggers.html)   
  
OnMouseOver can be a co-routine, simply use the yield statement in the function. This event is sent to all scripts attached to the [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html).
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to have it output messages when your mouse hovers over it.
using UnityEngine;  
  
public class OnMouseOverExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnMouseOver()
    {
        //If your mouse hovers over the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with the script attached, output this message
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Mouse is over GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).");
    }  
  
    void OnMouseExit()
    {
        //The mouse is no longer hovering over the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) so output this message each frame
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Mouse is no longer on GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).");
    }
}

```

Another example:
```
// This second example changes the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s color to red when the mouse hovers over it
// Ensure the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) has a MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html)  
  
using UnityEngine;  
  
public class OnMouseOverColor : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //When the mouse hovers over the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html), it turns to this color (red)
    Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) m_MouseOverColor = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);  
  
    //This stores the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s original color
    Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) m_OriginalColor;  
  
    //Get the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s mesh renderer to access the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s material and color
    MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html) m_Renderer;  
  
    void Start()
    {
        //Fetch the mesh renderer component from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Renderer = GetComponent<MeshRenderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MeshRenderer.html)>();
        //Fetch the original color of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_OriginalColor = m_Renderer.material.color;
    }  
  
    void OnMouseOver()
    {
        // Change the color of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to red when the mouse is over GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Renderer.material.color = m_MouseOverColor;
    }  
  
    void OnMouseExit()
    {
        // Reset the color of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) back to normal
        m_Renderer.material.color = m_OriginalColor;
    }
}

```

* * *
