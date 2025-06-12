* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.IgnoreLayerCollision.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).IgnoreLayerCollision
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
public static void IgnoreLayerCollision(int layer1, int layer2, bool ignore = true); 
### Description
Makes the collision detection system ignore all collisions between any collider in `layer1` and any collider in `layer2`.  
  
Note that IgnoreLayerCollision will reset the trigger state of affected colliders, so you might receive OnTriggerExit and OnTriggerEnter messages in response to calling this.
You can set the default values for your project for any layer combinations in the Physics inspector.  
  
Additional resources: [Physics.GetIgnoreLayerCollision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.GetIgnoreLayerCollision.html),[Physics.IgnoreCollision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.IgnoreCollision.html).
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and make sure it has a Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) component
//Make a second GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) to test collisions on. Make sure both GameObjects are the same on the y and z axes  
  
//This script stops collisions between two layers (in this case layers 0 and 8). Set up a new layer in the Inspector window by clicking the Layer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.Layer.html) option.
//Next click “Add Layer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.Layer.html)”. Then, assign this layer to the second GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).  
  
//In Play Mode[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.GarbageCollector.Mode.html), press the left and right keys to move the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) to the left and right. If your first GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) is in layer 0 and your second GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) is in layer 8, the collision is ignored.  
  

using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Set the speed number in the Inspector window
    public float m_Speed;
    Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) m_Rigidbody;  
  
    void Start()
    {
        //Fetch the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) component from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Rigidbody = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        //Ignore the collisions between layer 0 (default) and layer 8 (custom layer you set in Inspector window)
        Physics.IgnoreLayerCollision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.IgnoreLayerCollision.html)(0, 8);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Press right to move the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to the right. Make sure you set the speed high in the Inspector window.
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.RightArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.RightArrow.html)))
        {
            m_Rigidbody.AddForce(Vector3.right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html) * m_Speed);
        }  
  
        //Press the left arrow key to move the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) to the left
        if (Input.GetKey[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKey.html)(KeyCode.LeftArrow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.LeftArrow.html)))
        {
            m_Rigidbody.AddForce(Vector3.left[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-left.html) * m_Speed);
        }
    }  
  
    //Detect when there is a collision
    void OnCollisionStay(Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) collide)
    {
        //Output the name of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you collide with
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("I hit the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) : " + collide.gameObject.name);
    }
}

```

* * *
