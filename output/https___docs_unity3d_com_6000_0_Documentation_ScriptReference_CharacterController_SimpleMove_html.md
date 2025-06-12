* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.SimpleMove.html

#  [CharacterController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html).SimpleMove
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CharacterController.html "Go to CharacterController Component in the Manual")
## Declaration
public bool SimpleMove([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) speed); 
### Description
Moves the character with `speed`.
Velocity along the y-axis is ignored. Speed is in units/s. Gravity is automatically applied. Returns true if the character is grounded. It is recommended that you make only one call to [Move](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.Move.html) or [SimpleMove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.SimpleMove.html) per frame.
```
using UnityEngine;
        
[RequireComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RequireComponent.html)(typeof(CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html)))]
public class CharacterMover : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private float speed = 3.0f;
    private float rotationSpeed = 90.0f; // degrees per second
        
    private CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html) characterController;
        
    void Start()
    {
        characterController = GetComponent<CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html)>();
    }
        
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        float horizontalInput = Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Horizontal");
        float verticalInput = Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Vertical");
        
        // Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) character
        transform.Rotate(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html), horizontalInput * rotationSpeed * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html));
        
        // Move character
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) moveDirection = transform.forward * verticalInput * speed;
        
        characterController.SimpleMove(moveDirection);
    }
}

```

* * *
