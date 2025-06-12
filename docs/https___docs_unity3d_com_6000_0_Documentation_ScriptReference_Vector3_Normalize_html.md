* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Normalize.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).Normalize
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
public void Normalize(); 
### Description
Makes this vector have a [magnitude](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-magnitude.html) of 1.
When normalized, a vector keeps the same direction but its length is 1.0.  
  
Note that this function will change the current vector. If you want to keep the current vector unchanged, use [normalized](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-normalized.html) variable.  
  
If this vector is too small to be normalized it will be set to zero.  
  
Additional resources: [normalized](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-normalized.html) property.
* * *
## Declaration
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) Normalize([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) value); 
### Parameters
Parameter | Description  
---|---  
value | The vector to be normalized.  
### Returns
**Vector3** A new vector with the same direction as the original vector but with a magnitude of 1.0. 
### Description
Returns a normalized vector based on the given vector. The normalized vector has a [magnitude](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-magnitude.html) of 1 and is in the same direction as the given vector. Returns a zero vector If the given vector is too small to be normalized.
Note that this does not modify the given vector. To modify and normalize the current vector, use the [Normalize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Normalize.html) function without a parameter.  
  
Additional resources: [normalized](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-normalized.html) function.
* * *
