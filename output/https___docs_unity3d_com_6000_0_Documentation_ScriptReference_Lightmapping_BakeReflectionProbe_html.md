* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.BakeReflectionProbe.html

#  [Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.html).BakeReflectionProbe
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
public static bool BakeReflectionProbe([ReflectionProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html) probe, string path); 
### Parameters
Parameter | Description  
---|---  
probe | Target probe.  
path | The location where cubemap will be saved.  
### Returns
**bool** Returns true if baking was succesful. 
### Description
Starts a synchronous bake job for the probe.
Returns when the baking has finished. Additional resources: [ReflectionProbe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReflectionProbe.html).
* * *
