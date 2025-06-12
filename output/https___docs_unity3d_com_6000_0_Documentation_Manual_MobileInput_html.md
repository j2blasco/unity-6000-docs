* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/MobileInput.html

  * [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html)
  * [Legacy Input](https://docs.unity3d.com/6000.0/Documentation/Manual/InputLegacy.html)
  * Mobile device input


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-InputManager.html)
Input Manager
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
UI systems
# Mobile device input
**Important** : This page documents part of the **Input Manager** Settings where you can define all the different input axes, buttons and controls for your project. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-InputManager.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#InputManager) system, which is a legacy feature and not recommended for new projects. For mobile device input in new projects, use the [Input System Package](https://docs.unity3d.com/Packages/com.unity.inputsystem@latest?subfolder=/manual/index.html).
* * *
On mobile devices, the [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html) class offers access to touchscreen, accelerometer and geographical/location input. 
Access to keyboard on mobile devices is provided via the [Mobile keyboard](https://docs.unity3d.com/6000.0/Documentation/Manual/MobileKeyboard.html).
## Multi-touch screen
The iPhone, iPad and iPod Touch devices are capable of tracking up to five fingers touching the screen simultaneously. You can retrieve the status of each finger touching the screen during the last frame by accessing the [Input.touches](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-touches.html) property array.
Android devices don’t have a unified limit on how many fingers they track. Instead, it varies from device to device and can be anything from two-touch on older devices to five fingers on some newer devices.
Each finger touch is represented by an [Input.Touch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html) data structure
The following example script shoots a ray whenever the user taps on the screen:
```
using UnityEngine;

public class TouchInput : MonoBehaviour
{
    GameObject particle;

    void Update()
    {
        foreach(Touch touch in Input.touches)
        {
            if (touch.phase == TouchPhase.Began)
            {
                // Construct a ray from the current touch coordinates
                Ray ray = Camera.main.ScreenPointToRay(touch.position);
                if (Physics.Raycast(ray))
                {
                    // Create a particle if hit
                    Instantiate(particle, transform.position, transform.rotation);
                }
            }
        }
    }
}

```

### Mouse simulation
On top of native touch support Unity iOS/Android provides a mouse simulation. You can use mouse functionality from the standard [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html) class. Note that iOS/Android devices are designed to support multiple finger touch. Using the mouse functionality will support just a single finger touch. Also, finger touch on mobile devices can move from one area to another with no movement between them. Mouse simulation on mobile devices will provide movement, so is very different compared to touch input. The recommendation is to use the mouse simulation during early development but to use touch input as soon as possible.
### Accelerometer
As the mobile device moves, a built-in accelerometer reports linear acceleration changes along the three primary axes in three-dimensional space. Acceleration along each axis is reported directly by the hardware as G-force values. A value of 1.0 represents a load of about +1g along a given axis while a value of –1.0 represents –1g. If you hold the device upright (with the home button at the bottom) in front of you, the X axis is positive along the right, the Y axis is positive directly up, and the Z axis is positive pointing toward you.
You can retrieve the accelerometer value by accessing the [Input.acceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-acceleration.html) property.
The following is an example script which will move an object using the accelerometer:
```
using UnityEngine;

public class Accelerometer : MonoBehaviour
{
    float speed = 10.0f;

    void Update()
    {
        Vector3 dir = Vector3.zero;
        // we assume that the device is held parallel to the ground
        // and the Home button is in the right hand

        // remap the device acceleration axis to game coordinates:
        // 1) XY plane of the device is mapped onto XZ plane
        // 2) rotated 90 degrees around Y axis

        dir.x = -Input.acceleration.y;
        dir.z = Input.acceleration.x;

        // clamp acceleration vector to the unit sphere
        if (dir.sqrMagnitude > 1)
            dir.Normalize();

        // Make it move 10 meters per second instead of 10 meters per frame...
        dir *= Time.deltaTime;

        // Move object
        transform.Translate(dir * speed);
    }
}

```

### Low-Pass Filter
Accelerometer readings can be jerky and noisy. Applying low-pass filtering on the signal allows you to smooth it and get rid of high frequency noise.
The following script shows you how to apply low-pass filtering to accelerometer readings:
```
using UnityEngine;

public class LowPassFilterExample : MonoBehaviour
{
    float accelerometerUpdateInterval = 1.0f / 60.0f;
    float lowPassKernelWidthInSeconds = 1.0f;

    private float lowPassFilterFactor;
    private Vector3 lowPassValue = Vector3.zero;

    void Start()
    {
        lowPassFilterFactor = accelerometerUpdateInterval / lowPassKernelWidthInSeconds;
        lowPassValue = Input.acceleration;
    }

    private void Update()
    {
        lowPassValue = LowPassFilterAccelerometer(lowPassValue);
    }

    Vector3 LowPassFilterAccelerometer(Vector3 prevValue)
    {
        Vector3 newValue = Vector3.Lerp(prevValue, Input.acceleration, lowPassFilterFactor);
        return newValue;
    }
}

```

The greater the value of `LowPassKernelWidthInSeconds`, the slower the filtered value will converge towards the current input sample (and vice versa).
### I’d like as much precision as possible when reading the accelerometer. What should I do?
Reading the [Input.acceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-acceleration.html) variable does not equal sampling the hardware. Put simply, Unity samples the hardware at a frequency of 60Hz and stores the result into the variable. In reality, things are a little bit more complicated – accelerometer sampling doesn’t occur at consistent time intervals, if under significant CPU loads. As a result, the system might report 2 samples during one frame, then 1 sample during the next frame.
You can access all measurements executed by accelerometer during the frame. The following code will illustrate a simple average of all the accelerometer events that were collected within the last frame:
```
public class AccelerationEvents : MonoBehaviour
{ 
    void Update()
    {
        GetAccelerometerValue();
    }

    Vector3 GetAccelerometerValue()
    {
        Vector3 acc = Vector3.zero;
        float period = 0.0f;

        foreach(AccelerationEvent evnt in Input.accelerationEvents)
        {
            acc += evnt.acceleration * evnt.deltaTime;
            period += evnt.deltaTime;
        }
        if (period > 0)
        {
            acc *= 1.0f / period;
        }
        return acc;
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-InputManager.html)
Input Manager
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UIToolkits.html)
UI systems
