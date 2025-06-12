* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.html

# CollisionDetectionMode
enumeration
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
The collision detection mode constants used for [Rigidbody.collisionDetectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-collisionDetectionMode.html).
```
//This script allows you to switch collision detection mode at the press of the space key, and move your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). It also outputs collisions that occur to the console.
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and make sure it has a Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) component
//If it doesn't have a Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) component, click the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html), go to its Inspector and click the **Add Component** button. Then, go to **Physics**>**Rigidbody**.
//Create another GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). Make sure it has a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html), so you can test collisions between them.  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) m_Rigidbody;
    public float m_Speed;  
  
    void Start()
    {
        //Fetch the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) (make sure this is attached in the Inspector window)
        m_Rigidbody = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        //Make sure the Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) can't rotate or move in the z axis for this example
        m_Rigidbody.constraints = RigidbodyConstraints.FreezeRotation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.FreezeRotation.html) | RigidbodyConstraints.FreezePositionZ[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyConstraints.FreezePositionZ.html);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Change the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s movement in the X axis
        float translationX = Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Horizontal") * m_Speed;
        //Change the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s movement in the Y axis
        float translationY = Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Vertical") * m_Speed;  
  
        //Move the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        transform.Translate(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(translationX, translationY, 0));  
  
        //Press the space key to switch the collision detection mode
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
            SwitchCollisionDetectionMode();
    }  
  
    //Detect when there is a collision starting
    void OnCollisionEnter(Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) collision)
    {
        //Ouput the Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) to the console
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) : " + collision.gameObject.name);
    }  
  
    //Detect when there is are ongoing Collisions
    void OnCollisionStay(Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) collision)
    {
        //Output the Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) to the console
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Stay : " + collision.gameObject.name);
    }  
  
    //Switch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Switch.html) between the different Collision[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision.html) Detection Modes
    void SwitchCollisionDetectionMode()
    {
        switch (m_Rigidbody.collisionDetectionMode)
        {
            //If the current mode is continuous, switch it to continuous dynamic mode
            case CollisionDetectionMode.Continuous[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.Continuous.html):
                m_Rigidbody.collisionDetectionMode = CollisionDetectionMode.ContinuousDynamic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.ContinuousDynamic.html);
                break;
            //If the current mode is continuous dynamic, switch it to continuous speculative
            case CollisionDetectionMode.ContinuousDynamic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.ContinuousDynamic.html):
                m_Rigidbody.collisionDetectionMode = CollisionDetectionMode.ContinuousSpeculative[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.ContinuousSpeculative.html);
                break;  
  
            // If the current mode is continuous speculative, switch it to discrete mode
            case CollisionDetectionMode.ContinuousSpeculative[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.ContinuousSpeculative.html):
                m_Rigidbody.collisionDetectionMode = CollisionDetectionMode.Discrete[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.Discrete.html);
                break;  
  
            //If the current mode is discrete, switch it to continuous mode
            case CollisionDetectionMode.Discrete[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.Discrete.html):
                m_Rigidbody.collisionDetectionMode = CollisionDetectionMode.Continuous[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.Continuous.html);
                break;
        }
    }
}

```

### Properties
Property | Description  
---|---  
[Discrete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.Discrete.html) | Continuous collision detection is off for this Rigidbody.  
[Continuous](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.Continuous.html) | Continuous collision detection is on for colliding with static mesh geometry.  
[ContinuousDynamic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.ContinuousDynamic.html) | Continuous collision detection is on for colliding with static and dynamic geometry.  
[ContinuousSpeculative](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.ContinuousSpeculative.html) | Speculative continuous collision detection is on for static and dynamic geometries  
* * *
