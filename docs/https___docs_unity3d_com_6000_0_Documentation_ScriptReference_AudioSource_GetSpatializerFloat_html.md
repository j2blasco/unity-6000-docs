* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.GetSpatializerFloat.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).GetSpatializerFloat
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html "Go to AudioSource Component in the Manual")
## Declaration
public bool GetSpatializerFloat(int index, out float value); 
### Parameters
Parameter | Description  
---|---  
index | Zero-based index of user-defined parameter to be read.  
value | Return value of the user-defined parameter that is read.  
### Returns
**bool** True, if the parameter could be read. 
### Description
Reads a user-defined parameter of a custom spatializer effect that is attached to an AudioSource.
Since this is for internal use in custom inspectors controlling custom spatializer effects implemented as native audio plugins, it is up to the spatializer to perform necessary clipping on the UI and native sides through the setparameter/getparameter callbacks of the native audio plugin.
* * *
