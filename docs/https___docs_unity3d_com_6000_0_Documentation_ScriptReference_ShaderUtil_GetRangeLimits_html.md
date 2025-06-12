* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.GetRangeLimits.html

#  [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html).GetRangeLimits
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
public static float GetRangeLimits([Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) s, int propertyIdx, int defminmax); 
### Parameters
Parameter | Description  
---|---  
defminmax | Which value to get: 0 = default, 1 = min, 2 = max.  
s | The shader to check against.  
propertyIdx | The property index to use.  
### Description
Get Limits for a range property at index propertyIdx of Shader s.
* * *
