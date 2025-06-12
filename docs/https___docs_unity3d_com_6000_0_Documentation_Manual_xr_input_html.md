* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/xr_input.html

  * [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html)
  * Unity XR Input


[](https://docs.unity3d.com/6000.0/Documentation/Manual/MobileKeyboard.html)
Mobile Keyboard
[](https://docs.unity3d.com/6000.0/Documentation/Manual/InputLegacy.html)
Legacy Input
# Unity XR Input
This section of the Unity User Manual provides information about all of the Unity-supported input devices for **virtual reality** Virtual Reality (VR) immerses users in an artificial 3D world of realistic images and sounds, using a headset and motion tracking. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VirtualReality), **augmented reality** Augmented Reality (AR) uses computer graphics or video composited on top of a live video feed to augment the view and create interaction with real and virtual objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AugmentedReality), and Windows **Mixed Reality** Mixed Reality (MR) combines its own virtual environment with the user’s real-world environment and allows them to interact with each other.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MixedReality) applications. This page covers the following topics:
  * [XR input mappings](https://docs.unity3d.com/6000.0/Documentation/Manual/xr_input.html#XRInputMappings)
  * [Accessing input devices](https://docs.unity3d.com/6000.0/Documentation/Manual/xr_input.html#AccessingInputDevices)
  * [Accessing input features on an input device](https://docs.unity3d.com/6000.0/Documentation/Manual/xr_input.html#AccessingInputFeatures)
  * [Accessing XR input via the legacy input system](https://docs.unity3d.com/6000.0/Documentation/Manual/xr_input.html#XRInputLegacySystem)
  * [Haptics](https://docs.unity3d.com/6000.0/Documentation/Manual/xr_input.html#Haptics)


XR platforms have a rich variety of input features that you can take advantage of when you design user interactions. Your application can use specific data that references positions, rotations, touch, buttons, joysticks, and finger sensors. However, access to these input features can vary a lot between platforms. For instance, there are small differences between the Vive and the Oculus Rift, but a VR-enabled desktop platform and a mobile platform like Daydream differ a lot more.
Unity provides a C# struct called [InputFeatureUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputFeatureUsage.html), which defines a standard set of physical device controls (such as buttons and triggers) to access user input on any platform. These help you identify input types by name. See [XR.Input.CommonUsages](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages.html) for a definition of each `InputFeatureUsage`.
Each `InputFeatureUsage` corresponds to a common input action or type. For example, Unity defines the `InputFeatureUsage` called `trigger` as a single-axis input that the index finger controls, regardless of which **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR) platform you use. You can use `InputFeatureUsage` to get the `trigger` state using its name, so you don’t need to set up an axis (or a button on some XR platforms) for the conventional Unity Input system.
## XR input mappings
The following table lists the standard controller `InputFeatureUsage` names and how they map to the controllers of popular XR systems:
**InputFeatureUsage** | **Feature type** |  **Legacy input index** (left controller/right controller) | **WMR** | **Oculus** | **GearVR** | **Daydream** | **OpenVR (Full)** | **Vive** | **Oculus via OpenVR** | **WMR via OpenVR**  
---|---|---|---|---|---|---|---|---|---|---  
[primary2DAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-primary2DAxis.html) | 2D axis | [(1,2)/(4,5)] | Touchpad | Joystick | Touchpad | Touchpad | Trackpad/Joystick | Trackpad | Joystick | Joystick  
[trigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-trigger.html) | Axis | [9/10] | Trigger | Trigger | Trigger | Trigger | Trigger | Trigger | Trigger | Trigger  
[grip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-grip.html) | Axis | [11/12] | Grip | Grip |  | Bumper | Grip | Grip | Grip | Grip  
[secondary2DAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-secondary2DAxis.html) | 2D axis | [(17,18)/(19,20)] | Joystick |  |  |  |  |  |  | Touchpad  
secondary2DAxisClick | Button | [18/19] | Joystick - Click |  |  |  |  |  |  |   
[primaryButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-primaryButton.html) | Button | [2/0] |  | [X/A] - Press |  | App | Primary | Primary (sandwich button)(1) | Primary (Y/B) | Menu  
[primaryTouch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-primaryTouch.html) | Button | [12/10] |  | [X/A] - Touch |  |  |  |  |  |   
[secondaryButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-secondaryButton.html) | Button | [3/1] |  | [Y/B] - Press |  |  | Alternate |  | Alternate (X/A) |   
[secondaryTouch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-secondaryTouch.html) | Button | [13/11] |  | [Y/B] - Touch |  |  |  |  |  |   
[gripButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-gripButton.html) | Button | [4/5] | Grip - Press | Grip - Press |  |  | Grip - Press | Grip - Press | Grip - Press | Grip - Press  
[triggerButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-triggerButton.html) | Button | [14/15] | Trigger - Press | Trigger - Press | Trigger - Press | Trigger - Press | Trigger - Press | Trigger - Press | Trigger - Touch | Trigger - Press  
[menuButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-menuButton.html) | Button | [6/7] | Menu | Start (left controller only) |  |  |  |  |  |   
[primary2DAxisClick](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-primary2DAxisClick.html) | Button | [8/9] | Touchpad - Click | Thumbstick - Press | Touchpad - Press | Touchpad - Press | Trackpad/Joystick - Press | Trackpad - Press | Joystick - Press | Touchpad - Press  
[primary2DAxisTouch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-primary2DAxisTouch.html) | Button | [16/17] | Touchpad - Touch | Thumbstick - Touch | Touchpad - Touch | Touchpad - Touch | Trackpad/Joystick - Touch | Trackpad - Touch | Joystick - Touch | Touchpad - Touch  
[batteryLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-batteryLevel.html) | Axis |  | Battery level |  |  |  |  |  |  |   
[userPresence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-userPresence.html) | Button |  | User presence | User presence |  |  |  |  |  |   
(1) Sandwich button refers to the Vive menu button. This button is mapped to primaryButton, rather than menuButton, in order to better handle cross-platform applications.
See [XR.Input.CommonUsages](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages.html) for a definition of each `InputFeatureUsage`.
## Accessing input devices
An [InputDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice.html) represents any physical device, such as a controller, mobile phone, or headset. It can contain information about device tracking, buttons, joysticks, and other input controls. For more information on the `InputDevice` API, see documentation on [InputDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice.html).
Use the [XR.InputDevices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevices.html) class to access input devices that are currently connected to the XR system. To get a list of all connected devices, use [InputDevices.GetDevices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevices.GetDevices.html):
```
var inputDevices = new List<UnityEngine.XR.InputDevice>();
UnityEngine.XR.InputDevices.GetDevices(inputDevices);

foreach (var device in inputDevices)
{
    Debug.Log(string.Format("Device found with name '{0}' and role '{1}'", device.name, device.role.ToString()));
}

```

An input device remains valid across frames until the XR system disconnects it. Use the [InputDevice.IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice-isValid.html) property to determine whether an `InputDevice` still represents an active controller.
You can access input devices by:
  * Characteristics
  * Role
  * XR node


### Accessing input devices by characteristics
Device characteristics describe what a device is capable of, or what it’s used for (for example, whether it is head-mounted). The [InputDeviceCharacteristics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.html) is a series of flags you can add to your code to search for devices that fit a certain specification. You can filter devices by the following characteristics:
**Device** | **Characteristic**  
---|---  
[HeadMounted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.HeadMounted.html) | The device is attached to the user’s head. It has device tracking and center eye tracking. This flag is most commonly used to identify head-mounted displays (HMDs).  
[Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.Camera.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) | The device has camera tracking.  
[HeldInHand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.HeldInHand.html) | The user holds the device in their hand.  
[HandTracking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.HandTracking.html) | The device represents a physically-tracked hand. It has device tracking, and might contain hand and bone data.  
[EyeTracking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.EyeTracking.html) | The device can perform eye tracking and has an [EyesData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-eyesData.html) feature.  
[TrackedDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.TrackedDevice.html) | The device can be tracked in 3D space. It has device tracking.  
[Controller](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.Controller.html) | The device has input data for buttons and axes, and can be used as a controller.  
[TrackingReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.TrackingReference.html) | The device represents a static tracking reference object. It has device tracking, but that tracking data shouldn’t change.  
[Left](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.Left.html) | Use this characteristic in combination with the HeldInHand or HandTracking characteristics to identify the device as associated with the left hand.  
[Right](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.Right.html) | Use this characteristic in combination with the HeldInHand or HandTracking characteristics to identify the device as associated with the right hand.  
[Simulated6DOF](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.Simulated6DOF.html) | The device reports 6DOF data, but only has 3DOF sensors. Unity simulates the positional data.  
The XR provider **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) reports these characteristics. You can look them up with [InputDevice.Characteristics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice-characteristics.html). A device can, and often should, have multiple characteristics that you can filter and access with bit flags.
[InputDevices.GetDevicesWithCharacteristics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevices.GetDevicesWithCharacteristics.html) provides a way to search for all devices with a given set of characteristics. For example, you can search for Left, HeldInHand, Controller InputDevices available in the system with the following code:
```
var leftHandedControllers = new List<UnityEngine.XR.InputDevice>();
var desiredCharacteristics = UnityEngine.XR.InputDeviceCharacteristics.HeldInHand | UnityEngine.XR.InputDeviceCharacteristics.Left | UnityEngine.XR.InputDeviceCharacteristics.Controller;
UnityEngine.XR.InputDevices.GetDevicesWithCharacteristics(desiredCharacteristics, leftHandedControllers);

foreach (var device in leftHandedControllers)
{
    Debug.Log(string.Format("Device name '{0}' has characteristics '{1}'", device.name, device.characteristics.ToString()));
}

```

Devices this function finds contain at least the characteristics specified, but might contain additional characteristics. For example, to find a left handed controller you can look for InputDeviceCharacteristic.Left only, and not InputDeviceCharacteristic.Controller.
### Accessing input devices by role
A device role describes the general function of an input device. Use the [InputDeviceRole](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceRole.html) enumeration to specify a device role. The defined roles are:
**Role** | **Description**  
---|---  
[GameController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceRole.GameController.html) | A console-style **game controller** A device to control objects and characters in a game.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#gamecontroller).  
[Generic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceRole.Generic.html) | A device that represents the core XR device, such as a head-mounted display or mobile device.  
[HardwareTracker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceRole.HardwareTracker.html) | A tracking device.  
[LeftHanded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceRole.LeftHanded.html) | A device associated with the user’s left hand.  
[RightHanded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceRole.RightHanded.html) | A device associated with the user’s right hand.  
[TrackingReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceRole.TrackingReference.html) | A device that tracks other devices, such as an Oculus tracking camera.  
The XR provider plug-in reports these roles, but different providers might organize their device roles differently. Additionally, a user can switch hands, so the role assignment might not match the hand in which the user holds the input device. For example, a user must set up the Daydream controller as right or left-handed, but can choose to hold the controller in their opposite hand.
[GetDevicesWithRole](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevices.GetDevicesWithRole.html) provides a list of any devices with a specific `InputDeviceRole`. For example, you can use `InputDeviceRole.GameController` to get any connected `GameController` devices:
```
var gameControllers = new List<UnityEngine.XR.InputDevice>();
UnityEngine.XR.InputDevices.GetDevicesWithRole(UnityEngine.XR.InputDeviceRole.GameController, gameControllers);

foreach (var device in gameControllers)
{
    Debug.Log(string.Format("Device name '{0}' has role '{1}'", device.name, device.role.ToString()));
}

```

### Accessing input devices by XR node
XR nodes represent the physical points of reference in the XR system (for example, the user’s head position, their right and left hands, or a tracking reference such as an Oculus camera). 
The [XRNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.html) enumeration defines the following nodes:
**XR node** | **Description**  
---|---  
[CenterEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.CenterEye.html) | A point midway between the pupils of the user’s eyes.  
[GameController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.GameController.html) | A console-style game controller. Your app can have multiple game controller devices.  
[HardwareTracker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.HardwareTracker.html) | A hardware tracking device, typically attached to the user or a physical item. Multiple hardware tracker nodes can exist.  
[Head](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.Head.html) | The center point of the user’s head, as calculated by the XR system.  
[LeftEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.LeftEye.html) | The user’s left eye.  
[LeftHand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.LeftHand.html) | The user’s left hand.  
[RightEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.RightEye.html) | The user’s right eye.  
[RightHand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.RightHand.html) | The user’s right hand.  
[TrackingReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.TrackingReference.html) | A tracking reference point, such as the Oculus camera. Multiple tracking reference nodes can exist.  
Use [InputDevices.GetDevicesAtXRNode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevices.GetDevicesAtXRNode.html) to get a list of devices associated with a specific `XRNode`. The following example demonstrates how to get a left-handed controller:
```
var leftHandDevices = new List<UnityEngine.XR.InputDevice>();
UnityEngine.XR.InputDevices.GetDevicesAtXRNode(UnityEngine.XR.XRNode.LeftHand, leftHandDevices);

if(leftHandDevices.Count == 1)
{
    UnityEngine.XR.InputDevice device = leftHandDevices[0];
    Debug.Log(string.Format("Device name '{0}' with role '{1}'", device.name, device.role.ToString()));
}
else if(leftHandDevices.Count > 1)
{
    Debug.Log("Found more than one left hand!");
}

```

### Listening for device connections and disconnections
Input devices are consistent from frame to frame, but can connect or disconnect at any time. To avoid repeatedly checking if a device is connected to the platform, use [InputDevices.deviceConnected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevices-deviceConnected.html) and [InputDevices.deviceDisconnected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevices-deviceDisconnected.html) to notify your application when a device connects or disconnects. These also provide you with a reference to the newly connected input device.
Since you can retain these references over multiple frames, a device might disconnect, or is otherwise no longer available. To check if a device’s inputs are still available, use [InputDevice.isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice-isValid.html). **Scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) that access input devices should check this at the start of each frame before they attempt to use that device.
## Accessing input features on an input device
You can read an input feature, such as the state of a trigger button, from a specific [InputDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice.html). For example, to read the state of the right trigger, follow these steps:
  1. Use [InputDeviceRole.RightHanded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceRole.RightHanded.html) or [XRNode.RightHand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRNode.RightHand.html) to get an instance of the right-handed device.
  2. Once you have the correct device, use the [InputDevice.TryGetFeatureValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice.TryGetFeatureValue.html) method to access the current state.


`TryGetFeatureValue()` attempts to access the current value of a feature, and returns:
  * true if it successfully retrieves the specified feature value
  * false if the current device doesn’t support the specified feature, or the device is invalid (that is, the controller is no longer active)


To get a particular button, touch input, or joystick axis value, use the [CommonUsages](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages.html) class. `CommonUsages` includes each `InputFeatureUsage` in the [XR input mapping table](https://docs.unity3d.com/6000.0/Documentation/Manual/xr_input.html#XRInputMappings), as well as tracking features like position and rotation. The following code example uses [CommonUsages.triggerButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-triggerButton.html) to detect whether the user is currently pressing the trigger button on a particular `InputDevice` instance:
```
bool triggerValue;
if (device.TryGetFeatureValue(UnityEngine.XR.CommonUsages.triggerButton, out triggerValue) && triggerValue)
{
    Debug.Log("Trigger button is pressed.");
}

```

You can also use the [InputDevice.TryGetFeatureUsages](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice.TryGetFeatureUsages.html) method to get a list of every `InputFeatureUsage` that a device provides. This function returns a list of [InputFeatureUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputFeatureUsage.html) items, which have a type and a name property that describes the feature. The following example enumerates all of the Boolean features that a given input device provides:
```
var inputFeatures = new List<UnityEngine.XR.InputFeatureUsage>();
if (device.TryGetFeatureUsages(inputFeatures))
{
    foreach (var feature in inputFeatures)
    {
        if (feature.type == typeof(bool))
        {
            bool featureValue;
            if (device.TryGetFeatureValue(feature.As<bool>(), out featureValue))
            {
                Debug.Log(string.Format("Bool feature {0}'s value is {1}", feature.name, featureValue.ToString()));
            }
        }
    }
}

```

### Example for primaryButton
Different controller configurations provide access to different features. For example, you might have multiple controllers on one system, different controllers on different systems, or different buttons on the same controllers with different SDKs. This diversity makes it more complicated to support input from a range of XR systems. The Unity `InputFeatureUsage` API helps you get input that isn’t platform-dependent.
The following example accesses the `InputFeatureUsage` called `primaryButton`, no matter which controller or input device provides it. The example includes a class that scans the available devices for the `primaryButton` as they connect. The class monitors the value of the feature on any connected device and, if the value changes, the class dispatches a [UnityEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEvent.html).
To use this class, add it as a component to any **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). For example:
```
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.XR;

[System.Serializable]
public class PrimaryButtonEvent : UnityEvent<bool> { }

public class PrimaryButtonWatcher : MonoBehaviour
{
    public PrimaryButtonEvent primaryButtonPress;

    private bool lastButtonState = false;
    private List<InputDevice> devicesWithPrimaryButton;

    private void Awake()
    {
        if (primaryButtonPress == null)
        {
            primaryButtonPress = new PrimaryButtonEvent();
        }

        devicesWithPrimaryButton = new List<InputDevice>();
    }

    void OnEnable()
    {
        List<InputDevice> allDevices = new List<InputDevice>();
        InputDevices.GetDevices(allDevices);
        foreach(InputDevice device in allDevices)
            InputDevices_deviceConnected(device);

        InputDevices.deviceConnected += InputDevices_deviceConnected;
        InputDevices.deviceDisconnected += InputDevices_deviceDisconnected;
    }

    private void OnDisable()
    {
        InputDevices.deviceConnected -= InputDevices_deviceConnected;
        InputDevices.deviceDisconnected -= InputDevices_deviceDisconnected;
        devicesWithPrimaryButton.Clear();
    }

    private void InputDevices_deviceConnected(InputDevice device)
    {
        bool discardedValue;
        if (device.TryGetFeatureValue(CommonUsages.primaryButton, out discardedValue))
        {
            devicesWithPrimaryButton.Add(device); // Add any devices that have a primary button.
        }
    }

    private void InputDevices_deviceDisconnected(InputDevice device)
    {
        if (devicesWithPrimaryButton.Contains(device))
            devicesWithPrimaryButton.Remove(device);
    }

    void Update()
    {
        bool tempState = false;
        foreach (var device in devicesWithPrimaryButton)
        {
            bool primaryButtonState = false;
            tempState = device.TryGetFeatureValue(CommonUsages.primaryButton, out primaryButtonState) // did get a value
                        && primaryButtonState // the value we got
                        || tempState; // cumulative result from other controllers
        }

        if (tempState != lastButtonState) // Button state changed since last frame
        {
            primaryButtonPress.Invoke(tempState);
            lastButtonState = tempState;
        }
    }
}

```

The following `PrimaryReactor` class uses the `PrimaryButtonWatcher` to detect when you press a primary button and, in response to a press, rotates its parent GameObject. To use this class, add it to a visible GameObject, such as a Cube, and drag the `PrimaryButtonWatcher` reference to the **Watcher** property.
```
using System.Collections;
using UnityEngine;

public class PrimaryReactor : MonoBehaviour
{
    public PrimaryButtonWatcher watcher;
    public bool IsPressed = false; // used to display button state in the Unity Inspector window
    public Vector3 rotationAngle = new Vector3(45, 45, 45);
    public float rotationDuration = 0.25f; // seconds
    private Quaternion offRotation;
    private Quaternion onRotation;
    private Coroutine rotator;

    void Start()
    {
        watcher.primaryButtonPress.AddListener(onPrimaryButtonEvent);
        offRotation = this.transform.rotation;
        onRotation = Quaternion.Euler(rotationAngle) * offRotation;
    }

    public void onPrimaryButtonEvent(bool pressed)
    {
        IsPressed = pressed;
        if (rotator != null)
            StopCoroutine(rotator);
        if (pressed)
            rotator = StartCoroutine(AnimateRotation(this.transform.rotation, onRotation));
        else
            rotator = StartCoroutine(AnimateRotation(this.transform.rotation, offRotation));
    }

    private IEnumerator AnimateRotation(Quaternion fromRotation, Quaternion toRotation)
    {
        float t = 0;
        while (t < rotationDuration)
        {
            transform.rotation = Quaternion.Lerp(fromRotation, toRotation, t / rotationDuration);
            t += Time.deltaTime;
            yield return null;
        }
    }
}

```

### Accessing hand-tracking data
InputDevices support hand-tracking devices. A hand-tracking device always:
  * has the [HandTracking ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDeviceCharacteristics.HandTracking.html)characteristic
  * contains a [CommonUsages.HandData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-handData.html) usage of the [Hand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.html) type


Hand-tracking data consists of a Hand object and a series of up to 21 Bone input features. Each [Bone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Bone.html) has a position and orientation, as well as references to both its parent and any child bones in the hierarchy. The Hand object can get either the root bone, or a list of bones for each individual finger.
When [Hand.TryGetRootBone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.TryGetRootBone.html) gets the root bone, it retrieves an object that represents a bone located just above the wrist. You can also get a list of bones that represents each individual finger. Calling [Hand.TryGetFingerBones](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.TryGetFingerBones.html) returns a list, from knuckle to tip, of the bones that represents that finger.
### Accessing eye-tracking data
Input devices support eye-tracking devices, as well as hand-tracking devices. Eye-tracking consists of the left and right eye positions, the location in 3D space where the user is looking, and the amount that each individual eye is blinking. Its data type is [Eyes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Eyes.html). To retrieve it from a device, use [CommonUsages.eyesData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.CommonUsages-eyesData.html). 
### XRInputSubsystem and InputDevice association
Unity provides two input systems: the legacy input system, and the [XR plugin architecture](https://discussions.unity.com/t/xr-plugins-and-subsystems/746800) introduced in 2019.2. In the new setup, each InputDevice is associated with an [XRInputSubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystem.html). These subsystem objects control global input behavior that isn’t associated with any specific input device (for example, managing the tracking origin, or recentering tracked devices).
Each InputDevice contains a reference to its associated subsystem. This reference is null if the device comes from an integrated platform. You can also get all active XRInputSubsystem objects with [SubsystemManager.GetInstances<XRInputSubsystem>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SubsystemManager.GetInstances.html), and each XRInputSubsystem can get its devices with [XRInputSubsystem.TryGetInputDevices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystem.TryGetInputDevices.html).
You can use the Input Subsystem to recenter devices with [UnityEngine.XR.XRInputSubsystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystem.html). Recenter sets the current position of the HMD as the new origin for all devices. It returns false for devices that can’t be recentered, or if the platform doesn’t support recentering.
To retrieve the tracking boundary, use [TryGetBoundaryPoints](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystem.TryGetBoundaryPoints.html). This consists of a series of clockwise-ordered 3D points, where the y-value is at floor level, and they mark out the user-specified ‘safe zone’ to place content and interactions. You can listen for changes to this boundary with [XRInputSubsystem.boundaryChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystem-boundaryChanged.html).
The XRInputSubsystem is also responsible for the tracking origin mode, which provides context for where the origin of the tracking world is. Unity supports the following tracking origin modes:
  * [Device](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.TrackingOriginModeFlags.Device.html): The origin’s location is at the first known location of the primary display device; often an HMD or a phone.
  * [Floor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.TrackingOriginModeFlags.Floor.html): The origin’s location is at a known location on the floor.
  * [Tracking Reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.TrackingOriginModeFlags.TrackingReference.html): The origin’s location is on an InputDevice with the TrackingReference characteristic set.
  * [Unknown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.TrackingOriginModeFlags.Unknown.html): The type of tracking origin is unknown. This can be because of a system failure or lack of tracking origin-mode support.


There are three APIs you can use to manage the tracking origin mode:
  * [XRInputSubsystem.TrySetTrackingOriginMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystem.TrySetTrackingOriginMode.html) sets the tracking origin mode
  * [XRInputSubystem.GetTrackingOriginMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystem.GetTrackingOriginMode.html) retrieves the tracking origin mode
  * [XRInputSubsystem.GetSupportedTrackingOriginModes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystem.GetSupportedTrackingOriginModes.html) retrieves all tracking origin modes that the SDK supports


## XR input through the legacy input system
You can still use the legacy input system, consisting of [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html) and [XR.InputTracking](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputTracking.html), to retrieve XR input features. To do this, use the appropriate legacy input indices from the [XR input mappings table](https://docs.unity3d.com/6000.0/Documentation/Manual/xr_input.html#XRInputMappings) on this page. In the **Input** section of the **Player Settings** Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings) (menu: **Edit** > **Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings) > **Input**), create an axis mapping to add the appropriate mapping from input name to axis index for the platform device’s feature. To retrieve the button or axis value, use [Input.GetAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html) or [Input.GetButton](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetButton.html) and pass in the now-mapped axis or button name.
For more information about how to use the button and joystick axes, see documentation on the [InputManager](https://docs.unity3d.com/6000.0/Documentation/Manual/class-InputManager.html).
## Haptics
You can send haptic events to an [InputDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice.html). Haptics take on the form of an impulse, with an amplitude and duration.
Not all platforms support all types of haptics, but you can query a device for haptic capabilities. The following example gets an input device for the right hand, checks to see if the device is capable of haptics, and then plays back an impulse if it’s capable:
```
List<UnityEngine.XR.InputDevice> devices = new List<UnityEngine.XR.InputDevice>(); 

UnityEngine.XR.InputDevices.GetDevicesWithRole(UnityEngine.XR.InputDeviceRole.RightHanded, devices);

foreach (var device in devices)
{
    UnityEngine.XR.HapticCapabilities capabilities;
    if (device.TryGetHapticCapabilities(out capabilities))
    {
            if (capabilities.supportsImpulse)
            {
                uint channel = 0;
                float amplitude = 0.5f;
                float duration = 1.0f;
                device.SendHapticImpulse(channel, amplitude, duration);
            }
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MobileKeyboard.html)
Mobile Keyboard
[](https://docs.unity3d.com/6000.0/Documentation/Manual/InputLegacy.html)
Legacy Input
