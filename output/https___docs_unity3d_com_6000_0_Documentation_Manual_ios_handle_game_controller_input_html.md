* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ios-handle-game-controller-input.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone.html)
  * [Developing for iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-developing.html)
  * [Input for iOS devices](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-input.html)
  * [Game Controller support](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-game-controller-support.html)
  * Handle Game Controller input


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-detect-game-controllers.html)
Detect Game Controllers
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-testing-and-debugging.html)
Test and debug an iOS application
# Handle Game Controller input
The input scheme is dependent on the type of application you are developing. You can set up specific actions in Unity’s [Input Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/class-InputManager.html)Settings where you can define all the different input axes, buttons and controls for your project. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-InputManager.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#InputManager) settings. By default, the Unity Input Horizontal axis is mapped to the **game controller** A device to control objects and characters in a game.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#gamecontroller) D-pad and the left analog stick is mapped to extended profile controllers. See [Input mapping](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-handle-game-controller-input.html#InputMapping) for the KeyCodes and Axes that correspond to specific controller buttons.
## Example: Set up joystick button A for the Jump action
  1. Go to **Edit** > **Project Settings**.
  2. Select the **Input Manager** category.
  3. Open the **Jump** action.
  4. Set **Positive Button** to **joystick button 14**.


This code example demonstrates the corresponding input handling:
```
using UnityEngine;

public class Jumping : MonoBehaviour
{
    Rigidbody2D rb;
    float jumpForce = 100f;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    void Update()
    {
        if (Input.GetButtonDown("Jump"))
        {
            rb.AddForce(new Vector2(0f, jumpForce));
        }
    }
}

```

## Example: Set up joystick button X for the Fire action
  1. Go to **Edit** > **Project Settings**.
  2. Select the **Input Manager** category.
  3. Open the **Fire1** action.
  4. Set **Positive Button** to **joystick button 15**.


This code example demonstrates the corresponding input handling:
```
using UnityEngine;
 
public class Shooting : MonoBehaviour
{
    float bulletSpeed = 500f;
    public Transform gun;
    public Rigidbody2D bullet;
 
    void Update()
    {
        if (Input.GetButtonDown("Fire1"))
        {
            var bulletInstance = Instantiate(bullet, gun.position, gun.rotation);
            bulletInstance.AddForce(gun.up * bulletSpeed);
        }
    }
}

```

## Game Controller input mapping
You can map controller input in the Unity Input settings using the following:
**Name** | **KeyCode** | **Axis**  
---|---|---  
A | joystick button 14 | joystick axis 14  
B | joystick button 13 | joystick axis 13  
X | joystick button 15 | joystick axis 15  
Y | joystick button 12 | joystick axis 12  
Left Stick | N/A | Axis 1 (X) - Horizontal, Axis 2 (Y) - Vertical  
Right Stick | N/A | Axis 3 - Horizontal, Axis 4 - Vertical  
D-pad Up | joystick button 4 | Basic profile only: Axis 2 (Y)  
D-pad Right | joystick button 5 | Basic profile only: Axis 1 (X)  
D-pad Down | joystick button 6 | Basic profile only: Axis 2 (Y)  
D-pad Left | joystick button 7 | Basic profile only: Axis 1 (X)  
Pause | joystick button 0 | N/A  
L1/R1 | joystick button 8 / joystick button 9 | joystick axis 8 / joystick axis 9  
L2/R2 | joystick button 10 / joystick button 11 | joystick axis 10 / joystick axis 11  
## Additional resources:
  * [KeyCode API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-detect-game-controllers.html)
Detect Game Controllers
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ios-testing-and-debugging.html)
Test and debug an iOS application
