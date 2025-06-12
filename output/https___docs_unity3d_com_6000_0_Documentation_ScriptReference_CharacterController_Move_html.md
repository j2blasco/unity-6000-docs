* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.Move.html

#  [CharacterController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html).Move
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
public [CollisionFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionFlags.html) Move([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) motion); 
### Description
Supplies the movement of a GameObject with an attached CharacterController component.
The [CharacterController.Move](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.Move.html) motion moves the GameObject in the given direction. The given direction requires absolute movement delta values. A collision constrains the [Move](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.Move.html) from taking place. The return, [CollisionFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CollisionFlags.html), indicates the direction of a collision: None, Sides, Above, and Below. [CharacterController.Move](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.Move.html) does not use gravity.  
  
The example below demonstrates how to use [CharacterController.Move](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.Move.html). `Update` causes a [Move](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.Move.html) to re-position the player. In addition, `Jump` changes the player position in a vertical direction. 
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html) controller;
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) playerVelocity;
    private bool groundedPlayer;
    private float playerSpeed = 2.0f;
    private float jumpHeight = 1.0f;
    private float gravityValue = -9.81f;  
  
    private void Start()
    {
        controller = gameObject.AddComponent<CharacterController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CharacterController.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        groundedPlayer = controller.isGrounded;
        if (groundedPlayer && playerVelocity.y < 0)
        {
            playerVelocity.y = 0f;
        }  
  
        // Horizontal input
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) move = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Horizontal"), 0, Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Vertical"));
        move = Vector3.ClampMagnitude[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.ClampMagnitude.html)(move, 1f); // Optional: prevents faster diagonal movement  
  
        if (move != Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html))
        {
            transform.forward = move;
        }  
  
        // Jump
        if (Input.GetButtonDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButtonDown.html)("Jump") && groundedPlayer)
        {
            playerVelocity.y = Mathf.Sqrt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sqrt.html)(jumpHeight * -2.0f * gravityValue);
        }  
  
        // Apply gravity
        playerVelocity.y += gravityValue * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);  
  
        // Combine horizontal and vertical movement
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) finalMove = (move * playerSpeed) + (playerVelocity.y * Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html));
        controller.Move(finalMove * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html));
    }
}

```

* * *
