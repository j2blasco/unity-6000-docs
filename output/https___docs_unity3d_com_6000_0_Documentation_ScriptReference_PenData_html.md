* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenData.html

# PenData
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
Structure describing the status of a pen event.
The PenData struct is used by Unity to store data relating to a pen event. PenData contains information such as the position, pressure, and tilt of the pen for a given pen input event.
### Properties
Property | Description  
---|---  
[contactType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenData-contactType.html) | Contact type of a pen event, can be pen up, pen down, or no contact.  
[deltaPos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenData-deltaPos.html) | The position delta since last pointer event in pixel coordinates.  
[penStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenData-penStatus.html) | Specifies the state of the pen. For example, whether the pen is in contact with the screen or tablet, whether the pen is inverted, and whether buttons are pressed.  
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenData-position.html) | Specifies the position of the pen.  
[pressure](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenData-pressure.html) | How hard pen pressure is applied, normalized between 0 (no pressure) and 1 (maximum pressure).  
[tilt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenData-tilt.html) | Specifies the angle of the pen relative to the X and Y axes, expressed in radians.  
[twist](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenData-twist.html) | Specifies the rotation of the pen around its axis, expressed in radians.  
* * *
