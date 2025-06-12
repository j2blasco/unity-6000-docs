* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.GetDeviceCaps.html

#  [Microphone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.html).GetDeviceCaps
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Microphone.html "Go to Microphone Component in the Manual")
## Declaration
public static void GetDeviceCaps(string deviceName, out int minFreq, out int maxFreq); 
### Parameters
Parameter | Description  
---|---  
deviceName | The name of the device.  
minFreq | Returns the minimum sampling frequency of the device.  
maxFreq | Returns the maximum sampling frequency of the device.  
### Description
Get the frequency capabilities of a device.
Passing null or an empty string for the device name will select the default device. You can use the [devices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone-devices.html) property to get a list of all available microphones.  
  
When a value of zero is returned in the _minFreq_ and _maxFreq_ parameters, this indicates that the device supports any frequency.
* * *
