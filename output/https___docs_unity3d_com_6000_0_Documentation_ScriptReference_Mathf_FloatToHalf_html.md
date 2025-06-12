* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.FloatToHalf.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).FloatToHalf
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mathf.html "Go to Mathf Component in the Manual")
## Declaration
public static ushort FloatToHalf(float val); 
### Parameters
Parameter | Description  
---|---  
val | The floating point value to convert.  
### Returns
**ushort** The converted half-precision float, stored in a 16-bit unsigned integer. 
### Description
Encode a floating point value into a 16-bit representation.
Converting a floating point value to a half causes it to lose precision and also reduces the maximum range of values it can represent. The new range is from -65,504 and 65,504. For more information on 16-bit floating-point numbers, and for information on how precision changes over the range of values, see [Half-precision floating-point format](https://en.wikipedia.org/wiki/Half-precision_floating-point_format).  
  
If the converted floating point value falls exactly between two half-precision values, this method rounds it to the value furthest from zero (Round away from zero tie-break rule). This selects the value closer to positive or negative infinity, depending on the sign.  
  
You should only use the returned ushort as a storage format. If you want to perform mathematical operations on it, first convert it back to a float with [Mathf.HalfToFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.HalfToFloat.html).
* * *
