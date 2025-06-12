* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.FixupEmissiveFlag.html

#  [MaterialEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.html).FixupEmissiveFlag
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
public static [MaterialGlobalIlluminationFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialGlobalIlluminationFlags.html) FixupEmissiveFlag([Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) col, [MaterialGlobalIlluminationFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialGlobalIlluminationFlags.html) flags); 
### Parameters
Parameter | Description  
---|---  
col | Emission color.  
flags | Current global illumination flag.  
### Returns
**MaterialGlobalIlluminationFlags** The fixed up flag. 
### Description
Returns a properly set global illlumination flag based on the passed in flag and the given color.
* * *
## Declaration
public static void FixupEmissiveFlag([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) mat); 
### Parameters
Parameter | Description  
---|---  
mat | The material to be fixed up.  
### Description
Properly sets up the globalIllumination flag on the given Material depending on the current flag's state and the material's emission property.
* * *
