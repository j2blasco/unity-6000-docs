* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice.TryGetFeatureUsages.html

#  [InputDevice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputDevice.html).TryGetFeatureUsages
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
## Declaration
public bool TryGetFeatureUsages(List<InputFeatureUsage> featureUsages); 
### Parameters
Parameter | Description  
---|---  
featureUsages | A List of [InputFeatureUsage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.InputFeatureUsage.html) structures to receive the available features on this device.  
### Returns
**bool** true if device can be queried; otherwise false. 
### Description
Gets a list of all the input feature usages available on this device. For example, "Trigger" or "Device Position".
* * *
