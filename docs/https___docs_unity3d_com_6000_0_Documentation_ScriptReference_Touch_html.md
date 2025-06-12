* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html

# Touch
struct in UnityEngine
/
Implemented in:[UnityEngine.InputLegacyModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.InputLegacyModule.html)
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
Structure describing the status of a finger touching the screen.
Devices can track a number of different pieces of data about a touch on a touchscreen, including its `phase` of the touch lifecycle, its position and whether the touch was a single contact or several taps. Furthermore, the continuity of a touch between frame updates can be detected by the device, so a consistent ID number can be reported across frames and used to determine how a particular finger is moving.  
  
The touch lifecycle describes the state of a touch in any given frame: 
  * Began - A user has touched their finger to the screen this frame
  * Stationary - A finger is on the screen but the user has not moved it this frame
  * Moved - A user moved their finger this frame
  * Ended - A user lifted their finger from the screen this frame
  * Cancelled - The touch was interrupted this frame


The Touch struct is used by Unity to store data relating to a single touch instance and is returned by the [Input.GetTouch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetTouch.html) function. Fresh calls to GetTouch will be required on each frame update to obtain the latest touch information from the device but the [fingerId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-fingerId.html) property can be used to identify the same touch between frames.  
  
**Note** : On iOS devices, any Touch information that is being held in memory (for example, when you are part way through the touch lifecycle) will be lost if the application is minimized. This happens because iOS calls ResetTouch() and wipes all touch data from memory. The lifecycle of that touch ends there and any functionality that relies on later phases of the touch lifecycle is not executed. If you experience this problem, you should move the functionality that is not being executed into [MonoBehaviour.OnApplicationFocus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnApplicationFocus.html) or [MonoBehaviour.OnApplicationPause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnApplicationPause.html).  
  
Additional resources: [Input.GetTouch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetTouch.html), [TouchPhase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.html) enum.
### Properties
Property | Description  
---|---  
[altitudeAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-altitudeAngle.html) | Value of 0 radians indicates that the stylus is parallel to the surface, pi/2 indicates that it is perpendicular.  
[azimuthAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-azimuthAngle.html) | Value of 0 radians indicates that the stylus is pointed along the x-axis of the device.  
[deltaPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-deltaPosition.html) | The position delta since last change in pixel coordinates.  
[deltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-deltaTime.html) | Amount of time that has passed since the last recorded change in Touch values.  
[fingerId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-fingerId.html) | The unique index for the touch.  
[maximumPossiblePressure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-maximumPossiblePressure.html) | The maximum possible pressure value for a platform. If Input.touchPressureSupported returns false, the value of this property will always be 1.0f.  
[phase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-phase.html) | Describes the phase of the touch.  
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-position.html) | The position of the touch in screen space pixel coordinates.  
[pressure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-pressure.html) | The current amount of pressure being applied to a touch. 1.0f is considered to be the pressure of an average touch. If Input.touchPressureSupported returns false, the value of this property will always be 1.0f.  
[radius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-radius.html) | An estimated value of the radius of a touch. Add radiusVariance to get the maximum touch size, subtract it to get the minimum touch size.  
[radiusVariance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-radiusVariance.html) | This value determines the accuracy of the touch radius. Add this value to the radius to get the maximum touch size, subtract it to get the minimum touch size.  
[rawPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-rawPosition.html) | The first position of the touch contact in screen space pixel coordinates.  
[tapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-tapCount.html) | Number of taps.  
[type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch-type.html) | A value that indicates whether a touch was of Direct, Indirect (or remote), or Stylus type.  
* * *
