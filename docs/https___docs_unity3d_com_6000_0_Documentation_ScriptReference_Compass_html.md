* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compass.html

# Compass
class in UnityEngine
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
Interface into compass functionality.
### Properties
Property | Description  
---|---  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compass-enabled.html) | Use to enable or disable compass. Note, that if you want Input.compass.trueHeading property to contain a valid value, you must also enable location updates. To do this, call Input.location.Start().Note: On the web platform, the compass is available only with an HTTPS connection, except during development when you might use http://localhost.  
[headingAccuracy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compass-headingAccuracy.html) | Accuracy of heading reading in degrees.  
[magneticHeading](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compass-magneticHeading.html) | The heading in degrees relative to the magnetic North Pole. (Read Only)  
[rawVector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compass-rawVector.html) | The raw geomagnetic data measured in microteslas. (Read Only)  
[timestamp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compass-timestamp.html) | Indicates the time elapsed since the compass heading was last updated. (Read Only)  
[trueHeading](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Compass-trueHeading.html) | The heading in degrees relative to the geographic North Pole. (Read Only)  
* * *
