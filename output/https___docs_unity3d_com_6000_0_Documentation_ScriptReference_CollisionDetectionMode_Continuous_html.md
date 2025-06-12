* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.Continuous.html

#  [CollisionDetectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.html).Continuous
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
Continuous collision detection is on for colliding with static mesh geometry.
Collisions will be detected for any static mesh geometry in the path of this Rigidbody, even if the collision occurs between two FixedUpdate steps. Static mesh geometry is any MeshCollider which does not have a Rigidbody attached. This also prevent Rigidbodies set to ContinuousDynamic mode from passing through this Rigidbody.
```
//This script allows you to switch collision detection mode at the press of the space key
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
//Click the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html), go to its Inspector and click the **Add Component** Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html). Then, go to **Physics**>**Rigidbody**.  
  
using UnityEngine;
using UnityEngine.UI;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) m_Rigidbody;  
  
    void Start()
    {
        m_Rigidbody = GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
    }  
  
    public void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //Press the space key to switch the collision detection mode
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Space.html)))
            SwitchCollisionDetectionMode();
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
            //If the current mode is continuous dynamic, switch it to discrete mode
            case CollisionDetectionMode.ContinuousDynamic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.ContinuousDynamic.html):
                m_Rigidbody.collisionDetectionMode = CollisionDetectionMode.ContinuousSpeculative[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionDetectionMode.ContinuousSpeculative.html);
                break;  
  
            // If the curren mode is continuous speculative, switch it to discrete mode
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
* * *
