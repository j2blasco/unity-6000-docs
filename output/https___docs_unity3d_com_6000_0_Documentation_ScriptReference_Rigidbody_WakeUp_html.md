* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.WakeUp.html

#  [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html).WakeUp
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Rigidbody.html "Go to Rigidbody Component in the Manual")
## Declaration
public void WakeUp(); 
### Description
Forces a rigidbody to wake up.
For more information about [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) sleeping, refer to the [Rigidbody overview](https://docs.unity3d.com/6000.0/Documentation/Manual/RigidbodiesOverview.html).
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private float fallTime;
    private Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) rbGO;
    private bool sleeping;  
  
    void Start()
    {
        rbGO = gameObject.AddComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        rbGO.mass = 10.0f;
        Physics.gravity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-gravity.html) = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, -2.0f, 0);
        sleeping = false;
        fallTime = 0.0f;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (fallTime > 1.0f)
        {
            if (sleeping)
            {
                rbGO.WakeUp();
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("wakeup");
            }
            else
            {
                rbGO.Sleep();
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("sleep");
            }  
  
            sleeping = !sleeping;  
  
            fallTime = 0.0f;
        }  
  
        fallTime += Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);
    }
}

```

* * *
